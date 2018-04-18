# Python3垃圾回收机制详解
# gc模块 Garbage Collector interface垃圾回收接口
该模块提供了一个可选垃圾回收器的接口。 它提供了禁用收集器，调整收集频率并设置调试选项的功能。 它还提供对收集器找到但无法释放的不可访问对象的访问。 由于收集器补充了Python中已经使用的引用计数，所以如果您确定程序没有创建引用循环，则可以禁用收集器。 通过调用gc.disable（）可以禁用自动收集。 调试泄漏的程序调用gc.set_debug（gc.DEBUG_LEAK）。 请注意，这包括gc.DEBUG_SAVEALL，导致垃圾回收对象被保存在gc.garbage中以供检查。  
gc模块的自动垃圾回收机制  
必须要import gc模块，并且 is_enable()=True 才会启动自动垃圾回收  
这个机制的主要作用就是发现并处理不可达的垃圾对象  
垃圾回收=垃圾检查+垃圾回收  
在python3中，采用分代收集的方法。把对象分为三代，一开始，对象在创建的时候，放在一代，如果在一次一代的垃圾检查中，该对象存活下来，就会被放到二代中，同理在一次二代的垃圾检查中，该对象存活下来，就会被放到三代中。  
gc模块提供了下列函数：  
1， 获取gc模块中自动执行垃圾回收的频率  
gc.get_threshold()   
Return the current collection thresholds as a tuple of (threshold0, threshold1, threshold2).  
2， 设置自动执行垃圾回收的频率  
gc.set_threshold(threshold0[, threshold1[, threshold2]])  
3， 获取当前自动执行垃圾回收的计数器，返回一个长度为3的列表  
gc.get_count()   
Return the current collection counts as a tuple of (count0, count1, count2).  
4， 开启自动垃圾回收  
gc.enable()   
Enable automatic garbage collection.  
5， 禁止自动垃圾回收  
gc.disable()   
Disable automatic garbage collection.  
6， 如果自动垃圾回收功能开启，返回True  
gc.isenabled()   
Returns true if automatic collection is enabled.   
7,  设置gc的debug日志，一般设置为gc.DEBUG_LEAK  
gc.set_debug(flags)  
8,显式进行垃圾回收，可以输入参数，0代表只检查第一代的对象，1代表检查一，二代的对象，2代表检查一，二，三代的对象，如果不传参数，执行一个full collection，也就是等于传2.返回不可达（unreachable objects）对象的数目  
gc.collect(generation=2)

一,  什么情况下触发python垃圾回收  
`import gc
print(gc.get_threshold())
(700, 10, 10)`  
当没有释放的对象个数超过700，即开始0级垃圾回收，0级垃圾回收超过10次即开始1级垃圾回收，1级垃圾回收清除包括0级垃圾，1级垃圾回收超过10次，即开始2级垃圾回收，2级垃圾回收清除包括0级，1级垃级。垃圾回收机制python默认开启的，gc.disabled可关闭垃圾回收机制，当程序完成时，垃圾最后仍被回收，当gc.disabled时，gc.collect手动开启垃圾回收机制。
二，  查看一个对象的引用计数   
`import sys
a='Haddry'
print(sys.getrefcount(a))
>>>4`  
可以查看a对象的引用计数，但是比正常计数大1，因为调用函数的时候传入a，这会让a的引用计数+1  
三，导致引用计数+1的情况
对象被创建，例如a=23
对象被引用，例如b=a 
对象被作为参数，传入到一个函数中，例如func（a）
对象作为一个元素，存储在容器中，例如list1=[1,1]
四，导致引用计数-1的情况
对象的别名被显式销毁，例如del a 
对象的别名被赋予新的对象，例如a=24
一个对象离开它的作用域，例如f函数执行完毕时，func函数中的局部变量（全局变量不会）
对象所在的容器被销毁，或从容器中删除对象


# 一，引用计数和垃圾回收介绍  
python3采用"引用计数"和"垃圾回收"两种机制来管理内存。引用计数通过记录对象被引用的次数来管理对象。对对象的引用都会使得引用计数加1，移除对对象的引用，引用计数则会减1，当引用计数减为0时，对象所占的内存就会被释放掉。引用计数可以高效的管理对象的分配和释放，但是有一个缺点，就是无法释放引用循环的对象。
最简单的就是下面的自己引用自己的例子：  
`def make_cycle():
    data=[ ]
    data.append(10)
make_cycle()`  
这个时候就需要垃圾回收机制(garbage collection)，来回收循环应用的对象。垃圾回收机制会根据内存的分配和释放情况的而被调用，比如分配内存的次数减去释放内存的次数大于某一个阈值的时候。  
如下所示，我们可以通过gc对象来获取阈值：
