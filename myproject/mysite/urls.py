from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('members', views.members, name='members'),
    path('articles', views.articles, name='articles'),
    path('loan', views.loan, name='loan'),
    path('contact', views.contact, name='contact'),
    path('branchfiles/<branchwise>', views.branchfiles, name='branchfiles'),
    path('deletefile/<branch>/<filename>', views.deletefile, name='deletefile'),
    path('adminpanel', views.adminpanel, name='adminpanel'),
    path('deleteform/<int:id>', views.deleteform, name='deleteform'),
     path('deletecontact/<int:id>', views.deletecontact, name='deletecontact'),
    path('formstatus/<int:id>',views.formstatus,name='formstatus'),
    path('login',views.user_login,name="login"),
    path('logout',views.user_logout,name="logout"),

]
