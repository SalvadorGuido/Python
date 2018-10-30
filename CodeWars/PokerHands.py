hands = {'High Card'        :1,
         'Pair'             :2,
         'Two Pairs'         :3,
         'Three of a Kind'  :4,
         'Straight'         :5,
         'Flush'            :6,
         'Full House'       :7,
         'Poker'            :8,
         'Straight Flush'   :9,
         'Royal Flush'      :10}

kickers = {'2':2,
           '3':3,
           '4':4,
           '5':5,
           '6':6,
           '7':7,
           '8':8,
           '9':9,
           'T':10,
           'J':11,
           'Q':12,
           'K':13,
           'A':14}

class PokerHand(object):

    RESULT = ["Loss", "Tie", "Win"]

    def __init__(self, hand):
        kicker = 0
        play_card = 0
        hand = ''


    def create_hand(self, hand):
        pass

    def compare_with(self, other):
        pass
hand = "KS AS TS QS JS"
hand2 = "JS JD JC JH AD"
hand3 = "JS JD TC TH AD"

print(hand)
print(max(kickers[hand[0]],kickers[hand[3]],kickers[hand[6]],kickers[hand[9]],kickers[hand[12]]))


def max_kicker(cards):
    return max(kickers[cards[0][0]],kickers[cards[1][0]],kickers[cards[2][0]],kickers[cards[3][0]],kickers[cards[4][0]])


def check_straight(mylist):
    it = (int(x, 16) for x in mylist)
    first = next(it)
    return all(a == b for a, b in enumerate(it, first + 1))


def keep_best_hand(current_hand):
    while len(current_hand) > 1:
        current_hand.pop(0)

def add_kicker(current_hand, cards):
    return current_hand + (max_kicker(cards),)



def createhand(hand):
    current_hand = {}
    possible_hands = []
    card_values = []
    ch = hand.split(' ')
    for card in ch:
        card_values.append(str(kickers[card[0]]))
    card_values.sort()

    for card in ch:
        if card[0] in current_hand:
            current_hand[card[0]] += 1
        else:
            current_hand[card[0]] = 1
    for k,v in current_hand.items():
        if v == 2:
            possible_hands.append(('Pair', kickers[k]))
        if v == 3:
            possible_hands.append(('Three of a Kind', kickers[k]))
        if v == 4:
            possible_hands.append(('Poker', kickers[k]))

    for two in possible_hands:
        if two[0] == 'Pair':
            for three in possible_hands:
                if three[0] == 'Three of a Kind':
                    possible_hands.append(('Full House', three[1]))

    if len(possible_hands) > 1:
        if possible_hands[0][0] == 'Pair' and possible_hands[1][0] == 'Pair':
            possible_hands.append(('Two Pairs', max(possible_hands[0][1], possible_hands[1][1])))

    # print('='*40)
    # if len(possible_hands) > 1:
    #     print(max(possible_hands[0][1], possible_hands[1][1]))
    # print('='*40)


    suit = ch[0][1]
    count = 1
    for card in ch:
        if card[1] != suit:
            break
        if count == 5:
            possible_hands.append(("Flush", max_kicker(ch)))
        count += 1

    if not possible_hands:
        possible_hands.append(("High Card", max_kicker(ch)))

    if check_straight(card_values):
        possible_hands.append(("Straight", max_kicker(ch)))

    if 'Straight' and 'Flush' in possible_hands:
        possible_hands.append("Straight Flush")

    for straight in possible_hands:
        if straight[0] == 'Straight':
            for Flush in possible_hands:
                if Flush[0] == 'Flush':
                    possible_hands.append(('Straight Flush', Flush[1]))

    print(ch)
    print(card_values)
    print(current_hand)
    print(possible_hands)
    keep_best_hand(possible_hands)
    print(possible_hands)
    best_hand = possible_hands[0]
    print(best_hand)
    best_hand = add_kicker(best_hand, ch)
    # print(add_kicker(best_hand, ch))
    print(best_hand)
    return best_hand
createhand(hand)
createhand(hand2)
createhand(hand3)

# runTest("Highest straight flush wins",        "Loss", "2H 3H 4H 5H 6H", "KS AS TS QS JS")
# runTest("Straight flush wins of 4 of a kind", "Win",  "2H 3H 4H 5H 6H", "AS AD AC AH JD")
# runTest("Highest 4 of a kind wins",           "Win",  "AS AH 2H AD AC", "JS JD JC JH 3D")
# runTest("4 Of a kind wins of full house",     "Loss", "2S AH 2H AS AC", "JS JD JC JH AD")
# runTest("Full house wins of flush",           "Win",  "2S AH 2H AS AC", "2H 3H 5H 6H 7H")
# runTest("Highest flush wins",                 "Win",  "AS 3S 4S 8S 2S", "2H 3H 5H 6H 7H")