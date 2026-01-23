from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
from . import forms
from django.views import View


class sign_up(View):
    def post(self, request):
        new_form = forms.sign_up(request.POST)
        if new_form.is_valid():
            name = new_form.cleaned_data['name']
            email = new_form.cleaned_data['email']
            password = new_form.cleaned_data['password']
            user = new_form.cleaned_data['username']
            last_name = new_form.cleaned_data['last_name']
            check_email: bool = models.new_user.objects.filter(email=email).exists()
            val = 0
            if len(password) < 8:
                new_form.add_error("password", "تعداد کاراکتر پسورد کمتر از 8 می باشد")
                val = 1
            if check_email:
                new_form.add_error("email", "ایمیل شما تکراری می باشد!!!")
                val = 1
            if val == 1:
                return render(request, 'sign_up.html', {"form": new_form})
            else:
                new_user_test = models.new_user(
                    first_name=name, last_name=last_name, email=email, username=user, is_active=True)
                new_user_test.set_password(password)
                new_user_test.save()
                return redirect("/login")
        else:
            return HttpResponse("No Valid!!!!!!!!!!!!")
        # return render(request, 'sign_up.html', {"form": new_form})

    def get(self, request):
        new_form = forms.sign_up()
        return render(request, 'sign_up.html', {"form": new_form})
