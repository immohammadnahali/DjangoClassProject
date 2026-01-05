from django import forms
class sign_up(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"نام خود را وارد کنید"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"نام خانوادگی خود را وارد کنید"}))
    email = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"ایمیل خود را وارد کنید",}))
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"نام کاربری خود را وارد کنید",}))
    password = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"رمز عبور خود را وارد کنید",}))
