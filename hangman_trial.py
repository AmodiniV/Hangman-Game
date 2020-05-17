import linecache
import random
def word_fetch():
    file_name = "word_list.txt"
    num = random.randint(1,213)
    return linecache.getline(file_name,num)

def check_ans(word,guess):
    res = cmp(word,guess)
    if res == 0 :
        print "You won"
    else :
        print "You lost"


def convert (guess):
    new = " "
    for i in guess:
        new += i
    print "You have guessed so far:%s" %new

def guess_letter(word,letter,guess):
    j = 0
    flag = 0
    #print "going in main fn:%s" %guess
    for i in word:
        if i == letter:
            flag = 1
            #print "int:%d,word:%s " %(j,guess[j])
            guess[j] = i

        j = j + 1
    if flag == 0:
        print "incorrect guess"
    else:
        print "correct guess"
    convert(guess)
    return guess
    #return convert(guess1)

print "Hello! What is your name?"
name = raw_input(">")
print "Welcome %s!" %name
print "select 1 - to type the secret word and 2- take it from file "
choice = int(raw_input(">"))
if choice == 1:
    print "Type the secret word"
    word = raw_input(">")
else :
    word = word_fetch()
word = word.lower()
word1 = list(word)
print "Word has %d letters. Best of Luck!" %len(word)
guess = []
i = 0
while (i< len(word)):
    guess.append('-')
    i += 1
count = 5
#print guess
while(count>0):
    print "You have %d guesses left\n" %count
    letter = raw_input("guess the letter: ")
    guess = guess_letter(word1,letter,guess)
    count = count - 1

check_ans(word1,guess)
print "The correct ans was %s" %word
