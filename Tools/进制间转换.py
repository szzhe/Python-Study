
'''
↓		  2进制				8进制			10进制			16进制
2进制		-			bin(int(x, 8))	bin(int(x, 10))	bin(int(x, 16))
8进制	oct(int(x, 2))		-			oct(int(x, 10))	oct(int(x, 16))
10进制	int(x, 2)		int(x, 8)			-			int(x, 16)
16进制	hex(int(x, 2))	hex(int(x, 8))	hex(int(x, 10))		-
'''

''' 十进制数字与二进制(bin)、八进制(oct)、十六进制(hex)的转换" '''

a = -100
print('二进制bin:', bin(a))  # 0b111100
print('八进制oct:', oct(a))  # 0o74
print('十六进制hex:', hex(a))  # 0x3c

''' 二进制数字与八进制(oct)、十进制(int)、十六进制(hex)的转换" '''

b = -0b1100100
print('八进制oct:', oct(b))  # 0o74
print('十进制hex:', int(b))  # 60
print('十六进制bin:', hex(b))  # 0x3c

''' 八进制数字与二进制(oct)、十进制(int)、十六进制(hex)的转换" '''

# c = 0o74
# print('二进制oct:', bin(c))  # 0b111100
# print('十进制hex:', int(c))  # 60
# print('十六进制bin:', hex(c))  # 0x3c

''' 十六进制数字与二进制(oct)、八进制(int)、十进制(hex)的转换" '''

# d = 0x3c
# print('二进制oct:', bin(d))  # 0b111100
# print('八进制oct:', oct(d))  # 0o74
# print('十进制hex:', int(d))  # 60
