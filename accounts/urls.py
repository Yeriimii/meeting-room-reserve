from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views
from .forms import LoginForm


app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(
        template_name='accounts/login_form.html'
    ), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('profile/<int:pk>/', views.profile_detail, name='profile_detail'),  # Read-Detailed
    path('signup/', views.signup, name='signup'),
]