# -*- coding: utf-8 -*-
#!/usr/bin/env python
import re
from django import forms
from django.utils.translation import ugettext_lazy as _

from feedback.models import *

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact

    def clean_phone(self):
        """Проверка телефонного номера (>10 цифр)"""
        phone = self.cleaned_data['phone']
        stripped_phone = strip_non_numbers(phone)
        if len(stripped_phone) < 11:
            raise forms.ValidationError(_(u"""
            Введите правильный телефон, например (8-920-351-21-21 или 89203512121)"""))
        return self.cleaned_data['phone']

def strip_non_numbers(data):
    """Удаляет все символы которые не являются числом
    >>> strip_non_numbers('988f2ds2')
    '98822'
    """
    non_numbers = re.compile('\D')
    return non_numbers.sub('', data)

# class ContactForm(forms.Form):
#     name = forms.CharField(max_length=20)
