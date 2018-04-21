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
***生成器(generator)***
* 引例`(i for i in range(10))`它就是一个generator,必须用list方法转化为列表！！
```python
>>> m=(i for i in range(10))
>>> type(m)
<class 'generator'>
>>> list(m)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> [m]
[<generator object <genexpr> at 0x000002445AAF7990>]
```
