

# Detlev Aschhoff info@vmais.de
# 433 RC Remote for Quigg GT 7000, Tevion, GT-FSI-04
#
# first 12 bit = Adresse   0 to 11
# 12,13 Units 0=00 1=10 2=11 3=01  4 to 7 same wiith dim bit 16
# 14 Command to all units
# 15 1 = on    0 = off    oder Dimmer up/ down
# 16 0= Switch    1 = Dimmer
# 17 allways 0
# 18 set with unit why ?????
# 19 even partity = 1
#
# zero    -------
#      --|
#
# one         --
#      -------|
# Sycn=80000, short=700 long=1400 microsek

def code(dev):

  addr=dev["addr"]
  unit=dev["unit"]
  state=dev["state"]
  
  code=list(bin(int(addr))[2:])     # adress as binary List

  for i in range(12-len(code)):     # fill left with "0" for 12 bit length
      code.insert(i,"0")
  for i in range(20-len(code)):     # fill right with "0" last 8 bit 
      code.append("0")
      
  if unit>"3":code[16]="1"           # unit 4 to 7 is a dimmer
  if unit=="0" or unit=="4":         # code unit 0 to 7
    code[12]="0"
    code[13]="0"
  if unit=="1" or unit=="5":         # code unit 0 to 7
    code[12]="1"
    code[13]="0"
    code[18]="1"
  if unit=="2" or unit=="6":         # code unit 0 to 7
    code[12]="1"
    code[13]="1" 
    code[18]="1"
  if unit=="3" or unit=="7":         # code unit 0 to 7
    code[12]="0"
    code[13]="1" 

  if state=="2":code[14]="1"         # Command to all
  if state=="1":code[15]="1"         # on=1
  
  if code.count("1")%2==0:           # parity even
      code[19]="1"

  sync="80000"
  short="700"
  long="1400"
  outcode="".join(code)
  return sync,short,long,outcode




