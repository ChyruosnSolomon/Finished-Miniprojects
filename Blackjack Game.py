import random

# Global Variables for defining the cards.
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
'Queen':10, 'King':10, 'Ace':11}
playing = True

class Card():
	# Creates the cards object.

	def __init__(self,suit,rank):
		# Each card has a specific suit, rank and value.
		self.suit = suit
		self.rank = rank
		self.value = values[rank]

	def __str__(self):
		# Prints out the card.
		return self.rank + ' of ' + self.suit


class Deck():
	# Creates a deck of 52 cards.

	def __init__(self):
		# The list will store all the cards in the deck.
		self.card_deck = []

		for suit in suits:
			for rank in ranks:
				# Creates all the cards and puts them in the deck
				self.card_deck.append(Card(suit,rank))

	def shuffle(self):
		# Shuffles the deck
		random.shuffle(self.card_deck)

	def deal(self):
		# Draws a card from the deck.
		return self.card_deck.pop()


class Hand():
	# Creates the hand of the player.

	def __init__(self):
		# The list will note the cards in each player's hand as well as it's total value.
		self.hand = []
		self.hand_value = 0
		self.ace_count = 0

	def add_cards(self,new_card):
		# Adds cards to the player's hand.
		if new_card.rank == 'Ace':
			# If an ace is added to either player's hand.
			x = 11

			if self.hand_value <= 10:
				# Makes the player choose the value of Ace.
				y = input('Which value do you want to assign this ace? Input "A" for 1 or "B" for 11')

				while y not in ['A','B','a','b']:
					y = input('Invalid input.')

				if y in ['A','a']:
					x = 1

				elif y in ['B','b']:
					x = 11

			else:
				# If the value of the hand is greater than 10, it's value is assigned automatically to 1.
				x = 1

			new_card.value = x

		# Adds the card to the hand of the player, as well as increasing its value.
		self.hand.append(new_card)
		self.hand_value = self.hand_value + new_card.value

	def add_dealer(self,new_card):
		# Adds cards to the dealer's hand.
		if new_card.rank == 'Ace': 
			# If the card that the dealer receives is an ace, the following script is run.
			x = 11
			if self.hand_value <= 10:
				x = 1
			else:
				x = 11

			new_card.value = x

		# Adds the card to the hand of the dealer, as well as increasing its value.
		self.hand.append(new_card)
		self.hand_value = self.hand_value + new_card.value


class Chips():
	# This creates the chip class for the player.

	def __init__(self,player_name):
		# Creates the player's chips and the bet attributes.
		self.player_name = player_name
		self.player_chips = 100
		self.bet = 0

	def win_bet(self):
		# If player wins a bet they get to return their bet back plus get chips based on the amount of their bet.
		self.player_chips = self.player_chips + self.bet
		self.bet = 0

	def lose_bet(self):
		# If player losses a bet they get to return their bet back plus get chips based on the amount of their bet.
		self.player_chips = self.player_chips - self.bet
		self.bet = 0

	def blackjack(self):
		self.player_chips = self.player_chips + (self.bet * 1.5)

	def __str__(self):
		return f"Player {self.player_name}'s money is currently at ₱{self.player_chips}."


def take_bets(money):
	# Asks for bet amount.
	print(f'Your current money is {money.player_chips}.')
	x = input('Input the bet amount.')

	while True:
		# Handles incorrect inputs.
		try:
			x = int(x)
		except ValueError:
			x = input('Please input a numerical value.')
		else:
			if x > money.player_chips:
				x = input('Not enough money, please bet a lower amount.')
			elif x == 0:
				x = input('Please enter a bet amount.')
			else:
				break

	money.bet = x
	print(f'Bet of ₱{x} has been placed.')


def hit_player(deck,player_hand):
	# If the player requests a hit, the dealer adds a card to the player's hand.
	hit_card = deck.deal()
	player_hand.add_cards(hit_card)

	# Displays the player's hand.
	print("Your hand:")
	for card in player_hand.hand:
		print(card)
	

def hit_or_stand(deck,hand):
	# Asks for the player to hit or to stand.
	global playing
	x = input('Will you hit or stand? Input "H" for hit or "S" for stand')

	while not x in ['H','S','h','s']:
		# Handles incorrect inputs.
		x = input('Please input an "H or an "S" for hit or stand.')

	if x in ['H','h']:
		# Player requests to hit.
		playing = True

	elif x in ['S','s']:
		# Player requests to stand.
		playing = False


def dealer_draws(deck,dealer_hand):
	# Adds another card to the dealer's hand.
	dealer_draw = deck.deal()
	dealer_hand.add_dealer(dealer_draw)

	# The first card of the dealer's hand is not displayed.
	dealer_first_card = dealer_hand.hand[0]
	dealer_hand.hand[0] = '*'

	# Display's the dealer's hand and reassigns the first card of the dealer.
	print("Dealer's hand:")
	for card in dealer_hand.hand:
		print(card)
	dealer_hand.hand[0] = dealer_first_card


def dealer_show(dealer_hand):
	# Dealer's hand is shown at the end of a round.
	print(dealer_hand.hand)


def player_busts(player_chips):
	# Call up this function when the player losses a round.
	player_chips.lose_bet()


def player_wins(player_chips):
	# Call up this function when the player wins a round.
	player_chips.win_bet()
	

def player_blackjack(player_chips):
	# Call up this function when the player wins a round with a blackjack.
	player_chips.blackjack()


def dealer_busts(player_chips):
	# Call up this function when the player wins a round.
	player_chips.win_bet()


def dealer_wins(player_chips):
	# Call up this function when the player losses a round.
	player_chips.lose_bet()


def push(player_chips):
	# Call up this function when both the player and the dealer get blackjack.
	player_chips.bet = 0


print('Welcome to the blackjack game!')
player_name = input('Enter your name!')

# Creates the chips of the player.
player_chips = Chips(player_name)

# Records the number of rounds.
round_counter = 1

# Records the high score.
high_score = 0

while True:

	if player_chips.player_chips == 0:
		# Prompts when player losses all of his chips.
		print('Game over! You lost all your chips.')
		player_ask = input("Would you like to keep playing? Input 'Y' for yes or 'N' for a no.")

		while player_ask not in ['Y','N','y','n']:
			player_ask = input("Invalid input! Please input 'Y' if you want to keep playing or 'N' if not.")

		if player_ask in ['Y','y']:
			# The game continues.
			round_counter = 1 

		elif player_ask in ['N','n']:
			# The game ends. The game prints out the high score and the number of rounds that the player lasted.
			print('Thank you for playing! :)')
			print(f'Rounds lasted: {round_counter}')
			print(f'Highest chip score: ₱{high_score}')
			break


	# Records the highest chip score.
	if player_chips.player_chips > high_score:
		high_score = player_chips.player_chips

	# Records the number of rounds that have passed.
	print(f'Round {round_counter}')

	# Creates the deck of the player.
	game_deck = Deck()
	game_deck.shuffle()

	# Creates/resets the player's and dealer's hands for every round.
	player_hand = Hand()
	dealer_hand = Hand()

	# Resets the player's bet.
	push(player_chips)

	# Prompts the player's bet.
	take_bets(player_chips)

	# Gives the player one card.
	hit_player(game_deck,player_hand)

	# Gives one card to the dealer.
	dealer_draws(game_deck,dealer_hand) 

	# Resets conditions for player blackjack, dealer and player bust, and hit or stand prompt.
	player_wins_blackjack = False
	player_bust = False
	dealer_bust = False
	playing = True

	hit_or_stand(game_deck,player_hand)

	while playing:

		hit_player(game_deck,player_hand)

		dealer_draws(game_deck,dealer_hand)

		if player_hand.hand_value > 21:
			# Player busts.
			player_bust = True
			break

		elif dealer_hand.hand_value > 21:
			# Dealer busts.
			dealer_bust = True
			break

		elif (player_hand.hand_value == 21) and (player_hand.hand_value > dealer_hand.hand_value):
			# Player blackjacks.
			player_wins_blackjack = True
			break

		# Asks if the player is to hit or stand.
		hit_or_stand(game_deck,player_hand)

	if player_hand.hand_value < 21:
		# If the player chooses to stand.
		while dealer_hand.hand_value <= 17:
			dealer_draws(game_deck,dealer_hand)

			if dealer_hand.hand_value > 21:
				# Dealer busts.
				dealer_bust = True
				break

	# Shows the player's hand along with its corresponding value.
	print("Player's Hand:")
	for card in player_hand.hand:
		print(card)
	print(f"Player Hand Value: {player_hand.hand_value}")

	# Shows dealer's hand along with its corresponding value
	print("Dealer's Hand:")
	for card in dealer_hand.hand:
		print(card)
	print(f"Dealer Hand Value: {dealer_hand.hand_value}")

	if player_bust:
		# If the player busts:
		print('You busted! You lost this round.')
		player_busts(player_chips)	

	elif dealer_bust:
		# When the dealer busts.
		print('Dealer busted. You win this round.')
		dealer_busts(player_chips)

	elif player_wins_blackjack:
		# If the player gets a blackjack.
		print('You got a blackjack! You win this round.')
		player_blackjack(player_chips)

	elif player_hand.hand_value > dealer_hand.hand_value:
		# If player's hand value is greater than the dealer's:
		print("Your hand is greater than the dealer's. You win this round.")
		player_wins(player_chips)

	elif player_hand.hand_value < dealer_hand.hand_value:
		# If player's hand value is less than the dealer's:
		print("Your hand is less than the dealer's. You lost this round.")
		dealer_wins(player_chips)	

	elif player_hand.hand_value == dealer_hand.hand_value:
		# If player's hand value is less than the dealer's:
		print("Your hand is equal to the dealer's. Tie!")
		push(player_chips)


	# Displays the player's current chip value.
	print(player_chips)

	# Asks if the player wishes to continue.
	player_ask = input("Would you like to keep playing? Input 'Y' for yes or 'N' for a no.")

	while player_ask not in ['Y','N','y','n']:
		player_ask = input("Invalid input! Please input 'Y' if you want to keep playing or 'N' if not.")

	if player_ask in ['Y','y']:
		# The game continues.
		round_counter += 1 

	elif player_ask in ['N','n']:
		# The game ends. The game prints out the high score and the number of rounds that the player lasted.
		print('Thank you for playing! :)')
		print(f'Rounds lasted: {round_counter}')
		print(f'Highest chip score: ₱{high_score}')
		break