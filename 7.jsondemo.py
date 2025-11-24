import json

# 读取JSON文件
with open('database.json', 'r') as file:
    json_data = json.load(file)

print(json_data)

json_data['port'] = 5432
json_data['name'] = "中文"

# ensure_ascii=False 解决中文乱码确保中文以原始的 Unicode 形式编码而不是ASCII编码
with open('database.json', 'w') as file:
    json.dump(json_data, file, indent=2, ensure_ascii=False)

print('JSON文件已更新')