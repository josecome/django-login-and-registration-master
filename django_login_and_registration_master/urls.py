from django.contrib import admin
from django.urls import path
from users import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.Home),
    path('dashboard/', views.Dashboard),
    path('login/', views.loginPage, name='login'),
    path('admin/', admin.site.urls),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.registrationPage, name='register'),
    path('change-password/', auth_views.PasswordChangeView.as_view()),
]
