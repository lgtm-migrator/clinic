# -*- coding: utf-8 -*-

from django import forms

from .models import Schedule

class ScheForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ('name', 'phone', 'email', 'symptom')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'氏名', 'required': True}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'電話番号', 'required': True}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'連絡先', 'required': True}),
            'symptom': forms.Textarea(attrs={'class': 'form-control', 'rows':'5', 'placeholder':'症状などをご入力ください'}),
        }