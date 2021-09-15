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
        
        
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug','content','status']
        

class PostImageForm(forms.ModelForm):
    class Meta:
        model = PostImage
        extra = 3
        fields = ['images']



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
