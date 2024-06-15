import person
import items
import creatures
import termcolor as co
# Checkout pygame

name = input('Enter your name! ')
adventurer = person.Person(name)
print(f'Greetings {adventurer.name}! Welcome to your adventure!')

start = input('Would you rather play the game or perish? ')

if start == 'play':
    print('Great! Let\'s play the game!')
    print("-------- Herta's Nectar --------")
    dawnbringer = items.DawnBringer()
    woodensword = items.WoodenSword()
    print('You come across a chest! It contains a wooden sword and a big shiny blade!')
    print('Which one would you choose?')
    while True:
        choice = input('\twooden sword\n\tshiny blade\n\tnothing\n')
        if choice == 'wooden sword':
            print('You picked up the wooden sword')
            adventurer.pickup(woodensword)
            break
        elif choice == 'shiny blade':
            print('You picked up the Dawnbringer')
            adventurer.pickup(dawnbringer)
            break
        elif choice == 'nothing':
            print('You picked up nothing! Good ol\' fisting!')
            break
        else:
            print('Not a viable choice! Try again!')
    print('You come across a big wooden door! Why would there be a door out in the forest? Noone knows, but someone is banging it from the other side!')
    if choice != 'nothing':
        print('For good measure you equip your sword!')
        key = list(adventurer.inventory.keys())
        adventurer.equip(adventurer.inventory[key[0]])
    else:
        print('Maybe a sword would come in handy! You prepare your fists imagining you are Rocky (you are not)!')
    print('Would you like to open it?')
    while True:
        choice = input('Option:\n\tyes\n\tno\n')
        if choice == 'yes':
            print('You come across a really angry orc!')
            print(co.colored(text='FIGHT!', color='red'))
            break
        elif choice == 'no':
            print('A really angry orc breaks down the door!')
            print(co.colored(text='FIGHT!', color='red'))
            break
        else:
            print('Not a viable choice! Try again!')
    orc = creatures.Orc()
    if adventurer.apparel['right_arm'] != None:
        hit = adventurer.strength + adventurer.apparel['right_arm'].damage
    else:
        hit = adventurer.strength
    
    while True:
        choice = input('Option:\n\tattack\n\trun\n')
        if choice == 'attack':
            print('You attack the orc!')
            print(f'You deal {hit} damage to the orc!')
            orc.take_damage(hit)
            if orc.hp <= 0:
                break
            print(f'The orc attacks back! It whoops your ass dealing {orc.damage} damage!')
            adventurer.take_damage(orc.damage)
        elif choice == 'run':
            print('You try to run away but the orc catches you!')
            print('The orc deals to you 1 damage!')
            adventurer.take_damage(1)
        else:
            print('Not a viable choice! Try again!')
    print(co.colored('Congratulations! Tutorial complete!', color='green'))
else:
    print('Okay you\'re dead!')