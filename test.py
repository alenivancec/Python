# 1. Upiši n prirodnih brojeva. Svaki broj spremi u listu na mjesto x gdje je x jednak broju ponavljanja tog broja u listi prije dodavanja. Nakon svakog upisa ispišite listu.

n=int(input())
l=[]
for i in range(n):
    x=int(input())
    l.insert(l.count(x),x)
    print(l)
    
 # 2. Upiši n prirodnih brojeva. Svaki broj spremi u listu na mjesto x gdje je x jednak broju brojeva manjih od upisanog broja koji su već u listi. Nakon svakog upisa ispišite listu.

n=int(input("Upiši n prirodnih brojeva:"))
l=[]
for i in range(n):
    x=int(input("Upiši broj " + str(i+1) + ": "))
    br=0
    for j in l:
        if j<br:
            br+=1
    l.insert(br, x)
    print(l)

# 3. Upiši n prirodnih brojeva. S4premajte brojeve u listu na način da osigurate da broj nikad nema dva manja broja ispred sebe. Nakon svakog upisa ispišite listu.

n=int(input("Upiši n prirodnih brojeva:"))
l=[]
for i in range(n):
    l.append(int(input("Upiši broj " + str(i+1) + ": ")))
    l.sort()
    l.reverse()
    print(l)
    
# 6. Upiši n prirodnih brojeva i spremi ih u listu. Promjeni poredak elemenata u listi tako da ih sortirate po udaljenosti od prosjeka svih brojeva.

n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
zbroj=0
for i in l:
    zbroj+=i
prosjek=zbroj/n
d=[]
for i in l:
    d.append(abs(i-prosjek))
r=[]
for i in range(n):
    t=d.index(min(d))
    r.append(l.pop(t))
    d.pop(t)
    print(r)
    

# 7. Upiši n prirodnih brojeva i spremi ih u listu. Promjeni poredak elemenata u listi tako da ih sortirate po broju znamenaka djeljivih sa 3.

n=int(input("Upiši n prirodnih brojeva:"))
l=[]
for i in range(n):
    l.append(int(input("Upiši broj " + str(i+1) + ": ")))
d=[]
for i in l:
    br=0
    while(i>0):
        zn=i%10
        i//=10
        if zn%3==0:
            br+=1
    d.append(br)
print(d)
r=[]
for i in range(n):
    t=d.index(min(d))
    r.append(l.pop(t))
    d.pop(t)
    print(r)


# 8. Upiši n prirodnih brojeva i spremi ih u listu. Izbaci iz liste broj koji ima najmanje istih znamenaka. Ispišite listu nakon izbacivanja i ponavljajte ovaj postupak dok ne izbacite sve brojeve.

n=int(input("Upiši n prirodnih brojeva:"))
l=[]
for i in range(n):
    l.append(int(input("Upiši broj " + str(i+1) + ": ")))
z=[]
for i in l:
    m=0
    for j in range(10):
        x=i
        br=0
        while(x>0):
            zn=x%10
            x//=10
            if zn==j:
                br+=1
        if br>m:
            m=br
    z.append(m)
while(len(l)>0):
    t=z.index(min(z))
    l.pop(t)
    print(l)
    z.pop(t)
    
    
# 9. Upiši n prirodnih brojeva i spremi ih u listu. Izbaci iz liste broj koji ima najveću znamenku. Ispišite listu nakon izbacivanja i ponavljajte ovaj postupak dok ne izbacite sve brojeve.

n=int(input("Upiši n prirodnih brojeva:"))
l=[]
for i in range(n):
    l.append(int(input("Upiši broj " + str(i+1) + ": ")))
z=[]
for i in l:
    m=0
    while(i>0):
        zn=i%10
        i//=10
        if zn>m:
            m=zn
    z.append(m)
while(len(l)>0):
    t=z.index(min(z))
    l.pop(t)
    print(l)
    z.pop(t)

# 10. Upiši n prirodnih brojeva i spremi ih u listu. Izbaci iz liste broj koji ima najmanje zajedničkih djelitelja sa preostalim brojevima u listi. Ispišite listu nakon izbacivanja i ponavljajte ovaj postupak dok ne izbacite sve brojeve.

n=int(input("Upiši n prirodnih brojeva:"))
l=[]
for i in range(n):
    l.append(int(input("Upiši broj " + str(i+1) + ": ")))
djeli=[]
while(len(l)>0):
    for i in range(len(l)):
        d=0
        for j in range(len(l)):
            br=0
            for k in range(2,min(l[i],l[j])+1):
                if i!=j and l[i]%k==0 and l[j]%k==0:
                    br+=1
            d+=br
        djeli.append(d)
    l.pop(djeli.index(min(djeli)))
    djeli=[]
    print(l)
