from django import forms

from . import models


# Post 모델을 조작하는 PostModelForm 정의
class PostForm(forms.ModelForm):
    # 1. 어떤 input 필드를 가지는지 정하기
    content = forms.CharField(
        label="content", # label: html에서 붙일 이름
        widget=forms.Textarea(attrs={
            'placeholder': "오늘은 무엇을 하셨나요?"
        })
    )
    # 2. 해당 input 필드 속성 추가
    class Meta:
        model = models.Post
        fields = ['content', 'image']


# Comment 모델을 조작하는 CommentForm 정의
class CommentForm(forms.ModelForm):
    # 1. 어떤 input 필드를 가지는지 정하기
    content = forms.CharField(
        label="", # label: html에서 붙일 이름
        widget=forms.TextInput(attrs={
            'placeholder': "이 포스트에 댓글 남기기"
        })
    )
    # 2. 해당 input 필드 속성 추가
    class Meta:
        model = models.Comment
        fields = ('content',)
