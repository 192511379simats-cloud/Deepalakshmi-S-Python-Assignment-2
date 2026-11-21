CODE="482913"
def while_design(values,limit=3):
 attempts=0
 while attempts<limit:
  if not values: print("No more supplied input."); return
  otp=values.pop(0)
  if otp=="": print("Blank ignored"); continue
  attempts+=1
  if otp==CODE: print("Verified"); break
  print("Wrong",attempts)
 else: print("Locked for 30 minutes")
def for_design(values,limit=3):
 it=iter(values)
 for attempt in range(1,limit+1):
  while True:
   try:otp=next(it)
   except StopIteration: print("Input sequence ended"); return
   if otp=="": print("Blank ignored"); continue
   break
  if otp==CODE: print("Verified on",attempt); break
  print("Wrong",attempt)
 else: print("Locked for 30 minutes")
def extended(values,security):
 print("Extended allowance:",5 if security else 3)
 while_design(values,5 if security else 3)
def placeholder(): pass
if __name__=="__main__":
 print("WHILE:");while_design(["","111","222","333"])
 print("FOR:");for_design(["111","482913"])
 print("Security correct:");extended(["1","2","3","4","482913"],True)
