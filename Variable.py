'''Variables are containers for storing data values.
Python has no command for declaring a variable.
A variable is created the moment you first assign a value to it
'''

# Example
x = 5
y = "John"
print(x)
print(y)

# Variables do not need to be declared with any particular type,
# and can even change type after they have been set.
a = 4 # a is of type int
a = "Sally" # a is now of type str
print(a)

# If you want to specify the data type of a variable,
# this can be done with casting
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(x)
print(y)
print(z)

# You can get the data type of a variable with the type() function

x = 5
y = "John"
print(type(x))
print(type(y))


# String variables can be declared either by using single or double quotes
x = 'John'
# is the same as
x = "John"


# Case-sensitive
a = 4
A = "Sally"
print(A)
print(a)
# A will not overwrite a

f = r'a\b' # r means keep original meaning
print(f)

list1 = ["f0/0", "f0/1", "f0/2"]
print(list1)

dict1 = {"config_speed": "auto", "config_duplex" : "auto", "config_ip" : "192.168.1.1"}
print(dict1)


"Interface_Config" : {
    "ip_address" : "192.168.1.109",
    "subnet_mask" : "255.255.255.0",
    "speed" : 1000
}