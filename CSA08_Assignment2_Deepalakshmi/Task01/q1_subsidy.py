CASES=[("H1",100,False,False),("H2",101,True,False),("H3",101,False,False),("H4",200,True,False),("H5",200,False,True),("H6",201,False,False),("H7",201,False,True),("H8",80,True,True)]
def independent_if(u,r,s):
 out=[]
 if u<=100: out.append("FULL")
 if 101<=u<=200 and r: out.append("PARTIAL")
 if u>200 and s: out.append("SENIOR_EXCEPTION")
 return out or ["NONE"]
def exclusive(u,r,s):
 if u<=100:return "FULL"
 elif 101<=u<=200:
  if r:return "PARTIAL"
  else:return "NONE"
 elif u>200 and s:return "SENIOR_EXCEPTION"
 else:return "NONE"
def main():
 print("ID units ration senior | separate-if | if-elif-else")
 for i,u,r,s in CASES:print(i,u,r,s,"|",",".join(independent_if(u,r,s)),"|",exclusive(u,r,s))
 def faulty_independent_if(u,r,s):
  out=[]
  if u<=100: out.append("FULL")
  if u<=200 and r: out.append("PARTIAL")  # overlaps the <=100 band
  if s: out.append("SENIOR_EXCEPTION")
  return out
 print("Overlap example:",faulty_independent_if(100,True,True))
if __name__=="__main__":main()
