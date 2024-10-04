#author__uy_thea
#date_october_3_2024
#section_bscpe_2-2



def vowelsToUpper(phrase): #Create a function that will change all the vowels to uppercase 
    translated_phrase = str.maketrans("aeiou", "AEIOU")

    return phrase.translate(translated_phrase)


def get_number(): #get the number of times the user has to enter a value
    while True:
        try:
            number = int(input("Enter a number: "))
        except:
            print("Invalid Input")
            continue
        else:
            return number
        

list_of_phrases = [] #list for all the phrases the user will enter
number_of_phrases = get_number() 
while True:
    try:
        for phrase in range(number_of_phrases):#ask the user for the string input
            phrase = input("Enter a word/phrase/sentence: ")
            list_of_phrases.append(phrase)

        
        for phrase in list_of_phrases: #change all the vowels into uppercase
            phrase = vowelsToUpper(phrase)
            print(phrase)

    except:
        "Invalid"

    else:
        break

#end of the program    
           