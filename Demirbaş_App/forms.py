from django import forms
from .models import Worker, Device

class LoginForm (forms.Form):
    username = forms.CharField(label= "Kullanıcı Adı")
    password = forms.CharField(label= "Parola", widget= forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, label="Kullanıcı adı")
    password = forms.CharField(max_length=20, label="Parola", widget=forms.PasswordInput)
    confirm = forms.CharField(max_length=20, label="Parolayı doğrula", widget=forms.PasswordInput)


    def clean(self):

        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm and password != confirm:
            raise forms.ValidationError("Parolalar Eşleşmiyor")
        values = {"username": username, "password": password}
        return values



class DataForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ["stok", "device", "number", "brand", "model", "serial", "status", "exp"]



class WorkerName(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ["person"]