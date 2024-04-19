"""
URL configuration for web_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from Note import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.NoteList.as_view(), name='note_list'),
    path('create/', views.create_note, name='note_create'),
    # path('create/', views.NoteCreate.as_view(), name='note_create'),
    path('<int:pk>/', views.NoteDetail.as_view(), name='note_detail'),
    path('<int:pk>/update/', views.NoteUpdate.as_view(), name='note_update'),
    path('<int:pk>/delete/', views.NoteDelete.as_view(), name='note_delete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)