"""
URL configuration for upload_files project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from app.views import TeacherListCreateAPIView, TeacherDetailAPIView, StudentListCreateAPIView, StudentDetailAPIView, LeaveFormDetailAPIView, LeaveFormListCreateAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/teachers/', TeacherListCreateAPIView.as_view(), name='teacher-list-create'),
    path('api/teachers/<int:pk>/', TeacherDetailAPIView.as_view(), name='teacher-detail'),
    path('api/students/', StudentListCreateAPIView.as_view(), name='student-list-create'),
    path('api/students/<int:pk>/', StudentDetailAPIView.as_view(), name='student-detail'),

    path('api/leave_forms/', LeaveFormListCreateAPIView.as_view(), name='leave-form-list-create'),
    path('api/leave_forms/<int:pk>/', LeaveFormDetailAPIView.as_view(), name='leave-form-detail'),
]

# ] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
