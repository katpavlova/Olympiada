from django import forms
from .models import *


class AddBlankForm(forms.ModelForm):
    class Meta:
        model = Blank
        fields = ['fio', 'education', 'phone', 'email']
        widgets = {
            'fio' : forms.TextInput(attrs={'class': 'form-input form-control', 'placeholder': 'Иванов Иван Иванович'}),
            'education': forms.TextInput(attrs={'class': 'form-input form-control', 'placeholder': 'РГЭУ (РИНХ)'}),
            'phone': forms.TextInput(attrs={'class': 'form-input form-control', 'placeholder': '+7 (___) ___-__-__'}),
            'email': forms.TextInput(attrs={'class': 'form-input form-control', 'placeholder': 'example@mail.ru'}),

        }