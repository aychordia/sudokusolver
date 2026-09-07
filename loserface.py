def badcomplement(a,b,c):
    n = []
    bb=b
    m=0
    while bb <=c and m < len(a):
        if a[m] != bb:
            n=n+[bb]
        else:
            m=m+1
        bb=bb+1
    if m == len(a):
        for k in range(bb,c+1):
            n=n+[k]
    return n
        


def badchecker(b,n):
    f=[]
    c = n%9
    dd = -1*(n%3)
    uu = -1*((n//9)%3)
    d = badcomplement([0],dd,dd+2) #n%3
    u=badcomplement([0],uu,uu+2) #(n//9)%3
    
    v = n//9 * 9
    for o in range(0,9):
        tr1 = [b[c+o*9],b[v+o]]
        for t in tr1:
            if t!=' ':
                f=f+[int(t)]
    for x in u:
        for y in d:
            tr2 = b[n+x*9+y]
            if tr2 != ' ':
                f=f+[int(tr2)]
  
    return (badcomplement(sorted(list(set(f))),1,9))
stre="9  5 8  7 8 3 29 5 54    8  7 68  321    4  85  219 6    9 6  1726  1 4   147  56"
def badsolver(der):
    if der.find(' ') == -1:
        print(der)
        return(der)
    else:
        ter = der.find(' ')
        wer = badchecker(der,ter)
        for h in wer:
            badsolver(der[:ter]+str(h)+der[ter+1:])
ardef = "8          36      7  9 2   5   7       457     1   3   1    68  85   1  9    4  "
sdre = " 91    7 3       67   4       1    5 6   8 3 53    2 9     75   8     42  46     "

badsolver(ardef)


    


        

