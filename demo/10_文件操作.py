'''
1、 找到文件
open(path, mode='', encoding='')
path  路径 相对路径       绝对路

mode 模式 
   r: read 读取 

encoding 编码
'''

f = open("/Users/zhaoxin/code/github/learnPython/demo/我让窗子开着.txt",mode='r', encoding='utf-8')
content = f.read()
print(content)
from pathlib import Path

# 使用脚本所在目录下的文件路径，避免相对工作目录导致的 FileNotFoundError
file_path = Path(__file__).resolve().parent / '我让窗子开着.txt'

# 如果文件不存在，写入示例内容（可按需修改）
if not file_path.exists():
   file_path.write_text('这是示例内容\n', encoding='utf-8')
   print(f'已创建示例文件: {file_path}')

with file_path.open(mode='r', encoding='utf-8') as f2:
   content2 = f2.read()
   print(content2)


open('我让窗子开着.txt')