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
