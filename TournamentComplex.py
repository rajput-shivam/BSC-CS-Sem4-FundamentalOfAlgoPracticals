#Anomalies(1000 wala,100)


question=[6,22,23,30,36,5,32,314,34,11,1,24,7]

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
    d[x]=max(question)+1
    return d
        
tournament=[]
def tournamentFix(l):
    if len(l)%2==0:
        dic=evenElement(l)
    if len(l)%2==1:
        dic=oddElement(l)
    tournament.append(dic)
    print("\nTOURNAMENT",tournament)
    print("NEXT ROUND",list(dic))
    if len(dic)>1:
        return tournamentFix(list(dic))
    return l[0]

l=[]
def printElement(n,smallest):
    if n==1:
        return smallest
    for i in tournament:
        if smallest in i.keys():
            l.append(i[smallest])
    curSmall= min(l)
    l.remove(curSmall)
    print(n-1," ",l," ",curSmall)
    0
    if n>=3 and n<=len(question) :
        return printElement(n-1,curSmall)
    return curSmall
        

    
print("QUESTION:",question)
smallest=tournamentFix(question)
n=int(input("\n\nwhich smallest element?"))
print(str(n)+"-smallest element:",printElement(n,smallest))







