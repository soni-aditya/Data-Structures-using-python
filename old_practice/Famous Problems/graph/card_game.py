'''
Question Description:
You are playing a card game. The card game uses 4 decks of cards. Each deck of cards has 27 cards in it. Therefore, the game is played with 4 * 27 = 108 cards, in total.

Each card in a deck is defined by two properties:

The number on the card, which ranges from 1 to 9 inclusive, and
The color of the card, which can be red, blue, or green.
Each deck has every card combination of number and color with no duplicates, which totals 27 unique card combinations per deck. Therefore, the game is played with 4 of each card combination (since there are 4 decks).

The 4 decks are then shuffled together into one mega deck (containing 108 cards).

You are given 12 random cards from the mega deck. You win the game by grouping all 12 of your cards into 4 groups of 3, where each group of 3 cards meets EITHER of the critera:

All 3 cards have both the same color AND number
ex. [RED -1, RED -1, RED-1], [BLUE-2, BLUE-2, BLUE-2])
All 3 cards have the same color, but form a consecutive sequence
ex. [RED -1, RED -2, RED-3], [BLUE-7, BLUE-8, BLUE-9])
Return a boolean value reflecting whether you can win the game.
'''
def check_if_win(deck: list)->bool:
    visited = set()
    hands = []
    
    index = 0
    
    def same_cards(index):
        total = 1
        card = deck[index]
        visited.add(index)
        for i in range(index+1, len(deck)):
            if deck[i]==card:
                total+=1
                visited.add(i)
            if total == 3:
                print(f"same cards -True for index- {index} and visited - {visited}")
                return True
        print(f"same cards -False for index- {index} and visited - {visited}")
        return False
    
    def same_color_cards(index):
        total = 1
        color = deck[index][0]
        number = int(deck[index][1])
        visited.add(index)
        
        first_consec_card = f"{color}{number+1}"
        second_consec_card = f"{color}{number+2}"
        
        done_first = False
        done_sec = False
        
        for i in range(index+1, len(deck)):
            if (not done_first) and (deck[i]==first_consec_card):
                done_first = True
                visited.add(i)
            elif (not done_sec) and (deck[i]==second_consec_card):
                done_sec = True
                visited.add(i)
        
        print(f"same color cards - {done_first and done_sec} for index- {index} and visited - {visited}")
        return done_first and done_sec
        
    while index<len(deck):
        if index in visited:
            index+=1
            continue
        else:
            # checking same color and same number cards
            # also checking consecutive numbers of same color
            if (not same_cards(index)) and (not same_color_cards(index)):
                return False
            index +=1
    return True
    
print(check_if_win(['R1','R4','R4','G5','G6','G7','B1','R2','R3','R4','B2','B3']))
print(check_if_win(['R1','R4','R4','G5','G6','G7','B1','R2','R3','R4','B2','B2']))
print(check_if_win(['R1','R1','R1','R1','R1','R1','R1','R1','R1','R1','R1','R1']))



