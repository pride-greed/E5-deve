import re

content = 'Hello 1234567 is a number. Regex String'
result = re.match('^Hello (\d+).*String$', content)
# "^Hello " 匹配字符串开头; (\d+) 匹配任意个数字; .* 匹配任意字符(换行符除外); 
# String$ 匹配字符串结尾
if result:
    print(result.group(1)) # 取出第一个括号的内容, 即(\d+)中的数字
