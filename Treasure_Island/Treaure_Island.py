print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print(   r'''   (•_•)            (•_•)
  /|   |\          /|   |\
  / \   \         /   / \
     Right             Left''')
choice1 = input('Which way are you going ? Type left or right\n')
if choice1 == "left":
    print(r'''                          'Xx  xX*,
                          ,*xXXx_xXx
                            _xXXXXXxx*,
                          ,*XXx@x@Xx
                            X @|@@ `x
                            '  ||    '
                               ||
                               ||
                               ||
                               ||
                            /ssssssss.
                      /sssssssSSSSssssssssss.
        /\         /sssssSSSSSSSSSSSSSSSssssssssssss.              
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~''')
    choice2 = input("You have come to lake. There is an island in the middle of the lake.  "
          "type 'wait' to wait for a Boat. "
          "type 'swim' to swim across" )
    print(r'''               ~;
                  ,/|\,
                ,/' |\ \,
              ,/'   | |  \
            ,/'     | |   |
          ,/'       |/    |
        ,/__________|-----' ,
       ___.....-----''-----/
       \                  /
   ~~-~^~^~`~^~`~^^~^~-^~^~^~-~^~^
     ~-^~^-`~^~-^~^`^~^-^~^`^~^-~^''')
    print(r'''       RED               YELLOW                BLUE        
 __________________   __________________   __________________
|                  | |                  | |                  |
|      ______      | |      ______      | |      ______      |
|     |      |     | |     |      |     | |     |      |     |
|     |  []  |     | |     |  []  |     | |     |  []  |     |
|     |      |     | |     |      |     | |     |      |     |
|     |      |     | |     |      |     | |     |      |     |
|     |      |     | |     |      |     | |     |      |     |
|     |      |     | |     |      |     | |     |      |     |
|     |      |     | |     |      |     | |     |      |     |
|     |      |     | |     |      |     | |     |      |     |
|     |      |     | |     |      |     | |     |      |     |
|     |      |     | |     |      |     | |     |      |     |
|     |      |     | |     |      |     | |     |      |     |
|     |      |     | |     |      |     | |     |      |     |
|     |      |     | |     |      |     | |     |      |     |
|     |      |     | |     |      |     | |     |      |     |
|     |______|     | |     |______|     | |     |______|     |
|__________________| |__________________| |__________________|''')
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. "
              "there is house with 3 doors. "
              "One red, one yellow and one blue. "
              "Which color did you choose ?")
        if choice3 == 'red':
            print(r'''      (  .      )
      )           (              )
            .  '   .   '  .  '  .
   (    , )       (.   )  (   ',    )
    .' ) ( . )    ,  ( ,     )   ( .
  ). , ( .   (  ) ( , ')  .' (  ,    )
 (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^''')
            print(" You chose the door which have fire. Game over")
        elif choice3 == 'yellow':
            print(r'''           _.--.
       _.-'_:-'||        ✨✨✨
   _.-'_.-::::'||       YOU WIN! 🎉🏆
.-:'_.-::::::'  ||     GOLDEN TREASURE FOUND!
.'`-.-:::::::'   ||    
/.'`;|:::::::'    ||_     
||   ||::::::'     _.;._'-._  
||   ||:::::'  _.-!oo @.!-._'-.  
\'.  ||:::::.-!()oo @!()@.-'_.|
 '.'-;|:.-'.&$@.& ()$%-'o.'\U||  
   `>'-.!@%()@'@_%-'_.-o _.|'||  
    ||-._'-.@.-'_.-' _.-o  |'||  
    ||=[ '-._.-\U/.-'    o |'||  
    || '-.]=|| |'|      o  |'||  
    ||      || |'|        _| ';
    ||      || |'|    _.-'_.-'
    |'-._   || |'|_.-'_.-'     
     '-._'-.|| |' `_.-'        
         '-.||_/.-'            ✨✨✨''')
            print("You found the treasure, You win")
        elif choice3 == "blue":
            print(r'''             (    )
            ((((()))
            |o\ /o)|     RAAWRRR!!!
            ( (  _')      The Beast has awoken...
             (._.  /\__
            ,\___,/ '  ')
  '.,_,,       \__/'   |
    \_\\_       `----' |
    <___>            _/
     | |----.  ._//_/
    (_(___/  (_)__)   ''')
            print("You have eaten by beasts. Game Over")
        else:
            print("You chose the dooe which never exist. Game over")
    else:
        print(r'''          SPLASH!         SPLASH!         SPLASH!
        🐟     🐟              🐟      🐟            🐟      🐟

          >°))'>     >°))'>         >°))'>     >°))'>
               \       |     ~~~~~      /        |       ~~~~~
               ~\_____/~               ~\______/~
                    😵  <- You, being attacked by trouts!
               /     \                /      \
              /       \              /        \

        "Ahh! The trouts are everywhere!" 🐟💦🐟💦🐟''')
        print("You have been attacked by trouts. Game over!!")
else:
    print(" You have fallen into Hole. Game over")
