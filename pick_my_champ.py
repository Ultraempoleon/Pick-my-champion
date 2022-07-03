import random
from sqlite3 import connect
random.seed()
#So the idea here is that I got bored trying to decide what champion to
#play so I made this for fun
#the algorithm works like this
#there are levels = the number champions on the first line of the text file
#champs.txt

#so the way it works is with every level a new champion is added to a list
#starting from the first name of the list and so on
#so level 1 (bel veth)
#level 2 (bel veth, volibear) etc.

#the program will randomize a champion from that list


#python is doing dumb things when I try to read by the lines so I created
#this short algorithm to seperate the words into an array from the first
#line only
def serperate_into_words(line, champions_list):
    word = ""
    for l in line:
        if (l != ' '):
            word += l
        else:
            champions_list.append(word)
            word = ""


#if the 3rd line is empty create the list of available champions
#when its empty it will generate the next level of champions
def generate_list(level, level_list, champion_list):
    i = 0
    while i < level:
        level_list.append(champion_list[i])
        i += 1


#adds list into a string that can be written onto file
def concat_list_into_word(champ_list):
    word = ""
    for c in champ_list:
        word += c
        word += " "

    return word


#this function selects a champion from 
def select_champion(champ_list):
    list_size = len(champ_list)
    #picks a random number from 0 - #of champs in list
    number = random.randrange(0,len(champ_list))
    print()
    if (list_size-1 == 0):
        champ = champ_list[0]
        champ_list.pop(0)
        return champ


    number = random.randrange(0,list_size-1)
    i = 0
    champ = ""

    while (i<list_size):
        if i == number:
            champ = champ_list[i]
            champ_list.pop(i)
            return champ
        i += 1

    return "Error occurred, no champion slected"


#the idea here is to change the line of the file seperately 
def changelines1(champions):
    print("\nim here")
    myfile = open("champs.txt") #opens file
    file_content = myfile.readlines() #seperates lines so that each line can be read individually

    try:
        level = int(file_content[1])
    except:
        print("there is no line2?")

    print("level: {}".format(level))
    print("content[1]: {}".format(file_content[1]))

    if (level+1) > len(champions):
        level = 0
    else:
        level += 1


    file_content[1] = str(level)

    
    print("level: {}".format(level))
    print("content[1]: {}".format(file_content[1]))
    

    with open("champs.txt", 'w') as file_again:
        file_again.writelines(file_content)

    print("\nDone with function")


def main():
    champions = [] #all the champions on the list
    current_level_champions = [] #champions at that level
    file = open("champs.txt") #opens file
    content = file.readlines() #seperates lines so that each line can be read individually

    serperate_into_words(content[0], champions)

    try:
        level = int(content[1]) #level will determine how many champions will be in a pool
    except IndexError:
        print("there is no line 2")

    #checks if the third line exists
    try:
        #if it does exists, adds that list of champions into the list
        if (content[2] != "empty "):
            print("butts!!!!")
            serperate_into_words(content[2], current_level_champions) #put the champions on the second list


        #if there is not a list (the assumption is that the previous level was finished)
        #it will create a new pool adding one more champion to it (i.e. the next level)
        elif (content[2] == "empty "):
            changelines1(champions)
            print(content[2])
            print("\nbutts")
            #if the level would exceed the maximum number of champions
            #level is set to 0; else level is raised by 1

            # if (level+1) > len(champions):
            #     level = 0
            # else:
            #     level += 1

            generate_list(level, current_level_champions, champions)
            champion_list_string = concat_list_into_word(current_level_champions)
            content[2] = champion_list_string
            #content[1] = str(level)

    except IndexError:
        print("\nUhhh there is no line 3, write something on that line or indent on it")
        
        # if (level+1) > len(champions):
        #     level = 0
        # else:
        #     level += 1
        generate_list(level, current_level_champions, champions)
        champion_list_string = concat_list_into_word(current_level_champions)
        

        content[2] = champion_list_string
        #content[1] = str(level)

    print("Champions to pick from")
    for champs in current_level_champions:
        print(champs, end=" ")
    
    
    champion_selected = select_champion(current_level_champions)
    print("\nChampion Selected: {}\n".format(champion_selected))
    
    if (len(current_level_champions) == 0):
        content[2] = "empty "

    else:
        champion_list_string = concat_list_into_word(current_level_champions)
        content[2] = champion_list_string

    print(content[2])
    with open("champs.txt", 'w') as file2:
        file2.writelines( content )



  
# Using the special variable 
# __name__
if __name__=="__main__":
    main()