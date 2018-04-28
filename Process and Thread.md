# 进程和线程
* [定义](#定义)
* [多进程](#多进程)
* [例子一](#例子一)
* [例子二](#例子二)
* [例子三](#例子三)
* [例子四](#例子四)
* [例子五](#例子五)


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
* 并发：在操作系统中，是指一个时间段中有几个程序都处于已启动运行到运行完毕之间，且这几个程序都是在同一个处理机上运行，但任一个时刻点上只有一个程序在处理机上运行。并发当有多个线程在操作时,如果系统只有一个CPU,则它根本不可能真正同时进行一个以上的线程，它只能把CPU运行时间划分成若干个时间段,再将时间 段分配给各个线程执行，在一个时间段的线程代码运行时，其它线程处于挂起状。.这种方式我们称之为并发(Concurrent)。
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
