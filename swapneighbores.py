a=[1,2,3,4,5,6,7,8,9]
for i in range(0,len(a)-1,2):
  a[i],a[i+1]=a[i+1],a[i]
  print(a)
  i=len(a)-2
while i>=0:
  a[i],a[i+1]=a[i+1],a[i]
  i=i+2
print(a)

num=input()
numarr=num.split(".")
num=num[0]+'.'+num[1:]
print(num)
a=3.4923426
f="{:.2f}".format(a)
print(f)
