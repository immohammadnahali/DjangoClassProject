from django import forms
from .models import teach
from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "email", "message"]
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control rounded-pill",
                "placeholder": "نام خود را وارد کنید ..."
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control rounded-pill",
                "placeholder": "ایمیل خود را وارد کنید ..."
            }),
            "message": forms.Textarea(attrs={
                "class": "form-control w-100 rounded-lg p-3",
                "rows": 6,
                "placeholder": "پیام خود را وارد کنید ..."
            }),
        }


class TeachPublicForm(forms.ModelForm):
    class Meta:
        model = teach
        fields = [
            "fullname",
            "phone",
            "email",
            "educational_stage",  # اگر منظورت از "عنوان" اینه
            "category",
            "url",
            "comment",
        ]