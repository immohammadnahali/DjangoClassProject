from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
from . import forms
from django.views import View
import re
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required


class sign_up(View):
    def post(self, request):
        new_form = forms.sign_up(request.POST)
        if not new_form.is_valid():
            return render(request, 'sign_up.html', {"form": new_form})

        name = new_form.cleaned_data['name']
        last_name = new_form.cleaned_data['last_name']
        email = new_form.cleaned_data['email']
        username = new_form.cleaned_data['username']
        password = new_form.cleaned_data['password']

        has_error = False

        # 1. بررسی تکراری بودن ایمیل
        if models.new_user.objects.filter(email=email).exists():
            new_form.add_error("email", "این ایمیل قبلاً ثبت شده است.")
            has_error = True

        # 2. بررسی تکراری بودن یوزرنیم
        if models.new_user.objects.filter(username=username).exists():
            new_form.add_error("username", "این نام کاربری قبلاً استفاده شده است.")
            has_error = True

        # 3. یوزرنیم فقط شامل حروف انگلیسی، عدد و _
        if not re.match(r'^[a-zA-Z0-9_]+$', username):
            new_form.add_error(
                "username",
                "نام کاربری شامل حروف انگلیسی، عدد و _"
            )
            has_error = True

        # 4. طول پسورد
        if len(password) < 8:
            new_form.add_error(
                "password",
                "رمز عبور باید حداقل ۸ کاراکتر باشد."
            )
            has_error = True

        # 5. وجود حروف بزرگ، کوچک و عدد در پسورد
        if not re.search(r'[A-Z]', password):
            new_form.add_error(
                "password",
                "رمز عبور باید حداقل یک حرف بزرگ داشته باشد."
            )
            has_error = True

        if not re.search(r'[a-z]', password):
            new_form.add_error(
                "password",
                "رمز عبور باید حداقل یک حرف کوچک داشته باشد."
            )
            has_error = True

        if not re.search(r'[0-9]', password):
            new_form.add_error(
                "password",
                "رمز عبور باید حداقل یک عدد داشته باشد."
            )
            has_error = True

        if has_error:
            return render(request, 'sign_up.html', {"form": new_form})

        # 6. ساخت کاربر
        user = models.new_user(
            first_name=name,
            last_name=last_name,
            email=email,
            username=username,
            is_active=True
        )
        user.set_password(password)
        user.save()

        return redirect("/account/login/")

    def get(self, request):
        new_form = forms.sign_up()
        return render(request, 'sign_up.html', {"form": new_form})


class login(View):
    def post(self, request):
        new_form = forms.login(request.POST)
        if new_form.is_valid():
            username_form = new_form.cleaned_data['username']
            password_form = new_form.cleaned_data['password']
            check_user = models.new_user.objects.filter(username=username_form).first()

            if check_user:
                if check_user.check_password(password_form):

                    auth_login(request, check_user)

                    # ✅ Remember Me Logic
                    if not request.POST.get('remember_me'):
                        request.session.set_expiry(0)
                    else:
                        request.session.set_expiry(1209600)

                    return redirect("/panel_user/")
                else:
                    return HttpResponse("Not Valid pass !!!!!!!!!")
            else:
                return HttpResponse("Not Valid user !!!!!!!!!")
        else:
            return HttpResponse("Not Valid Form !!!!!!!!!")

    def get(self, request):
        new_form = forms.login()
        return render(request, 'login.html', {"form": new_form})


@login_required(login_url="/account/login/")
def panel_user(request):
    return render(request, 'panel_user.html', {
        "user": request.user
    })

def logout(request):
    auth_logout(request)
    return redirect("/")
# class sign_up(View):
#     def post(self, request):
#         new_form = forms.sign_up(request.POST)
#         if new_form.is_valid():
#             name = new_form.cleaned_data['name']
#             email = new_form.cleaned_data['email']
#             password = new_form.cleaned_data['password']
#             user = new_form.cleaned_data['username']
#             last_name = new_form.cleaned_data['last_name']
#             check_email: bool = models.new_user.objects.filter(email=email).exists()
#             val = 0
#             if len(password) < 8:
#                 new_form.add_error("password", "تعداد کاراکتر پسورد کمتر از 8 می باشد")
#                 val = 1
#             if check_email:
#                 new_form.add_error("email", "ایمیل شما تکراری می باشد!!!")
#                 val = 1
#             if val == 1:
#                 return render(request, 'sign_up.html', {"form": new_form})
#             else:
#                 new_user_test = models.new_user(
#                     first_name=name, last_name=last_name, email=email, username=user, is_active=True)
#                 new_user_test.set_password(password)
#                 new_user_test.save()
#                 return redirect("/login")
#         else:
#             return HttpResponse("No Valid!!!!!!!!!!!!")
#         # return render(request, 'sign_up.html', {"form": new_form})
#
#     def get(self, request):
#         new_form = forms.sign_up()
#         return render(request, 'sign_up.html', {"form": new_form})
