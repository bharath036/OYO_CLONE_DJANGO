from django.contrib import admin
from django.urls import path
from accounts import views

urlpatterns = [
    path('login/',views.login_page,name='login_page'),
    path('register/',views.register,name="register"),
    path('send_otp/<email>/',views.send_otp,name="send_otp"),
    path('verify-otp/<email>/',views.verify_otp,name="verify_otp"),


    path('verify-otp/<email>/',views.verify_otp,name="verify_otp"),
    path('register-vendor/',views.register_vendor,name="register_vendor"),
    path('login-vendor/',views.login_vendor,name="login_vendor"),
    path('dashboard/',views.dashboard,name = "dashboard"),
     path('add-hotel/',views.add_hotel,name = "add_hotel"),



    path('verify-account/<token>/',views.verify_email_token,name="verify_email_token"),

]