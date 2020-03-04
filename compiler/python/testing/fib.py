from lib import *

a = uint8(0)
b = uint8(1)

past = array(uint8,15)
index = uint8(0)

while a < 500:
 print(a)
 past[index] = a
 index = index + 1
 temp = a + b
 a = b
 b = temp


