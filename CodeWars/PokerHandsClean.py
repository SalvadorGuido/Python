hands = {'High Card'        :1,
         'Pair'             :2,
         'Two Pairs'        :3,
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


def max_kicker(cards):
    return max(kickers[cards[0][0]],kickers[cards[1][0]],kickers[cards[2][0]],kickers[cards[3][0]],kickers[cards[4][0]])


def check_straight(mylist):
    it = (x for x in mylist)
    first = next(it)
    return all(a == b for a, b in enumerate(it, first + 1))


def keep_best_hand(current_hand):
    while len(current_hand) > 1:
        current_hand.pop(0)

def add_kicker(current_hand, cards):
    return current_hand + (max_kicker(cards),)

def add_addition(current_hand, addition):
    return current_hand + (addition,)


class PokerHand(object):

    RESULT = ["Loss", "Tie", "Win"]

    def __init__(self, hand = ''):
        self.hand = self.createhand(hand)[0]
        self.playCard = self.createhand(hand)[1]
        self.kic = self.createhand(hand)[2]
        self.suma = self.createhand(hand)[3]

    def createhand(self, hand):
        current_hand = {}
        possible_hands = []
        card_values = []
        ch = hand.split(' ')
#        print(ch)
        addition = int(kickers[ch[0][0]]) + int(kickers[ch[1][0]]) + int(kickers[ch[2][0]]) + int(kickers[ch[3][0]]) + int(kickers[ch[4][0]])
#        print(addition)
        for card in ch:
            card_values.append(str(kickers[card[0]]))
        # print('='*40)
        # print(card_values)
        # print('='*40)
        card_values = list(map(int, card_values))
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

        suit = ch[0][1]
        count = 1
        for card in ch:
            if card[1] != suit:
                break
            if count == 5:
                possible_hands.append(("Flush", max_kicker(ch)))
            count += 1
        print('possible hands: {}'.format(possible_hands))
        print('Current Hand: {}'.format(card_values))
        if not possible_hands:
            possible_hands.append(("High Card", max_kicker(ch) + card_values[-2]))

        if check_straight(card_values):
            print('='*40)
            print('Straight')
            print('='*40)
            possible_hands.append(("Straight", max_kicker(ch)))

        for straight in possible_hands:
            if straight[0] == 'Straight':
                for Flush in possible_hands:
                    if Flush[0] == 'Flush':
                        possible_hands.append(('Straight Flush', Flush[1]))

        # print(ch)
        # print(card_values)
        # print(current_hand)
        # print(possible_hands)
        keep_best_hand(possible_hands)
        # print(possible_hands)
        best_hand = possible_hands[0]
        # print(best_hand)
        best_hand = add_kicker(best_hand, ch)
        best_hand = add_addition(best_hand,addition)
        # print(add_kicker(best_hand, ch))
        print(best_hand)
        return best_hand
        # self.hand = best_hand[0]
        # self.playCard = best_hand[1]
        # self.kic = best_hand[2]

    def compare_with(self, other):
        if hands[self.hand] > hands[other.hand]:
            print("Win")
            return
        if hands[self.hand] == hands[other.hand]:
            if self.playCard == other.playCard:
                if self.kic == other.kic:
                    if self.suma > other.suma:
                        print('Win')
                        return 'Win'
                    if self.suma < other.suma:
                        print('Loss')
                        return 'Loss'
                    print("Tie")
                    return
                if self.kic > other.kic:
                    print('Win')
                    return 'Win'
            if self.playCard > other.playCard:
                print("Win")
                return "Win"
            else:
                print("Loss")
                return "Loss"
        print('Loss')
        return "Loss"


hand1 = 'KD 6S 9D TH AD'
hand2 = 'JH 8S TH AH QH'

player, opponent = PokerHand(hand1), PokerHand(hand2)
print(player.hand)
player.compare_with(opponent)
