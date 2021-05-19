from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.sign_up, name='signup'),
    path('portal/', views.portal, name='portal'),
    path('logout/', views.logout, name='logout'),
    path('setting/', views.setting, name='setting'),

]