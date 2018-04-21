# 函数式编程
该模块提供了支持函数式编程风格的函数和类，以及可调用函数的一般操作。
* [高阶函数](#高阶函数)
    * [函数作为变量](#函数作为变量)
    * [函数作为参数](#函数作为参数)
    * [函数作为返回值](#函数作为返回值)
    * [闭包](#闭包)
    * [map](#map)
    * [functools.reduce()](#reduce)
    * [filter](#filter)
    * [sorted](#sorted)   
* [匿名函数](#匿名函数)
* [装饰器](#装饰器)
* [偏函数](#偏函数)

***
## 高阶函数
```
高阶函数(Higher-order function)
一，接受一个或者多个函数作为输入
二，输出一个函数
至少满足上诉一个条件的函数
```
### 函数作为变量
```
在Python中，对象和方法都是变量。
函数名其实就是指向函数的变量。
函数本身也能赋值给变量，即：变量指向函数。
如果一个变量指向了一个函数，那么，就能通过该变量来调用这个函数
```
```python
def print_hello(name):
    print('Hello, %s' % name)
ph = print_hello # 将函数变量赋值给ph变量
ph('python3')
>>>Hello, python3
```
### 函数作为参数
变量能指向函数，函数的参数能接收变量，那么一个函数就能接收另一个函数作为参数，这种函数就称之为高阶函数。
编写高阶函数，就是让函数的参数能够接收别的函数。<br>
* Ex.1
```python
def get(a):
    return a*10
def printAll(x,y,func):
    print(func(x) + func(y))  
printAll(3,3,get)  
>>>60
```
* Ex.2
```python
def abssum(f,*num):
    sum=0
    for item in num:
        sum+=f(item)
    return sum
result=abssum(abs,1,2,3,-4)
print(result)
>>>10
```

***
### 函数作为返回值
高阶函数除了能接受函数作为参数外，还能把函数作为结果值返回。
```python
def return_nu(*args):
    def accumulate():
        a = 1
        for n in args:
            a = a * n
        return a
    return accumulate 
accu= return_nu(3,6,2)
print(accu()) 
>>>36
```
调用return_nu函数时，没有计算乘积，而是返回了一个计算乘积的函数。调用这个返回的函数，才会计算乘积。

***
### 闭包
如果在一个内部函数里，对在外部作用域（但不是在全局作用域）的变量进行引用，那么内部函数就被认为是闭包（closure)。<br>
在上面的return_nu函数中，内部函数accumulate能引用外部函数的变量，这就是闭包。

***
### map
```
Python3内建了map()和functools.reduce()函数
map(function, iterable, ...) 
map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
```
* Ex.1 请利用map函数生成0~9数字平方组成的list
```python
m=map(lambda x:x**2,range(0,10))
print(m,"---",list(m))
>>><map object at 0x000002D001E90588> --- [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```
```
map()传入的第一个参数是func，即函数对象本身。
由于结果m是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。
所以，map()作为高阶函数，事实上它把运算规则抽象了。
```
* Ex.2 用列表生成式改写
```python
print([x**2 for x in range(0,10)])
print(list(x**2 for x in range(0,10)))
>>>[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```
我们发现了在列表生成式中，既可以用list,也可以用[ ],这也是我一直比较纠结的问题！！！<br>
* Ex.3 用一行代码，将一个数组的元素全部变成字符串，返回这个字符串组成的数组
```python
>>> list(map(str,range(0,5)))
['0', '1', '2', '3', '4']
```

***
### reduce
***functools.reduce用法***<br>
reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：<br>
reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)<br>
* Ex.1 对一个序列求和
```python
import functools
result=functools.reduce(lambda x,y:x+y,[1,3,5,7,9])
print(result)
```
* Ex.2 不要用int函数，另外写一函数，将类似于'98765'的字符串转化为类似于98765的数字
```python
from functools import reduce
digits={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
def char_to_num(s):
    return digits[s]
def str_to_int(s):
    return reduce(lambda x,y:x*10+y,map(char_to_num,s))
print(str_to_int('98765'))
>>>98765
```

***
### filter
```
Python内建的filter()函数用于过滤序列。和map()类似，filter()也接收一个函数和一个序列。
filter()把传入的函数依次作用于每个元素，然后根据返回值是True决定保留元素，反之。
```
* Ex.1 在一个list中，删掉偶数，只保留奇数
```python
>>> list(filter(lambda x:x%2==1, [1, 2, 4, 5, 6, 9, 10, 15]))
[1, 5, 9, 15]
```
* Ex.2 把一个序列中的空字符串删掉
>>> list(filter(lambda s:s and s.strip(), ['A', '', 'B', None, 'C', '  ']))
['A', 'B', 'C']

***
### sorted
***排序算法***<br>
```
排序也是在程序中经常用到的算法。无论使用冒泡排序还是快速排序，排序的核心是比较两个元素的大小。
如果是数字，我们可以直接比较，但如果是字符串或者两个dict呢？
直接比较数学上的大小是没有意义的，因此，比较的过程必须通过函数抽象出来。
```
* Ex.1 对list进行排序
```python
>>> sorted([36, 5, -12, 9, -21])
[-21, -12, 5, 9, 36]
```
* Ex.2 sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序
```python
>>> sorted([36, 5, -12, 9, -21], key=abs)
[5, 9, -12, -21, 36]
```
* Ex.3 字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面
```python
>>> sorted(['bob', 'about', 'Zoo', 'Credit'])
['Credit', 'Zoo', 'about', 'bob']
```
* Ex.4 sorted传入key函数，即可实现忽略大小写的排序
```python
>>> sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
['about', 'bob', 'Credit', 'Zoo']
```
* Ex.5 要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True
```python
>>> sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
['Zoo', 'Credit', 'bob', 'about']
```

***
## 匿名函数
```
当我们在传入函数时，有些时候，不需要显式地定义函数，直接传入匿名函数更方便。
关键字lambda表示匿名函数，冒号前面的x表示函数参数。
匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。此外，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数：
```
* Ex.1
```python
>>> f = lambda x: x**2
>>> f
<function <lambda> at 0x000001D46321A9D8>
>>> f(5)
25
```

***
## 装饰器

***
## 偏函数
