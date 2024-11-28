import datetime

# 获取当前日期
current_date = datetime.date.today()

# 设置计算的生日
birthday = datetime.date(2024, 8, 28)

# 计算年龄
age = current_date.year - birthday.year 

# 计算月份差
month_diff = current_date.month - birthday.month

# 计算是否已经过了生日
if current_date.month < birthday.month or (current_date.month == birthday.month and current_date.day < birthday.day):
    age -= 1
    month_diff+=12
    

# 计算下一次生日的天数
next_birthday = datetime.date(current_date.year, birthday.month, birthday.day)
# 如果已经过了生日，计算下一年的生日
if current_date > next_birthday:
    next_birthday = datetime.date(current_date.year + 1, birthday.month, birthday.day)

days_util_next_birthday = (next_birthday - current_date).days

#计算总天数
total_days = (current_date - birthday).days

print(current_date.month)
print(f"年龄：{age}岁 {month_diff}个月")
print(f"距离下一次生日还有：{days_util_next_birthday}天")
print(f"总天数：{total_days}天")