from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect ,HttpResponse

# Create your views here.
from django.urls import reverse

from article.models import Article
from comment.models import Comment, Relpy

from article.views import Articleview

@login_required
def comment(request,reply_id_id):
    article_id = Comment.objects.filter(id = reply_id_id).first().article_id
    reply_id_id = request.POST['id']
    user_id = request.user.id
    reply = request.POST['reply']
    # print(user_id,reply_id_id,reply)
    rep = Relpy(reply = reply,user_id = user_id, reply_id_id = reply_id_id)
    rep.save()
    return Articleview().get(request,article_id)
    # return HttpResponse('success')


def display(request):
    dicts = {}
    comments = Comment.objects.all()
    for comment in comments:
        replys = Relpy.objects.filter( reply_id_id = comment.id).all()
        dicts[comment] = replys
    print(dicts)
    return render(request,'reply.html',{'dicts':dicts})
