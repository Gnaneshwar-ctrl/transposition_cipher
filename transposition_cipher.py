string = input("Enter string: ")
shift = len(string)

a = shift - 1

if( shift%2 == 0 ):

    cipher_1 = ""
    cipher_2 = ""

    i = 0
    
    while("true"):
        cipher_1 += string[i]
        i = i + 2
        if(i>a):
            i = 1
            break

    while("true"):
        cipher_2 += string[i]
        i = i + 2
        if(i>a):
            break

elif( shift%2 != 0 ):

    cipher_1 = ""
    cipher_2 = ""

    i = 0
    
    while("true"):
        cipher_1 += string[i]
        i = i + 2
        if(i>a):
            i = 1
            break

    while("true"):
        cipher_2 += string[i]
        i = i + 2
        if(i>a):
            break

b = cipher_1 + cipher_2

print("Therefore the encrypted message is :" , b)
