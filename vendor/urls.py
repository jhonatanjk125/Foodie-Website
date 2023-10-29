from django.urls import include, path
from . import views
from accounts import views as accounts_views


urlpatterns = [
    path('', accounts_views.myAccount),
    path('profile/', views.vendorProfile, name='vendorProfile'),

]