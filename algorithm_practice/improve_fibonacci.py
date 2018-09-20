# 传统使用递归的斐波拉切计算：
# 涉及到了大部分重复计算
# def fib(n):
#     if n<=0:
#         return 0
#     if n==1:
#         return 1
#     return fib(n-1)+fib(n-2)


# 使用动态规划解
# 动态规划：记住求解过的解节省时间/空间
# 自底向上的动态规划
import time
# def fib(n):
#     rem_result = [0,1]
#     for _ in range(2,n+1):
#         rem_result.append(rem_result[-1]+rem_result[-2])
    
#     return rem_result[n]



# 第三种写法，不需要存储时，速度更快
def fib(n):
    prev,current = 0,1
    for _ in range(2,n+1):
        prev,current = current,prev+current
    return current

start = time.clock()
print(fib(300))
end = time.clock()
print(end - start)
