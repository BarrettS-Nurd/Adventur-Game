import random
btn_prs = 'False'
sac_dagger = 'False'
three = "false"
cthulhu_hlth = 10
cthulhu = "False"
lvr_pl = 'False'
inspct_pdstl = 'False'
lve_rm_atmp = 'False'
pck_axe = 'True'
brkn_pck_axe = 'False'
prtl = 'False'
smthng = 'False'
fnd_usbs = 'False'
srchd = 'False'
usb = 0
spl = "False"
mimic_hlth = 4
four = "False"
five = "False"
it_nnja = 'False'
hlth = 5
cthulhu_hlth = 10
mx_hlth = 5
mnstr_hlth = 5
drgn_hlth = 10
usb_tkn = 'False'
chk_pnt1 = 'False'
dwn_strs_lft = "False"
treasure_hlth = 5
clone_amnt = 1
seven =  "False"
uf3 = "False"
uf2 = "False"
uf1 = "False"
ms = "False"
s100 = "False"
pwk = "False"
head = "True"
fb = "False"
c = "False"
cw = "False"
healz = "False"
monsters = ['The Chimera', 'The Dragon', 'Todd Howard', 'Litterally Satan']
for x in range(1):
        mnstr = (random.randint(0,3))

spls = {
        '1 Word Unrelenting Force': 'UF1',
        'Fire Ball': 'FB',
        'Clone': 'C',
        'Cure Wounds': 'CW'
}

spl_desc = {
        'UF1': 'You yell at the top of your lungs and anything you yell at falls over.',
        'FB': 'You shoot a fireball out of your hands and disintigrate essentially anything.',
        'C': 'You make a clone of yourself, it is a physical copy of you that does what you do.',
        'CW': 'You heal yourself, this is the most boring yet most effecive spell.'
}

btr_spls = {
        '3 Word Unrelenting Force': 'UF3',
        'Meteor Shower': 'MS',
        'LVL 100 Speech': 'S100',
        'Power Word Kill': 'PWK'
}

btr_desc = {
        'UF3': 'You yell higher than your lungs and everything in front of you flies back.',
        'MS': 'Meteors rain from the sky when you use this, your in a cave though.',
        'S100': 'You have the abillity to convince anything of anything.',
        'PWK': 'Kills the target, pretty straightforward.'
}

def cthulhu_win():
        print("You are now litterally Cthulhu, you win")

def cthulhu_fght():
        global hlth
        global cthulhu_hlth
        global usb
        global head
        usb_dmg = 2
        while (cthulhu_hlth > 0 and hlth > 0):
                print(f"You have {hlth} health")
                print(f"The monster hand {cthulhu_hlth} health")
                print("Attack List")
                print("1. Stab")
                if usb > 0:
                        print("2. USB thow")
                        print(f"USB amount: {usb}")

                choice = input("> ")

                if choice == "1":
                        for x in range(1):
                                stab = random.randint(1,3)
                        cthulhu_hlth = cthulhu_hlth - stab
                elif choice == "2":
                        if usb > 0:
                                cthulhu_hlth = cthulhu_hlth - usb_dmg
                                usb = usb - 1
                        elif usb <= 0:
                                print("You dont have any USBs")
                        else:
                                print("I'm sorry i must not have seen option \"{choice}\" would you point it out?")
                                fight()
                if cthulhu_hlth > 0:
                        for x in range(1):
                                cthulhu_dmg = random.randint(1,2)
                        hlth = hlth - cthulhu_dmg
                elif cthulhu_hlth <= 0:
                        print("Cthulhu is dead!")
                        cthulhu_win()
                if hlth <= 0:
                        if head == "True":
                                print("Cthulhu bites your head off")
                        elif head == "False":
                                print("Cthulhu eats the rest of you")

                        die()

def mgc_rm():
        global seven
        global hlth
        global max_hlth
        global mnstr_hlth
        global uf1
        global fb
        global c
        global cw
        global treasure_hlth
        if seven == "False":
                print("You open the book and you there is a list of spells")
                print("what do you choose?")
                seven = "True"
        print("1. 1 Word Unrelenting Force")
        print("2. Fire Ball")
        print("3. Clone")
        print("4. Cure Wounds")
        mnstr_hlth = 10
        hlth = 10
        max_hlth = 10
        treasure_hlth = 15

        spl_chce = input("> ")

        if spl_chce == "1":
                uf1 = "True"
                print("1 Word Unrelenting Force: ", spl_desc['UF1'])
                mnstr = "The Dragon"
        elif spl_chce == "2":
                fb == "True"
                print("Fire Ball: ", spl_desc['FB'])
        elif spl_chce == "3":
                c = "True"
                print("Clone: ", spl_desc['C'])
        elif spl_chce == "4":
                cw = "True"
                print("Cure Wounds: ", spl_desc['CW'])
        print("You get teleported into a room you fight stuff in")
        fight()


def treasure_fght():
        global it_nnja
        global hlth
        global treasure_hlth
        global usb
        global clone_amnt
        fst_dmg = 1
        if it_nnja == "True":
                fst_dmg = 2
        for x in range(1):
                usb_dmg = (random.randint(1,2))
                treasure_dmg = (random.randint(1,2))
        if it_nnja == "True":
                for x in range(1):
                        usb_dmg = (random.randint(2,3))
        while (treasure_hlth > 0 and hlth > 0):
                print(f"You have {hlth} health")
                print(f"The monster hand {treasure_hlth} health")
                print("Attack List")
                print("1. Punch")
                if usb > 0:
                        print("2. USB trhow")
                        print(f"USB amount: {usb}")
                if uf1 == "True":
                        print("3. One Word Unrelenting Force")
                elif uf3 == "True":
                        print("3. Three Word Unrelenting Force")
                elif ms == "True":
                        print("3. Meteor Storm")
                elif s100 == "True":
                        print("\(Persuade\)Why dont we all just be friends and not fight.")
                elif pwk == "True":
                        print("3. Power Word Kill")
                elif fb == "True":
                        print("3. Fire Ball")
                elif c == "True":
                        print("3. Clone")
                elif cw == "True":
                        print("3. Cure Wounds")

                choice = input("> ")

                if choice == "1":
                        treasure_hlth = treasure_hlth - fst_dmg
                elif choice == "2":
                        if usb > 0:
                                treasure_hlth = treasure_hlth - usb_dmg
                                usb = usb - 1
                        elif usb <= 0:
                                print("You dont have any USBs")
                elif choice == "3":
                        if uf1 == "True":
                                print("The monster stumbles backwards")
                                treasure_hlth = treasure_hlth - 4
                        elif uf3 == "True":
                                print("The monster gets thrown back and slams into the side of the room, its dead")
                                treasure_hlth = treasure_hlth - 20
                        elif ms == "True":
                                print("Meteors storm down, and hit the roof of the cave")
                                print("thankfully the monster is standing right above a")
                                print("stalagmite and it falls up and hits the monster")
                                treasure_hlth = treasure_hlth - 1009
                        elif s100 == "True":
                                print("You convince the creature to become your friend")
                                treasure_frnd = "True"
                        elif pwk == "True":
                                print("You do as the spell says and kill the monster")
                                mntr_hlth = treasure_hlth - 1000009
                        elif fb == "True":
                                print("You shoot a fireball at the monster")
                                treasure_hlth = treasure_hlth - 30
                        elif c == "True":
                                print("You produce a clone of yourself")
                                clone_amnt = clone_amnt + 1
                        elif cw == "True":
                                print("You heal yourself")
                                hlth = hlth + 2
                        else:
                                print("play the game how it was meant to be played")
                else:
                        print("I'm sorry i must not have seen option \"{choice}\" would you point it out?")
                if treasure_hlth > 0:
                        hlth = hlth - treasure_dmg
        if treasure_hlth <= 0:
                print("The monster is dead!")
                print("you take all the treasure and leave")
                win()
        elif hlth <= 0:
                print("The monster kills you")
                die()

def treasure_mnstr():
        global healz
        global hlth
        global mx_hlth
        if healz == "False":
                print("You find a healing potion +1 when your walking to the next room")
                print("do you drink it")

                yn = input("y/n ")

                if yn == "y":
                        hlth = mx_hlth + 1
                        print(f"You have {hlth} health")
                elif yn == "n":
                        print(f"You have {hlth} health")
                healz = "True"
                print("You walk into a room filled with treasure and the physical")
                print("manifestation of glory, a monster made of treasure")
        print("what would you like to do?")
        print("1. Attack the monster")
        print("2. Take a chance and try to sneak some treasure out")
        print("3. Take all the treasue including the monster")

        choice = input("> ")

        if choice == "1":
                treasure_fght()
        elif choice == "2":
                for x in range(1):
                        sneak = (random.randint(0,3))
                        if it_nnja == "True":
                                sneak = sneak + 1
                if sneak == "5":
                        print("You stuff everything into a bag, and i mean everything")
                        print("you now how everything in existence in a bag")
                        win()
                if sneak == "4":
                        print("You steal all the treasure and the monster ignores you")
                        win()
                elif sneak == "2" or "3":
                        print("You steal a bag full of treasure and barely make it out")
                        win()
                elif sneak == "1":
                        print("As soon as you touch the hord of treasure the monster attacks you")
                        print("The monster gets the first move and hits you with its tail")
                        hlth - 1
                        treasure_fght()
        elif choice == "3":
                print("You get all the treasure into a truly massive sack and ride")
                print("the monster into the sunset")
                win()
        else:
                treasure_mnstr()

def win():
        print("You win!")

def prtl():
        global five
        global cthulhu
        global head
        global hlth
        hlth = 10
        if five == "False":
                print("When you go through the portal you end up in a massive underground lake")
                print("with a small island in the middle")
                five = "True"
        print("What do you do?")
        if cthulhu == "False":
                print("1. Touch the water")
        elif cthulhu == "True":
                print("1. Touch Cthulhu")
        print("2. Wait")
        print("3. Pray")

        choice = input("> ")

        if choice == "1":
                if cthulhu == "False":
                        print("Cthulhu rises out of the water")
                        print("Do you want to fight Cthulhu?")

                        choice2 = input("y/n ")

                        if choice2 == "y":
                                cthulhu_fght()
                        elif choice2 == "n":
                                cthulhu = "True"
                                prtl()
                elif cthulhu == "True":
                        print("When you touch Cthulhu it decides to fight you")
                        cthulhu_fght()
        elif choice == "2":
                if cthulhu == "False":
                        print("nothing happens")
                        prtl()
                elif cthulhu == "True":
                        if head == "True":
                                print("Cthulhu bites your head off")
                                print("somehow your still alive")
                                hlth - 1
                                head = "False"
                                prtl()
                        elif head == "False":
                                print("Cthulhu eats the rest of you and instead of dying you feel yourself")
                                print("being chewed to pieces and then churned by its stomache")
                                die()
        elif choice == "3":
                if cthulhu == "False":
                        print("You pray to Cthulhu and he rises out of the water to great you")
                        print("do you want to pray again?")

                        yn = input("y/n ")

                        if yn == "y":
                                print("Cthulhu turns you into a kraken")
                                print("you win?")
                        elif yn == "n":
                                print("Cthulhu leaves you in the cavern to starve")
                                die()
                elif cthulhu == "True":
                        print("Cthulhu turns you into a kraken")
                        win2()

def win2():
        print("You win?")

def die():
        print("YOU ARE DIED")

def down_stairs():
        global four
        global dwn_strs_lft
        global spl
        global uf3
        global ms
        global s100
        global pwk
        global mnstr_hlth
        global hlth
        global max_hlth
        global treasure_hlth
        treasure_hlth = 15
        max_hlth = 10
        hlth = 10
        mnstr_hlth = 10
        if four == "False":
                print("You walk down the stairs to find, another pedestal, with another book on it")
                four = "True"
        print("what do you do?")
        print("1. examine book")
        if dwn_strs_lft == "False":
                print("2. leave room")
        elif dwn_strs_lft == "True":
                print("2. Sit Around And Die")

        choice = input("> ")

        if choice == "2":
                if dwn_strs_lft == "False":
                        print("There is no way out of the room")
                        dwn_strs_lft = "True"
                        down_stairs()
                elif dwn_strs_lft == "True":
                        die()
        elif choice == "1":
                while spl == "False":
                        print("You get to choose a spell\\power to learn")
                        print("Which spell do you want to learn?")
                        print("1. Unrelenting Force LVL 3")
                        print("2. Meteor Storm ")
                        print("3. LVL 100 Speech ")
                        print("4. Power Word Kill ")

                        spl = input("> ")

                        if spl == "1":
                                uf3 = "True"
                                print("congrats you know know Unrelenting Force")
                                print("Desc: ", btr_desc['UF3'])
                        elif spl == "2":
                                ms == "True"
                                print("congrats you know know Meteor Storm")
                                print("Desc: ", btr_desc['MS'])
                        elif spl == "3":
                                s100 = "True"
                                print("congrats you have LVL 100 Speech")
                                print("Desc: ", btr_desc['S100'])
                        elif spl == "4":
                                pwk = "True"
                                print("congrats you know know Power Word Kill")
                                print("Desc: ", btr_desc['PWK'])
                        print("You appear in a room you fight things")
                        fight()
        else:
                down_stairs()

def start():
        global smthng
        global srchd
        global usb_tkn
        global usb
        if smthng == 'False':
                print("You, Barry Stetler, wake up outside a cave entrance")
                print("with nothing but the clothes on your back")
                print("and a pickaxe")
                smthng = 'True'
        print("would you like to...")
        print("1. Head into the cave")
        if srchd == 'False':
                print("2. Search the area")
        if srchd == 'True':
                print("2. Search")
                print("3. Wade into the water")
                if usb_tkn == 'False':
                        print("4. Take usb sticks")

        choice = input("> ")

        if choice == "1":
                cave()
        elif choice == "2":
                if srchd == 'False':
                        print("you search the area you woke up in to find out you")
                        print("woke up on a small island with a cave and some usb sticks")
                        srchd = 'True'
                        start()
                elif srchd == 'True':
                        print("You search the island again and find nothing of interest")
                        start()
        elif choice == "3":
                if srchd == 'True':
                        print("You wade into the water and your vision fades to black")
                        input("ENTER to continue")
                        print("You wake back up at the mouth of the cave")
                        start()
                elif srchd == 'False':
                        print("This wasnt one of your choices, stick to the script")
                start()
        elif choice == "4":
                if srchd == 'True':
                        if usb_tkn == 'False':
                                usb = 3
                                print("you take three usb sticks out of the pile")
                                print("you now have three usb sticks")
                                usb_tkn = 'True'
                                start()
                        elif usb_tkn == 'True':
                                print("you already took your share, begone")
                                start()
                elif srchd == 'False':
                        print("that wasnt one of your choices stick to the script")
                        start()
        else:
                print(f"that wasnt one of your choices, stick to the script")
                start()


def cave():
        global chk_pnt1
        if chk_pnt1 == 'False':
                print("When you walk into the cave you see two doors one on your")
                print("left and one on your right")
#               print("a lever in the unpward position")
        print("WHat would you like to do")
        print("1. Go through the left door")
        print("2. Go through the right door")
#       if chk_pnt1 == 'False':
#               print("3. Pull down the lever(Checkpoint)")

        choice = input("> ")

        if choice == "1":
                lft_rm()
        elif choice == "2":
                rght_room()
#       elif choice == "3":
#               chk_pnt1 = 'True'
        else:
                print("That wasnt one of your choices, try again")
                cave()

def lft_rm():
        global mnstr_frnd
        global monsters
        global mnstr
        print("As you walk through the door on the left of the room")
        print("it slams behind you and you hear something ahead of you")
        print(f" a massive {monsters[mnstr]} appears ahead of you")
        print("What do you want to do?")
        print(f"1. Fight the {monsters[mnstr]}")
        print(f"2. Flee from the {monsters[mnstr]}")

        choice = input("> ")

        if choice == "1":
                fight()
        elif choice == "2":
                print("You slide under the monsters legs and make it to the next room")
                treasure_mnstr()
        else:
                print(f"You hesitate and the {monsters[mnstr]} bites your head off")
                die()

def fight():
        global clone_amnt
        global usb
        global mnstr_hlth
        global hlth
        global it_nnja
        global mx_hlth
        hi = 'True'
        fst_dmg = 1
        for x in range(1):
                usb_dmg = random.randint(0,1)
        usb_dmg = usb_dmg + 1

        while (mnstr_hlth > 0 and hlth > 0):
                print(f"You have {hlth} health")
                print(f"The monster hand {mnstr_hlth} health")
                print("Attack List")
                print("1. Punch")
                if usb > 0:
                        print("2. USB thow")
                        print(f"USB amount: {usb}")

                if uf1 == "True":
                        print("3. One Word Unrelenting Force")
                elif uf3 == "True":
                        print("3. Three Word Unrelenting Force")
                elif ms == "True":
                        print("3. Meteor Storm")
                elif s100 == "True":
                        print("\(Persuade\)Why dont we all just be friends and not fight.")
                elif pwk == "True":
                        print("3. Power Word Kill")
                elif fb == "True":
                        print("3. Fire Ball")
                elif c == "True":
                        print("3. Clone")
                elif cw == "True":
                        print("3. Cure Wounds")

                choice = input("> ")

                if choice == "1":
                        mnstr_hlth = mnstr_hlth - (fst_dmg * clone_amnt)
                elif choice == "2":
                        if usb > 0:
                                mnstr_hlth = mnstr_hlth - (usb_dmg * clone_amnt)
                                usb = usb - 1
                        elif usb <= 0:
                                print("You dont have any USBs")
                elif choice == "3":
                        if uf1 == "True":
                                print("The monster stumbles back a little")
                                mnstr_hlth = mnstr_hlth - 4
                        elif uf3 == "True":
                                print("The monster gets thrown back and slams into the side of the room, its dead")
                                mnstr_hlth = mnstr_hlth - 20
                        elif ms == "True":
                                print("Meteors storm down, and hit the roof of the cave")
                                print("thankfully the monster is standing right above a")
                                print("stalagmite and it falls up and hits the monster")
                                mntsr_hlth = mnstr_hlth - 1009
                        elif s100 == "True":
                                print("You convince the creature to become your friend")
                                mnstr_frnd = "True"
                        elif pwk == "True":
                                print("You do as the spell says and kill the monster")
                                mntr_hlth = mnstr_hlth - 1000009
                        elif fb == "True":
                                print("You shoot a fireball at the monster")
                                mnstr_hlth = mnstr_hlth - 30
                        elif c == "True":
                                print("You produce a clone of yourself")
                                clone_amnt = clone_amnt + 1
                        elif cw == "True":
                                print("You heal yourself")
                                hlth = hlth + 2
                        else:
                                print("No hacking")
                else:
                        print("I'm sorry i must not have seen option \"{choice}\" would you point it out?")
                if mnstr_hlth > 0:
                        hlth = hlth - 1
                elif mnstr_hlth <= 0:
                        print("The monster is dead!")
                if hlth <= 0:
                        die()
        print(f"When you slay the {monsters[mnstr]} you find your favorite")
        print("shirt in it's stash it reads Dont worry, im an IT ninja")
        while hi == "True":
                print("do you want to take your shirt before you leave?")

                choice = input("y/n? ")

                if choice == "y":
                        print("You put on your IT ninja shirt and leave")
                        it_nnja = 'True'
                        hi = 'False'
                        mx_hlth = mx_hlth + 1
                elif choice == "n":
                        print("You leave your it ninja shirt behind for no reason")
                        hi = 'False'
                else:
                        print("What is wrong with you")
        treasure_mnstr()


def rght_room():
        global btn_prs
        global lvr_pl
        global lve_rm_atmp
        global inspct_pdstl
        if lve_rm_atmp == 'True':
                print("You walk into the room on the right and you see a pedestal")
                print("in the middle of the room, and a door in the back")
                print("on the pedestal there is a book")
        print("what do you do?")
        print("1. Examine Book")
        if lve_rm_atmp == 'False':
                print("2. Leave Room")
        elif lve_rm_atmp == 'True':
                if inspct_pdstl == 'False':
                        print("2. Examine wall")
                elif inspct_pdstl == 'True':
                        print("2. Examine pedestal")

        if (btn_prs and lvr_pl) == 'True':
                print("3. go down stairs")
        else:
                print("3. search room")

        choice = input("> ")

        if choice == "1":
                mgc_bk()
        elif choice == "2":
                if lve_rm_atmp == 'False':
                        print("when you try to leave the way you came the doorway")
                        print("is gone and in its place a wall")
                        lve_rm_atmp = 'True'
                        rght_room()
                elif lve_rm_atmp == 'True':
                        if inspct_pdstl == 'False':
                                print("There is nothing weird about the wall")
                                print("why would you even inspect it?")
                                inspct_pdstl = 'True'
                                rght_room()
                        elif inspct_pdstl == 'True':
                                print("You find a button on the bottom of the pedestal")
                                print("Do you press the button?")
                                yn = input("y/n? ")
                                if yn == "y":
                                        btn_prs = 'True'
                                        if lvr_pl == 'True':
                                                print("The pedestal slides away to reveal a stairwell")
                                                print("do you want to walk down the stairwell?")

                                                yn = input("y/n? ")

                                                if yn == "y":
                                                        down_stairs()
                                                else:
                                                        print("you sit around")
                                                        rght_room()
                                        elif lvr_pl == 'False':
                                                btn_prs = 'True'
                                                print("The pedestal slides back to reveal, the floor")
                                else:
                                        print("Nothing happens")
                                rght_room()
        elif choice == "3":
                if (btn_prs and lvr_pl) == 'False':
                        print("When you search the room you find a obvious lever")
                        print("do you want to pull it?")

                        yn = input("y/n? ")

                        if yn == "y":
                                if btn_prs == 'True':
                                        print("You watch as the floor where the pedestal used to be")
                                        print("retracts to reveal a stairwell, do you want to go down?")

                                        yn = input("y/n? ")

                                        if yn == "y":
                                                down_stairs()
                                        elif yn == "n":
                                                rght_room()
                                        else:
                                                print("it is because of people like you i hate this")
                                                rght_room()
                                else:
                                        print("you hear what sounds like stone grinding stone")
                                        print("coming from under the pedestal")
                                        lvr_pl = 'True'
                                        rght_room()
                        elif yn == "n":
                                print("nothing happens when you dont pull the obvious lever")
                                rght_room()
                        else:
                                print("I dont know that one")
                                rght_room()
                elif (btn_prs and lvr_pl) == 'True':
                        down_stairs()
                else:
                        rght_room()
        else:
                rght_room()

def mgc_bk():
        global sac_dagger
        global three
        global prtl
        if three == "False":
                print("When you touch the book on the pedestal you get sucked into it")
                print("and get shot out into a white void with nothing but the pedestal and book")
                three = "True"
        print("what do you want to do")
        print("1. Examine book")
        print("2. Wait and die")
        if prtl == "True":
                print("3. Go through portal")
        elif sac_dagger == "False":
                print("3. search")
        elif sac_dagger == "True":
                print("3. sacrafice the cow")

        choice = input("> ")

        if choice == "1":
                mgc_rm()
        elif choice == "2":
                die()
        elif choice == "3":
#               if prtl == "True":
#                       prtl()
                if sac_dagger == "False":
                        print("You find a sacrificial dagger behind the pedestal")
                        print("do you want to take the dagger?")

                        yn = input("y/n? ")

                        if yn == "y":
                                sac_dagger = "True"
                                print("You take a dagger and as soon as you do a cow appears in front of the")
                                print("pedestal, as you take the dagger a cow appears in front of you")
                                mgc_bk()
                        elif yn == "n":
                                print("You ignore the dagger and do nothing")
                                mgk_bk()
                elif sac_dagger == "True":
                        print("You sacrafice the cow, a massive portal opens up on the ground and sucks")
                        print("in the remnants of cow, as well as you")
#                       prtl = "True"
#                       mgc_bk()
                        prtl()
                elif prtl == "False":
                        print("Congrats, you boke my game!")
        else:
                mgc_bk()

start()