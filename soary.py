"""
 =====================================================================
 Auth: Alex Celani
 File: soary.py
 Revn: 02-18-2021  1.0
 Func: Play Sorry! with Emma <3

 TODO: create
       research networking
       research graphics
       comment go()
 =====================================================================
 CHANGE LOG
 ---------------------------------------------------------------------
 02-18-2021: init
             wrote and commented generate(), draw(), and decide()
             wrote go()
             wrote testing while loop
             wrote simple input parsing
             wrote move:, leave:, and swap:

 =====================================================================
"""

# used for drawing cards
import random


def generate():
    global cards
    
    # Start with list of all cards
    cards = list( range( 1, 13 ) ) + ['Sorry!']
    del cards[5]    # take out 6 and 9 cards
    del cards[8]
    cards *= 4      # four of each card
    cards += [1]    # include an extra 1 card

def draw():
    global cards

    # If we're out of cards, announce it and remake the deck
    if len( cards ) is 0:
        print( 'Shuffling!' )
        generate()

    # pick the place of a random card
    index = random.randint( 0, len( cards ) - 1 )
    card = cards[index]     # find card at that place
    
    del cards[index]        # remove that card

    return card             # return that card

def decide( card ):
    dec = [ 'move' ]    # Every card (but Sorry!) makes you move

    # 1's and 2's can also leave home
    if card in [1,2]:
        dec.append( 'leave' )
    elif card is 7:             # 7's can split
        dec.append( 'split' )
    elif card is 11:            # 11's can swap
        dec.append( 'swap' )
    elif card == 'Sorry!':      # Reassign for Sorry!
        dec = [ 'Sorry!' ]

    return dec

def go( old, card ):
    
    # Keep track of old position
    x = old[0]
    y = old[1]

    # Upper Left corner (blue)
    if x is 0:
        if y + card <= 15:
            newX = x
            newY = y + card
        else:
            newX = y + card - 15
            newY = 15
        return (newX, newY)
    # Lower Right corner (green)
    if x is 15:
        if y - card >= 0:
            newX = x
            newY = y - card
        else:
            newX = x + y - card
            newY = 0
        return (newX, newY)

    # Upper Right corner (yellow)
    if y is 15:
        if x + card <= 15:
            newX = x + card
            newY = y
        else:
            newX = 15
            newY = y - ( card - 15 + x )
    # Lower Left corner (red)
    if y is 0:
        if x - card >= 0:
            newX = x - card
            newY = y
        else:
            newX = 0
            newY = card - x

    return (newX, newY)



cards = []      # initialize array of cards
piecesU = { '1':(-1,-1), '2':(-1,-1), '3':(-1,-1), '4':(-1,-1) }
#piecesE = { '1':(-1,-1), '2':(-1,-1), '3':(-1,-1), '4':(-1,-1) }
piecesE = { '1':(-1,-1), '2':(-1,-1), '3':(-1,-1), '4':(6,6) }
generate()      # init deck
    

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
                if not -1 in piecesU[key]:
                    print( 'r' + key + ':', piecesU[key] )
            print()
        if 'swap' in decision:      # if I can swap...
            print( 'swap' )
            # Print the pawns that can swap and their coordinates

            for key in sorted( piecesU.keys() ):
                if not -1 in piecesU[key]:
                    print( 'r' + key + ':', piecesU[key] )
            for i in range(20):
                print( '-', end = '' )
            print( '\nwith' )
            for key in sorted( piecesE.keys() ):
                if not -1 in piecesE[key]:
                    print( 'b' + key + ':', piecesE[key] )
            print()
        if 'split' in decision:
            continue
        if 'leave' in decision:
            print( 'leave' )
            # Print the pawns that can leave
            for key in sorted( piecesU.keys() ):
                if -1 in piecesU[key]:
                    print( 'r' + key + ': home' )
            print()
        if 'Sorry!' in decision:
            print( 'Sorry!' )
            # Print the pawns that can Sorry! a mf
            for key in sorted( piecesU.keys() ):
                if -1 in piecesU[key]:
                    print( 'r' + key + ': home' )
            print()

        # Take user input
        move = input().lower().split(' ')

        # Hitting enter redraws
        if move[0] == '':
            continue

        # If the user types the wrong thing, redraw
        # FIX
        if not move[0] in decision:
            print( 'Bad!' )
            continue

        if 'move' == move[0]:
        # signature
        #   move px
        #       p is the colour pawn -> r, b, y, g
        #       x is the number pawn -> 1, 2, 3, 4
        # examples
        #   move r1
        #   move g3
        
            # Don't let pawns in home "move" and crash the game
            if -1 in piecesU[move[1][1]]:
                print( 'Bad!' )
                continue
            
            newPosition = go( piecesU[move[1][1]], card )
            piecesU.update( { move[1][1]:newPosition } )
            
            for key in sorted( piecesU.keys() ):
                if not -1 in piecesU[key]:
                    print( 'r' + key + ':', piecesU[key] )
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
            piecesU.update( { move[1][1]:piecesE[move[2][1]] } )
            piecesE.update( { move[2][1]:temp } )
            
            for key in sorted( piecesU.keys() ):
                if not -1 in piecesU[key]:
                    print( 'r' + key + ':', piecesU[key] )
        elif 'split' == move[0]:
        # signature
        #   split px1 y1 px2 [y2]
        #       p1 is the   colour pawn -> r, b, y, g
        #       x1 is first number pawn -> 1, 2, 3, 4
        #       x2 is first number pawn -> 1, 2, 3, 4
        #       y1 is the first split
        #       y2 is the second split
        #           if y2 is not given, it will be calculated
        #       y1 + y2 must be 7
        # examples
        #   split r1 3 r2 4 
        #   split r3 1 r1
        
            continue
            print()
        elif 'leave' == move[0]:
        # signature
        #   leave px
        #       p is the colour pawn -> r, b, y, g
        #       x is the number pawn -> 1, 2, 3, 4
        # examples
        #   leave r2
        #   leave g3
        
            piecesU.update( { move[1][1]:(0,0) } )
            
            for key in sorted( piecesU.keys() ):
                if -1 in piecesU[key]:
                    print( 'r' + key + ': home' )
                else:
                    print( 'r' + key + ':', piecesU[key] )
            print()
        elif 'Sorry!' == move[0]:
        # signature
        #   sorry px [p2x2]
        #       p  is the other colour pawn -> r, b, y, g
        #       x  is the other number pawn -> 1, 2, 3, 4
        #       p2 is the users colour pawn -> 4, b, y, g
        #       x2 is the users number pawn -> 1, 2, 3, 4
        # examples
        #   sorry r2
        #   sorry r2 g3
        
            for key in sorted( piecesU.keys() ):
                if -1 in piecesU[key]:
                    print( 'r' + key + ': home' )
            print()
            
except KeyboardInterrupt:
    print( 'Goodbye!' )

