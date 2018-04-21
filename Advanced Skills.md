# 高级技巧
* if-else

***
## if-else
***if-else 语句的多种写法***
* Ex.1 把两个数中最大的一个赋值给另一个数
```python
a,b=1,2
if a>b:
    c=a
else:
    c=b
print(c)
```
* Ex.2 改写为表达式
```python
a,b=1,2
c=a if a>b else b
print(c)
```
* Ex.3 改写为二维列表
```python
a,b=1,2
c=[b,a][a>b]
print(c)
```
* Ex.4 传说中源自某个黑客
```python
a,b=1,2
c=(a>b and [a] or [b])[0]
print(c)
```
