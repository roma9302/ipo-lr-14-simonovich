from django.shortcuts import render,redirect
from .forms import SkillCodeSearch
from store.scripts.outAllSkills import *
from store.scripts.showAboutSkill import *

def home_page(request):
    return render(request, 'home_page.html') #render возвращает шаблон html на запрос пользователя

def about_me_page(request):
    return render(request, 'about_me_page.html') #render возвращает шаблон html на запрос пользователя

def bag_shop(request):
    return render(request, 'bag_shop.html') #render возвращает шаблон html на запрос пользователя

def out_skills_page(request):
    form = SkillCodeSearch(request.POST or None)
    if(form.is_valid()):
        skill_code = form.cleaned_data['skill_code']
        return redirect(f'spec/{skill_code}/')
    skills = outAllSkills('store/data/dump.json')
    return render(request, 'skills_list.html', {'skills': skills,'form': form})

def skill_info(request, skill_code):
    skill_data = showAboutSkill(skill_code, 'store/data/dump.json')
    return render(request, "out_skill_info.html", {"skill_data": skill_data})
