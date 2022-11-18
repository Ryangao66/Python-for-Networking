Interface_Config = {
    "ip_address" : "192.168.1.109",
    "subnet_mask" : "255.255.255.0",
    "speed" : 1000
}
a = Interface_Config
print(a)


# 这个符号是但行注释

'''
这个
符号
是
多行
注释

'''
a = 1; b = 2; c = 3
print(a)
print(b)
print(c)

a,b,c = 4,5,6
print(a)
print(b)
print(c)


IP = "10.1.1.253"
protocol = "https://"
url_1 = "/device-list"
DNAC_API = "/api/v1"

dd = "{}{}{}{}".format(protocol,IP,DNAC_API,url_1)
print(dd)

a,b,c = 10,20,30
if a + b == c:
    print('true')
elif a + b > c:
    print("ab>c")
elif a + b < c:
    print("ab<c")


