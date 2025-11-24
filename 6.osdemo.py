import os

def list_items(directory):
  items = os.listdir(directory)

  for item in items:
      item_path = os.path.join(directory, item)
      if os.path.isdir(item_path):
         print(f"{item}:目录")
      else:
         print(f"{item}:文件")

list_items('./')

