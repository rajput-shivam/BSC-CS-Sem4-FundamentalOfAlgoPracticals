def evenElement(l):
    d={}
    i=0
    while i<len(l)-1:
        if l[i]<=l[i+1]:
            key=l[i]
            value=l[i+1]
            d[key]=value
        if l[i+1]<=l[i]:
            key=l[i+1]
            value=l[i]
            d[key]=value
        i=i+2
    return d

def oddElement(l):
    d={}
    x=l.pop()
    d=evenElement(l)
    d[x]="advdg"
    return d
        
tournament=[]
def tournamentFix(l):
    if len(l)%2==0:
        d=evenElement(l)
    if len(l)%2==1:
        d=oddElement(l)
    tournament.append(d)
    l=list(d)
    print("\nTOURNAMENT",tournament)
    print("NEXT ROUND",l)
    if len(d)>1:
        return tournamentFix(l)
    return l[0]



question=[1,2,3,4,5]
small=tournamentFix(question)
print("\nFirst Smallest:",small)
x=10**10
for i in tournament:
    if type(i[small])==int:
        if i[small]<x:
            x=i[small]
print("Second smallest",x)






