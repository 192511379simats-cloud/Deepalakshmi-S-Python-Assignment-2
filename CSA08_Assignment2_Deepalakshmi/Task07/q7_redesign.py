from functools import lru_cache
import time,csv,pathlib
def memo(n):
 @lru_cache(None)
 def f(k):
  if k<=1:return 1
  return f(k-1)+f(k-2)
 return f(n),f.cache_info().currsize
def iterative(n):
 if n<=1:return 1
 a=b=1
 for _ in range(2,n+1):a,b=b,a+b
 return b
if __name__=="__main__":
 rows=[]
 for n in (10,25,100,500,900,1000):
  t=time.perf_counter()
  try:old,count=memo(n);status="OK"
  except RecursionError:old=None;count=None;status="RecursionError"
  mt=time.perf_counter()-t
  t=time.perf_counter();new=iterative(n);it=time.perf_counter()-t
  print(n,status,"cache states",count,"same",old==new if old is not None else "not comparable","memo",mt,"loop",it)
  rows.append([n,status,count,mt,it,len(str(new))])
 p=pathlib.Path(__file__).resolve().parents[1]/"evidence/q7_redesign.csv";p.parent.mkdir(exist_ok=True)
 with p.open("w",newline="") as f:
  w=csv.writer(f);w.writerow(["n","memo_status","cache_states","memo_seconds","iterative_seconds","digits"]);w.writerows(rows)
