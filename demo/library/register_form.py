from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import books

class signup_form(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First name'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last name'}))
    
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')

    def __init__(self, *args, **kwargs):
        super(signup_form,self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Enter max 150 words</span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<span class="form-text text-muted"><small>Password must be at least 8 character, can\'t be similar to username, entirely numerical. </span>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Password confirm does not match</span>'
        
# Create Add Record Form
class AddRecordForm(forms.ModelForm):
	book_id = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Book Id", "class":"form-control"}), label="")
	title = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Book Title", "class":"form-control"}), label="")
	author = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Author", "class":"form-control"}), label="")
	borower_name = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Borower Name", "class":"form-control"}), label="")
	identity_id = forms.CharField(required=False, widget=forms.widgets.NumberInput(attrs={"placeholder":"Identity Id", "class":"form-control"}), label="")
	borrow_day = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Borrow Day", "class":"form-control"}), label="")
	return_day = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Return Day", "class":"form-control"}), label="")
	days_late = forms.CharField(required=False, widget=forms.widgets.NumberInput(attrs={"placeholder":"Days Late", "class":"form-control"}), label="")
	fee_return_late = forms.CharField(required=False, widget=forms.widgets.NumberInput(attrs={"placeholder":"Fee Return Late", "class":"form-control"}), label="")

	class Meta:
		model = books
		exclude = ("user",)