# 读取 books.txt 的内容
with open('books.txt', 'r', encoding='utf-8') as file:
    books = file.read().splitlines()

# 检查是否包含四大名著

classics = ['红楼梦', '三国演义', '西游记', '水浒传']

missing_classics = [classics for classics in classics if classics not in books]

if len(missing_classics) ==0:
    print('已包含四大名著')
else:
    # 补充缺失的名著到文件里
    with open('books.txt', 'a', encoding='utf-8') as file:
      file.write('\n'+'\n'.join(missing_classics))
    print(f'已补充缺失的名著到文件中：{",".join(missing_classics)}')

  

