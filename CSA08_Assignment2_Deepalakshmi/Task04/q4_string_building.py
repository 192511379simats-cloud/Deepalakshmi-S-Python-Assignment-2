import time,csv,pathlib,statistics
def build_plus(parts):
 s=""
 for p in parts:s+=p+";"
 return s
def build_join(parts):return "".join(p+";" for p in parts)
def build_fstring(n):return "".join(f"Item{i}:Rs{i%50};" for i in range(n))
def measure(fn,arg):
 ts=[];v=None
 for _ in range(3):
  t=time.perf_counter();v=fn(arg);ts.append(time.perf_counter()-t)
 return v,ts,statistics.mean(ts)
if __name__=="__main__":
 rows=[]
 for n in (1000,10000,200000):
  parts=[f"Item{i}:Rs{i%50}" for i in range(n)]
  a,ta,ma=measure(build_plus,parts);b,tb,mb=measure(build_join,parts);c,tc,mc=measure(build_fstring,n)
  assert a==b==c
  print(n,len(a),"same",a==b,"+= ",ta,"avg",ma,"join",tb,"avg",mb,"fstring",tc,"avg",mc)
  rows.append([n,*ta,*tb,*tc,ma,mb,mc,len(a)])
 out=pathlib.Path(__file__).resolve().parents[1]/"evidence/q4_timings.csv";out.parent.mkdir(exist_ok=True)
 with out.open("w",newline="") as f:
  w=csv.writer(f);w.writerow(["n","plus1","plus2","plus3","join1","join2","join3","fstr1","fstr2","fstr3","plus_avg","join_avg","fstr_avg","length"]);w.writerows(rows)
