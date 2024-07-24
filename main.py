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

# 作業三: 找出質數 (輸入數值 -> 計算1~數值中有幾個質數 -> 印出所有質數)
num = 0
count = 0
pp =0
num = int(input('請輸入數字:'))
for i in range(2,num+1):           # 小於數值的所有數字
    for j in range(2,num):         # 數值判斷是否為質數
        if i%j == 0:
            pp = pp + 1            # 不是質數     

    if pp == 0:
        count = count + 1          # 是質數
        pp = 0
    else:
        pp = 0
        break
 
        
print('\n',end='') 
print('質數總個數:',count,end = '')

