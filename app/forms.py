from django import forms
from django.http import HttpResponse

def check_for_a(value):
    if value[0].lower()=='a':
        raise forms.ValidationError("cannot start with a")

def check_for_len(value):
    if value>30:
        raise forms.ValidationError("age is more")
        
class StudentForm(forms.Form):
    name=forms.CharField(max_length=100,validators=[check_for_a])
    age=forms.IntegerField(validators=[check_for_len])
    email=forms.EmailField()
    re_enter_email=forms.EmailField()
    botcatcher=forms.CharField(max_length=100,widget=forms.HiddenInput,required=False)

    def clean(self):
        e=self.cleaned_data['email']
        r=self.cleaned_data['re_enter_email']
        if e!=r:
            raise forms.ValidationError('Data is invalid')
    
    '''def clean_name(self):
        n=self.cleaned_data['name']
        if len(n)>12:
            raise forms.ValidationError('age is less')'''
    #(clean_element method cannot use for all the elements ,it is only suitable for botcatcher)

    def clean_botcatcher(self):
        bot=self.cleaned_data['botcatcher']
        if len(bot)>0:
            raise forms.ValidationError('length is more')

