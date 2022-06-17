from os import system
from random import randint

game_title="Castle Dungeons - an interactive game"
system("mode 110, 30")
system("title" + game_title)

#clear screen function
def cls():
    system("cls")

charecter_name = None
charecter_race = None
charecter_class = None
charecter_strength = None
charecter_magic = None
charecter_dexterity = None
charecter_life = None
charecter_intelligence = None

#clearing the screen to get the game ready
cls()

print("Castle Dungeons - An interactive fiction game in Python")


def intro():
    print(" ")
    print("In this adventure you are the hero!")
    print("Your Choices, skills, and a bit of luck will influence the outcome of the game.")
    print("")
    print("An evil sorcerer is holding your fellow adventurers prisoner")
    print("Will you succeed in freeing your friends fromt he castle dungeons or perish trying?")
    print("")
    input("Press enter to start...")

intro()

def create_charecter():
    cls()
    global charecter_name
    charecter_name = input("""
    Lets begin by creating your charecter.
    What is your charecter's name?
    > """)
    cls()
    global charecter_race
    while charecter_race is None:
        race_choice = input("""
        Choose your charecter race from the list below by entering the the relevant number:
        1 - Elf
        2 - Dwarf
        3 - Human
        4 - Gnome

        > """)
        if race_choice == "1":
            charecter_race = "Elf"
        elif race_choice == "2":
            charecter_race = "Dwarf"
        elif race_choice == "3":
            charecter_race = "Human"
        elif race_choice == "4":
            charecter_race = "Gnome"
        else:
            print("Not a valid choice please try again")
    cls()
    global charecter_class
    while charecter_class == None:
        class_choice = input("""
        Choose your charecter's class from the list below by entering the associated number:
        1 - Warrior
        2 - Wizard
        3 - Mage
        4 - Ranger
        > """)
        if class_choice == "1":
            charecter_class = "Warrior"
        elif class_choice == "2":
            charecter_class = "Wizard"
        elif class_choice == "3":
            charecter_class = "Mage"
        elif class_choice == "4":
            charecter_class = "Ranger"
        else:
            print("Not a valid choice please try again")
    cls()
    

create_charecter()

def create_charecter_skill_sheet():
    cls()
    global charecter_name, charecter_class, charecter_race, charecter_dexterity, charecter_life, charecter_magic, charecter_strength, charecter_intelligence
    print("""
		Now let's determine your charecter's skills, which you will use throughout the game.
		In this game your chaecter has four skills:

		- Strenght, which you will use in combat or any strenght test
		- Dexterity, which you will use in any ability test
		- Magic, which you will use whenever you need to cast a spell or inspect a magical item r place
		- Life, which determines your life  energy. Points will be lost if you are hurt, if your life reaches 0 you will  die. 
		
		Depending on your race and class, you will have a certian point-base already claculated by the game.
		You will also be able to increase your skills by rolling a 6-sided die.

		Here is your base charecter skills sheet:
		""")
    
    charecter_strength=5
    charecter_magic=0
    charecter_dexterity=3
    charecter_life=10
    charecter_intelligence = 3
    
    if charecter_race=="Elf":
        charecter_strength=charecter_strength + 3
        charecter_magic=charecter_magic + 6
        charecter_dexterity=charecter_dexterity + 4
        charecter_life = charecter_life + 2
        charecter_intelligence = charecter_intelligence + 2
   
    elif charecter_race == "Dwarf":
        charecter_strength=charecter_strength + 5
        charecter_life = charecter_life + 4
   
    elif charecter_race == "Human":
        charecter_dexterity = charecter_dexterity + 2
        charecter_intelligence = charecter_intelligence + 4
   
    elif charecter_race == "Gnome":
        charecter_intelligence = charecter_intelligence + 4
        charecter_life = charecter_life + 4
        charecter_dexterity = charecter_dexterity +4
   
    
    if charecter_class == "Warrior":
        charecter_strength = charecter_strength + 3
        charecter_life = charecter_life + 4
    
    elif charecter_class == "Wizard":
        charecter_magic = charecter_magic + 4
        charecter_intelligence = charecter_intelligence +2

    elif charecter_class == "Mage":
        charecter_life = charecter_life + 4
        charecter_magic = charecter_magic + 8
        charecter_dexterity = charecter_dexterity +2
        charecter_intelligence = charecter_intelligence + 2

    print("""
        Name: """+charecter_name+
        """
        Race: """+charecter_race+
        """
        Class: """+charecter_class+
        """

        Strength: """+str(charecter_strength)+
        """
        Dexterity: """+str(charecter_dexterity)+
        """
        Magic: """+str(charecter_magic)+
        """
        Intelligence: """+str(charecter_intelligence)+
        """
        
        Life: """+str(charecter_life)+"""

    """)
    input("Press enter to apply your modifiers")

create_charecter_skill_sheet()

def modify_skills():
    cls()
    global charecter_strength, charecter_dexterity, charecter_intelligence, charecter_life
    print("Roll the dice to modify your skills")

    input("Press enter to roll for Strenght")
    roll = randint(1,6)
    print(f"You rolled a {roll}!")
    charecter_strength=charecter_strength + roll

    input("Press enter to roll for Dexterity")
    roll = randint(1,6)
    print(f"You rolled a {roll}!")
    charecter_dexterity=charecter_dexterity + roll

    input("Press enter to roll for intelligence")
    roll = randint(1,6)
    print(f"You rolled a {roll}")
    charecter_intelligence = charecter_intelligence + roll

    input("Press enter to roll for life")
    roll = randint(1,6)
    print(f"You rolled a {roll}!")
    charecter_life=charecter_life + roll

    input("Press enter to continue...")
    cls()
    print("""
    Congratulations! You have completed your character creation!
    Your final character sheet is:

    Name:"""+charecter_name+
    """
    Race:"""+charecter_race+
    """
    Class:"""+charecter_class+
    """
    
    Strength:"""+str(charecter_strength)+
    """
    Dexterity:"""+str(charecter_dexterity)+
    """
    Magic:"""+str(charecter_magic)+
    """

    Intelligence: """+str(charecter_intelligence)+
    """
    Life:"""+str(charecter_life)+"""

    """)
    input("Press enter to begin if you dare...")

modify_skills()

def scene_1():
    cls()
    choice = None
    while choice is None:
        user_input = input("""
        You have entered the Castel Dungeons...
        It is dark but thankfully your torchis lit and you can see about 20 feet in front of you.
        The stone walls are damp and the smell of rats and orcs is strong. 
        You follow a narrow cooridor until you reacha  thick stone wall.

        The cooridor forks left and right

        What do you do?

        1 - Turn Left
        2 - Turn Right
        >""")
        if user_input == "1":
            choice = "1"
            encounter_1()
        elif user_input == "2":
            choice = "2"
            encounter_2()
        else:
            print("""
            Not  valid choice
            """)

def encounter_1():
    cls()
    choice = None
    while choice is None:
        user_input = input("""
        From the darkness behind you hear a strange noise.

        What do you do?

        1 - Continue walking
        2 - stop to listen
        >""")
        if user_input == "1":
            choice = "1"
            combat()
        elif user_input == "2":
            choice = "2"
            skills_check()
        else:
            print("""
            Not  valid choice
            """)

def encounter_2():
    cls()
    choice = None
    while choice is None:
        user_input = input("""
        From the darkness ahead you hear a strange noise.

        What do you do?

        1 - Continue walking
        2 - Stop to listen
        >""")
        if user_input == "1":
            choice = "1"
            combat()
        elif user_input == "2":
            choice = "2"
            skills_check()
        else:
            print("""
            Not a valid choice
            """)

def skills_check():
    cls()
    print("A giant rock falls from the ceiling. Roll the die to see of you can dodge it.")
    roll = randint(1,6)
    print(f"you rolled a {str(roll)}")
    if roll+charecter_dexterity > 10:
        print("""
        You dodge the stone and survive! The Danger is not over though...

        The strange noise in the darkness continues and feels closer now...
        """)
        input("Press enter to continue")
        combat()
    else:
        print("You are crushed by the rock and have died. Game Over")
        input("Press enter to exit the game")

def combat():
    cls()
    global charecter_life
    print("A horrible orc attacks you!")
    input("Press enter to fight...")
    orc = [10, 14]
    while orc[1] >0 and charecter_life > 0:
        char_roll = randint(1, 6)
        print(f"You rolled {str(char_roll)}")
        monst_roll = randint(1, 6)
        print(f"The orc rolled {str(monst_roll)}")
        if char_roll+charecter_strength >= monst_roll+orc[0]:
            print("You hit the orc!")
            orc[1] = orc[1] - randint(1, 6)
        else:
            print("The monster hits you!")
            charecter_life = charecter_life-randint(1, 6)
    if orc[1] <= 0:
        print("You defeated the orc!")
        # input("Press enter to continue")
    elif charecter_life <= 0:
        print("You lost...your friends will never be freed and you are dead.")
        input("Press enter to exit the game")


scene_1() 

def scene_2():
    cls()
    choice = None
    while choice is None:
        user_input = input("""You have now reached 2 doors at the end of the cooridoor...
        You must choose which on to go through

        What do you do?

        1 - door to the left
        2 - door to the right
        
        >""")
        if user_input =="1":
            choice = "1"
            encounter_3()
        # elif user_input == "2":
        #     choice = "2"
        #     encounter_4()
        else:
            print("You have run into the wall...That was not a valid choice...please try again")

def encounter_3():
    cls()
    choice = None
    while choice is None:
        user_input = input("""
        You open the door and find a cooridor with a faint light coming from the end 
        and a flight of stairs leading down, deeper into the dungoen to the right...

        Which do you choose?

        1 - Continue down the cooridor
        2 - Coninue down the stairs
        """)
        if user_input == "1":
            choice = "1"
            spell()
        elif user_input == "2":
            choice = "2"
            combat()
        else:
            print("You have run into a wall, please try a valid choice...")


def spell():
    global charecter_magic
    cls()
    print("A spell has been cast to disarm you!")
    input("Press enter to fight...")
    dark_wizzard = [10, 14]
    while dark_wizzard[1] >0 or charecter_magic > 0:
        char_roll = randint(1, 6)
        print(f"You rolled a {str(char_roll)}")
        monst_roll = randint(1, 6)
        print(f"The dark wizzard rolled a {str(monst_roll)}")
        if char_roll+charecter_magic >= monst_roll + dark_wizzard[0]:
            print("You hit back with a stronger defensive spell!")
            dark_wizzard[1] = dark_wizzard[1] - randint(1,6)
        else:
            print("The spell hit you!")
            charecter_magic = charecter_magic - randint(1, 6)

    if dark_wizzard[1] <= 0:
        print("You defeated the dark wizard!")
        input(" Press enter to continue")
    elif charecter_magic <= 0:
        print("You have been hit by the spell and it has weakened you")
        charecter_life = charecter_life - 2

    if charecter_life > 0:
        print("You are weak but must go on...")
        input("Press enterto continue")
    else:
        print("You have been killed by the spell...You friends are lost forever...")
        input("Press enter to exit the game")
    

scene_2()