from django.forms import ModelForm
from django import forms
from .models import GroupMessage, ChatGroup


class ChatMessageCreateForm(ModelForm):
    
    class Meta:

        model = GroupMessage
        fields = ['body']
        widgets = {
            'body': forms.TextInput(attrs={'placeholder': 'Add Message ...', 'class': 'form-control rounded-3 p-2 text-dark', 'maxlength': '300', 'autofocus': True}),
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['body'].label = ''

