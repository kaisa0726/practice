from django.forms import ModelForm,TextInput,Textarea
from blogs.models import Comment,Replay

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('author','text')
        widgets = {
            'author': TextInput(attrs={
                'class':'form-control',
                'placeholder':'名前',
            }),
            'text':Textarea(attrs={
                'class':'form-control',
                'placeholder':'コメント内容',
            }),
        }
        labels = {
            'author':'',
            'text':'',
        }

class ReplayForm(ModelForm):
    class Meta:
        model = Replay
        fields = ('author','text')
        widgets = {
            'author':TextInput(attrs={
                'class':'form-control',
                'placeholder':'名前',
            }),
            'text':Textarea(attrs={
                'class':'form-control',
                'placeholder':'返信内容',
            })
        }
        labels = {
            'author':'',
            'text':'',
        }