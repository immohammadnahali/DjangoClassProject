from django import forms
from .models import teach


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