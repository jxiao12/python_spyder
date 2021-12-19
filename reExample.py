import re

# 创建模式对象
pat = re.compile("AA")
m = pat.search("UC San Deigo")
compare_m = pat.search("AA American, THE US")

print(m)
print(compare_m)

#===================
a = re.search("aa", "UC San Deigo") #第一个元素是规则，第二个是被校验对象
compare_a = re.search("AA", "AA American, THE US")
print(a)
print(compare_a)

#===================
print(re.findall("a", "ahdiqhrlkb,jfhoihfa"))
print(re.findall("[a-z]", "AndaihANKHBJKAGdkjhAD"))
print(re.findall("[a-z]+", "AndaihANKHBJKAGdkjhAD"))



#===================
print(re.sub("A", "a", "adihAKLHDihAjdlkDKLhioLKAJ")) #找到A然后用a替换
       # 第一个是要找对象，第二个是替换目标，第三个是检验对象