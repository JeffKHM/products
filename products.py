products = []
while True:
    name = input('请输入产品名称：')
    if name == 'q':
        break
    price = input('请输入厂品价格：')
    p = []
    p.append(name)
    p.append(price)
    products.append(p) #把 p 加入 products 大清单
print(products)    

