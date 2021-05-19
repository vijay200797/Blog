from django import forms
from .models import Post

class Post_Form(forms.ModelForm):
    class Meta:
        model = Post
        readonly_fields=('post_datetime',)
        fields = ['post_title', 'post_content', 'post_type', 'post_status', 'post_additionalContext']
        widgets = {
            'post_title': forms.TextInput(attrs={'class':'form-control'}),
            'post_content': forms.TextInput(attrs={'class':'form-control'}),
            'post_type': forms.Select(attrs={'class':'form-control'}),
            'post_status': forms.Select(attrs={'class':'form-control'}),
            'post_additionalContext': forms.Textarea(attrs={'class':'form-control'}),
        }
