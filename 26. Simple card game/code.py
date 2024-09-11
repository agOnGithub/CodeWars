def winner(deck_steve, deck_josh):
    card_rank = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
    scoreS, scoreJ = 0, 0
    

    for card in zip(deck_steve, deck_josh): 
        scoreS += card_rank.index(card[0]) > card_rank.index(card[1])
        scoreJ += card_rank.index(card[0]) < card_rank.index(card[1])          
     
    if scoreS < scoreJ:
        return "Josh wins " + str(scoreJ) + " to " + str(scoreS)
    elif scoreS > scoreJ:
        return "Steve wins " + str(scoreS) + " to " + str(scoreJ)
    else:
        return "Tie"