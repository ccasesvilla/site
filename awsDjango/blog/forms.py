from django import forms
from .models import Topic, Entry, Post, Comment, PostImage
from django.forms import Form, ChoiceField, CharField





class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text':''}
        
        
class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
        
class PostImageForm(forms.ModelForm):


    class Meta:

        fields =  ['images']        
        
class PostForm(PostImageForm):
    images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}),required=False)  
    class Meta(PostImageForm.Meta):
        model = Post
        fields = PostImageForm.Meta.fields + ['title', 'slug','content','status','images']
        





class FilterForm(Form):
    FILTER_CHOICES = (
        ('text', 'Test'),
        ('topic', 'Topic'),
        ('date_added', 'Date_Added'),
    )
    search = CharField(required=False)
    filter_field = ChoiceField(choices=FILTER_CHOICES)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('email', 'body')
