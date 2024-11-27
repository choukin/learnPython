personal_info={}
personal_info['name']='韶瑾'
personal_info['age']=18
personal_info['city']='南砚池'

personal_ap = {"name":'毛',"age":20,"city":'北京'}

print(personal_info)

print(personal_ap)

print(len(personal_ap))

personal_info.update(personal_ap)
print(personal_info)

personal_info3 = dict(name='韶瑾',age=18,city='南砚池')
print(personal_info3)