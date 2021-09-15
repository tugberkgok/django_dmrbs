from django import forms
from .models import Worker, Device


class LoginForm (forms.Form):
    username = forms.CharField(label="Kullanıcı Adı")
    password = forms.CharField(label="Parola", widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, label="Kullanıcı adı")
    password = forms.CharField(max_length=20, label="Parola", widget=forms.PasswordInput)
    confirm = forms.CharField(max_length=20, label="Parolayı doğrula", widget=forms.PasswordInput)
    special_key= forms.CharField(max_length=20, label="Özel Anahtar", widget=forms.PasswordInput)


    def clean(self):

        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")
        special_key=self.cleaned_data.get("special_key")


        if password and confirm and password != confirm:
            raise forms.ValidationError("Parolalar Eşleşmiyor")


        if special_key != "piriadmin":
            raise forms.ValidationError("Kullanıcı Açmaya Yetkiniz Yok")


        values = {"username": username, "password": password}
        return values



class DataForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ["stok", "device", "number", "brand", "model", "serial", "status", "exp", "iz", "price", "take_date", "zim_date"]



class WorkerName(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ["person"]

class File(forms.FileInput):
    pass


