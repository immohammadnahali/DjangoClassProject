from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
from . import forms
from django.views import View
from .forms import ContactForm


def index(request):
    data = models.product.objects.all()
    Futurecoursess = models.Futurecoursess.objects.all()
    bestteachers = models.bestteachers.objects.all()
    articles = models.article.objects.all()
    teach = models.teach.objects.all()
    return render(request, 'index.html', {
        'data': data,
        'Futurecoursess': Futurecoursess,
        'bestteachers': bestteachers,
        'articles': articles,
        'teach': teach})


def article(request):
    return render(request, 'article.html')


def category(request):
    return render(request, 'category.html')


def contact_us(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "contact_us.html", {
                "form": ContactForm(),
                "success": True
            })
    else:
        form = ContactForm()

    return render(request, "contact_us.html", {
        "form": form
    })


def error404(request):
    return render(request, 'error404.html')


def search(request):
    return render(request, 'search.html')


def teach(request):
    if request.method == "POST":
        fullname = request.POST.get('fullname')
        phone = request.POST.get('phonenamber')
        email = request.POST.get('email')
        title = request.POST.get('course_title')
        url = request.POST.get('url')
        category = request.POST.get('category')
        comment = request.POST.get('comment')


        models.teach.objects.create(
            fullname=fullname,
            phone=phone,
            email=email,
            title=title,
            url=url,
            category=category,
            comment=comment,
            image=""
        )

        return HttpResponse("saved!!!!!!!!!!!")

    return render(request, 'teach.html')


def dkp(request, slug):
    data = models.product.objects.filter(slug=slug).first()
    return render(request, 'course.html', {'data': data})


def art(request, slug):
    data = models.article.objects.filter(slug=slug).first()
    return render(request, 'article.html', {'data': data})


def Fc(request, slug):
    data = models.Futurecoursess.objects.filter(slug=slug).first()
    return render(request, 'Futurecoursess.html', {'data': data})
