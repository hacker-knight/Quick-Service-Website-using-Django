from django import forms
from django.forms import ModelForm
from .models import*

class A_signup(forms.ModelForm):
    class Meta:
        model=Shop
        fields='__all__'

class A_Signin(forms.Form):
    a_uname=forms.CharField(label='Enter Username', required=True)
    a_psw=forms.CharField(label='Enter password',max_length=10)
    
class A_Prod(forms.ModelForm):
    class Meta:
        model=Product
        fields='__all__'
        
class Signup(forms.ModelForm):
    class Meta:
        model=Client
        fields='__all__'

class Signin(forms.Form):
    uname=forms.EmailField(label='uname', required=True)
    psw=forms.CharField(label='psw',max_length=10)

class Add_Order(forms.ModelForm):
    class Meta:
        model=Orders
        fields='__all__'

class Final_Order(forms.ModelForm):
    class Meta:
        model=Orders
        fields=('p_deliver',)
