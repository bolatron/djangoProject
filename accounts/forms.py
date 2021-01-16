# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms

from .models import Account

# Definindo um formulário para o modelo 'Account'.
# O formulário é inserido direto no html para facilitar a criação da sua parte 
# visual. 
class AccountModelForm(forms.ModelForm):

    # Deixando os campos nickname e observations como não obrigatórios.
    nickname = forms.CharField(required=False)
    observations = forms.CharField(required=False)

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'age', 'birth_date', 'email', 'nickname', 'observations']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 200, 'placeholder': 'Primeiro nome'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 200, 'placeholder': 'Sobrenome'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Idade'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Data de nascimento (AAAA/MM/DD)'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'maxlength': 200, 'placeholder': 'Email'}),
            'nickname': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 200, 'placeholder': 'Apelido'}),
            'observations': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 800, 'placeholder': 'Observações'})
        }

        error_messages = {
            'first_name': {
                'required': 'Este campo é obrigatório!'
            },
            'last_name': {
                'required': 'Este campo é obrigatório!'
            },
            'age': {
                'required': 'Este campo é obrigatório!'
            },
            'birth_date': {
                'required': 'Este campo é obrigatório!'
            },
            'email': {
                'required': 'Este campo é obrigatório!'
            }
        }
