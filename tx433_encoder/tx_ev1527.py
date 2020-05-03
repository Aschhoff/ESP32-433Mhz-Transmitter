







# Detlev Aschhoff info@vmais.de
# Protokoll EV1527 Contact

def code(dev):
    addr=dev["addr"]
    state=dev["state"]
#----------------  first 12 bits are the Address -----------------------
    a=bin(int(addr))[2:]      # addr in binaer  MSB  LSB
    rev = "" 
    for i in a: 
      rev = i + rev           # binaer string umdrehen LSB MSB
    a=rev
    a+=(20-len(a))*"0"        # Rest rechts mit 0 auffuellen 
      
    b=bin(int(state))[2:]     # gleiche fuer State
    rev=""
    for i in b: 
      rev = i + rev           # binaer string umdrehen LSB MSB
    b=rev
    b+=(4-len(b))*"0"

    out=list(a+b)

    for i in range(24):       # Liste invertieren 1 -- 0
        if out[i]=="1":
            out[i]="0"
        else:
            out[i]="1"
    #---------------------- Puls Pattern ------------------------------------
    sync="14000"
    short="400"
    long="1400"
    
    outcode="".join(out)
    return sync,short,long,outcode











