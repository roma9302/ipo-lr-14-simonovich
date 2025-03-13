from django.urls import path
from .views import home_page,about_me_page,bag_shop

urlpatterns = [
    path('', home_page, name='home_page'),
    path('about_me', about_me_page, name='about_me'),
    path('bag_shop', bag_shop, name='bag_shop'),
]
