from django import forms
from .models import Topic, Entry, Post, Comment, PostImage
from django.forms import Form, ChoiceField, CharField
from django.utils.text import slugify
from django import forms
from tinymce.widgets import TinyMCE

class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False





class TopicForm(forms.ModelForm):
    text = forms.CharField(widget=TinyMCEWidget(attrs={'required': False, 'cols': 30, 'rows':1}))

    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text':''}
        
        
class EntryForm(forms.ModelForm):
    text = forms.CharField(widget=TinyMCEWidget(attrs={'required': False, 'cols': 30, 'rows':1}))

    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
       # widgets = {'text': forms.Textarea(attrs={'cols': 80})}
        
class PostImageForm(forms.ModelForm):
    images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}),required=False)


    class Meta:
        model = PostImage
        fields =  ['images']      



    
        
class PostForm(PostImageForm):
    title = forms.CharField(widget=TinyMCEWidget(attrs={'required': False, 'cols': 30, 'rows':1}))#cover_Pic = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}),required=False)
    images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}),required=False)  
    content = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols': 30, 'rows': 15}
        )
    )

    class Meta(PostImageForm.Meta):
        model = Post
        fields = ['title','content','status'] + PostImageForm.Meta.fields





class FilterForm(Form):
    FILTER_CHOICES = (
        ('text', 'Test'),
        ('topic', 'Topic'),
        ('date_added', 'Date_Added'),
    )
    search = CharField(required=False)
    filter_field = ChoiceField(choices=FILTER_CHOICES)


class CommentForm(forms.ModelForm):


    body = forms.CharField(widget=TinyMCEWidget(attrs={'required': False, 'cols': 30, 'rows':1}))
    class Meta:
        model = Comment
        fields = ('email', 'body')
