from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from .forms import NewCommentForm, NewPostForm, PostImageForm
from django.views.generic import ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Comments, Like, PostImage
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
import json
from django.forms import modelformset_factory



class PostListView(ListView):
    model = Post
    template_name = 'feed/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 10
    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            liked = [i for i in Post.objects.all() if Like.objects.filter(user = self.request.user, post=i)]
            photos = PostImage.objects.all()
            context['liked_post'] = liked
        return context



class UserPostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'feed/user_post.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(UserPostListView, self).get_context_data(**kwargs)
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        liked = [i for i in Post.objects.filter(user_name=user) if Like.objects.filter(user = self.request.user, post=i)]
        context['liked_post'] = liked
        return context

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(user_name=user).order_by('-date_posted')



def image_detail(request, id):
    post = get_object_or_404(Post, id=id)
    photo = PostImage.objects.filter(post=post)

    return render(request, 'feed/home.html', {'photo':photo} )




@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    photos = PostImage.objects.filter(post=post)
    user = request.user
    is_liked =  Like.objects.filter(user=user, post=post)
    if request.method == 'POST':
        form = NewCommentForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.post = post
            data.username = user
            data.save()
            return redirect('post-detail', pk=pk)
    else:
        form = NewCommentForm()
    return render(request, 'feed/post_detail.html', {'post':post, 'is_liked':is_liked, 'form':form, 'photos': photos})

@login_required
def create_post(request):
        user = request.user
        # ImageFormSet = modelformset_factory(PostImage, form=PostImageForm, max_num = 10)

        if request.method == "POST":
            # formset = ImageFormSet(request.POST, request.FILES)
            form = PostImageForm(request.POST or None, request.FILES or None)
            files = request.FILES.getlist('images')
            if form.is_valid():
                data = form.save(commit=False)
                
                data.user_name = request.user
             
                data.save()
                for f in files:
                    photo = PostImage.objects.create(post=data,images=f)
                    photo.save()
                # for form in formset.cleaned_data:
                #     if form:
                #         images = form['images']
                #         photo = PostImage(post=data, images=images)
                #         photo.save(commit=False)

                messages.success(request, f'Posted Successfully')
                return redirect('home')
        else:
            form = PostImageForm()
            # formset = ImageFormSet()
        return render(request, 'feed/create_post.html', {'form':form})





class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['description', 'pic', 'tags']
	template_name = 'feed/create_post.html'

	def form_valid(self, form):
		form.instance.user_name = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.user_name:
			return True
		return False

@login_required
def post_delete(request, pk):
	post = Post.objects.get(pk=pk)
	if request.user== post.user_name:
		Post.objects.get(pk=pk).delete()
	return redirect('home')


@login_required
def search_posts(request):
	query = request.GET.get('p')
	object_list = Post.objects.filter(tags__icontains=query)
	liked = [i for i in object_list if Like.objects.filter(user = request.user, post=i)]
	context ={
		'posts': object_list,
		'liked_post': liked
	}
	return render(request, "feed/search_posts.html", context)

@login_required
def like(request):
    post_id = request.GET.get("likeId", "")
    user = request.user
    post = Post.objects.get(pk=post_id)
    liked= False
    like = Like.objects.filter(user=user, post=post)
    if like:
        like.delete()
    else:
        liked = True
        Like.objects.create(user=user, post=post)
    resp = {
        'liked':liked
    }
    response = json.dumps(resp)
    return HttpResponse(response, content_type = "application/json")
