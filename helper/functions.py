"""
 =====================================================================
 Auth: Alex Celani
 File: functions.py
 Revn: 06-08-2021  1.0
 Func: Helper functions for Sorry!

 TODO: create
 =====================================================================
 CHANGE LOG
 ---------------------------------------------------------------------
 06-08-2021: init
 06-11-2021: added import random for card generation

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

    cards[3] *= -1  # make 4 a backwards 4
    
    cards *= 4      # four of each card
    cards += [1]    # include an extra 1 card

    return cards




def draw():
    global cards

    # If we're out of cards, announce it and remake the deck
    if len( cards ) == 0:
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
    elif card == 7:             # 7's can split
        dec.append( 'split' )
    elif card == 11:            # 11's can swap
        dec.append( 'swap' )
    elif card == 'Sorry!':      # Reassign for Sorry!
        dec = [ 'sorry' ]

    return dec




def go( old, card ):
    # the idea here is that there are 60 spaces on the board
    # each number maps to a space on the board

    # combine old position with drawn card
    new = card + old
    # this line makes the modulus 60 work for wrapping around negative
    new += 60 if card < 0 and abs( card ) > old else 0
    # modulus 60 (60 spaces on board)
    new %= 60

    return new



