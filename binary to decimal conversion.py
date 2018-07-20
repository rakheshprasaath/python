strg=input("enter the conversion string")

i=len(strg)-1

x=0

dec=0

count=0

for x in range (len(strg)):

    dec+=int(strg[i-count])*(x**2)

    count+=1

print("decimal integer",dec)