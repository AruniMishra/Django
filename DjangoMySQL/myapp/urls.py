from django.urls import re_path 
from myapp import views

from django.conf.urls.static import static
from django.conf import settings

from rest_framework.routers import DefaultRouter

from django.urls import path, include
from .views import DepartmentViewSet

router = DefaultRouter()
router.register(r"department", DepartmentViewSet)

urlpatterns=[
    # re_path(r'^department$',views.departmentApi),
    # re_path(r'^department/([0-9]+)$',views.departmentApi),

    path("", include(router.urls)),

    re_path(r'^employee$',views.employeeApi),
    re_path(r'^employee/([0-9]+)$',views.employeeApi),

    re_path(r'^employee/savefile',views.SaveFile)
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)