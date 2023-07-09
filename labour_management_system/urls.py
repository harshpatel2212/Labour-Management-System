"""Django_EventManager_WebApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from labour_management_system import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('district', views.district, name='district'),
    path('person', views.person, name='person'),
    path('supervisor', views.supervisor, name='supervisor'),
    path('perform', views.perform, name='perform'),
    path('showDistrict', views.showDistrict, name='showDistrict'),
    path('showPerson', views.showPerson, name='showPerson'),
    path('showSupervisor', views.showSupervisor, name='showSupervisor'),
    path('editDistrict', views.editDistrict, name='editDistrict'),
    path('editPerson', views.editPerson, name='editPerson'),
    path('editSupervisor', views.editSupervisor, name='editSupervisor'),
    path('deleteDistrict', views.deleteDistrict, name='deleteDistrict'),
    path('deletePerson', views.deletePerson, name='deletePerson'),
    path('deleteSupervisor', views.deleteSupervisor, name='deleteSupervisor'),
]
