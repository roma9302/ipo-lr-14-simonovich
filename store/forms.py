from django import forms

class SkillCodeSearch(forms.Form):
    skill_code = forms.CharField(max_length=15, label="Введите код Квалификации")
