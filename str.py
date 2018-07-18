str=raw_input("enter the string")
countl=0
countu=0
for x in range(len(str)):
  if str[x]>='a' and str[x]<='z':
     countl=countl+1
  if str[x]>='A' and str[x]<='Z':
     countu=countu+1
print "count for lower case is",countl
print "count for upper case is",countu