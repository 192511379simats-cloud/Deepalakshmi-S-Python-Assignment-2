def normalise(text):
 return text.strip().replace(" ","").replace("-","").upper()
def is_valid(reg):
 return (len(reg) in (9,10) and reg[:2].isalpha() and reg[2:4].isdigit()
         and len(reg[4:-4]) in (1,2) and reg[4:-4].isalpha() and reg[-4:].isdigit())
def receipt_format(reg):
 if not is_valid(reg):raise ValueError("Invalid registration")
 return f"{reg[:2]} {reg[2:4]} {reg[4:-4]} {reg[-4:]}"
if __name__=="__main__":
 for raw in ["tn 09 ab 1234","KA-01-M-0007","Tn09Ab1234","TN9AB1234","TN 22 1234 AB","12-09-AB-1234"]:
  r=normalise(raw);print(f"{raw:16} -> {r:11} {'valid' if is_valid(r) else 'INVALID'}",receipt_format(r) if is_valid(r) else "")
