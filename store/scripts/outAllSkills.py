import json

def outAllSkills(file_path):
    skills = {}  
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file) 

        for skill in data:
            if skill.get("model") == "data.skill":
                skill_code = skill["fields"].get("code")
                skill_title = skill["fields"].get("title")


                if skill_code and skill_title:
                    skills[skill_code] = skill_title  
    return skills

