import json


def showAboutSkill(id,file_path):
    skills = False
    with open(file_path, 'r', encoding='utf-8') as file: 
        data = json.load(file) 
        for skill in data:
            if skill.get("model") == "data.skill":
                if skill["fields"].get("code") == id: 
                    skill_code = skill["fields"].get("code")
                    skill_title = skill["fields"].get("title")
                    skill_specialty =  skill["fields"].get("specialty")
                    skills = True
                      
                    for profession in data:
                        if profession.get("model") == "data.specialty":
                            specialty_code = profession["fields"].get("code")
                            specialty_pk = profession["pk"]
                            if specialty_code in id and  skill_specialty == specialty_pk :  
                                specialty_title = profession["fields"].get("title")
                                specialty_educational = profession["fields"].get("c_type")
                                break             
                    break  
                
    if not skills:
        return 0
      
    else:
        return [specialty_code,specialty_title,specialty_educational,skill_code,skill_title]
