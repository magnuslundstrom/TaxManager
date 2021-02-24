from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('sign-up/', views.signUp, name='signUp'),
    path('reset-password/', views.resetPassword, name="resetPassword"),
    path('request-password-reset', views.requestResetPassword,
         name='requestPasswordReset')
]
