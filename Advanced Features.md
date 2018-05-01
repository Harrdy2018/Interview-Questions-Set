# 高级特性
* [容器](#容器)
* [切片](#切片)
* [迭代](#迭代)
* [列表生成式](#列表生成式)
* [生成器](#生成器)
* [迭代器](#迭代器)
***
***Python数据结构***
* 容器(container)
* 可迭代对象(iterable)
* 迭代器(iterator)
* 生成器(generator)
* 列表/集合/字典推导式(list,set,dict comprehension)
***
## 容器
***容器(container)***
* Ex.1 assert在列表，集合，元组中的用法
```python
>>> assert 1 in [1,2,3]
>>> assert 1 in {1,2,3}
>>> assert 1 in (1,2,3)
```
* Ex.2 询问元素是否在dict中用key
```python
>>> d={1:'a',2:'b',3:'c'}
>>> assert 1 in d
>>> assert 'a' not in d
```
* Ex.3 询问substring是否在string中
```python
>>> s='Harrdy2018'
>>> assert 'H' in s
>>> assert 'l' not in s
```
***

## 可迭代对象
***str,list,dict,tuple,generator,set都是可迭代对象***<br>
**Iterable:可以直接作用于for循环的对象统称为可迭代对像**
* Ex.1 可以使用isinstance()判断一个对象是否是Iterable
```python
>>> from collections import Iterable
>>> isinstance('Harrdy2018',Iterable)
True
>>> isinstance('[1,2,3,4]',Iterable)
True
>>> isinstance({'a':1,'b':2},Iterable)
True
>>> isinstance((1,2,3),Iterable)
True
>>> isinstance((x for x in range(10)),Iterable)
True
>>> isinstance({1,2,3},Iterable)
True
```



## 列表生成式
***列表生成式(List Comprehensions)***
* Ex.1 生成[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```python
>>> list(range(1,11))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```
* Ex.2 生成[1x1, 2x2, 3x3, ..., 10x10]
```python
>>> list(i**2 for i in range(1,11))
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```
* Ex.3 for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方
```python
>>> list(i**2 for i in range(1,11) if i%2==0)
[4, 16, 36, 64, 100]
```
* Ex.4 使用两层循环，可以生成全排列
```python
>>> [m + n for m in 'ABC' for n in 'XYZ']
['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
```
* Ex.5 for循环其实可以同时使用两个甚至多个变量，比如dict.items()可以同时迭代key和value
```python
>>> d = {'x': 'A', 'y': 'B', 'z': 'C' }
>>> for k,v in d.items():
	print(k,"=",v)	
x = A
y = B
z = C
```
* Ex.6 列表生成式也可以使用两个变量来生成list
```python
>>> d = {'x': 'A', 'y': 'B', 'z': 'C' }
>>> [k+"="+v for k,v in d.items()]
['x=A', 'y=B', 'z=C']
```
* Ex.7 把一个list中所有的字符串变成小写
```python
>>> L = ['Hello', 'World', 'IBM', 'Apple']
>>> [s.lower() for s in L]
['hello', 'world', 'ibm', 'apple']
```

***
## 生成器
***生成器(generator)***<br>
**算法+节约内存**
```
注意区别以下两种情况：
[x for x in range(10)]------>>列表生成式
(x for x in range(10))------>>generator
```

***
## 迭代器
***迭代器(Iterator)***<br>
**可以被next()函数调用并不断返回下一个值的对象称为迭代器**
* Ex.1 使用isinstance()判断一个对象是否是Iterator
```python
>>> from collections import Iterator
>>> isinstance((x for x in range(10)),Iterator)
True
```

* Ex.2 生成器都是Iterator，但list、dict、str...虽然是Iterable，却不是Iterator。
* 把list、dict、str等Iterable变成Iterator可以使用iter()函数
```python
>>> from collections import Iterator
>>> isinstance(iter('Harrdy2018'),Iterator)
True
>>> isinstance(iter([1,2,3]),Iterator)
True
>>> isinstance(iter({'a':1,'b':2}),Iterator)
True
>>> isinstance(iter({1,2,3}),Iterator)
True
```
```
为什么？
这是因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，
直到没有数据时抛出StopIteration错误。可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，
只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。
Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。
```

* Ex.3 for循环本质就是通过不断调用next()函数实现的
```python
it=iter([1,2,3,4,5])
while True:
    try:
        x=next(it)
        print(x)
    except StopIteration:
        break
>>>
1
2
3
4
5
```
