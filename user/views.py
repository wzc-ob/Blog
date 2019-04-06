from django.contrib.auth.decorators import login_required
from django.http import response
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login ,logout
# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import TemplateView

from article.models import Article


def user(request):
    article = Article.objects.filter(id=14).values('article').first()
    return render(request,'user.html',{'article':article})


def information(request,id):
    id = id
    return render(request,'UserInformation.html',{'id':id} )

def logoutuser(request):
    logout(request)
    return redirect(reverse("blog:list"))


class Modify(TemplateView):
    @method_decorator(login_required)
    def get(self, request):
        return render(request, 'modify.html')


    def post(self, request):
        password = request.POST['password']
        user = User.objects.get(id = request.user.id)
        print(password)
        if password :
            user.set_password(password)
            user.save()
            return redirect(reverse("user:login"))
        else:
            return render(request, 'modify.html')



class Login(View):
    def get(self,request):
        return render(request, 'login.html')
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user =authenticate(username = username , password = password)
        if user is not None:
            if user.is_active:
                login(request, user)
            return redirect(reverse("blog:list"))
        else:
            return render(request, 'login.html')


class Register(View):
    def get(self,request):
        return render(request, 'register.html')
    def post(self, request):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username,email,password)
        user.save()
        return redirect(reverse("user:login"))