from django.urls import path

from comment import views
app_name = 'comment'
urlpatterns = [
    path('',views.display,name = 'display'),
    path('comment/<reply_id_id>',views.comment,name = 'comment'),
]