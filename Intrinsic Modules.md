# 常用内建模块
* [itertools](#itertools)
* [functools](#functools)
***


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
