# hw0722_碩0_張雅淇

# 作業一: 畫出等腰三角形
n = 0
n = int(input('請輸入三角形層數:'))
for i in range(1,n+1):               # 行數
    for j in range(1,n-i+1):         # 空幾格
        print(' ',end = '')
    for k in range(1,2*i):           # 印幾個*
        print('*',end = '')
    print('\n',end = '')

print('------------------------------------------------------------------------------------------------')

# 作業二: 九九乘法表
for i in range(1,10):
    for j in range(1,10):
        print('{0} x {1} = {2}\t'.format(j,i,i*j),end='')
    print('\n',end='')

print('------------------------------------------------------------------------------------------------')

# 作業三: 找出質數 (輸入數值 -> 計算1~數值中有幾個質數 -> 印出所有質數)
num = 0
count = 0
flag =0
num = int(input('請輸入數字:'))
print('從 1 ~ num 質數有:',end = '')

for i in range(2,num+1):                # 小於數值的所有數字
    for j in range(2,num):              # 數值判斷是否為質數
        if i != j:                      # 排除自己除自己
            if i%j == 0:                # 不是質數時 flag+1
                flag = flag + 1               
    if flag == 0:                       # 當 flag=0 代表是質數，此時 count+1，並印出質數
        count = count + 1          
        print(i,' ',end = '')
        flag = 0
    else:
        flag = 0
print('\n',end='') 
print('質數總個數:',count,end = '')

  