import random

# Global Variables for defining the cards.
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11,
'Queen':12, 'King':13, 'Ace':14}


class Card():
	
	def __init__(self,suit,rank):
		# For each card there is a suit and a rank = value.
		self.suit = suit
		self.rank = rank
		self.value = values[rank]

	def __str__(self):
		# String method, returning the rank of a card along its suit.
		return self.rank + ' of ' + self.suit


class Deck():

	def __init__(self):
		# Creates a new deck. Note: This only happens once when a new deck is being made.
		self.all_cards = []

		for suit in suits:
			for rank in ranks:
				# Creates a deck from the 52 cards.
				self.all_cards.append(Card(suit,rank))

	def shuffle(self):
		# Shuffles the deck.
		random.shuffle(self.all_cards)

	def deal_card(self):
		# Remove one card from the deck to be distributed to one player.
		return self.all_cards.pop()


class Player():

	def __init__(self,name):
		# Defines the player along with his/her empty starting deck.
		self.name = name
		self.player_cards = []

	def deal_one(self):
		# Method of removing a card from the top of a player's deck.
		return self.player_cards.pop(0)

	def add_cards(self,new_cards):
		if type(new_cards) == type([]):
			self.player_cards.extend(new_cards)
		else:
			self.player_cards.append(new_cards)

	def __str__(self):
		return f'Player {self.name} has {len(self.player_cards)} cards.'


# Crates the instance of two players and a deck.
new_deck = Deck()
new_deck.shuffle()
player_one = Player('One')
player_two = Player('Two') 

# Distributes the 52 cards of the deck to each player.
for x in range(26):
	player_one.add_cards(new_deck.deal_card())
	player_two.add_cards(new_deck.deal_card())

# Boolean while the game is still going on.
game_on = True
round_num = 0

# For loop while there is no winner.
while game_on:

	round_num += 1
	print(f'Round: {round_num}')

	# Checks if either players have run out of cards, ending the game.
	if len(player_one.player_cards) == 0:
		print('Player One is out of cards! Player Two wins!')
		game_on = False
		break

	elif len(player_two.player_cards) == 0:
		print('Player Two is out of cards! Player One wins!')
		game_on = False
		break

	else:
		pass

	# Start a new round
	player_one_hand = []
	player_one_hand.append(player_one.deal_one())

	player_two_hand = []
	player_two_hand.append(player_two.deal_one())

	at_war = True

	# While the game is unresolved.
	while at_war:
		# Prints the card in which each player goes to war with.
		print(f'Player One goes to war with {player_one_hand[-1]}')
		print(f'Player Two goes to war with {player_two_hand[-1]}')

		if player_one_hand[-1].value > player_two_hand[-1].value:
			print('Player One wins this round.')
			# Return the cards player one played in his hand and takes the cards player two played in hand.
			player_one.add_cards(player_one_hand)
			player_one.add_cards(player_two_hand)

			at_war = False

		elif player_one_hand[-1].value < player_two_hand[-1].value:
			print('Player Two wins this round.')
			# Return the cards player two played in his hand and takes the cards player one played in hand.
			player_two.add_cards(player_one_hand)
			player_two.add_cards(player_two_hand)

			at_war = False

		else:
			# If the value of each card that was played was of equal value.
			print('At War!')

			if len(player_one.player_cards) < 5:
				# If player one does not have enough cards to present for a war, player one loses.
				print('Player One is out of cards for a war! Player Two wins!')
				game_on = False
				break	

			elif len(player_two.player_cards) < 5:
				# If player two does not have enough cards to present for a war, player two loses.
				print('Player Two is out of cards for a war! Player One wins!')
				game_on = False
				break

			else:
				# Each player plays 5 additional cards to their hand.
				for num in range(5):
					player_one_hand.append(player_one.deal_one())
					player_two_hand.append(player_two.deal_one())
