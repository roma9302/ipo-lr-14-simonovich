from django.urls import path
from .views import home_page,about_me_page,bag_shop, out_skills_page,skill_info

urlpatterns = [
    path('', home_page, name='home_page'),
    path('about_me', about_me_page, name='about_me'),
    path('bag_shop', bag_shop, name='bag_shop'),
    path('spec', out_skills_page, name='spec'),
    path('spec/<str:skill_code>/', skill_info, name='skill_info'),
]
