"""
URL configuration for CodeWise project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from Repository import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('question/',views.QuestionList_CreationView.as_view()),
    path('question/<pk>/',views.QuestionRetriveUpdateDeleteView.as_view()),

    path('submission/',views.SubmissionListCreateView.as_view()),
    path('submission/<int:pk>/',views.SubmissionRetriveUpdateDelete.as_view()),

    path('submission/<int:pk>/evaluate/',views.EvaluateSubmissionView.as_view()),
]
