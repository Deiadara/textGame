import person
import items
import creatures
import room
import termcolor as co
name = ''
##############################################################################
#   WELCOME PAGE AND RULE EXPLAINATION   #
##############################################################################
starting_items = [
[items.Sword('Cutlass', 1), items.Armor('Brown Leather Vest', 1), 
 items.Pants('Beat-Up Cargo Pants', 1), items.Shoes('Black Boots', 1), 
 items.Item('Compass', 'misc'), items.Item('Rope', 'misc')],
[items.Sword('Longsword', 1), items.Helmet('Silver Helmet', 1) ,
 items.Armor('Silver Chestplate', 1), items.Pants('Silver Leg Armor', 1), 
 items.Shoes('Silver Boots', 1)],
[items.Sword('Hunter\'s Knife', 1), items.Armor('Light Leather Vest', 1), 
 items.Pants('Leather Pants', 1), items.Shoes('Sandals', 1), 
 items.Item('Bow', 'misc'), items.Item('Matches', 'misc')]
]
backgrounds = [
    """
[Oar's Rest] : A harbor town, connecting Herta with the kingdoms across 
the sea. Oarians, as they call them, have spent most of their lives sailing,
or at the docks. Open to trading, or just chatting, Oarians are usually 
extroverted loud people with have many stories and tales to tell.

Starting Equipment : Cutlass (Sword), Brown Leather Vest, Beat-Up Cargo Pants, 
                     Black Boots, Compass, Rope""",
    """
[Greenguard] : More of a fortress than a city,  it stands across the sea, 
on a hill surrounded by a huge valley. Few people other than the Greens 
visit, mainly to trade, since Greenguard is not known for its hospitality. 
Most of the locals are disciplined soldiers, often serving as mercenaries 
to other cities, in exchange for gold or goods.

Starting Equipment : Longsword, Silver Leg Armor, Silver Chestplate, 
                     Silver Helmet, Silver Boots""",
    """
[Hilthia] : The neighbouring city of Herta, it hugs the mountains and the 
forests of the North. Herta and Hilthia used to be one kingdom, that went 
by the name of Lyria. The split happened a little more than a century ago 
with the sudden death of the king Emis the Second, after which his two 
daughters, Herta and Hilthia, went to war to gain control of Lyria. 
The relationship between the two cities has now gotten better than it used 
to be, but many Hertans and Hilthians still have negative feelings towards 
one another. The latter are mainly hunters, farmers and shepherds, accustomed 
with the woods and the mountains, who know how to endure hardships and get 
through tough times.

Starting Equipment : Leather Pants, Light Leather Vest, Bow and Arrows, 
                     Sandals, Matches, Hunter's Knife"""
]

print("""
------------------------------ Hectar's Nectar ------------------------------
""")

print("""
Close by you hear the sound of a flute playing and the smell of fresh baked
pie feeds your appetite. Nearby you see a tavern. You decide to walk towards
and you walk inside!""")

tavern = room.Tavern()
print("""
You walk up to the bartender to order some pie and mead.""")

tavern.people['bartender'].dialogues['Greeting']()
name = input('\n> ')
adventurer = person.Person(name)

tavern.people['bartender'].dialogues['Question'](name)
print("""
You seem a bit surprised that he could immediately tell you're not a local, 
but you assume he knows most of Herta's people by now. He notices your pause
and follows up with a grin:""")
tavern.people['bartender'].dialogues['Line1']()
bogus = input('\n[Press Any Key to continue]')
print(co.colored("""
Now that the bartender brought it up, where are you from?""", color="green"))

while True:
    for b in backgrounds:
        print(b)

    background_choice = input('\n> ').lower()
    if background_choice == "oar's rest":
        adventurer.background = 0
        tavern.people['bartender'].relationship = 8
        for start_item in starting_items[0]:
            adventurer.pickup(start_item)
        print(co.colored("""
Oh, an Oarian! First drink's on the house then! You people have been of much 
help with the supplies for the tavern. 20 years now, I haven't had a single 
problem when going down to the docks to get the goods. 

What can I get you?""",
color = 'light_yellow'))
        break
    elif background_choice == "greenguard":
        adventurer.background = 1
        tavern.people['bartender'].relationship = 6
        print(co.colored("""
Oh, a Green. I remember when we were still in war with Hilthia, and my father 
ran the tavern, we would feed the Green Sellswords for months at a time. 
Honorable fellows. 

What can I get you sir?""", color = 'light_yellow'))
        for start_item in starting_items[1]:
            adventurer.pickup(start_item)
        break
    elif background_choice == "hilthia":
        adventurer.background = 2
        tavern.people['bartender'].relationship = 5
        print(co.colored("""
A Hilthian huh? Well, I've never been one to hate someone because of their 
origin, despite past conflicts. If anyone gives you any trouble, just holler 
at me. 

What can I get you?""", color = 'light_yellow'))
        for start_item in starting_items[2]:
            adventurer.pickup(start_item)
        break
    else:
        print(co.colored("Invalid Choice! Try Again!", color="red"))

while True:
    print("""
[Ale] : 5 coins
[Cider] : 6 coins
[Wine] : 7 coins, +1 to Oliver's Happiness
[Nothing]""")

    choice = input('\n> ').lower()
    if choice == 'ale':
        if tavern.people['bartender'].relationship >= 6:
            print(co.colored("""
Here you go, drink up!

Oliver also grabs his ale ...

To good health!""", color="light_yellow"))
        else:
            if adventurer.give_gold(5):
                print(co.colored("""
That'll be 5 coins. 
I'd appreciate if I saw some coin before pouring you the drink. 
Nothing personal, it's just that yesterday an old geezer drank a gallon 
of ale and then tried to run on me.""", color="light_yellow"))
            else:
                print(co.colored("Invalid Choice! Try Again! (No money, no honey)", color="red")) 
                continue
        break
    elif choice == 'cider':
        if tavern.people['bartender'].relationship >= 6:
            print(co.colored("""
Here you go, drink up!

Oliver also grabs his ale ...

To good health!""", color="light_yellow"))
        else:
            if adventurer.give_gold(6):
                print(co.colored("""
That'll be 6 coins. 
I'd appreciate if I saw some coin before pouring you the drink. 
Nothing personal, it's just that yesterday an old geezer drank a gallon 
of ale and then tried to run on me.""", color="light_yellow"))
            else:
                print(co.colored("Invalid Choice! Try Again! (No money, no honey)", color="red"))
                continue
        break
    elif choice == 'wine':
        tavern.people['bartender'].add_relationship(1)
        if tavern.people['bartender'].relationship >= 6:
            print(co.colored("""
Here you go, drink up!

Oliver also grabs his ale ...

To good health!""", color="light_yellow"))
        else:
            if adventurer.give_gold(6):
                print(co.colored("""
That'll be 6 coins. 
I'd appreciate if I saw some coin before pouring you the drink. 
Nothing personal, it's just that yesterday an old geezer drank a gallon 
of ale and then tried to run on me.""", color="light_yellow"))
            else:
                print(co.colored("Invalid Choice! Try Again! (No money, no honey)", color="red"))
                continue
        break
    else:
        print(co.colored("Invalid Choice! Try Again!", color="red"))

print(co.colored(f"""
So, {adventurer.name}, what brought you to Herta?""", color="light_yellow"))

bogus = input('\n[Press Any Key to continue]')
print(co.colored(f"""
I heard rumours of dark creatures disrupting cargo shipments and terrorizing 
the locals around here...""", color="light_cyan"))
print(co.colored(f"""
Oliver interrupts you""", color="light_yellow", on_color="on_red", attrs=['bold', 'blink']))
print(co.colored(f"""
Ah, the damn goblins, they're a nuisance. My customers have halved since 
they appeared in the area, everyone is afraid to go out at night! But that 
usually turns people away. Not you, I reckon?""", color="light_yellow"))

bogus = input('\n[Press Any Key to continue]')
print(co.colored(f"""
I am here to get rid of them!""", color="light_cyan"))
print(co.colored(f"""
Oliver laughs""", color="light_yellow", on_color="on_red", attrs=['bold', 'blink']))
print(co.colored(f"""
Oh I hope you brought an army with you then! Those creatures only know violence. 
And there's dozens of them, from what I've heard.""", color="light_yellow"))

bogus = input('\n[Press Any Key to continue]')
print(co.colored(f"""
I do not expect to do it alone. Other than information, what I am hoping to 
find here is a person brave enough to accompany me on this quest. 
I have a few tricks up my sleeve to get put an end to them!""", color="light_cyan"))
print(co.colored(f"""
Well, if you say so... I'll drink to that! To the end of those demons!""", color="light_yellow"))

bogus = input('\n[Press Any Key to continue]')

asked = [False, False, False]
questions = [
    """
[a] : Do you have any knowledge of these creatures that could of use to me?""",
    """
[b] : Do you know any people who would be willing - and able - to assist me?""",
    """
[c] : Do you know where their camp is?"""
]
while True:
    print(co.colored("""
Ask Oliver:""", color="green"))
    for qu in range(len(questions)):
        if asked[qu]:
            print(co.colored(questions[qu], color="dark_grey"))
        else:
            print(co.colored(questions[qu], color="light_grey"))
    
    print(co.colored("""
[leave] : Goodbye!""", color="light_grey"))
    choice = input('\n> ').lower()
    if choice == "a":
        asked[0] = True
        print("choice a")
        bogus = input('\n[Press Any Key to continue]')
    elif choice == "b":
        asked[1] = True
        print("choice b")
        bogus = input('\n[Press Any Key to continue]')
    elif choice == "c":
        asked[2] = True
        print("choice c")
        bogus = input('\n[Press Any Key to continue]')
    elif choice == "leave":
        print("choice leave")
        break
    else:
        print(co.colored("Invalid Choice! Try Again!", color="red"))
# while True:
#     print("[goblins]: Tell me about the goblins roaming the area.")
#     print("[social]: Tell me about the people that come here.")
#     print("[hostile]: Fuck you you fat fuck!")
#     print("[food]: I would like something to eat.")
#     print("[drink]: I would like something to drink.")
#     print("[leave]: Bye.")

#     choice = input('> ').lower()
#     if choice == 'goblins':
#         print("information about the goblins...")
#     elif choice == 'social':
#         print("hunter and parrot")
#     elif choice == 'hostile':
#         print("GRAHH!")
#     elif choice == 'food':
#         print("edibles")
#     elif choice == 'drink':
#         print("drinks")
#     elif choice == 'leave':
#         print("Bye!")
#         break
#     else:
#         print('Not a viable choice! Try again!')

#     print("Would you like anything else? [yes/no]")
#     exit = input("> ")
#     if exit == 'no':
#         break