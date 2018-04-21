# 函数式编程
该模块提供了支持函数式编程风格的函数和类，以及可调用函数的一般操作。
## 目录
* [高阶函数](#高阶函数)
    * [函数作为变量](#函数作为变量)
    * [函数作为参数](#函数作为参数)
    * [函数作为返回值](#函数作为返回值)
    * [闭包](#闭包)
    * [强化练习题](#强化练习题)
* [itertools](#itertools)
    * itertools.groupby()
* [functools](#functools)
    * functools.reduce()
## 高阶函数
```
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
```python
def get(a):
    return a*10
def printAll(x,y,func):
    print(func(x) + func(y))  
printAll(3,3,get)  
>>>60
```
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
### 闭包
如果在一个内部函数里，对在外部作用域（但不是在全局作用域）的变量进行引用，那么内部函数就被认为是闭包（closure)。<br>
在上面的return_nu函数中，内部函数all能引用外部函数的变量，这就是闭包。
### 强化练习题
* 请分析下面一段代码的原理，研究函数作为参数是如何使用的。
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
* 请利用map函数生成0~9数字平方组成的list
```python
m=map(lambda x:x**2,range(0,10))
print(m,"---",list(m))
>>><map object at 0x000002D001E90588> --- [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```
当然可以用我们学过的列表生成式
```python
print([x**2 for x in range(0,10)])
print(list(x**2 for x in range(0,10)))
>>>[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```
我们发现了在列表生成式中，既可以用list,也可以用[ ],这也是我一直比较纠结的问题！！！
* 用一行代码，将一个数组的元素全部变成字符串，返回这个字符串组成的数组
```python
>>> list(map(str,range(0,5)))
['0', '1', '2', '3', '4']
```
* 不要用int函数，另外写一函数，将类似于'98765'的字符串转化为类似于98765的数字
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
## itertools
```
为高效循环创建迭代器的函数
该模块实现了许多受APL，Haskell和SML构造启发的迭代器构建块。 每一个都以适合Python的形式进行了重新编排。
该模块标准化了一套核心快速，高效的内存工具，这些工具本身或其组合都很有用。 它们一起构成了一个“iterator algebra”，可以在纯Python中简洁高效地构建专用工具。
```
以下模块函数都构造并返回迭代器。 一些提供无限长度的流，所以它们只能由截断流的函数或循环访问。
* itertools.groupby(iterable, key=None)
```
用于对序列进行分组
key是分组函数，用于对iterable的连续项进行分组
如果不指定，则默认对iterable中的连续相同的项进行分组，返回一个(key,sub_iterator)的迭代器
创建一个从迭代器中返回连续键和组的迭代器。 关键是计算每个元素的关键值的函数。 如果没有指定或者是None，那么key默认为一个标识函数，并且返回该元素不变。 一般来说，迭代器需要在同一个关键函数上进行排序。
```
```python
from itertools import groupby
for key,g in groupby('aaabbbaaccd'):
    print(type(key))
    print(type(g))
    break
>>><class 'str'>
<class 'itertools._grouper'>
```
正如上面所说的，返回连续建和组的迭代器，也就是很多迭代器组成一个组，下面我把它打印出来：
```python
from itertools import groupby
for key,g in groupby('aaabbbaaccd'):
    print(key,":",g)
>>>a : <itertools._grouper object at 0x0000027494270828>
b : <itertools._grouper object at 0x000002749425FB38>
a : <itertools._grouper object at 0x0000027494270828>
c : <itertools._grouper object at 0x000002749425FB38>
d : <itertools._grouper object at 0x0000027494270828>
```
打印出来这些迭代器就相当于组内的成员，怎么样显示呢？用`list(iterator)`,千万不能用`[iterator]`，最后结果如下所示：
```python
from itertools import groupby
for key,g in groupby('aaabbbaaccd'):
    print(key,":",list(g))
>>>
a : ['a', 'a', 'a']
b : ['b', 'b', 'b']
a : ['a', 'a']
c : ['c', 'c']
d : ['d']
```
这就是`itertools.groupby(iterable, key=None)`中`key=None`的情况。下面介绍带函数参数的情况：<br>
使用len函数作为分组函数
```python
from itertools import groupby
data=['a','bb','cc','ddd','eee','f']
for key,g in groupby(data,len):
    print(key,":",list(g))
>>>
1 : ['a']
2 : ['bb', 'cc']
3 : ['ddd', 'eee']
1 : ['f']
```
## functools
```
可调用对象的高阶函数(higher-order functions)和操作
functools模块用于高阶函数：作用于或返回其他函数的函数。 一般而言，任何可调用对象都可以作为本模块用途的函数来处理
```
* functools.reduce(function, iterable[, initializer]) 
```
将两个参数的函数累积地应用到序列的项目，从左到右，以便将序列减少到单个值。 
左边的参数x是累加值，右边的参数y是序列中的更新值。 如果存在可选的初始值设定项，则将其置于计算中序列的项之前，并在序列为空时用作默认值。 
如果初始化程序没有给出，并且序列只包含一项，则返回第一个项。
```
大体上等价如:
```python
def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    return value
```
Example:
```python
from functools import reduce
function=lambda x,y:x+y
iterable=[1,2,3,4,5]
value=reduce(function, iterable)
print(value)
>>>15
```
上面的程序就是reduce（lambda x，y：x + y，[1，2，3，4，5]）计算（（（（1 + 2）+3）+4）+5）
