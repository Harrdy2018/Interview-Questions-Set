# 进程和线程
* [定义](#定义)
* [多进程](#多进程)
* [例子一](#例子一)
* [例子二](#例子二)
* [例子三](#例子三)
* [例子四](#例子四)
* [例子五](#例子五)
* [使用进程池](#使用进程池)
* [使用阻塞进程池](#使用阻塞进程池)
* [关注进程池结果](#关注进程池结果)
* [多线程](#多线程)
* [线程锁](#线程锁)
* [多核处理器](#多核处理器)
* [为什么说多线程是鸡肋](#为什么说多线程是鸡肋)
* [多线程小结](#多线程小结)
* [](#)


***
# 定义
* 对于操作系统来说，一个任务就是一个进程（Process），比如打开一个浏览器就是启动一个浏览器进程，打开一个记事本就启动了一个记事本进程，打开两个记事本就启动了两个记事本进程，打开一个Word就启动了一个Word进程。
* 有些进程还不止同时干一件事，比如电脑上看电影，就必须由一个线程播放视频，另一个线程播放音频，否则，单线程实现的话就只能先把视频播放完再播放音频，或者先把音频播放完再播放视频，这显然是不行的。比如Word，它可以同时进行打字、拼写检查、打印等事情。在一个进程内部，要同时干多件事，就需要同时运行多个“子任务”，我们把进程内的这些“子任务”称为线程（Thread）。
```
由于每个进程至少要干一件事，所以，一个进程至少有一个线程。当然，像Word这种复杂的进程可以有多个线程，多个线程可以同时执行，多线程的执行方式和多进程是一样的，也是由操作系统在多个线程之间快速切换，让每个线程都短暂地交替运行，看起来就像同时执行一样。当然，真正地同时执行多线程需要多核CPU才可能实现。
多任务的实现有3种方式:
一，多进程模式；启动多个进程，每个进程虽然只有一个线程，但多个进程可以一块执行多个任务。
二，多线程模式；启动一个进程，在一个进程内启动多个线程，这样，多个线程也可以一块执行多个任务。
三，多进程+多线程模式；启动多个进程，每个进程再启动多个线程，这样同时执行的任务就更多了，当然这种模型更复杂，实际很少采用。
```
**总结：线程是最小的执行单元，而进程由至少一个线程组成。如何调度进程和线程，完全由操作系统决定，程序自己不能决定什么时候执行，执行多长时间。**
**多进程和多线程的程序涉及到同步、数据共享的问题，编写起来更复杂。**

***
# 多进程
```
要让Python程序实现多进程（multiprocessing），我们先了解操作系统的相关知识。
Unix/Linux操作系统提供了一个fork()系统调用，它非常特殊。普通的函数调用，调用一次，返回一次，但是fork()调用一次，返回两次，因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回。
子进程永远返回0，而父进程返回子进程的ID。这样做的理由是，一个父进程可以fork出很多子进程，所以，父进程要记下每个子进程的ID，而子进程只需要调用getppid()就可以拿到父进程的ID。
Python的os模块封装了常见的系统调用，其中就包括fork，可以在Python程序中轻松创建子进程：
```

***
* 一个应用程序至少有一个进程,一个进程至少有一个线程.线程  进程 也是程序。
* 并发：在操作系统中，是指一个时间段中有几个程序都处于已启动运行到运行完毕之间，且这几个程序都是在同一个处理机上运行，但任一个时刻点上只有一个程序在处理机上运行。并发在多线程的情况,如果系统只有一个CPU,则它根本不可能真正同时进行一个以上的线程，它只能把CPU运行时间划分成若干个时间段,再将时间 段分配给各个线程执行，在一个时间段的线程代码运行时，其它线程处于挂起状。.这种方式我们称之为并发(Concurrent)。
* 并行：当系统有一个以上CPU时,则线程的操作有可能非并发。当一个CPU执行一个线程时，另一个CPU可以执行另一个线程，两个线程互不抢占CPU资源，可以同时进行，这种方式我们称之为并行(Parallel)
* 进程同步:就是在发出一个功能调用时，在没有得到结果之前，该调用就不返回。也就是必须一件一件事做,等前一件做完了才能做下一件事.就像早上起床后,先洗涮,然后才能吃饭,不能在洗涮没有完成时,就开始吃饭.按照这个定义，其实绝大多数函数都是同步调用（例如sin,isdigit等）。但是一般而言，我们在说同步、异步的时候，特指那些需要其他部件协作或者需要一定时间完成的任务。最常见的例子就是sendmessage。该函数发送一个消息给某个窗口，在对方处理完消息之前，这个函数不返回。当对方处理完毕以后，该函数才把消息处理函数所返回的lresult值返回给调用者。
* 进程异步:异步的概念和同步相对

***
# 多进程例子
# 例子一
* 程序一旦开始执行就在此刻创建一个父进程，然后我们用程序创建两个子进程
```python
from multiprocessing import Process
import os,time
def r1(name):
    for i in range(5):
        print(name,"**",os.getpid())
        time.sleep(2)
def r2(name):
    for i in range(5):
        print(name,"**",os.getpid())
        time.sleep(2)
if __name__=="__main__":
    print("parent process %s  run..."% os.getpid())
    p1=Process(target=r1,args=('process1',))
    p2 = Process(target=r2, args=('process2',))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("parent process %s  end"% os.getpid())
>>>
parent process 5656  run...
process1 ** 5232
process2 ** 8836
process1 ** 5232
process2 ** 8836
process1 ** 5232
process2 ** 8836
process1 ** 5232
process2 ** 8836
process1 ** 5232
process2 ** 8836
parent process 5656  end
```
***
# 例子二
* `multiprocessing.Process(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)`
* `run方法 如果在创建Process对象的时候不指定target,那么就会默认执行Process的run方法`
```python
from multiprocessing import Process
import  os
def r():
    print("process %s run the method"% os.getpid())

if __name__=="__main__":
    print('parent process %s run..'% os.getpid())
    #没有指定Process的target
    p1=Process()
    p2=Process()
    #如果在创建Process时候不指定target,那么执行时木有任何效果。
    #因为默认的run方法是判断如果不指定target，那就什么都不做
    #所以这里手动改变run方法
    p1.run=r
    p2.run=r
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("parent process %s end"% os.getpid())
>>>
parent process 8360 run..
process 6560 run the method
process 7312 run the method
parent process 8360 end
```

***
# 例子三
* join()方法：阻塞当前进程，直到调用join方法的那个进程执行完，再继续执行当前进程
* 把例子一代码的两个join注释掉
```python
from multiprocessing import Process
import os,time
def r1(name):
    for i in range(5):
        print(name,"**",os.getpid())
        time.sleep(2)
def r2(name):
    for i in range(5):
        print(name,"**",os.getpid())
        time.sleep(2)
if __name__=="__main__":
    print("parent process %s  run..."% os.getpid())
    p1=Process(target=r1,args=('process1',))
    p2 = Process(target=r2, args=('process2',))
    p1.start()
    p2.start()
    #p1.join()
    #p2.join()
    print("parent process %s  end"% os.getpid())
>>>
parent process 8428  run...
parent process 8428  end
process1 ** 4868
process2 ** 6112
process1 ** 4868
process2 ** 6112
process1 ** 4868
process2 ** 6112
process1 ** 4868
process2 ** 6112
process1 ** 4868
process2 ** 6112
```
**加join()函数是把主进程阻塞，直到子进程进行完，再执行主进程；而注释掉join()主进程先执行完**

# 例子四
* 加大进程2的睡眠时间，注释掉p2.join()
```python
from multiprocessing import Process
import os,time
def r1(name):
    for i in range(5):
        print(name,"**",os.getpid())
        time.sleep(2)
def r2(name):
    for i in range(5):
        print(name,"**",os.getpid())
        time.sleep(5)
if __name__=="__main__":
    print("parent process %s  run..."% os.getpid())
    p1=Process(target=r1,args=('process1',))
    p2 = Process(target=r2, args=('process2',))
    p1.start()
    p2.start()
    p1.join()
    #p2.join()
    print("parent process %s  end"% os.getpid())
>>>
parent process 8288  run...
process1 ** 6812
process2 ** 5640
process1 ** 6812
process1 ** 6812
process2 ** 5640
process1 ** 6812
process1 ** 6812
parent process 8288  end
process2 ** 5640
process2 ** 5640
process2 ** 5640
```
**由于是p1.join(),执行这一步的时候，阻塞当前进程，先把p1执行，以后，由于没有阻塞，所以就要执行父进程，最后把木有执行完的子进程执行完**

***
# 例子五
* 为什么对于所有的子进程是先依次调用start再调用join，而不是每一子进程调用start就立刻调用join呢
```python
from multiprocessing import Process
import os,time
def r1(name):
    for i in range(5):
        print(name,"**",os.getpid())
        time.sleep(2)
def r2(name):
    for i in range(5):
        print(name,"**",os.getpid())
        time.sleep(5)
if __name__=="__main__":
    print("parent process %s  run..."% os.getpid())
    p1=Process(target=r1,args=('process1',))
    p2 = Process(target=r2, args=('process2',))
    p1.start()
    p1.join()
    p2.start()
    #p2.join()
    print("parent process %s  end"% os.getpid())
>>>
parent process 3936  run...
process1 ** 8952
process1 ** 8952
process1 ** 8952
process1 ** 8952
process1 ** 8952
parent process 3936  end
process2 ** 8228
process2 ** 8228
process2 ** 8228
process2 ** 8228
process2 ** 8228
```
**发现是先执行完p1,再执行主进程，最后才开始p2**
**join是用来阻塞当前进程的，p1.start()之后，p1就提示主进程，你要等我执行完之后你再执行你的，那么主进程就乖乖的等，自然就没有执行p2.start()这一句话了**


***
# 使用进程池
* multiprocessing.pool.Pool([processes[, initializer[, initargs[, maxtasksperchild[, context]]]]])
* 调用join之前要先调用join函数，否则会出错。执行完close后不会有新的进程加入到进程池，join函数等待所有子进程结束
```python
from multiprocessing.pool import Pool
import time,os

def f(name):
    print('%s current child process %s start runing...'%(name,os.getpid()))
    time.sleep(1)
    print('%s current child process %s end'%(name,os.getpid()))

if __name__=="__main__":
    print("parent process %s run..."% os.getpid())
    p=Pool(processes=3)
    for i in range(4):
        p.apply_async(f,(i,))#维持执行进程的总数为3,当一个进程执行完之后，会添加新的进程进去
    print('****************')
    p.close()
    p.join()
    print("parent process %s end..."% os.getpid())
>>>
parent process 2376 run...
****************
0 current child process 2096 start runing...
1 current child process 6328 start runing...
2 current child process 3980 start runing...
0 current child process 2096 end
3 current child process 2096 start runing...
1 current child process 6328 end
2 current child process 3980 end
3 current child process 2096 end
parent process 2376 end...
```
***
```
apply_async(func[, args[, kwds[, callback[, error_callback]]]]) 异步，非阻塞    async:异步的
apply(func[, args[, kwds]]) 阻塞的
close()关闭pool，使其不再接受新的任务
terminate()结束工作进程，不再处理未完成的任务
join()阻塞当前进程，等待子进程的推出，join()要用在close()或terminate()之后
```
***
```
执行说明：
创建一个进程池pool，并设定进程的数量为3，range(4)会相继产生四个对象[0, 1, 2, 3]，四个对象被提交到pool中，因pool指定进程数为3，
所以0、1、2会直接送到进程中执行，当其中一个执行完事后才空出一个进程处理对象3，
所以会输出3 current child process 2096 start runing...
因为为非阻塞，主函数会自己执行自个的，不搭理进程的执行，所以有****************
最后主程序在pool.join（）处等待各个进程的结束。然后自己再结束
```

***
# 使用阻塞进程池
```python
from multiprocessing.pool import Pool
import time,os

def f(name):
    print('%s current child process %s start runing...'%(name,os.getpid()))
    time.sleep(1)
    print('%s current child process %s end'%(name,os.getpid()))

if __name__=="__main__":
    print("parent process %s run..."% os.getpid())
    p=Pool(processes=3)
    for i in range(4):
        p.apply(func=f,args=(i,))
    print('****************')
    p.close()
    p.join()
    print("parent process %s end..."% os.getpid())
>>>
parent process 8112 run...
0 current child process 7976 start runing...
0 current child process 7976 end
1 current child process 4540 start runing...
1 current child process 4540 end
2 current child process 3556 start runing...
2 current child process 3556 end
3 current child process 7976 start runing...
3 current child process 7976 end
****************
parent process 8112 end...
```

***
# 关注进程池结果
* get()得出每个结果返回的值
```python
from multiprocessing.pool import Pool
import time,os

def f(name):
    print('%s current child process %s start runing...'%(name,os.getpid()))
    time.sleep(1)
    print('%s current child process %s end'%(name,os.getpid()))
    return('%s current child process %s end'%(name,os.getpid()))

if __name__=="__main__":
    print("parent process %s run..."% os.getpid())
    p=Pool(processes=3)
    result=[]
    for i in range(3):
        result.append(p.apply_async(func=f,args=(i,)))
    print('****************')
    p.close()
    p.join()
    for item in result:
        print("*****",item.get())
    print("parent process %s end..."% os.getpid())
>>>
parent process 7552 run...
****************
0 current child process 8136 start runing...
1 current child process 5584 start runing...
2 current child process 6180 start runing...
0 current child process 8136 end
1 current child process 5584 end
2 current child process 6180 end
***** 0 current child process 8136 end
***** 1 current child process 5584 end
***** 2 current child process 6180 end
parent process 7552 end...
```

***
# 多线程
```
多线程使用threading高级模块
由于任何进程默认就会启动一个线程，我们把该线程称为主线程，主线程又可以启动新的线程，
Python的threading模块有个current_thread()函数，它永远返回当前线程的实例。
主线程实例的名字叫MainThread，子线程的名字在创建时指定，我们用LoopThread命名子线程。
名字仅仅在打印时用来显示，完全没有其他意义，如果不起名字Python就自动给线程命名为Thread-1，Thread-2...
```

***
* Ex.1
```python
import time,threading
def loop():
    print("thread %s is running..."% threading.current_thread().name)
    n=0
    while n<5:
        n=n+1
        print("thread %s >>> %s"% (threading.current_thread().name,n))
        time.sleep(1)
    print("thread %s ended"% threading.current_thread().name)
if __name__=="__main__":
    print("thread %s is running..."% threading.current_thread().name)
    t=threading.Thread(target=loop,name="LoopThread")
    t.start()
    t.join()
    print("thread %s ended"% threading.current_thread().name)
>>>
thread MainThread is running...
thread LoopThread is running...
thread LoopThread >>> 1
thread LoopThread >>> 2
thread LoopThread >>> 3
thread LoopThread >>> 4
thread LoopThread >>> 5
thread LoopThread ended
thread MainThread ended
```

***
# 线程锁
```
多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，
而多线程中，所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改，
因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了。
解决办法：线程锁，因此其他线程不能同时执行此目标，只能等待，直到锁被释放后，获得该锁以后才能改。
由于锁只有一个，无论多少线程，同一时刻最多只有一个线程持有该锁，所以，不会造成修改的冲突。
创建一个锁就是通过threading.Lock()来实现
```
```python
import threading
balance=0
lock=threading.Lock()
def change_it(n):
    global balance
    balance=balance+n
    balance=balance-n
def run_thread(n):
    for i in range(1000000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()
t=threading.Thread(target=run_thread,args=(8,))
t.start()
t.join()
print(balance)
```
```
当多个线程同时执行lock.acquire()时，只有一个线程能成功地获取锁，然后继续执行代码，其他线程就继续等待直到获得锁为止。
获得锁的线程用完后一定要释放锁，否则那些苦苦等待锁的线程将永远等待下去，成为死线程。所以我们用try...finally来确保锁一定会被释放。
锁的好处就是确保了某段关键代码只能由一个线程从头到尾完整地执行，坏处当然也很多，首先是阻止了多线程并发执行，
包含锁的某段代码实际上只能以单线程模式执行，效率就大大地下降了。其次，由于可以存在多个锁，不同的线程持有不同的锁，
并试图获取对方持有的锁时，可能会造成死锁，导致多个线程全部挂起，既不能执行，也无法结束，只能靠操作系统强制终止。
```

***
# 多核处理器
```
如果你不幸拥有一个多核CPU，你肯定在想，多核应该可以同时执行多个线程。
因为Python的线程虽然是真正的线程，但解释器执行代码时，有一个GIL锁：Global Interpreter Lock，
任何Python线程执行前，必须先获得GIL锁，然后，每执行100条字节码，解释器就自动释放GIL锁，
让别的线程有机会执行。这个GIL全局锁实际上把所有线程的执行代码都给上了锁，所以，多线程在Python中只能交替执行，
即使100个线程跑在100核CPU上，也只能用到1个核。
GIL是Python解释器设计的历史遗留问题，通常我们用的解释器是官方实现的CPython，要真正利用多核，除非重写一个不带GIL的解释器。
所以，在Python中，可以使用多线程，但不要指望能有效利用多核。如果一定要通过多线程利用多核，
那只能通过C扩展来实现，不过这样就失去了Python简单易用的特点。
不过，也不用过于担心，Python虽然不能利用多线程实现多核任务，但可以通过多进程实现多核任务。
多个Python进程有各自独立的GIL锁，互不影响。
```

***
# 为什么说多线程是鸡肋
* 实验：将数字一亿递减，减到0就终止，计算时间
* 单线程花费16秒
```python
import threading,multiprocessing,time
print("thread %s is running..."% threading.current_thread().name)
n=multiprocessing.cpu_count()
print("自己电脑上CPU的核数为%s核！！！"% n)
#任务
def decrement(n):
    while n>0:
        n-=1
#single thread
start=time.time()
decrement(100000000)
cost=time.time()-start
print(cost)
print("thread %s ended"% threading.current_thread().name)
>>>
thread MainThread is running...
自己电脑上CPU的核数为4核！！！
16.042685508728027
thread MainThread ended
```

***
* 多线程
```python
import threading,multiprocessing,time
print("thread %s is running..."% threading.current_thread().name)
n=multiprocessing.cpu_count()
print("自己电脑上CPU的核数为%s核！！！"% n)
#任务
def decrement(n):
    while n>0:
        n-=1
#single thread
start=time.time()
t1=threading.Thread(target=decrement,args=(100000000,))
t2=threading.Thread(target=decrement,args=(100000000,))
t1.start()
t2.start()
t1.join()#主线程阻塞，直到t1执行完成，主线程继续往后执行
t2.join()
cost=time.time()-start
print(cost/2)
print("thread %s ended"% threading.current_thread().name)
>>>
thread MainThread is running...
自己电脑上CPU的核数为4核！！！
16.09876549243927
thread MainThread ended
```

***
* 多线程不快反而慢
```
在Cpython解释器(python语言的主流解释器)中，有一把GIL(Global Interpreter Lock 全局解释器锁),在解释器解释执行python代码时，先要得到这把锁，
意味着，任何时候只可能有一个线程在执行代码，其他线程要想获得CPU执行代码指令，就必须先获得这把锁，如果锁被其他线程占用了，
那么该线程就只能等待，直到占有该锁的线程释放锁才有执行代码指令的可能。

因此，这也就是为什么两个线程一起执行反而更加慢的原因，因为同一时刻，只有一个线程在运行，其它线程只能等待，即使是多核CPU，
也没办法让多个线程「并行」地同时执行代码，只能是交替执行，因为多线程涉及到上线文切换、锁机制处理（获取锁，释放锁等），
所以，多线程执行不快反慢。
```

***
# 多线程小结
```
多线程编程，模型复杂，容易发生冲突，必须用锁加以隔离，同时，又要小心死锁的发生。
Python解释器由于设计时有GIL全局锁，导致了多线程无法利用多核。多线程的并发在Python中就是一个美丽的梦。
```
