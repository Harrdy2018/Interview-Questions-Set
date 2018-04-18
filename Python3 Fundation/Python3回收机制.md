# Python3垃圾回收机制
## 一，gc模块` Garbage Collector interface`垃圾回收接口
### gc模块介绍
该模块提供了一个可选垃圾回收器的接口。 它提供了禁用收集器，调整收集频率并设置调试选项的功能。 它还提供对收集器找到但无法释放的不可访问对象的访问。 由于收集器补充了`Python3`中已经使用的引用计数，所以如果您确定程序没有创建引用循环，则可以禁用收集器。 通过调用`gc.disable（）`可以禁用自动收集。 调试泄漏的程序调用`gc.set_debug（gc.DEBUG_LEAK）`。请注意，这包括`gc.DEBUG_SAVEALL`，导致垃圾回收对象被保存在`gc.garbage`中以供检查。
### gc模块的自动垃圾回收机制  
必须要import gc模块，并且 is_enable()=True 才会启动自动垃圾回收  
这个机制的主要作用就是发现并处理不可达的垃圾对象  
垃圾回收=垃圾检查+垃圾回收  
在python3中，采用分代收集的方法。把对象分为三代，一开始，对象在创建的时候，放在一代，如果在一次一代的垃圾检查中，该对象存活下来，就会被放到二代中，同理在一次二代的垃圾检查中，该对象存活下来，就会被放到三代中。  
### gc模块提供了下列函数：
1. gc.get_threshold()<br>
获取gc模块中自动执行垃圾回收的频率<br>
Return the current collection thresholds as a tuple of (threshold0, threshold1, threshold2).  
2. gc.set_threshold(threshold0[, threshold1[, threshold2]])
设置自动执行垃圾回收的频率<br> 
3. gc.get_count()
获取当前自动执行垃圾回收的计数器，返回一个长度为3的列表    
Return the current collection counts as a tuple of (count0, count1, count2).  
4. gc.enable()
开启自动垃圾回收   
Enable automatic garbage collection.  
5. gc.disable()
禁止自动垃圾回收  
Disable automatic garbage collection.  
6. gc.isenabled()
如果自动垃圾回收功能开启，返回True   
Returns true if automatic collection is enabled.   
7. gc.set_debug(flags)
设置gc的debug日志，一般设置为gc.DEBUG_LEAK  
8. gc.collect(generation=2)
没有参数，运行一个完整的集合。 可选参数的生成可以是一个整数，指定要收集哪一代（从0到2）。如果代号数字是无效的，则会引发ValueError异常。返回不可达（unreachable objects）对象的数量 
### 垃圾回收机制有关问题
* 什么情况下触发python垃圾回收
```python
import gc
print(gc.get_threshold())
>>>(700, 10, 10)
```
当没有释放的对象个数超过700，即开始0级垃圾回收，0级垃圾回收超过10次即开始1级垃圾回收，1级垃圾回收清除包括0级垃圾，1级垃圾回收超过10次，即开始2级垃圾回收，2级垃圾回收清除包括0级，1级垃级。垃圾回收机制python默认开启的，gc.disabled可关闭垃圾回收机制，当程序完成时，垃圾最后仍被回收，当gc.disabled时，gc.collect手动开启垃圾回收机制。
* 查看一个对象的引用计数
```python
import sys
a='Haddry'
print(sys.getrefcount(a))
>>>4
```
可以查看a对象的引用计数，但是比正常计数大1，因为调用函数的时候传入a，这会让a的引用计数+1  
* 导致引用计数+1的情况
  * 对象被创建，例如a=23
  * 对象被引用，例如b=a 
  * 对象被作为参数，传入到一个函数中，例如func（a）
  * 对象作为一个元素，存储在容器中，例如list1=[1,1]
* 导致引用计数-1的情况
  * 对象的别名被显式销毁，例如del a 
  * 对象的别名被赋予新的对象，例如a=24
  * 一个对象离开它的作用域，例如f函数执行完毕时，func函数中的局部变量（全局变量不会）
  * 对象所在的容器被销毁，或从容器中删除对象

## 二，引用计数和垃圾回收介绍
python3采用"引用计数"和"垃圾回收"两种机制来管理内存。引用计数通过记录对象被引用的次数来管理对象。对对象的引用都会使得引用计数加1，移除对对象的引用，引用计数则会减1，当引用计数减为0时，对象所占的内存就会被释放掉。引用计数可以高效的管理对象的分配和释放，但是有一个缺点，就是无法释放引用循环的对象。
最简单的就是下面的自己引用自己的例子：  
```python
def make_cycle():
    data=[ ]
    data.append(10)
make_cycle()
```
这个时候就需要垃圾回收机制(garbage collection)，来回收循环应用的对象。垃圾回收机制会根据内存的分配和释放情况的而被调用，比如分配内存的次数减去释放内存的次数大于某一个阈值的时候。
如下所示，我们可以通过gc对象来获取阈值：
```python
import gc
print(gc.get_threshold())
>>>(700, 10, 10)
```
当内存溢出时，不会自动调用garbage collection（ gc ），
因为gc更看重的是垃圾对象的个数， 而不是大小。
对于长时间运行的程序，尤其是一些服务器应用，人为主动的调用gc是非常有必要的，如下代码所示：
```python
import sys, gc
def hello():
    dic={}
    dic[0]=1
def main():
    collected = gc.collect()
    print(collected)
    for i in range(10):
        hello()
    collected = gc.collect()
    print(collected)
if __name__ == "__main__":
    ret=main()
    sys.exit(ret)
>>>112
>>>0
```
调用gc的策略有两种，一种是固定时间间隔进行调用，另一种是基于事件的调用。如
1. 用户终止了对应用的访问，
2. 明显监测到应用进入到闲置的状态，
3. 运行高性能服务前后，
4. 周期性、或阶段性工作的前后。

注意gc虽好，但也不能常用，毕竟还是会消耗一定的计算资源。
## 三，gc垃圾回收方法（寻找引用循环对象）：
可以发现，只有容器对象才会出现引用循环，比如列表、字典、类、元组。<br>
首先，为了追踪容器对象，需要每个容器对象维护两个额外的指针，<br>
用来将容器对象组成一个链表，指针分别指向前后两个容器对象，方便插入和删除操作。<br>
其次，每个容器对象还得添加gc_refs字段。<br>
一次gc垃圾回收步骤：
1. 使得gc_refs等于容器对象的引用计数。
2. 遍历每个容器对象(a)，找到它(a)所引用的其它容器对象(b)，将那个容器对象(b)的gc_refs减去1。
3. 将所有gc_refs大于0的容器对象(a)取出来，组成新的队列，因为这些容器对象被容器对象队列的外部所引用。
4. 任何被新队列里面的容器对象，所引用的容器对象(旧队列中)也要加入到新队列里面。
5. 释放旧队列里面的剩下的容器对象。（释放容器对象时，它所引用的对象的引用计数也要减1）
## 四，gc分代机制：
* gc采用分代(generations)的方法来管理对象，总共分为三代（generation 0,1,2）。
* 新产生的对象放到第0代里面。
* 如果该对象在第0代的一次gc垃圾回收中活了下来，那么它就被放到第1代里面。
* 如果第1代里面的对象在第1代的一次gc垃圾回收中活了下来，它就被放到第2代里面。
* `gc.set_threshold(threshold0[, threshold1[, threshold2]])`
* 设置gc每一代垃圾回收所触发的阈值。从上一次第0代gc后，如果分配对象的个数减去释放对象的个数大于threshold0，
* 那么就会对第0代中的对象进行gc垃圾回收检查。从上一次第1代gc后，如过第0代被gc垃圾回收的次数大于threshold1，
* 那么就会对第1代中的对象进行gc垃圾回收检查。同样，从上一次第2代gc后，如过第1代被gc垃圾回收的次数大于threshold2，
* 那么就会对第2代中的对象进行gc垃圾回收检查。
* 如果threshold0设置为0，表示关闭分代机制。
## 五，最后的bug：__del__方法：
最后的问题就是__del__方法的调用。<br>
我们知道当引用计数变为0的时候，会先调用对象的__del__方法，然后再释放对象。<br>
但是当一个引用循环中对象有__del__方法时，gc就不知道该以什么样的顺序来释放环中对象。<br>
因为环中的a对象的__del__方法可能调用b对象，而b对象的__del__方法也有可能调用a对象。<br>
所以需要人为显式的破环。<br>
```python
import gc  
class A(object):  
    def __del__(self):  
        print '__del__ in A'  
class B(object):  
    def __del__(self):  
        print '__del__ in B'           
class C(object):  
    pass             
if __name__=='__main__':  
    print 'collect: ',gc.collect()  
    print 'garbage: ',gc.garbage  
    a = A()  
    b = B()  
    c = C()  
    a.cc = c  
    c.bb = b  
    b.aa = a  
    del a,b,c  
    print 'collect: ',gc.collect()  
    print 'garbage: ',gc.garbage  
    del gc.garbage[0].cc # 当然，这是在我们知道第一个对象是 a的情况下，手动破除引用循环中的环  
    del gc.garbage[:] # 消除garbage对a和b对象的引用，这样引用计数减1等于0，就能回收a、b、c三个对象了  
    print 'garbage: ',gc.garbage  
    print '----------------------------'  
    print 'collect: ',gc.collect()  
    print 'garbage: ',gc.garbage 
```
* 如上所示：调用一次gc.collect()，首先检查因为引用循环而不可达对象，
* 如果一个引用循环中所有对象都不包含__del__方法，那么这个引用循环中的对象都将直接被释放掉。
* 否则，将引用循环中包含__del__方法的对象加入到gc.garbage列表中。
* （这时它们的引用计数也会加1，因此gc.collect()不会再对这个环进行处理）
* 用户通过gc.garbage来获取这些对象，手动消除引用，进行破环。
* 最后消除gc.garbage对这些对象的引用，这时这些对象的引用计数减1等于0，就自动被回收了。
* 否则由于gc.garbage对这些对象存在引用，这些对象将永远不会被回收。
## 六，其它
```python
import weakref  
class Foo(object):  
    pass  
a = Foo()  
a.bar = 123  
a.bar2 = 123  
  
  
del a  
del a.bar2  
  
  
b = weakref.ref(a)  
print b().bar  
print a == b()  
  
  
c = weakref.proxy(a)  
print c.bar  
print c == a 
```
del：只是使变量所代表的对象的引用计数减1，并在对应空间中删除该变量名。<br>
weak.ref：会返回a对象的引用，但是不会让a对象的引用计数加1。但是每次都得通过b()来获取a对象。<br>
weak.proxy：相对于weakref.ref更透明的可选操作，即直接通过c就获取a对象。<br>
### 闭包空间的变量和自由变量的释放问题：
```python
class A(object):  
    def __init__(self,name):  
        self._name = name  
    def __del__(self):  
        print '__del__ in ',self._name       
def f1():  
    a = A('a')  
    b = A('b')  
    def f2():  
        c = A('c')  
        print a  
    return f2              
if __name__=='__main__':  
    print 'f2 = f1():'  
    f2 = f1()  
    print '\na.__closure__:'  
    print f2.__closure__ # 查看f2的闭包里面引用了a对象  
    print '\na():'  
    f2()  
    print '\ndel f2:'  
    del f2 # 此时已经没有任何变量可以引用到返回的f2对象了。  
    print '\nover!' 
```
