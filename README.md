# Python3.6.1教程
***
|Author|Harrdy2018|
|:----------------:|:----------------:|
|Email|995122077@qq.com|
## 目录
* [函数](#函数)
  * [递归函数](#递归函数)

## 函数
### 递归函数
**定义：如果一个函数在内部调用自身本身，这个函数就是递归函数。**
```
举个例子，我们来计算阶乘(factorial),用函数fact(n)表示，可以看出：fact(n)=fact(n-1)xn
所以，fact(n)可以表示为n x fact(n-1)，只有n=1时需要特殊处理。
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
9332621544394415268169923885626670049071596826438162146859296389521759999322991560
8941463976156518286253697920827223758251185210916864000000000000000000000000
```
我们调试fact(5)的计算过程：
```
>>> fact(5)
>>> 5 * fact(4)
>>> 5 * (4 * fact(3))
>>> 5 * (4 * (3 * fact(2)))
>>> 5 * (4 * (3 * (2 * fact(1))))
>>> 5 * (4 * (3 * (2 * 1)))
>>> 5 * (4 * (3 * 2))
>>> 5 * (4 * 6)
>>> 5 * 24
>>> 120
```
```
递归函数的优点是定义简单，逻辑清晰。理论上，所有的递归函数都可以写成循环的方式，但循环的逻辑不如递归清晰。
使用递归函数需要注意防止栈溢出。在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。可以试试fact(1000)：
```
```python
Traceback (most recent call last):
  File "E:/Kang Lu/PycharmProjects/text.py", line 9, in <module>
    main()
  File "E:/Kang Lu/PycharmProjects/text.py", line 7, in main
    print(fact(1000))
  File "E:/Kang Lu/PycharmProjects/text.py", line 5, in fact
    return n*fact(n-1)
  File "E:/Kang Lu/PycharmProjects/text.py", line 5, in fact
    return n*fact(n-1)
  File "E:/Kang Lu/PycharmProjects/text.py", line 5, in fact
    return n*fact(n-1)
  [Previous line repeated 993 more times]
  File "E:/Kang Lu/PycharmProjects/text.py", line 2, in fact
    if n==1:
RecursionError: maximum recursion depth exceeded in comparison
```
```
解决递归调用栈溢出的方法是通过尾递归优化，事实上尾递归和循环的效果是一样的，所以，把循环看成是一种特殊的尾递归函数也是可以的。
尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。
这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。
上面的fact(n)函数由于return n * fact(n - 1)引入了乘法表达式，所以就不是尾递归了。
要改成尾递归方式，需要多一点代码，主要是要把每一步的乘积传入到递归函数中：
```
```python
def fact(n):
    return fact_iter(n, 1)
def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
def main():
    print(fact(5))
if __name__=="__main__":
    main()
>>>120
```
可以看到，return fact_iter(num - 1, num * product)仅返回递归函数本身，num - 1和num * product在函数调用前就会被计算，不影响函数调用。<br>
fact(5)对应的fact_iter(5, 1)的调用如下：
```
>>> fact(5)
>>> fact_iter(5, 1)
>>> fact_iter(4, 5)
>>> fact_iter(3, 20)
>>> fact_iter(2, 60)
>>> fact_iter(1, 120)
>>> 120
```
尾递归调用时，如果做了优化，栈不会增长，因此，无论多少次调用也不会导致栈溢出。<br>
遗憾的是，大多数编程语言没有针对尾递归做优化，Python解释器也没有做优化，所以，即使把上面的fact(n)函数改成尾递归方式，也会导致栈溢出。<br>
**小结**
```
使用递归函数的优点是逻辑简单清晰，缺点是过深的调用会导致栈溢出。
针对尾递归优化的语言可以通过尾递归防止栈溢出。尾递归事实上和循环是等价的，没有循环语句的编程语言只能通过尾递归实现循环。
Python标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题。
```
**练习**
***华为2018校园大使笔试春季题目***
```
斐波那契数列（Fibonacci sequence），又称黄金分割数列、因数学家列昂纳多·斐波那契（Leonardoda Fibonacci）以兔子繁殖为例子而引入，
故又称为“兔子数列”，指的是这样一个数列：1、1、2、3、5、8、13、21、34、……
在数学上，斐波纳契数列以如下被以递归的方法定义：F(0)=1，F(1)=1, F(n)=F(n-1)+F(n-2)（n>2，n∈N*）
在现代物理、准晶体结构、化学等领域，斐波纳契数列都有直接的应用，为此，美国数学会从1963年起出版了以《斐波纳契数列季刊》为名的一份数学杂志，
用于专门刊载这方面的研究成果。
```
```python
def Fib(n):
    if n==2 or n==1:
        return 1
    else:
        return Fib(n-1)+Fib(n-2)
def main():
    num=eval(input('请输入要计算多少次>>>'))
    ls=[]
    for i in range(num):
        ls.append(eval(input('请输入第{}次要计算的数字>>>'.format(i+1))))
    for item in ls:
        print(Fib(item))
if __name__=="__main__":
    main()
>>>请输入要计算多少次>>>5
请输入第1次要计算的数字>>>1
请输入第2次要计算的数字>>>2
请输入第3次要计算的数字>>>3
请输入第4次要计算的数字>>>4
请输入第5次要计算的数字>>>5
1
1
2
3
5
```
IT笔试的时候，一般输出不是让你简单的输出结果，一般先是给出让你计算这个程序多少次，每次给一个数据，然后再让你输出所有结果。<br>
当然这个程序还是存在问题的，就是当n特别大的时候，时间复杂度大，在笔试中只可以拿30%的分数。<br>
***参考源码：***[Fibonacci sequence.py](https://github.com/Harrdy2018/Interview-Questions-Set/blob/master/Fibonacci%20sequence.py)
