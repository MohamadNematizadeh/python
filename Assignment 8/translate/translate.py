import pyfiglet
import gtts

words_bank = []
def read_from_file():
    global words_bank
    f=open("session8/translate.txt","r")
    temp = f.read().split("\n")
    words_bank = []
    for i in range(0, len(temp),2):
        my_dict = {"en": temp[i], "fa": temp[i+1]}
        words_bank.append(my_dict)
    f.close()
    # .-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
def translate_english_to_persian(): 
    user_text = input("enter your english text :")

    output = ""

    user_words = user_text.split(" ")
    for user_word in user_words:
        for word in words_bank:
            if user_word == word["en"]:
                output= output + word["fa"] + " "
                break
        else:
         output= output +  user_word + " " 

    print(output)  
def show_menu():

    title =pyfiglet.figlet_format("translate._.",font="slant")
    print(title)
    
    print("1-translate english to persian ")
    print("2-translate persian to persian ")
    print("3-add a nae word to databast ")
    print("4-exit")

def persian_to_english():
     user_text = input("enter your persan text: ")
     user_words = user_text.split(" ")

     output = ""
for user_word in user_words:
            for word in words_bank:
                if user_word == word["fa"]:
                    output = output + word["en"] + " "
                    break
            else:
                output = output + user_word + " "

print(output)
text = str(output)
Voice = gtts.gTTS(text,lang="en",slow = False)
Voice.save("translate.mp3")





while True:
    show_menu()
    choice = int(input(""))

    if choice == 1 :
        translate_english_to_persian()
    elif choice == 2 :
        persian_to_english()
    elif choice == 3 :
        ...
    elif choice ==4 :
        exit(0)            

       





# i am a programmer