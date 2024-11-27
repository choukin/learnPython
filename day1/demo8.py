''' 将文本中的水果按照空格拆分，去除重复项并对其进行排序 '''
text = 'apple banana cherry apple banana'
words = text.split(' ')
unique_wrods = set(words)
sorted_words = sorted(unique_wrods)
print(sorted_words)
