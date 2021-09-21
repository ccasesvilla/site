from django import forms
from .models import Comments, Post, PostImage

from tinymce.widgets import TinyMCE

class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


    
        



# class PostImageForm(forms.ModelForm):

#     images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

#     class Meta:
#         models = PostImage

#         fields =  ['images',]


class PostImageForm(forms.ModelForm):
    class Meta:
        model = PostImage   
        fields = ['images']


class NewPostForm(PostImageForm):
    description = forms.CharField(widget=TinyMCEWidget(attrs={'required': False, 'cols': 30, 'rows': 2}))
    cover_Pic = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}),required=False)   

    images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}),required=False)   
    tags = forms.CharField(widget=TinyMCEWidget(attrs={'required': False, 'cols': 30, 'rows': 5}))
    class Meta(PostImageForm.Meta):
        model = Post
        fields = ['description','tags','cover_Pic'] + PostImageForm.Meta.fields



class NewCommentForm(forms.ModelForm):
    comment = forms.CharField(widget=TinyMCEWidget(attrs={'required': False, 'cols': 40, 'rows': 1}))

    class Meta:
        model = Comments
        fields = ['comment']