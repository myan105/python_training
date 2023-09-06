#Write a Deck method called deal_hands that takes two parameters, the number of hands 
#and the number of cards per hand. It should create the appropriate number of 
#Hand objects, deal the appropriate number of cards per hand, 
#and return a list of Hands.

def deal_hands(self, num_hands, cards_per_hand):
        if num_hands * cards_per_hand > len(self.cards):
            raise ValueError("Not enough cards in the deck to deal hands.")

        hands = []
        for _ in range(num_hands):
            hand = Hand()
            for _ in range(cards_per_hand):
                card = self.cards.pop()
                hand.add_card(card)
            hands.append(hand)

        return hands