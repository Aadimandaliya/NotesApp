from django import forms
from.models import usersignup,mynotes,feedback

class signupform(forms.ModelForm):
    class Meta:
        model = usersignup
        fields = '__all__'

class notesform(forms.ModelForm):
    class Meta:
        model = mynotes
        fields = '__all__'

class updateform(forms.ModelForm):
    class Meta:
        model = usersignup
        fields = ['firstname','lastname','username','email','password','city','state','mobile']

class feedbackform(forms.ModelForm):
    class Meta:
        model = feedback
        fields = '__all__'