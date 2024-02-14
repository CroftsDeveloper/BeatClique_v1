from django.urls import path
from django.contrib.auth import views as auth_views 

from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('account/', views.account_view, name='account'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('account/update/', views.account_update, name='account_update'),

]
