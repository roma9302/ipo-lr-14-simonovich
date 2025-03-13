from django.shortcuts import render

def home_page(request):
    return render(request, 'home_page.html') #render возвращает шаблон html на запрос пользователя

def about_me_page(request):
    return render(request, 'about_me_page.html') #render возвращает шаблон html на запрос пользователя

def bag_shop(request):
    return render(request, 'bag_shop.html') #render возвращает шаблон html на запрос пользователя