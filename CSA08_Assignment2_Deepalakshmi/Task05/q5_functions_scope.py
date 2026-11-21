def add_item_buggy(item,order=[]):
 order.append(item);return order
def add_item(item,order=None):
 if order is None:order=[]
 order.append(item);return order
def calculate(items,gst_rate=0.05):
 subtotal=sum(price for _,price in items);gst=subtotal*gst_rate
 return subtotal,gst,subtotal+gst
counter=0
def change_global():
 global counter
 counter+=1
def make_counter():
 value=0
 def increment():
  nonlocal value
  value+=1;return value
 return increment
if __name__=="__main__":
 print(add_item_buggy("Tea"),add_item_buggy("Vada"))
 print(add_item("Tea"),add_item("Vada"))
 print("defaults:",add_item_buggy.__defaults__)
 print("three customers:",add_item("Tea"),add_item("Vada"),add_item("Coffee"))
 print("subtotal,GST,total:",calculate([("Idli",30),("Tea",15)],gst_rate=0.05))
 change_global();print("global:",counter)
 c=make_counter();print("nonlocal:",c(),c())
