import sys 
def bm(q,nr,h):
    nr2=""
    for i in nr:
	    nr2=nr2+bin(ord(i))+" "
    nr2=nr2.replace("b","")
    nr3="\u200d"
    for i in nr2:
        if i=="0":
            nr3=nr3+"\u200b"
        if i=="1":
            nr3=nr3+"\u200c"
        if i==" ":
            nr3=nr3+"\u200d"
    print(q+nr3+h)
def jm(nr):
    nr=nr.split("\u200d")
    nr=nr[1:-1]
    nr1=""
    for i in nr:
        i=i.replace("\u200b","0")
        i=i.replace("\u200c","1")
        nr1=nr1+chr(int(i,2))
    print(nr1)
if len(sys.argv)>2:
    if sys.argv[1]=="bm":
        bm(sys.argv[2],sys.argv[3],sys.argv[4])
    else:
        jm(sys.argv[2])