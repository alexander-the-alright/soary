"""
 =====================================================================
 Auth: Alex Celani
 File: soary.py
 Revn: 06-11-2021  1.2
 Func: Play Sorry! with Emma <3

 TODO: COMMENT
       research networking
       research graphics
       make test folder
       unify prompts
       collision detection
 =====================================================================
 CHANGE LOG
 ---------------------------------------------------------------------
 02-18-2021: init
             wrote and commented generate(), draw(), and decide()
             wrote go()
             wrote testing while loop
             wrote simple input parsing
             wrote move:, leave:, and swap:
 06-08-2021: simplified go() CONSIDERABLY
             commented go()
             changed Sorry! command to sorry
 06-11-2021: wrote split() and split:
             changed piecesE to piecesO (enemy to opponent)

 =====================================================================
"""

from helper.functions import *


start = 'start'
home = 'home'

user = 'r'
opponent = 'b'

cards = generate()      # init deck of cards
piecesU = { '1':start, '2':start, '3':start, '4':start }
piecesO = { '1':start, '2':start, '3':start, '4':20 }


try:
    # Test loop
    while True:
        
        card = draw()               # Draw a card
        print( card )               # Show the card
        decision = decide( card )   # What can I do with the card?
        
        if 'move' in decision:      # if I can move...

            print( 'move' )
            # Print the pawns that can move and their coordinates
            
            for key in sorted( piecesU.keys() ):
                if not piecesU[key] is start:
                    print( user + key + ':', piecesU[key] )
            print()
            
        if 'swap' in decision:      # if I can swap...

            print( 'swap' )
            # Print the pawns that can swap and their coordinates
            for key in sorted( piecesU.keys() ):
                if not piecesU[key] is start:
                    print( user + key + ':', piecesU[key] )
                    
            for i in range(20):
                print( '-', end = '' )
                
            print( '\nwith' )
            for key in sorted( piecesO.keys() ):
                if not piecesO[key] is start:
                    print( opponent + key + ':', piecesO[key] )
            print()
            
        if 'split' in decision:

            print( 'split' )
            # Print the pawns that can move and their coordinates
            
            for key in sorted( piecesU.keys() ):
                if not piecesU[key] is start:
                    print( user + key + ':', piecesU[key] )
            print()
        
        if 'leave' in decision:
            
            print( 'leave' )
            
            # Print the pawns that can leave
            for key in sorted( piecesU.keys() ):
                if piecesU[key] is start:
                    print( user + key + ': start' )
            print()
            
        if 'sorry' in decision:

            print( 'sorry' )
            
            # Print the pawns that can Sorry! a mf
            for key in sorted( piecesU.keys() ):
                if piecesU[key] is start:
                    print( user + key + ': start' )
                    
            for i in range(20):
                print( '-', end = '' )
            print()
            
            for key in sorted( piecesO.keys() ):
                if not piecesO[key] is start:
                    print( opponent + key + ':', piecesO[key] )

            print()

        # Take user input
        move = input().lower().split(' ')

        # Hitting enter redraws
        if move[0] == '':
            continue

        # If the user types the wrong thing, redraw
        # FIX
        if not move[0] in decision:
            print( 'Bad!\n' )
            continue

        if 'move' == move[0]:
        # signature
        #   move px
        #       p is the colour pawn -> r, b, y, g
        #       x is the number pawn -> 1, 2, 3, 4
        # examples
        #   move r1
        #   move g3
        
            # Don't let pawns in start "move" and crash the game
            if piecesU[move[1][1]] is start:
                print( 'Bad!' )
                continue
            
            newPosition = go( piecesU[move[1][1]], card )
            piecesU.update( { move[1][1]:newPosition } )
            
            for key in sorted( piecesU.keys() ):
                if not piecesU[key] is start:
                    print( user + key + ':', piecesU[key] )
            print()
        elif 'swap' == move[0]:
        # signature
        #   swap p1x1 p2x2
        #       p1 is users colour pawn -> r, b, y, g
        #       x1 is users number pawn -> 1, 2, 3, 4
        #       p2 is other colour pawn -> r, b, y, g
        #       x2 is other number pawn -> 1, 2, 3, 4
        # examples
        #   swap r1 b2
        #   swap g3 y3

            temp = piecesU[move[1][1]]
            piecesU.update( { move[1][1]:piecesO[move[2][1]] } )
            piecesO.update( { move[2][1]:temp } )
            
            for key in sorted( piecesU.keys() ):
                if not piecesU[key] is start:
                    print( user + key + ':', piecesU[key] )
        elif 'split' == move[0]:
        # signature
        #   split px1 y1 px2 [y2]
        #       p  is the   colour pawn -> r, b, y, g
        #       x1 is first number pawn -> 1, 2, 3, 4
        #       x2 is first number pawn -> 1, 2, 3, 4
        #       y1 is the first split
        #       y2 is the second split
        #           if y2 is not given, it will be calculated
        #       y1 + y2 must be 7
        # examples
        #   split r1 3 r2 4 
        #   split r3 1 r1
        

            newPosition1 = go( piecesU[move[1][1]], int( move[2] ) )
            piecesU.update( { move[1][1]: newPosition1 } )
            

            newPosition2 = go( piecesU[move[3][1]], 7 - int( move[2] ) )
            piecesU.update( { move[3][1]: newPosition2 } )
            
            print()

            
        elif 'leave' == move[0]:
        # signature
        #   leave px
        #       p is the colour pawn -> r, b, y, g
        #       x is the number pawn -> 1, 2, 3, 4
        # examples
        #   leave r2
        #   leave g3
        
            piecesU.update( { move[1][1]:0 } )
            
            for key in sorted( piecesU.keys() ):
                if piecesU[key] is start:
                    print( user + key + ': start' )
                else:
                    print( user + key + ':', piecesU[key] )
            print()
        elif 'sorry' == move[0]:
        # signature
        #   sorry px [p2x2]
        #       p  is the other colour pawn -> r, b, y, g
        #       x  is the other number pawn -> 1, 2, 3, 4
        #       p2 is the users colour pawn -> r, b, y, g
        #       x2 is the users number pawn -> 1, 2, 3, 4
        # examples
        #   sorry r2
        #   sorry r2 g3

            position = piecesO[move[2][1]]
            piecesU.update( { move[1][1]:position } )
            piecesO.update( { move[2][1]:start } )

            
            for key in sorted( piecesU.keys() ):
                print( user + key + ':', piecesU[key] )
                
            print()

            for key in sorted( piecesO.keys() ):
                print( opponent + key + ':', piecesO[key] )
                
            print()
            
except KeyboardInterrupt:
    print( 'Goodbye!' )

