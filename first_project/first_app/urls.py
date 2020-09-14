from django.conf.urls import url
from first_app import views
from django.urls import path

#Template URLs
app_name = 'first_app'

urlpatterns =[
    # path('index', views.index,name="index"),
    # #path('help', views.help,name="help"),
    # path('formpage', views.form_name_view,name="form_name"),
    path('register', views.register,name="register"),
    path('user_login', views.user_login,name="user_login"),



]
