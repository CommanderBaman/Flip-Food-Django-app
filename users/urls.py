from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path( '', auth_views.LoginView.as_view( template_name='users/login.html'), name= 'users-login'),
    path( 'register/', views.register, name= 'users-register'),
    path( 'logout/', auth_views.LogoutView.as_view( template_name='users/logout.html'), name= 'users-logout'),
    path( 'profile/', views.profile, name= 'users-profile'),
    path( 'password-reset/', auth_views.PasswordResetView.as_view( template_name='users/password-reset.html'), name= 'users-password-reset'),
    path( 'password-reset/done/', auth_views.PasswordResetDoneView.as_view( template_name='users/password-reset-done.html'), name= 'password_reset_done'), # these 3 need to be this because of convention
    path( 'password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view( template_name='users/password-reset-confirm.html'), name= 'password_reset_confirm'),
    path( 'password-reset-complete/', auth_views.PasswordResetCompleteView.as_view( template_name='users/password-reset-complete.html'), name= 'password_reset_complete'),
]