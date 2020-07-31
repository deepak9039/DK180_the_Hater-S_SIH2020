from django.urls import path
from . import views
 
urlpatterns = [
    path('',views.home,name='home'),
    path('subscribe/',views.subscribe,name='subscribe'),
    path('search/',views.search,name='search'),
    path('notification/',views.notification,name='notification'),
    path('makeRead/',views.makeRead),
    # path('signup',views.signup,name='signup'),
    # path('login/',views.login,name='login'),        
    # path('<str:username>/',views.profile,name='profile')
 ]