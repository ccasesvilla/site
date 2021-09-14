from django import forms
from .models import Comments, Post, PostImage



class NewPostForm(forms.ModelForm):
    cover_Pic = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}),required=False)
    
    class Meta:
        model = Post
        fields = ['description','cover_Pic','tags']



# class PostImageForm(forms.ModelForm):

#     images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

#     class Meta:
#         models = PostImage

#         fields =  ['images',]


class PostImageForm(NewPostForm):
    images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}),required=False)
    class Meta(NewPostForm.Meta):

        fields = NewPostForm.Meta.fields + ['images']




class NewCommentForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ['comment']