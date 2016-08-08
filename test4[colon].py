#coding: utf-8;

a = range(1,10)
b = a[:] #将a的内容复制一份传给b，a、b指向不同的变量空间
#b = a //将a的空间地址传给b，a、b指向相同的变量空间
b[3] = 10
print a
print b



            
