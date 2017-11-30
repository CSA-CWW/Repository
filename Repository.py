#Cameron Watts#
#11 9 17#
#Comp Sci 2017#
somethingss = 2332958532982340982094803498423
def letter_count():
    while True:
        word=input("Wut word?").lower()
        print ("")
        letter = input("What letter to count?").lower()
        count = 0
        for x in word:
            if x == letter:
                count = count + 1
        print ("")
        print(count)
        print ("")
        break
        letter_count()

def word_count():
    while True:
        sent = input("Input some words")
        sent_count = 1
        if sent == "":
            sent_count = 0
        for x in sent:
            if x == " ":
                sent_count = sent_count + 1
        print ("")
        print (sent_count)
        print ("")
        break
        word_count()

def run_count():
    while True:
        somethings = input("Letter(1) or word(2) count?")
        print ("")
        if somethings == "1":
            letter_count()
        if somethings == "2":
            word_count()
run_count()
