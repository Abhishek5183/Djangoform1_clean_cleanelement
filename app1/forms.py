from typing import Any, Dict
from django import forms
from django.http import HttpResponse

def valid_for_a(value):
    if value[0].lower() == 'a':
        raise forms.ValidationError('hello')

def valid_for_age(num):
    if len(str(num)) <= 1:
        raise forms.ValidationError('Your age must be above 10')





class Registration(forms.Form):
    st_name = forms.CharField(max_length=100, validators=[valid_for_a])
    st_age = forms.IntegerField(validators=[valid_for_age])
    st_email = forms.EmailField()
    st_remail = forms.EmailField()
    st_course = forms.CharField(max_length=100)
    botcatcher = forms.CharField(max_length=100, widget=forms.HiddenInput, required=False)

    def clean(self):
        em = self.cleaned_data['st_email']
        rem = self.cleaned_data['st_remail']
        if em != rem:
            raise forms.ValidationError('Not correct')
    def clean_botcatcher(self):
        bot = self.cleaned_data['botcatcher']
        
        if len(bot) > 0:
            raise forms.ValidationError('no')
    '''def clean_st_course(self):
        cu = self.cleaned_data['st_course']

        if cu[0] == 'b':
            raise forms.ValidationError('no')'''#We should not use clean_element for normal input field it should use for only a bot means source code

