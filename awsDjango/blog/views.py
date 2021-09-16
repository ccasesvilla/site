from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Topic, Entry, Post, Comment, PostImage
from .forms import EntryForm, TopicForm, PostForm, PostImageForm, CommentForm
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.forms import modelformset_factory
from django.contrib import messages

from notifications import settings
from notifications.models import Notification
from notifications.signals import notify
from notifications.utils import slug2id
from swapper import load_model

Notification = load_model('notifications', 'Notification')




@login_required
def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = Topic.objects.get(id=topic_id)
    # Make sure the topic belongs to the current user.
    if topic.owner != request.user:
        return render(request, 'blog/topics.html')
    
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'blog/topic.html', context)


@login_required
def topics(request):
    """Show all topics."""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'blog/topics.html', context)



@login_required
def new_topic(request):
    """Add a new topic."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('blog:topics')
        
    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'blog/new_topic.html', context)


@login_required
def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    topic = Topic.objects.get(id=topic_id)
    
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EntryForm()
    else:
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('blog:topic', topic_id=topic_id)
    # Display a blank or invalid form.
    context = {'topic': topic, 'form': form}
    return render(request, 'blog/new_entry.html', context)






@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        return render(request, 'blog/topics.html')
    
    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:topic', topic_id=topic.id)
    
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'blog/edit_entry.html', context)
        


@login_required
def delete_entry(request, entry_id):
    """Delete an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        return render(request, 'learning_logs/index.html')

    else:
        # POST data submitted; process data.
        entry.delete()

    return redirect('learning_logs:topic', topic_id=topic.id)
    
import feed.models as feeds

@login_required
def search(request):
    if request.method == "POST":
      
        searched = request.POST['searched']
        entries = Entry.objects.filter(text__contains=searched)
        blogs = feeds.Post.objects.filter(description=searched)
        comments = feeds.Comments.objects.filter(post=searched)
        topics = Post.objects.filter(content__contains=searched)
        topics = Post.objects.filter(title__contains=searched)

        length = (len(entries)+len(blogs)+len(comments)+len(topics))

        return render(request, 'blog/show_results.html', {'length':length,'searched': searched, 'comments':comments, 'entries': entries, 'topics':topics, 'blogs':blogs})
    else:
        return render(request, 'blog/show_results.html')



@login_required
def show_results(request, entry_id):
	entry = Entry.objects.get(pk=entry_id)
	return render(request, 'blog/show_results.html', 
		{'entry': entry})



def PostList(request):
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    paginator = Paginator(queryset, 5)
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)    


        
    return render(request, 'learning_logs/index.html', {'page_obj': page_obj})

def Blog_List1(request):
    queryset = Post.objects.filter(status=1).order_by("-created_on")

    paginator = Paginator(queryset, 5)
    for page in queryset:
        photos = PostImage.objects.filter(post=page)
        #return render(request, 'blog/blog_list.html', {'photos': photos})


    
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'blog/blog_list.html', {'page_obj': page_obj})


def postimage_list(request, slug):
    template_name = "blog/blog_list.html"
    post = get_object_or_404(Post, slug=slug)
    photos = PostImage.objects.filter(post=post)

    return render(
        request,
        template_name,
        {
            "photos": photos,

        },
    )


def delete(request, slug=None):
    notification_id = slug2id(slug)

    notification = get_object_or_404(
        Notification, recipient=request.user, id=notification_id)

    if settings.get_config()['SOFT_DELETE']:
        notification.deleted = True
        notification.save()
    else:
        notification.delete()

    _next = request.GET.get('next')

    if _next:
        return redirect(_next)

    return redirect('learning_logs/index.html')



def mark_as_read(request, slug=None):
    notification_id = slug2id(slug)

    notification = get_object_or_404(
        Notification, recipient=request.user, id=notification_id)
    notification.mark_as_read()

    _next = request.GET.get('next')

    if _next:
        return render(request,'blog_detail.html')

    return render(request, 'blog_detail.html')




def delete_notifications (request, slug):
    notifi = notify.objects.get(pk = slug, user = request.user)
    notifi.State = True
    notifi.save ()
    return HttpResponseRedirect ('/')  



def blog_detail(request, slug):
    template_name = "blog/blog_detail.html"
    post = get_object_or_404(Post, slug=slug)
    photos = PostImage.objects.filter(post=post)
    comments = post.comments.filter(active=True).order_by("-created_on")
    new_comment = None
    # Comment posted
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.user = request.user
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
            sender = User.objects.get(username=request.user)
            notify.send(sender, recipient=new_comment.post.author, target=new_comment, verb=new_comment.post.title , description=new_comment.post.slug)
            return redirect ('/blog_list' )
            
            
            
    else:
        comment_form = CommentForm()

    return render(
        request,
        template_name,
        {
            "post": post,
            "photos": photos,
            "comments": comments,
            "new_comment": new_comment,
            "comment_form": comment_form,
        },
    )









def new_blog(request):

    
    #ImageFormSet = modelformset_factory(PostImage,
                                       # form=PostImageForm, extra=3)

    if request.method == 'POST':
        #formset = ImageFormSet(request.POST, request.FILES,
                               #queryset=PostImage.objects.none())
        postForm = PostForm(request.POST or None)
        files = request.FILES.getlist('images')
        if postForm.is_valid():
            post_form = postForm.save(commit=False)
            post_form.author = request.user
            post_form.save()
    
            #for form in formset.cleaned_data:
                #this helps to not crash if the user   
                #do not upload all the photos
            for f in files:
                photo = PostImage.objects.create(post=post_form.title, images=f)
                photo.save()
            # use django messages framework
            messages.success(request,
                             "Yeeew, check it out on the home page!")
            return HttpResponseRedirect("/")
        else:
            print(postForm.errors)
    else:
        postForm = PostForm()
        #formset = ImageFormSet(queryset=PostImage.objects.none())
    return render(request, 'blog/new_blog.html',
                  {'postForm': postForm})



@login_required
def in_progress(request):
    entry = Post.objects.filter(status=0).order_by("-created_on")
    return render(request, 'in_progress.html', 
		{'entry': entry})
