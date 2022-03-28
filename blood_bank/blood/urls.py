from django.urls import path
from . import views

app_name = 'blood'

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('add/', views.donor_create_view, name='donor_add'),
    path('<int:pk>/', views.donor_update_view, name='donor_change'),
    path('ajax/load-branches/', views.load_branches, name='ajax_load_branches'), # AJAX

]

