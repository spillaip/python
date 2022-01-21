import random
from random import randint, randrange
#from posixpath import split
#from random import randint, randrange

# read file Strategyforclinicals.csv
#from random import random
from secrets import randbelow

# for final review
reviewlist = []
totalquestions = 0
correctanswer = 0
totalmarks = 0


file = open('Strategyforclinicals.csv', 'r')

# create a tuple and store a row
rowtuple = ()

# create a list and store the tuple
ppmquizlist = file.readlines()
diseases_list = []


# Create a unique list of diseases

# Loop the file and populate tuple and add tuple to list
for _element in ppmquizlist:
    resultrow = _element.split(",")
    # check if exists in unq_list
    if resultrow[1] not in diseases_list:
        diseases_list.append(resultrow[1])
#print(diseases_list)

if diseases_list:
    diseases_list
else:
    diseases_list.append("No entries")


# create the menu for the quiz using while loop until exit is typed
while True:
    print()
    print("Quiz - PPM")
    print()
    print("1. Exit")
    print("2. New Question")
    print()
    option = input("Enter your option: ")
    if option == "1":
        print("\nSession Summary\n")
        print("Total Marks: " + str(totalmarks) + " \n")
        print("Total Questions: "+ str(totalquestions) + " \n" )
        print("Total Correctly Answers: "+ str(correctanswer) + " \n")

        #print(reviewlist)
        outputfile = open("review.txt","w")
        for element in reviewlist:
            outputfile.write(element + "\n")
        outputfile.close()
        break
    else:
        # Track total questions, and correct answers
        # for each question intent is to find the disease (2nd col)
        # provide hint in this order, each additional hint subract .167
        # 1) clinical feature (5th col)
        # 2) diagnosis (7th col)
        # 3) Treatment (8th col)
        # 4) Causes (3rd col)
        # 5) Risk factor (4th col)
        # 6) Progression (5th col)
        # provide 5 options
        # marks +4 for correct answer -1 for wrong
        print("\nGood choice! Identify the disease based on the hints given.  Correct answer you get 4, wrong answer -1.\n")
        #noofquestions = ppmquizlist.__len__()
        
        # get the random file line
        randnum = randrange(ppmquizlist.__len__())
        print("\nQuestion No. is "+str(randnum)+"\n")
        
        # Check a choice number randomly
        choicenum = randint(1,6)
        choicenum1 = randint(1,len(diseases_list))
        choicenum2 = randint(1,len(diseases_list))
        choicenum3 = randint(1,len(diseases_list))
        choicenum4 = randint(1,len(diseases_list))
        choicenum5 = randint(1,len(diseases_list))

        # get the row split into columns
        cols = ppmquizlist[randnum].split(",")

        # Get Random Question Number
        question = ppmquizlist[randnum]
        # print(question)
        
        rowtuple = question.split
        
        #print(rowtuple)
        
        if choicenum == 1:
            print("\nHint (Clinical Feature): " + cols[4])
        if choicenum == 2:
            print("\nHint (Diagnosis): "+cols[6])
        if choicenum == 3:
            print("\nHint (Treatment): "+cols[7])
        if choicenum == 4:
            print("\nHint (Causes): "+cols[2])
        if choicenum == 5:
            print("\nHint (Risk Factor): " + cols[3])
        if choicenum == 6:
            print("\nHint (Progression): " + cols[5])

        #print("Hint: "+ question[4])

        optionlist = []
        optionlist.append(diseases_list[choicenum1])
        optionlist.append(diseases_list[choicenum2])
        optionlist.append(diseases_list[choicenum3])
        optionlist.append(diseases_list[choicenum4])
        optionlist.append(cols[1])
        random.shuffle(optionlist)
        

        print("\na. "+optionlist[0])
        print("b. "+optionlist[1])
        print("c. "+optionlist[2])
        print("d. "+optionlist[3])
        print("e. "+optionlist[4])
        optionansc = input("\nType the Choice: ")
        
        #To review all the questions rendered later
        reviewlist.append(question)
        print("Option selected is: "+optionansc)

        optionselected = -1
        
        if optionansc == "a":
            optionselected = 0
        if optionansc == "b":
            optionselected = 1
        if optionansc == "c":
            optionselected = 2
        if optionansc == "d":
            optionselected = 3
        if optionansc == "e":
            optionselected = 4

        if optionlist[int(optionselected)] == cols[1] :
            print("Your answer is correct!! ")
            currquestionmarks = 4
            totalmarks = totalmarks + currquestionmarks
            totalquestions = totalquestions+1
            correctanswer = correctanswer+1
            print("So far total questions: "+str(totalquestions) +
                  " Correctly answered are: "+str(correctanswer))

        else:
            currquestionmarks = -1
            totalquestions = totalquestions+1
            totalmarks = totalmarks + currquestionmarks
            print("Incorrect answer... The Disease is " + cols[1])


# If answer not found by 6th hint, show complete tuple
# add the tuple to another list for review later
# ask if wish to continue
# on typing exit, display total number of questions attempted, and correct answers, score
# write all the questions attempted and answers to a text file and display the filename.
