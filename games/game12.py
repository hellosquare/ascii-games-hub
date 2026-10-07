#Third and Final Checkpoint - Ms. Christine
#please make sure you check that player stats are being printed out at every decision - like when the player is losing or adding HP, make sure you print those values out as well. 
#this is in line 148, 165, 170ish... and onwards
#also double check your operators whether they should be plus or minus

import random as r

print("")
print("")

player = input("what is your character name ? ")
health = 50

print("")


print ("==================================")
print("== WELCOME!!" , player , " LET'S START!!!== ")
print ("==================================")


print("")

print(" Here is our backgrond story:")
print("")
print ("In the year 2150, Earth's resources are on the verge of exhaustion.\n Humanity's last hope lies in the ancient alien technology fragments scattered across the edge of the Milky Way. \n You play as an independent star scavenger,\n piloting your modified small craft, the Stardust, \n into the perilous asteroid belt.")

print("----------------------------")
print ("")
print ("this is your goal >>")
print ("")
print ("Control your ship to move up and down, \n collect green crystals for points, and avoid red obstacles. \n The longer you survive, the higher your score.(you need to get 250 crystals to win this game)")
print("")

#VARIABLES - this should be at the very top
round = 1
crystals = 100
hp = 50
s = 0
shield = r.randint ( 0 , 5 )
health_potion = r.randint ( 0 , 5 )

print("Here are your stats, " + player)
print ("hp = " , hp )
print ("crystals = " , crystals )
end = 0

while 1 :
   
    print("----------------------------")


    print("")
    print("")
    print ("Round " , round )
    round += 1

    print ( " your crystals left: " , crystals )
    print ( " your hp left: " , hp )
    print ( " " )
    print("Where do you want to go ?")
    print(" ")


    event = int(input(" 1:shopping || 2:collect crystals || 3:skip this round ") )
    print( " " )
    if event == 1 :
        print( "that is what now you can buy :" )
        print( " " )
        print( " " )
        print ( "we have a: " , shield , " shield (which can help you to avoid getting hurt once) : 25 crystals" )
        print ( "we have b: " , health_potion , " health potion (which can help you to increase HP by 10) : 10 crystals" )
        goods = input ( " which one do you want to buy ?   a or b " )
        if goods == 'a' :
            crystals -= 25
            shield -= 1
            s += 1
            print("""        
______________________________
|                            |
| @@@@@@@@@@@@@@@@@@@@@@@@@@ |
| @                        @ |
| @           /\\          @ | 
| @         {    }         @ |
| @          |  |          @ |
| @          |  |          @ |
| @   ^ -----|  |----- ^   @ |
| @ <                    > @ |
| @   \\/-----|  |-----\\/ @ |
| @          |  |          @ |
| @          |  |          @ |
| @          |  |          @ |
| @          |  |          @ |
| @          |  |          @ |
| @         {    }         @ |
| @           \\/           @ |
 \\ @                      @ /
  \\ @                    @ /
   \\ @                  @ /      
    \\ @                @ /
     \\ @              @ /
      \\ @            @ /
       \\ @@@@@@@@@@@@ /
        ---------------
""")


        elif goods == 'b' :
            crystals -= 10
            health_potion -= 1
            health += 10
            print("""        
   _____
  `.___,'
   (___)
   <   >
    ) (
   /`-.\\
  /     \\
 / _    _\\
:,' `-.' `:
|         |
:         ;
 \\       /
  `.___.' 
                            """)
            print ("")


    elif event == 2 :

            print ( " now you go to collect crystals !!" )
            print ()
            print ()
            print ()
            mine = input ( "you can choose where do you want go: \n 1) normal mine \n 2) The Chaotic Star-Falling Mine ( more dangerous!! but several harvest!!!! )")
            print("")
            x = r.randint ( 1 , 4 )
            if mine == 1 :
                if x > 1 :
            
                    collect = r.randint( 10 , 50 )
                    crystals += collect

                    print ( "  let's go !! you collected " , collect , "crystals !!!!!" )
                
                else :
                    print ( " ohhhh no , space pirates avoid you !! You lose 20 HP ><  ")
                    hp -= 20
                    print("""                                     _
  (  +____________________/\\/\\___ / /|
   .''._____________'._____      / /|/\\
  : () :              :\\ ----\\|    \\ )
   '..'______________.'0|----|      \\
                    0_0/____/        \\
                        |----    /----\\
                       || -\\ --|      \\
                       ||   || ||\\      \\
                        \\____// '|      \\
                                .'/       |
                               .:/        |
                               :/_________|
                                         
                """)
                    if s >= 1 :
                        hp += 20 #should this be lose or minus
                        s -= 1

            else :
                if x > 3 :
                            
                    collect = r.randint( 50 , 1000 )
                    crystals += collect
                
                    print ( "  let's go !! you collect " , collect , "crystals !!!!!" )
                                
                else :
                    print ( " ohhhh no , space pirates avoid you !! You lose 20 HP ><  " ) #this should say HP instead of ph - also is it possible to have pnly 2 random choice - pirates get you or you are safe, you have 3 random choices here so the likelihood of attack is greater
                    hp -= 40
                    print("""        _
   (  +____________________/\\/\\___ / /|
   .''._____________'._____      / /|/\\
  : () :              :\\ ----\\|    \\ )
   '..'______________.'0|----|      \\
                    0_0/____/        \\
                        |----    /----\\
                       || -\\ --|      \\
                       ||   || ||\\      \\
                        \\____// '|      \\
                                .'/       |
                               .:/        |
                               :/_________|
                            
                                """)
                    if s >= 1 :
                        hp += 20 #should this be lose or minus
                        s -= 1
            print("")  

    elif event == 3 :
        print (" you skip this round , nothing happend...")

    if ( crystals >= 250 ) :
        print ("")
        print ("")
        print (" you win !!", player , " !! LET'S GOOOO!"  )
        pass

    if hp <= 0 or round >= 15 :
        print (" you lose" +player + "!!!" )
        

        print("""        _
                     ,.-" "-.,
                    /   ===   \\
                    /  =======  \\
                __|  (o)   (0)  |__      
                / _|    .---.    |_ \\         
                | /.----/ O O \\----.\\ |       
                \\/     |     |     \\/        
                |                   |            
                |                   |           
                |                   |          
                _\\   -.,_____,.-   /_         
            ,.-"  "-.,_________,.-"  "-.,
            /          |       |          \\  
            |           l.     .l           | 
            |            |     |            |
            l.           |     |           .l             
            |           l.   .l           | \\,     
            l.           |   |           .l   \\,    
            |           |   |           |      \\,  
            l.          |   |          .l        |
            |          |   |          |         |
            |          |---|          |         |
            |          |   |          |         |
            /"-.,__,.-"\\   /"-.,__,.-"\"-.,_,.-"  \\
            |            \\ /            |         |
            |             |             |          |
            \\__|__|__|__/ \\__|__|__|__/ \\_|__|__/

    """)
        break   
        print (" you lose" +player + "!!!" )
        break 
