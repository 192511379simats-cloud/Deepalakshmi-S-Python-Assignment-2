from functools import lru_cache
import sys,time
calls=0
def ways_naive(n):
 global calls
 calls+=1
 if n<=1:return 1
 return ways_naive(n-1)+ways_naive(n-2)
@lru_cache(None)
def ways_memo(n):
 global calls
 calls+=1
 if n<=1:return 1
 return ways_memo(n-1)+ways_memo(n-2)
def ways_loop(n):
 if n<=1:return 1
 a=b=1
 for _ in range(2,n+1):a,b=b,a+b
 return b
if __name__=="__main__":
 print("hand answers:",[ways_loop(i) for i in range(1,7)])
 for n in (10,20,25,30):
  calls=0;v=ways_naive(n);nc=calls
  ways_memo.cache_clear();calls=0;m=ways_memo(n);mc=calls
  print(n,v,"naive calls",nc,"memo calls",mc,"loop",ways_loop(n))
 print("recursion limit",sys.getrecursionlimit())
 ways_memo.cache_clear()
 try:print("memo 1000",ways_memo(1000))
 except RecursionError:print("memo 1000: RecursionError")
 print("loop 1000 digits",len(str(ways_loop(1000))))
