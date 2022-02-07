from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('members', views.members, name='members'),
    path('articles', views.articles, name='articles'),
    path('contact', views.contact, name='contact'),
    path('branchfiles/<branchwise>', views.branchfiles, name='branchfiles'),
    path('deletefile/<branch>/<filename>', views.deletefile, name='deletefile'),
    path('adminpanel', views.adminpanel, name='adminpanel')

]
