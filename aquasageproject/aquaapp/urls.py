from django.urls import path
from . import views

urlpatterns = [
    path("", views.welcome, name="welcome"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("nodeview/", views.nodeview, name="nodeview"),
    path("mapview/", views.mapview, name="mapview"),


    # # Register/Login/Logout
    # path('user_login/', views.user_login, name='user_login'),
    # path('user_logout/', views.user_logout, name='user_logout'),
    # path('user_register/', views.user_register, name='user_register'),
  
    
    
    # path("business", views.business, name="Business"),
    # path("about/", views.about, name="AboutUs"),
    # path("contact/", views.contact, name="ContactUs"),
    # path("products/<int:myid>", views.productView, name="ProductView"),
    # path("products/<str:myslug>", views.productView, name="ProductView"),
]
