def reverse_word(strr):

    strr=strr.split(" ")

    strr=strr[-1::-1]

    strr= " ".join(strr)

    return(strr)





str=input()


print("the reverse word is")
print(reverse_word(str))