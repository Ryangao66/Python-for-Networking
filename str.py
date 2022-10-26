# 单引号等于双引号
a = "cisco"
b = 'cisco'
a = b


#换行

xh = "Cisco and Juniper are very good, and they \
are racing."

print(xh)



# 字符串包含反斜杠
a = 'd:\router\config'
print(a)

path = "var\\log\\bacula"
print(path)


b = 'd:\\router\config'
print(b)

c = r"d:\router\config" # r means the original meaning
print(c)

d = "C:\some\name"  #\n means new lien
print(d)

e = r"C:\some\name" # r means the original meaning
print(e)

# 横向制表符 \t 一般用于对齐数据列

print("name \t Ryan")
print("tel \t 022xxx2821")
print("addr \t Napier")


# 原始字符串 r 或者R
print("C:\some\name")   #\n 表示新行
print(r"C:\come\name")

# 多行字符串 """ xxx """
print('''
Usage: man 

\t -h    \t HELP
\t -a    \t ALL
\t -L   \t LARGE

''')

# 整型转换为字符串
sint = 1234567
sint1 = str(sint)
print(sint,type(sint),'\n', sint1,type(sint1))

# 字符串长度测量及索引
s1 = 'supercalifragilisticexpialidocious'
print(len(s1))
print(s1[8])

# 字符串切片
s1 = 'supercalifragilisticexpialidocious'
sla = s1[14:18]
print(sla)
slb = s1[0:5]
print(slb)
slc = s1[-7:]
print(slc)
sld = s1[12:]
print(sld)




# 字符串分割为列表
syslog= b'show cdp neighbors | begin Device\r\nDevice ID        Local Intrfce     Holdtme    Capability  Platform  Port ID\r\ncsr1000v-1.2022skill.com\r\n                 Gig 0/2           153              R I   CSR1000V  Gig 1\r\n\r\nTotal cdp entries displayed : 1\r\nSwitch1#'
print(syslog)
print('='*120)
print(syslog.decode())
print('='*120)
lines = syslog.decode().splitlines()
print(lines)
print(lines[2])
print('='*120)
print(lines[3])
print('='*120)
NBR_if = lines[3].split()[0] + lines[3].split()[1]
print(NBR_if)



# 交互式字符串
name = input("What's your name?")
print("Your name is " + name)

# 格式化字符串
name = input("What's your name?")
name = "Groot"
print("Your name is {}".format(name))
print("Your name is %s" % name)
print(f"Your name is {name}")


# 其他字符串方法
qt = 'abcdefg                  '
print('c' in qt)
print("c" not in qt)
print('x' in qt)
print("x" not in qt)
qt1 = qt.replace("c","c")
print(qt,qt1,"|")

qt2 = qt.strip()
print(qt,qt2,"|")

