s=input("GTCATGAC")
comp={"G":"C","C":"G","A":"T","T":"A"}
slist=list(s)
rs=""
for i in slist:
    rs=comp[i]+rs
if rs==s:
    print("DNA palindrome")
else:
    print("Not DNA palindrome")

s=input("GAATTC")
comp={"G":"C","C":"G","A":"T","T":"A"}
slist=list(s)
rs=""
for i in slist:
    rs=comp[i]+rs
if rs==s:
    print("DNA palindrome")
else:
    print("Not DNA palindrome")

s=input("GTTAATTG")
comp={"G":"C","C":"G","A":"T","T":"A"}
slist=list(s)
rs=""
for i in slist:
    rs=comp[i]+rs
if rs==s:
    print("DNA palindrome")
else:
    print("Not DNA palindrome")

    
    
