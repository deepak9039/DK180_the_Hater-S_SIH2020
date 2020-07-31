from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
 
urlpatterns = [
    # path('',views.home,name='home'), 
    path('signup',views.signup,name='signup'),
    path('companysignup/',views.companysignup,name='companysignup'),
    path('login/',views.login,name='login'),        
    path('logout/',views.logout,name='logout'),        
    path('modify/',views.modify_profile,name='modify_profile'),

    path('company_update/',views.company_update,name='company_update'),


    # password seset
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='reset_password'),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_form.html'), name='password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_done.html'), name='password_reset_complete'),
    
    # path('_<str:username>/',views.company_profile,name='company_profile'),
    path('<str:username>/',views.profile,name='profile'),
 ]