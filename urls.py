from django.contrib import admin
from django.urls import path
from visitors import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homePage,name='home'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('about/', views.about, name='about'),
    path('visitorlist/', views.visitor_list, name='visitor_list'),
    path('add/', views.add_visitor, name='add_visitor'),
    path('update/<int:id>/', views.update_visitor, name='update_visitor'),
    path('delete/<int:id>/', views.delete_visitor, name='delete_visitor'),
    path('staff-login/', auth_views.LoginView.as_view(template_name='staff_login.html'), name='staff_login'),
    path('visitor-action/', views.visitor_action, name='visitor_action'),
    path('add-visitor/', views.add_visitor, name='add_visitor'),
    path('staff-visitor-log/', views.staff_visitor_log, name='staff_visitor_log'),
]
