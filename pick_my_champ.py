import random
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
def seperate_into_words(line, champions_list):
    word = ""
    for l in line:
        if (l != ' '):
            word += l
        else:
            champions_list.append(word)
            word = ""


#if the 3rd line is empty create the list of available champions
#when its empty it will generate the next level of champions
def generate_list(level, current_level_champions, champions):

    #This function assumes that the the level is being incremented
    level += 1
    current_level_champions[0] = str(level)

    i = 0
    while i < level:
        current_level_champions.append(champions[i])
        i += 1
    current_level_champions.append("Fiddlesticks")


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

    #if there is only one champion in the list it just pops it
    if (list_size-1 == 1):
        champ = champ_list[1]
        champ_list.pop(1)
        return champ
    
    #picks a random number from 1 - #of champs in list
    number = random.randrange(1,len(champ_list))

    #Has an indent because of a while loop with end= " "
    print("\nChamp Selected: {}".format(champ_list[number]))
    print("Was this champion selected? Y/N", end=" ")
    confirm = input()

    #sometimes the champion could not be selected
    while(confirm == 'N' or confirm == 'n'):
        number = random.randrange(1,len(champ_list))
        print("\nChampion Selected: {}".format(champ_list[number]))
        print("Was this champion selected? Y/N", end=" ")
        confirm = input()


    champ = champ_list[number]
    champ_list.pop(number)
    return champ


#prints the list of champions ignoring the first element
def print_champ_list(current_level_champions):
    i = 1
    while (i < len(current_level_champions)):
        print("{} ".format(current_level_champions[i]), end=" ")
        i += 1


def main():
    champions = [] #all the champions on the list
    current_level_champions = [] #champions at that level
    file = open("champs.txt") #opens file
    content = file.readlines() #seperates lines so that each line can be read individually

    #Seperates the first line into a list called champions
    try:
        seperate_into_words(content[0], champions)
    except IndexError:
        print("You're missing the first line, the list of champions")
        exit()


    try:
        #so now the first element of current level champions has the level
        seperate_into_words(content[1], current_level_champions)
        level = int(current_level_champions[0]) #grabs first element as int
        
        #create the list if the list is empty
        if (len(current_level_champions) < 2):
            generate_list(level, current_level_champions, champions)

        #prints the list of available champions
        print("Champions to pick from: ", end=" ")
        print_champ_list(current_level_champions)

        #selects the champion
        #champ selected isn't being used, too lazy too change it
        champ_selected = select_champion(current_level_champions)
        #print("Champion Selected: {}".format(champ_selected))

        #turns the list into a string that can be written back onto the file
        champion_list_string = concat_list_into_word(current_level_champions)
        content[1] = champion_list_string

        #writes the lines back onto the file
        with open("champs.txt", 'w') as file2:
            file2.writelines(content)


    #repeat of the else statement the exact same code twice, why not create a call function?
    #it might overcomplicate things? I'll try it later
    except IndexError:

        print("You're missing the second line of the file")
        exit()
  
# Using the special variable 
# __name__
if __name__=="__main__":
    main()