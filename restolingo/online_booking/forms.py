from django import forms
# from myapp.models import Dreamreal


class CustomerForm(forms.Form):
    username = forms.CharField(max_length = 100)
    phone_number = forms.IntegerField()


    # def clean_message(self):
    #     username = self.cleaned_data.get("username")
    #     dbuser = Dreamreal.objects.filter(name = username)
  
    #     if not dbuser:
    #         raise forms.ValidationError("User does not exist in our db!")
  
    #     return username

class ConfirmForm(forms.Form):
    manager_password = forms.CharField(widget = forms.PasswordInput())

