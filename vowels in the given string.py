def getvowels(str1):

    str2=""

    for x in range(len(str1)):

        if str1[x] in ['a','e','i','o','u']:

           str2+=str1[x]

    print("vowels in the string is",str2.split(" "))

str=input("enter the string")

getvowels(str)