from django.urls import path
from . import views

urlpatterns = [
    path('', views.l, name='home'),  # Home page
    path('login/', views.p, name='p'),  # Login page
    path('signin/', views.sp, name='sup2'),  # Signup page
    path('search/', views.sr, name='search2'),  # Search functionality
    path('property/', views.pr, name='prop'),  # Properties listing
    path('logout/', views.lt, name='logout'),  # Logout functionality
]
