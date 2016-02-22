# -*- coding: utf-8 -*-

from django import forms

from .models import Schedule

class ScheForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ('name', 'phone', 'email', 'symptom')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'氏名'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'メールアドレス'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'電話番号'}),
            'symptom': forms.Textarea(attrs={'class': 'form-control', 'rows':'5', 'placeholder':'症状などをご入力ください'}),
        }

    def __init__(self, *args, **kwargs):
        super(ScheForm, self).__init__(*args, **kwargs)
        self.fields['name'].error_messages = {'required': '氏名は必須です'}
        self.fields['email'].error_messages = {'required': 'メールアドレスは必須です'}
        self.fields['phone'].error_messages = {'required': '電話番号は必須です'}
