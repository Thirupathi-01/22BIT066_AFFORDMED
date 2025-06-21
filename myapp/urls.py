from django.urls import path

from myapp import views
urlpatterns = [
    path('/e', views.get_even),
    path('/p',views.prime),
    path('/r',views.rand),
    path('/f',views.fibo),    # Add more paths as needed
]