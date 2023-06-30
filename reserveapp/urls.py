from django.urls import path, re_path
from . import views

app_name = 'reserveapp'

urlpatterns = [
    path('new/', views.reserve_new, name='reserve_new'),  # Create
    path('<int:pk>/edit/', views.reservedroom_edit, name='reservedroom_edit'),  # Update
    path('<int:pk>/delete/', views.reservedroom_delete, name='reservedroom_delete'),  # Delete

    path('', views.reservedroom_list, name='reservedroom_list'),  # Read
    path('<int:pk>/', views.reservedroom_detail, name='reservedroom_detail'),  # Read-Detailed

    path('reservation/', views.myreservedroom_list, name='myreservedroom_list'),  # Read-User
]