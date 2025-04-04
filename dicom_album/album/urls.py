from django.urls import path
from album import views

urlpatterns = [
    path('', views.upload_file, name='upload'),
    path('list/', views.dicom_list, name='dicom_list'),
]
