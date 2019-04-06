from django.urls import path

from user import views
app_name = 'user'
urlpatterns = [
    path('login/',views.Login.as_view(),name = 'login'),
    path('register/',views.Register.as_view(),name = 'register'),
    path('information/<id>',views.information,name = 'information' ),
    path('user/',views.user,name = 'user'),
    path('logout/',views.logoutuser,name = 'logout'),
    path('modufy',views.Modify.as_view(),name = 'modify')
]