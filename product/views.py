from django.shortcuts import render
from django.http import HttpResponse

from . import  models
# Create your views here.
def index(request):
    data=models.product.objects.all()
    Futurecoursess=models.Futurecoursess.objects.all()
    bestteachers=models.bestteachers.objects.all()
    articles=models.article.objects.all()
    teach=models.teach.objects.all()
    return render(request, 'index.html',{
        'data':data,
        'Futurecoursess':Futurecoursess,
        'bestteachers':bestteachers,
        'articles':articles,
        'teach':teach})
def blog(request):
    return render(request, 'blog.html')
def article(request):
    return render(request, 'article.html')
def category(request):
    return render(request, 'category.html')
def contact_us(request):
    return render(request, 'contact_us.html')

def error404(request):
    return render(request, 'error404.html')
def forget_password(request):
    return render(request, 'forget_password.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        new_login=models.new_login(password=password,username=username)
        new_login.save()
        return HttpResponse("saved!!!!!!!!!!!")
    else:
         return render(request, 'login.html')


def panel_user(request):
    return render(request, 'panel_user.html')
def search(request):
    return render(request, 'search.html')
from . import  models
from  . import forms
def sign_up(request):
    if request.method == "POST":
        new_form = forms.sign_up(request.POST)
        if new_form.is_valid():
            name = new_form.cleaned_data['name']
            email = new_form.cleaned_data['email']
            password = new_form.cleaned_data['password']
            user = new_form.cleaned_data['username']
            last_name=new_form.cleaned_data['last_name']
            new_user=models.users(name=name,email=email,password=password,last_name=last_name,username=user)
            new_user.save()
            return HttpResponse(f"name:{name},email:{email},password:{password},last_name:{last_name},username:{user}")
        else:
            return HttpResponse("No Valid!!!!!!!!!!!!")
        return HttpResponse("saved!!!!!!!!!!!")
    elif request.method == "GET":
        new_form = forms.sign_up()
        return render(request, 'sign_up.html',{"form":new_form})



def teach(request):
    if request.method == "POST":
        fullname = request.POST['fullname']
        phonenamber = request.POST['phonenamber']
        email = request.POST['email']
        course_title = request.POST['course_title']
        url = request.POST['url']
        category = request.POST['category']
        comment = request.POST['comment']
        teach = models.teach(fullname=fullname, phone=phonenamber, email=email, course_title=course_title, url=url , category=category, comment=comment )
        teach.save()
        return HttpResponse("saved!!!!!!!!!!!")

    else:
         return render(request, 'teach.html')






def dkp(request,slug):
    data=models.product.objects.filter(slug=slug).first()
    return render(request, 'course.html',{'data':data})

def art(request,slug):
    data=models.article.objects.filter(slug=slug).first()
    return render(request, 'article.html',{'data':data})

def Fc(request,slug):
    data=models.Futurecoursess.objects.filter(slug=slug).first()
    return render(request, 'Futurecoursess.html',{'data':data})

