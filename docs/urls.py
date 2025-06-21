from django.urls import path
from docs import views

urlpatterns = [
    path('upload/', views.upload_document, name='upload_doc'),
    path('table/', views.table_data, name='table_doc'),
]
