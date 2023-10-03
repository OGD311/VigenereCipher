#Vigneire Cipher

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def vigneire(keyphrase,alphabet):
    ciphergrid = []
    ciphergrid.append(alphabet)
    for i in range(len(keyphrase)):        
        startpos = alphabet.index(keyphrase[i])
        order = []
        
        for x in range(startpos,len(alphabet)):
            order.append(alphabet[x])

        for h in range(0,startpos):
            order.append(alphabet[h])

        ciphergrid.append(order)
    

    
    return ciphergrid

def printgrid(keyphrase, grid):
    print(" ",grid[0])
    for i in range(1,len(keyphrase)+1):
        print(keyphrase[i-1],grid[i])


def encode(alphabet,grid,word):
    encoded = ""
    rownum = 1
    letters = []
    for letter in word:
        letters.append(letter.upper())

    
    while len(encoded) != len(word):
        for i in range(len(letters)):
            if rownum == len(grid):
                rownum = 1
            if letters[i].isalpha() == False:
                encoded += letters[i]
            else:
                encoded += grid[rownum][alphabet.index(letters[i])]
            rownum += 1

    print(encoded)


def decode(word,grid):
    decoded = ""
    rownum = 1
    letters = []
    for letter in word:
        letters.append(letter.upper())

    #print(letters)
    
    while len(decoded) != len(word):
        for i in range(len(letters)):
            if rownum == len(grid):
                rownum = 1
           
            if letters[i].isalpha() == False:
                decoded += letters[i]

            else:
                letterpos = grid[rownum].index(letters[i]) 
                decoded += grid[0][letterpos]

            rownum += 1

    print(decoded)

def choice():
    while True:
        try:
            choice = int(input("Encode/Decode/Exit? (1/2/3): "))
            break
 
        except:
            print("Please enter an option")
    
    return choice


def inputs(type,spaces,digits):
    while True:
        inputs = input(f"Enter a {type}: ")

        for letter in inputs:
            if letter.isdigit() and digits == True:
                break
            if letter == " " and spaces == True:
                break
                

        
        if letter.isdigit():
            print(f"{type.title()} cannot contain numbers - please try again")
        
        if letter == " ":
            print(f"{type.title()} cannot contain spaces - please try again")
        
        

        else:
            break

    inputs = inputs.upper()
    return inputs



while True:
    choices = choice()
    if choices == 1:
        key = inputs("key",False,False)
        word = inputs("word",True,False)
        grid = vigneire(key,alphabet)
        encode(alphabet,grid,word)


    elif choices == 2:
        key = inputs("key",False,False)
        word = inputs("word",True,False)
        grid = vigneire(key,alphabet)
        #printgrid(key,grid)
        decode(word,grid)

    else:
        break
    