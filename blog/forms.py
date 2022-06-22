from django import forms
from django.contrib.auth.models import User



class BlogForm(forms.Form):
    title = forms.CharField(max_length=200, unique=True)
    slug = forms.SlugField(max_length=500, unique=True)
    author = forms.InlineForeignKeyField(User,related_name='blog_posts')
    updated_on = forms.DateTimeField(auto_now= True)
    content = forms.Textarea()
    created_on = forms.DateTimeField(auto_now_add=True)
    
