def startendvowels(str1):

    x=0

    y=len(str1)-1

    if((str1[x]=='a' or str1[x]=='e' or str1[x]=='i' or str1[x]=='o' or str1[x]=='u' or str1[x]=='A' or str1[x]=='E' or str1[x]=='I' or str1[x]=='O' or str1[x]=='U') and (str1[y]=='a' or str1[y]=='e' or str1[y]=='i' or str1[y]=='o' or str1[y]=='u' or str1[x]=='A' or str1[x]=='E' or str1[x]=='I' or str1[x]=='O' or str1[x]=='U')):

        return True

    else:

        
return False


str=input("enter the string")

print("result:",startendvowels(str))