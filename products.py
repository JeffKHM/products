products = []
while True:
    name = input('请输入产品名称：')
    if name == 'q':
        break
    price = input('请输入厂品价格：')
    p = []
    p.append(name) # comprehensive list "p = [name, price]" = p=[];p.append(name);p.append(price)
    p.append(price)
    products.append(p) #把 p 加入 products 大清单
print(products)    

for product in products:   # for loop 的定义是 products 中一个一个那出来
	print(product[0], '的价格是', product[1])