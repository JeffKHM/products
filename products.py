#读取档案
products = []
with open('products.csv', 'r', encoding='utf-8') as f:
    for line in f:
        if '商品,价格' in line:# if '商品,价格' in line:
            continue  #   continue # 继续 如果在 line 里面就跳下一回继续
        name, price = line.strip().split(',')
        products.append([name, price])

print(products)

#让使用者输入
while True:
    name = input('请输入产品名称：')
    if name == 'q':
        break
    price = input('请输入厂品价格：')
    price = int(price)
    products.append([name, price]) 
print(products)


# 印出所有购买今纪录
for p in products:   # for loop 的定义是 products 中一个一个那出来
    print(p[0], '的价格是', p[1])

# 写入档案
with open('products.csv', 'w', encoding='utf-8') as f: # write (w) 写入模式, 如果没有 products.txt or csv file 没关系
    f.write('商品,价格\n')
    for p in products:          # read (r) 读取模式
        f.write(p[0] + ',' + str(p[1]) + '\n') #.write 是写入





       