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
def serperate_into_words(line, champions_list):
    word = ""
    i = 0
    for l in line:
        print("current letter: {}".format(i))
        if (l != ' '):
            word += l
        else:
            champions_list.append(word)
            word = ""

#if the 3rd line is empty create the list of available champions
def generate_list(level, level_list, champion_list):
    i = 0
    while i < level:
        level_list.append(champion_list[i])
        i +=1


#adds list into a string that can be written onto file
def concat_list_into_word(champ_list):
    i = 0
    word = ""
    for c in champ_list:
        word += c
        word += " "

    return word


def select_champion(champ_list):
    list_size = len(champ_list)


def main():
    champions = []
    current_level_champions = []
    file = open("champs.txt")
    content = file.readlines()

    serperate_into_words(content[0], champions)

    for c in champions:
        print(c)

    print("\n")

    print(content[2])

    try:
        level = int(content[1])
    except IndexError:
        print("there is no line 2")

    try:
        if (content[2] != "\n"):
            serperate_into_words(content[2], current_level_champions) #put the champions on the second list
        else:
            generate_list(level, current_level_champions, champions)
            champion_list_string = concat_list_into_word(current_level_champions)
            content[2] = champion_list_string

    except IndexError:
        print("\nUhhh there is no line 3, write something on that line or indent on it")
    
    print(current_level_champions)
    # print("Champions to pick from")
    # for champs in current_level_champions:
    #     print(champs)
    
    
    #champion_selected = select_champion(current_level_champions)


    with open("champs.txt", 'w') as file2:
        file2.writelines( content )    

        
  
# Using the special variable 
# __name__
if __name__=="__main__":
    main()