# Python3.6.1教程
***
|Author|Harrdy2018|
|:----------------:|:----------------:|
|Email|995122077@qq.com|
## 目录

## 函数
### 递归函数
**定义：如果一个函数在内部调用自身本身，这个函数就是递归函数。
```
举个例子，我们来计算阶乘(factorial),用函数fact(n)表示，可以看出：fact(n)=fact(n-1)xn所以，fact(n)可以表示为n x fact(n-1)，只有n=1时需要特殊处理。
于是，fact(n)用递归的方式写出来就是：
```
```python
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
>>> fact(1)
1
>>> fact(5)
120
>>> fact(100)
93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
```
