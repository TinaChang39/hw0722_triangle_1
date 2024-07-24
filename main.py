print("Hello World")

# 作業一: 畫出等腰三角形
n = 0
n = int(input('請輸入三角形層數:'))
for i in range(1,n+1):               # 行數
    for j in range(1,n-i+1):         # 空幾格
        print(' ',end = '')
    for k in range(1,2*i):           # 印幾個*
        print('*',end = '')
    print('\n',end = '')


# 作業二: 九九乘法表
for i in range(1,10):
    for j in range(1,10):
        print('{0} x {1} = {2}\t'.format(j,i,i*j),end='')
    print('\n',end='')

# 作業三: 找出質數


