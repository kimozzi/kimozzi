from django import forms
from blog.models import Post, Comment

class PostForm(forms.ModelForm):
    #is_agree = forms.BooleanField(label='약관동의', error_messages = {'required' : '약관에 동의해야함'})
    class Meta:
        model = Post
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        #fields = '__all__'
        fields = ['title']