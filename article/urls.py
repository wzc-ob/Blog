from django.conf import settings
from django.templatetags.static import static
from django.urls import path

from article import views
app_name = 'article'
urlpatterns = [
    # path('list/',views.ArticleListView.as_view(),name = 'list'),
    path('list/', views.imglist, name='list'),
    path('article/<article_id>',views.Articleview.as_view(),name = 'article'),
    path('article/<article_id>/<reply_id_id>',views.comment,name = 'comment')
]