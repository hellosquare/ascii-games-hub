RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"
import time

def typewriter(text, delay=0.02):
    for c in text:
        print(c, end="", flush=True)
        time.sleep(delay)
    print()

#print(f"{RED}红色文字{RESET}")
import time

text = "WELCOME"
for _ in range(5):
    print(f"\r{text}", end="", flush=True)
    time.sleep(0.3)
    print("\r" + " "*len(text), end="", flush=True)
    time.sleep(0.3)
print("\rPlease press enter to load the game.")
input ()
import time

def progress_bar(total=100):
    for i in range(total+1):
        percent = i / total
        bar_len = 30
        filled = int(bar_len * percent)
        bar = "█" * filled + "-" * (bar_len - filled)
        print(f"\r[{bar}] {i}%", end="", flush=True)
        time.sleep(0.04)
    print()

progress_bar()
print ("Welcome to the game, in here you can choose to join and participate in Police Department or Fire Department in the State.")
print ("")
print ("Now, please carefully read the ", f"{RED}liability exemption {RESET}", "and enter 'understand' to acknowledge.")
while True:
    liability = input("1. All character setting are for game-design purpose only, not intend to refer or associate with real life situation.\n2. All process and procedure present in the game are NOT professional and NOT teachable.\n3. I am agree of all the clauses above.\nNow please enter 'understand' to acknowledge.")
    
    if liability == "understand":
        print("")
        print("Now, we will launch the character create system.")
        break
        
    print ("")    
    print (f"You typed: {liability}", ". Please check your spelling and re-enter 'understand', if not please exit the game.")

print ("")
print ("===CHARACTER-CREATE-SYSTEM===")
typewriter ("Welcome Players, please give your character a name:")
characterName = input("")
print ("")
typewriter ("Welcome " + characterName + ". Now please enter a number that represents your character type:")
typewriter ("1.Police Department\n2.Fire Department")
xp = 100
characterType = int(input())
if characterType == 1:
    typewriter ("Welcome Officer " + characterName + ". Now please enter a number that represents your department location.\n1.LAPD\n2.NYPD\n3.LVPD")
    characterLocation = int(input())
    if characterLocation == 1:
        typewriter ("Welcome Officer " + characterName + " from the LAPD. Your XP point will be 100, when the XP point reach 0, game lose.")
    if characterLocation == 2:
        typewriter ("Welcome Officer " + characterName + " from the NYPD. Your XP point will be 100, when the XP point reach 0, game lose.")
    if characterLocation == 3:
            typewriter ("Welcome Officer " + characterName + " from the LVPD. Your XP point will be 100, when the XP point reach 0, game over.")

    print ("")
    print ("===!!CHARACTER IMOFRMATION!!===")
    typewriter ("Patrol Officer " + characterName)
    print ("XP:", xp)
    print("")
    print ("Press Enter to start.")
    input ()
    import time

    def wave_bar(width=20):
        pos = 0
        direction = 1
        for _ in range(40):
            bar = [" "] * width
            bar[pos] = "▬"
            print(f"\r|{''.join(bar)}|", end="", flush=True)
            pos += direction
            if pos >= width-1:
                direction = -1
            if pos <= 0:
                direction = 1
            time.sleep(0.08)
        print("\r" + " "* (width+2))

    wave_bar()

    typewriter ("▬▬▬▬▬ GAME START ▬▬▬▬▬")
    typewriter ("Welcome! You have total 15 team members, as a captain please memorize this very carefully!")
    input ()
    print(r'''
              ____----------- _____
\~~~~~~~~~~/~_--~~~------~~~~~     \
 `---`\  _-~      |                   \
   _-~  <_         |                     \[]
 / ___     ~~--[""] |      ________-------'_
> /~` \    |-.   `\~~.~~~~~                _ ~ - _
 ~|  ||\%  |       |    ~  ._                ~ _   ~ ._
   `_//|_%  \      |          ~  .              ~-_   /\
          `--__     |    _-____  /\               ~-_ \/.
               ~--_ /  ,/ -~-_ \ \/          _______---~/
                   ~~-/._<   \ \`~~~~~~~~~~~~~     ===--~/
                         \    ) |`--------==-~~~~-~  ) )
                          ~-_/_/                  ~~ ~~
''')
    typewriter (f"▬▬▬ Mission 1 ▬▬▬\nThere is a reckless driving reported in Broadway Street, please {RED}assign number {RESET}of members you bring to the scene.")
    memberNumber = int(input())
    if memberNumber < 16:
        typewriter ("Member assigned! XP + 5")
        xp = xp + 5
        print (f"XP = {xp}")        
    else:
        typewriter ("Member failed to assign, reach the available members! XP - 10!!!")
        xp = xp - 10
        typewriter (f"XP = {xp}")

    typewriter ("Member(s) arrived the scene, please enter 'stop' to taffic stoping. ")
    while True:
        pdstop = input("")
    
        if pdstop == "stop":
            print("")
            typewriter("Control, suspect in in custody, code 4.")
            xp = xp + 5
            print (f"XP = {xp}")
            break
        
        print ("")    
        xp = xp - 10
        if xp > 0:
            print ("Suspect out of sight, try again!")
            print (f"XP = {xp}")
        else:
            text = "=== GAME OVER ==="
            for _ in range(5):
                print(f"\r{text}", end="", flush=True)
                time.sleep(0.3)
                print("\r" + " "*len(text), end="", flush=True)
                time.sleep(0.3)
            exit()

    typewriter ("Before we start Mission 2, please select a difficulty")
    print ("1. Easy Mode\n2. Hard Mode")
    pdlevel = int(input("Please enter a number:"))
    if pdlevel == 1:
        typewriter ("▬▬▬ Easy Mode Slected ▬▬▬")
        import time

        def dot_loading(msg="Processing"):
            for i in range(1, 12):
                dots = "." * (i % 20)
                print(f"\r{msg}{dots}", end="", flush=True)
                time.sleep(0.2)
            print(f"\r{msg} COMPLETE    ")

        dot_loading("LOADING")

        print ("▬▬▬ Mission 2-1 ▬▬▬")
        print(r'''
                                           ___________                        
                                              __..--""""           """"--..__              
                                          _.-"""""""""""-----...      ______ `.            
                                       .-"                      l ,-""    \ "-.`.          
                                    .-"                         ; ;        ;   \ ""--.._   
                                  .'                           : :         |    ;      .l  
                            _.._.'                             ; ;  ___    |    ;    .' :  
                           (  .'                              : :  :   ".  :..-'   .'    ; 
                            )'                                | ;  ; __.'-"(     .'  .--.: 
                    ___...-'""""----....____          ______.-' :-/.'       \_.-'  .' .-.\l
            __..--""                        """"""""""          /\"          ;    / .gs./\;
        _.-"                                                   /  ;          |   . d$P"Tb  
     .-""""-,                       ____                        /   |          :   ;:$$   $; 
   .'     ;                    ,""    ""--..__               /    :          |   $$$;   :$ 
  /"-._  /                     ;       ____..-'    .-"""-.  /     :          ;  _$$$;   :$ 
 :     ""--.._          ___....+---""""          .'  _._  \/      |         _:-" $$$;   :$ 
 ;                                              /  .d$$$b./       ;      .-".'   :$$$   $P 
:            .----...____                      :  dP' `T$P        |   .-" .' _.gd$$$$b_d$' 
;    __...---|    bug    |----....____         | :$     $b        : .'   (.-"  `T$$$$$$P'  
;  .';       '----...____;       /    "-.      ; $;     :$;_____..-"  .-"                  
: /  :                          /        \__..-':$       $$ ;-.    .-"                     
 Y    ;                        /          ;     $;       :$;|  `.-"                        
 :    :                       /           |     $$       $$;:.-"                           
 '$$$ggggp...____            /            :     :$;     :$$                                
  $$$$$$$$$$$$   """"----...:________....gggg$$$$$$     $$;                                
  'T$$$$$$$$P'                           T$$$$$$$$$b._.d$P                                 
    `T$$$$P'                              T$$$$$$$$$$$$$P                                  
                                           `T$$$$$$$$$P'
''')
        typewriter ("Amber Alart: Kidnapping with silver Corolla possible at 150-freeway.")
        typewriter ("Kiddnapper: 1000 Bitcoin to exchange the kid.")
        input ("")
        typewriter ("Your priority is talk to the kidnapper with patience, enter 'patience' to communicate.")
        while True:
            kidnapword = input ("Enter here:")

            if kidnapword == "patience":
                def dot_loading(msg="Negotiating"):
                    for i in range(1, 12):
                        dots = "." * (i % 20)
                        print(f"\r{msg}{dots}", end="", flush=True)
                        time.sleep(0.2)
                    print(f"\r{msg} Negotiating    ")

                dot_loading("Negotiating")
                xp = xp + 15
                print (f"Final XP = {xp}")
                break

            print("")
            print(f"You typed: {kidnapword}, Please check your spelling! XP - 10")
            xp = xp - 10
            if xp > 0:
                print ("Try again!")
                print (f"XP = {xp}")
            else:
                text = "=== GAME OVER ==="
                for _ in range(5):
                    print(f"\r{text}", end="", flush=True)
                    time.sleep(0.3)
                    print("\r" + " "*len(text), end="", flush=True)
                    time.sleep(0.3)
                exit()
        
        typewriter ("▬▬▬▬ MISSION ACCOMPLISHED ▬▬▬▬")
        text = "▬▬▬▬ GAME COMPLETED ▬▬▬▬"
        for _ in range(5):
            print(f"\r{text}", end="", flush=True)
            time.sleep(0.3)
            print("\r" + " "*len(text), end="", flush=True)
            time.sleep(0.3)
        print("\rTHANKS FOR PLAYING!")



    
    
    if pdlevel == 2:
        typewriter ("▬▬▬ Hard Mode Slected ▬▬▬")
        import time

        def dot_loading(msg="Processing"):
            for i in range(1, 12):
                dots = "." * (i % 20)
                print(f"\r{msg}{dots}", end="", flush=True)
                time.sleep(0.2)
            print(f"\r{msg} COMPLETE    ")

        dot_loading("LOADING")
        print ("▬▬▬ Mission 2-2 ▬▬▬")
        
        print(r'''
                                           ___________                        
                                              __..--""""           """"--..__              
                                          _.-"""""""""""-----...      ______ `.            
                                       .-"                      l ,-""    \ "-.`.          
                                    .-"                         ; ;        ;   \ ""--.._   
                                  .'                           : :         |    ;      .l  
                            _.._.'                             ; ;  ___    |    ;    .' :  
                           (  .'                              : :  :   ".  :..-'   .'    ; 
                            )'                                | ;  ; __.'-"(     .'  .--.: 
                    ___...-'""""----....____          ______.-' :-/.'       \_.-'  .' .-.\l
            __..--""                        """"""""""          /\"          ;    / .gs./\;
        _.-"                                                   /  ;          |   . d$P"Tb  
     .-""""-,                       ____                        /   |          :   ;:$$   $; 
   .'     ;                    ,""    ""--..__               /    :          |   $$$;   :$ 
  /"-._  /                     ;       ____..-'    .-"""-.  /     :          ;  _$$$;   :$ 
 :     ""--.._          ___....+---""""          .'  _._  \/      |         _:-" $$$;   :$ 
 ;                                              /  .d$$$b./       ;      .-".'   :$$$   $P 
:            .----...____                      :  dP' `T$P        |   .-" .' _.gd$$$$b_d$' 
;    __...---|    6767    |----....____         | :$     $b        : .'   (.-"  `T$$$$$$P'  
;  .';       '----...____;       /    "-.      ; $;     :$;_____..-"  .-"                  
: /  :                          /        \__..-':$       $$ ;-.    .-"                     
 Y    ;                        /          ;     $;       :$;|  `.-"                        
 :    :                       /           |     $$       $$;:.-"                           
 '$$$ggggp...____            /            :     :$;     :$$                                
  $$$$$$$$$$$$   """"----...:________....gggg$$$$$$     $$;                                
  'T$$$$$$$$P'                           T$$$$$$$$$b._.d$P                                 
    `T$$$$P'                              T$$$$$$$$$$$$$P                                  
                                           `T$$$$$$$$$P'
''')
        typewriter ("Amber Alart: Kidnapping with silver Corolla possible at 150-freeway.")
        typewriter ("Kiddnapper: 1000 Bitcoin to exchange the kid.")
        input ("")
        typewriter ("Enter a number that represents your action:\n1. Pay Ransom for 1000 Bitcoin.\n2. Talk to kidnapper with patient\n3. Isolation. No communication.")
        negotiation = int(input("Enter a valid number please:"))
        if negotiation == 1:
            print ("Victim went lost, money disappear, XP-50!!!")
            xp = xp -50
            if xp < 1:
                print ("▬▬▬ GAME LOSE ▬▬▬")
                print (f"XP = {xp}")
                exit()
            
            if xp > 0:
                print ("▬▬▬ GAME OVER ▬▬▬")
                print (f"XP = {xp}")
                exit()
        if negotiation == 2:
            print ("Victim safe, kidnapper turn himself in.")
            xp = xp + 50
            typewriter ("▬▬▬▬ MISSION ACCOMPLISHED ▬▬▬▬")
            print (f"Final XP = {xp}")
            text = "▬▬▬▬ GAME COMPLETED ▬▬▬▬"
            for _ in range(5):
                print(f"\r{text}", end="", flush=True)
                time.sleep(0.3)
                print("\r" + " "*len(text), end="", flush=True)
                time.sleep(0.3)
            print("\rTHANKS FOR PLAYING!")
        if negotiation == 3:
            ("Victim dead, game over.")
            xp = xp -50
            if xp < 1:
                print ("▬▬▬ GAME LOSE ▬▬▬")
                print (f"XP = {xp}")
                exit()
            
            if xp > 0:
                print ("▬▬▬ GAME OVER ▬▬▬")
                print (f"XP = {xp}")
                exit()
    
    if pdlevel == 3:
        print ("▬▬▬ EXTREMELY HARD DEVELOPER MODE SELECTED ▬▬▬")
        print ("A scanning of the mountain where the kidnapper is hiding given a result of\nf(x)=(-X^4)+(4X^2)+5 \nGiven that the kidnapper is hidden in point where x equal to 10, please determine the instant slope rate of the point for teams to rescue!")
        #20
        height = int(input("Please enter the rescue height:"))
        if height == -3920:
            typewriter ("Kidnapper under control, victim is safe!")
            xp = xp + 100
            print (f"XP + 100\rXP = {xp}")
            text = "▬▬▬▬ GAME ACCOMPLISHED ▬▬▬▬"
            for _ in range(5):
                print(f"\r{text}", end="", flush=True)
                time.sleep(0.3)
                print("\r" + " "*len(text), end="", flush=True)
                time.sleep(0.3)
            print("\rTHANKS FOR PLAYING!")
            exit ()
        else:
            typewriter ("No sight on the kidnapper and victim!")
            xp = xp - 100
            print (f"XP - 100\rXP = {xp}")
            text = "▬▬▬▬ GAME FAILED ▬▬▬▬"
            for _ in range(5):
                print(f"\r{text}", end="", flush=True)
                time.sleep(0.3)
                print("\r" + " "*len(text), end="", flush=True)
                time.sleep(0.3)
            print("\rTHANKS FOR PLAYING!")
            exit ()



#FD
if characterType == 2:
    typewriter ("Welcome Officer " + characterName + ". Now, please enter a number that represents your department location.\n1.LAFD\n2.NYFD\n3.LVFD")
    characterLocation = int(input())
    if characterLocation == 1:
        typewriter ("Welcome Officer " + characterName + " from the LAFD. Your XP point will be 100, when the XP point reach 0, game lose.")
    if characterLocation == 2:
        typewriter ("Welcome Officer " + characterName + " from the NYFD. Your XP point will be 100, when the XP point reach 0, game lose.")
    if characterLocation == 3:
            typewriter ("Welcome Officer " + characterName + " from the LVFD. Your XP point will be 100, when the XP point reach 0, game over.")

    print ("")
    print ("===!!CHARACTER IMOFRMATION!!===")
    typewriter ("Officer " + characterName)
    print ("XP:", xp)
    print("")
    print ("Press Enter to start.")
    input ()
    import time

    def wave_bar(width=20):
        pos = 0
        direction = 1
        for _ in range(40):
            bar = [" "] * width
            bar[pos] = "▬"
            print(f"\r|{''.join(bar)}|", end="", flush=True)
            pos += direction
            if pos >= width-1:
                direction = -1
            if pos <= 0:
                direction = 1
            time.sleep(0.08)
        print("\r" + " "* (width+2))

    wave_bar()

    typewriter ("▬▬▬▬▬ GAME START ▬▬▬▬▬")
    typewriter ("Welcome! You have total 17 team members, as a captain please memorize this very carefully!")
    input ()
    typewriter (f"▬▬▬ Mission 1 ▬▬▬\nThere is a fire reported at mid-wilshire, please {RED}assign number {RESET}of members you bring to the scene.")
    memberNumber = int(input())
    if memberNumber < 18:
        typewriter ("Member assigned! XP + 5")
        xp = xp + 5
        print (f"XP = {xp}")        
    else:
        typewriter ("Member failed to assign, reach the available members! XP - 10!!!")
        xp = xp - 10
        typewriter (f"XP = {xp}")

    typewriter ("Member(s) arrived the scene, please enter 'water' to spot the fire.")
    while True:
        pdstop = input("")
    
        if pdstop == "water":
            print("")
            typewriter("Fire under control, code 4.")
            xp = xp + 5
            print (f"XP = {xp}")
            break
        
        print ("")    
        xp = xp - 10
        if xp > 0:
            print ("Fire still on, try again!")
            print (f"XP = {xp}")
        else:
            text = "=== GAME OVER ==="
            for _ in range(5):
                print(f"\r{text}", end="", flush=True)
                time.sleep(0.3)
                print("\r" + " "*len(text), end="", flush=True)
                time.sleep(0.3)
            exit()

    typewriter ("Before we start Mission 2, please select a difficulty")
    print ("1. Easy Mode\n2. Hard Mode")
    fdlevel = int(input("Please enter a number:"))
    if fdlevel == 1:
        typewriter ("▬▬▬ Easy Mode Slected ▬▬▬")
        import time

        def dot_loading(msg="Processing"):
            for i in range(1, 12):
                dots = "." * (i % 20)
                print(f"\r{msg}{dots}", end="", flush=True)
                time.sleep(0.2)
            print(f"\r{msg} COMPLETE    ")

        dot_loading("LOADING")

        print ("▬▬▬ Mission 2-1 ▬▬▬")
        print(r'''
                         __    _
                    _wr""        "-q__
                 _dP                 9m_
               _#P                     9#_
              d#@                       9#m
             d##                         ###
            J###                         ###L
            {###K                       J###K
            ]####K      ___aaa___      J####F
        __gmM######_  w#P""   ""9#m  _d#####Mmw__
     _g##############mZ_         __g##############m_
   _d####M@PPPP@@M#######Mmp gm#########@@PPP9@M####m_
  a###""          ,Z"#####@" '######"\g          ""M##m
 J#@"             0L  "*##     ##@"  J#              *#K
 #"               `#    "_gmwgm_~    dF               `#_
7F                 "#_   ]#####F   _dK                 JE
]                    *m__ ##### __g@"                   F
                       "PJ#####LP"
 `                       0######_                      '
                       _0########_
     .               _d#####^#####m__              ,
      "*w_________am#####P"   ~9#####mw_________w*"
          ""9@#####@M""           ""P@#####@M""
''')
        typewriter ("Chemical leackage: Hydrochloric acid (HCl) found leak in a chemical factory")
        typewriter ("Control: Use some base chemical to neutralize it.")
        input ("")
        typewriter ("Your priority is to use proper chemical to address the scene, please enter 'base' to neutralize the leaking chemical.")
        while True:
            neutralize = input ("Enter here:")

            if neutralize == "base":
                def dot_loading(msg="Processing"):
                    for i in range(1, 12):
                        dots = "." * (i % 20)
                        print(f"\r{msg}{dots}", end="", flush=True)
                        time.sleep(0.2)
                    print(f"\r{msg} Processing    ")

                dot_loading("Processing")
                xp = xp + 15
                print (f"Final XP = {xp}")
                break

            print("")
            print(f"You typed: {neutralize}, Please check your spelling! XP - 10")
            xp = xp - 10
            if xp > 0:
                print ("Try again!")
                print (f"XP = {xp}")
            else:
                text = "=== GAME OVER ==="
                for _ in range(5):
                    print(f"\r{text}", end="", flush=True)
                    time.sleep(0.3)
                    print("\r" + " "*len(text), end="", flush=True)
                    time.sleep(0.3)
                exit()
        
        typewriter ("▬▬▬▬ MISSION ACCOMPLISHED ▬▬▬▬")
        text = "▬▬▬▬ GAME COMPLETED ▬▬▬▬"
        for _ in range(5):
            print(f"\r{text}", end="", flush=True)
            time.sleep(0.3)
            print("\r" + " "*len(text), end="", flush=True)
            time.sleep(0.3)
        print("\rTHANKS FOR PLAYING!")



    
    
    if fdlevel == 2:
        typewriter ("▬▬▬ Hard Mode Slected ▬▬▬")
        import time

        def dot_loading(msg="Processing"):
            for i in range(1, 12):
                dots = "." * (i % 20)
                print(f"\r{msg}{dots}", end="", flush=True)
                time.sleep(0.2)
            print(f"\r{msg} COMPLETE    ")

        dot_loading("LOADING")
        print ("▬▬▬ Mission 2-2 ▬▬▬")
        print(r'''
                         __    _
                    _wr""        "-q__
                 _dP                 9m_
               _#P                     9#_
              d#@                       9#m
             d##                         ###
            J###                         ###L
            {###K                       J###K
            ]####K      ___aaa___      J####F
        __gmM######_  w#P""   ""9#m  _d#####Mmw__
     _g##############mZ_         __g##############m_
   _d####M@PPPP@@M#######Mmp gm#########@@PPP9@M####m_
  a###""          ,Z"#####@" '######"\g          ""M##m
 J#@"             0L  "*##     ##@"  J#              *#K
 #"               `#    "_gmwgm_~    dF               `#_
7F                 "#_   ]#####F   _dK                 JE
]                    *m__ ##### __g@"                   F
                       "PJ#####LP"
 `                       0######_                      '
                       _0########_
     .               _d#####^#####m__              ,
      "*w_________am#####P"   ~9#####mw_________w*"
          ""9@#####@M""           ""P@#####@M""
''')
        typewriter ("Chemical Factory: Hydrochloric acid (HCl) found leakage with container A11-02.")
        typewriter ("Control: Please use proper chemical to address the leakage.")
        input ("")
        typewriter ("Enter a number that represents your action:\n1. Use Sulfuric Acid (H₂SO₄).\n2. Sodium bicarbonate (NaHCO₃)\n3. Liquid Bromine (Br)")
        negotiation = int(input("Enter a valid number please:"))
        if negotiation == 1:
            print ("Great heat released, hydrogen chloride (HCl) vapor occur, a corrosive vapor. XP-50!!!")
            xp = xp -50
            if xp < 1:
                print ("▬▬▬ GAME LOSE ▬▬▬")
                print (f"XP = {xp}")
                exit()
            
            if xp > 0:
                print ("▬▬▬ GAME OVER ▬▬▬")
                print (f"XP = {xp}")
                exit()
        if negotiation == 2:
            print ("You had successful neutralized the leaked acid! XP + 50")
            xp = xp + 50
            typewriter ("▬▬▬▬ MISSION ACCOMPLISHED ▬▬▬▬")
            print (f"Final XP = {xp}")
            text = "▬▬▬▬ GAME COMPLETED ▬▬▬▬"
            for _ in range(5):
                print(f"\r{text}", end="", flush=True)
                time.sleep(0.3)
                print("\r" + " "*len(text), end="", flush=True)
                time.sleep(0.3)
            print("\rTHANKS FOR PLAYING!")
        if negotiation == 3:
            ("Extremely dangerous corrosive and toxic brown bromine vapor form! Caution!")
            xp = xp -50
            if xp < 1:
                print ("▬▬▬ GAME LOSE ▬▬▬")
                print (f"XP = {xp}")
                exit()
            
            if xp > 0:
                print ("▬▬▬ GAME OVER ▬▬▬")
                print (f"XP = {xp}")
                exit()
