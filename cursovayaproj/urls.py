"""cursovayaproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from cursovayaapp.views import *
from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainPage.as_view()),
    path('material.html', MaterialPage.as_view()),
    path('service.html', ServicePage.as_view()),
    path('review.html', ReviewPage.as_view()),
    path('form_review.html', FormReviewPage.as_view()),
    path('enter.html', EnterPage.as_view()),
    path('master.html', MasterPage.as_view()),
    path('order.html', OrderPage.as_view()),
    path('edit_order.html/<int:id>', EditOrderPage.as_view()),
    path('admin.html', AdminPage.as_view()),
    path('<int:id>', AdminMasterPage.as_view()),
    path('back', SessionCheck.as_view()),
]
