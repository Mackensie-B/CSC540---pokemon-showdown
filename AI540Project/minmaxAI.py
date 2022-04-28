# Following this guide for general idea on using a custom player
# https://poke-env.readthedocs.io/en/latest/max_damage_player.html#max-damage-player
# node pokemon-showdown start --no-security

import asyncio
from poke_env.player.player import Player
from poke_env.player.random_player import RandomPlayer
import time

# battle has properties: https://poke-env.readthedocs.io/en/latest/battle.html?highlight=battle_format
	# active_pokemon
	# available_moves
	# available_switches
	# opponent_active_pokemon
	# opponent_team 
	# team

#  Pokemon properties: https://poke-env.readthedocs.io/en/latest/pokemon.html
# move obj: https://poke-env.readthedocs.io/en/latest/move.html
# List of avilable properties for a pokemon object
	# https://poke-env.readthedocs.io/en/latest/pokemon.html
class BattleNode:
	'''	Holds information about the turn in a battle. 
		These nodes are part of a tree that is built by considering 
		all possible options. This tree is then parsed through to 
		find the best choice for the move to make.'''

	def __init__(self, battle, player_turn, parentNode):
		''' player_active = player's active pokemon
			opp_active = opponents active pokemon
			player_turn = true if player turn, false if not, None if root node'''
		self.battle = battle
		self.player_turn = player_turn
		self.parent = parentNode
		self.children = []
		self.move = None
		self.value = None

	def setbattle(self, battle):
		'''	Set the battle object for this node'''
		self.battle = battle

	def getbattle(self):
		return self.battle

	def setPlayerTurn(self, value):
		'''	Set the turn for this node. True for player turn, false for opponent's'''
		self.player_turn = value

	def getPlayerTurn(self):
		return self.player_turn

	def setMove(self, move):
		'''	Set the chosen move for this node'''
		self.move = move

	def getMove(self):
		return self.move

	def setParent(self, parent):
		self.parent = parent

	def getParent(self):
		return self.parent

	def setChildren(self, children):
		self.children = children
	
	def getChildren(self):
		return self.children

	def addChild(self, child):
		self.children.append(child)

	def setValue(self, value):
		'''	Set the value for this node'''
		self.value = value

	def getValue(self):
		return self.value

class minMaxPlayer(Player):
	
	def choose_move(self, battle):
		if battle.available_moves:
			# send in battle object so all properties are available
			rootNode = BattleNode(battle, None, None)
			rootNode = buildTree(rootNode) #send root, returns root node of constructed tree
			best_move = minmax(rootNode, 0) # send in root node(current battle), get chosen move
			
			print("move: ", best_move)
			# From max damage example:
				# Now that we have selected a move, we need 
				# to return a corresponding order, which takes
				# the form of a string. Fortunately, Player 
				# provides a method designed to craft such strings 
				# directly: create_order. It takes a Pokemon 
				# (for switches) or Move object as argument, 
				# and returns a string corresponding to the order.
			return self.create_order(best_move)
		else: 
			# From max damage example:
				# We also have to return an order 
				# corresponding to a random switch if 
				# the player cannot attack. Player objects 
				# incorporate a choose_random_move method, 
				# which we will use if no attacking move is available.
			return self.choose_random_move(battle)
		

def buildTree(node, layerCount):
	'''	Builds a 2 or 3 level tree of possible moves for the current battle state.
		Returns root node which is the current battle state. '''
	if(layerCount >= 3):
		return node #only want 3 layers, so stop making children
	else:
		# Add each available move as a node
		for i in range(0, len(node.getBattle.available_moves)):
			if node.getPlayerTurn == None:
				value = True
			else:
				value = not node.getPlayerTurn
			# Add 1 to layer count
			layerCount += 1
			child = BattleNode(node.getBattle, value, node)
			child.setMove(node.getBattle.available_moves[i])
			# go to next layer of branch
			buildTree(child, layerCount)
			# when it comes back, add to parent
			node.addChild(child)

		# Add node(s) for switch
			# make child
			# call buildTree on child
			# add child to parent

		# return node, should be the root when all the recursive calls come back
		return node

def minmax(node):
	'''	Goes through the battle tree recursively to evaluate the nodes.
		Then chooses a best move and sends that node back to choose_move.'''
	# simple start, returns the first child node
	# return root.getChildren()[0]


	# assign that branch a value
	# # # value based on the predicted amount of damage a move will do. calculate predicted damge 
	# # # 			calculate predicted damge
	# # # 			if the value is above threshold like 0.25*opponents_HP --> +10
	# # # 			between .10 and .25 --> 0
	# # # 			below .10 --> -10
	# # # or if it is a switch, base it on if the current poke type combo 
	# # # 			bad for us (+10), neutral for us (0), good for us (-10)
	# bubble the values by choosing the largest of the children depending on who's turn it is
	# # # 			player turn --> pick larget of children
	# # # 			opponent turn --> pick smallest of children


	### if poke_env.environment.battle.Battle.opponent_active_pokemon == poke_env.environment.battle.Battle.current_hp:
	####	

	if node.battle.available_moves:
		best_move = max(node.battle.available_moves, key = lambda move: move.base_power)

	### If opponent's hp == max damage from ability, run move. Currently needs to account for effectiveness, but should work in mean time
	if node.environment.pokemon.Pokemon.opponent.current_hp == max(node.battle.available_moves, key = lambda move: move.base_power):
		best_move = max(node.battle.available_moves, key = lambda move: move.base_power)
		return node.create_order(best_move)

	type_1 = node.environment.pokemon.Pokemon.type_1
	type_2 = node.environment.pokemon.Pokemon.type_2

	# define types 
	# https://poke-env.readthedocs.io/_/downloads/en/latest/pdf/ page 58
	bug_pokemon = node.environment.pokemon_type.PokemonType == 1
	dark_pokemon = node.environment.pokemon_type.PokemonType == 2
	dragon_pokemon = node.environment.pokemon_type.PokemonType == 3
	electric_pokemon = node.environment.pokemon_type.PokemonType == 4
	fairy_pokemon = node.environment.pokemon_type.PokemonType == 5
	fighting_pokemon = node.environment.pokemon_type.PokemonType == 6
	fire_pokemon = node.environment.pokemon_type.PokemonType == 7
	flying_pokemon = node.environment.pokemon_type.PokemonType == 8
	ghost_pokemon = node.environment.pokemon_type.PokemonType == 9
	grass_pokemon = node.environment.pokemon_type.PokemonType == 10
	ground_pokemon = node.environment.pokemon_type.PokemonType == 11
	ice_pokemon = node.environment.pokemon_type.PokemonType == 12
	normal_pokemon = node.environment.pokemon_type.PokemonType == 13
	poison_pokemon = node.environment.pokemon_type.PokemonType == 14
	psychic_pokemon = node.environment.pokemon_type.PokemonType == 15
	rock_pokemon = node.environment.pokemon_type.PokemonType == 16
	steel_pokemon = node.environment.pokemon_type.PokemonType == 17
	water_pokemon = node.environment.pokemon_type.PokemonType == 18

	#move_1_type = node.environment.move.type
	move_1_type = node.getBattle.available_moves[0].type
	move_2_type = node.getBattle.available_moves[1].type
	move_3_type = node.getBattle.available_moves[2].type
	move_4_type = node.getBattle.available_moves[3].type

	### Goal is to check to see if move_type is super_effective. It is currently defining it as the best move

	# ice and rock effectiveness
	if (type_1 == 12 and type_2 == 16 or type_1 == 16 and type_2 == 12):
	#checkMoves
		# takes 4* damage from fighting and steel
		if (move_1_type == 6 or move_1_type == 17):
			return -20 # best move cause quad superEffective

		elif (move_2_type == 6 or move_2_type == 17):
			return -20
			
		elif (move_3_type == 6 or move_3_type == 17):
			return -20

		elif (move_4_type == 6 or move_1_type == 17):
			return -20

		# takes 2* damage from ground, rock, grass, and water
		elif (move_1_type == 11 or move_1_type == 16 or move_1_type == 10 or move_1_type == 18):
			return -10
		
		elif (move_2_type == 11 or move_2_type == 16 or move_2_type == 10 or move_2_type == 18):
			return -10

		elif (move_3_type == 11 or move_3_type == 16 or move_3_type == 10 or move_3_type == 18):
			return -10

		elif (move_4_type == 11 or move_4_type == 16 or move_4_type == 10 or move_4_type == 18):
			return -10

		# takes 1* damage from bug, ghost, fire, electric, psychic, dragon, dark, and fairy
		elif (move_1_type == 1 or move_1_type == 9 or move_1_type == 7 or move_1_type == 4 or move_1_type == 15 or move_1_type == 3 or move_1_type == 5):
			return 0

		elif (move_2_type == 1 or move_2_type == 9 or move_2_type == 7 or move_2_type == 4 or move_2_type == 15 or move_2_type == 3 or move_2_type == 5):
			return 0

		elif (move_3_type == 1 or move_3_type == 9 or move_3_type == 7 or move_3_type == 4 or move_3_type == 15 or move_3_type == 3 or move_3_type == 5):
			return 0

		elif (move_4_type == 1 or move_4_type == 9 or move_4_type == 7 or move_4_type == 4 or move_4_type == 15 or move_4_type == 3 or move_4_type == 5):
			return 0

		# takes .5 damage from normal, flying, poison, and ice
		elif (move_1_type == 13 or move_1_type == 8 or move_1_type == 14 or move_1_type == 12):
			return 10
		
		elif (move_2_type == 13 or move_2_type == 8 or move_2_type == 14 or move_2_type == 12):
			return 10

		elif (move_3_type == 13 or move_3_type == 8 or move_3_type == 14 or move_3_type == 12):
			return 10

		elif (move_4_type == 13 or move_4_type == 8 or move_4_type == 14 or move_4_type == 12):
			return 10


		### test for Dark Psychic
	if (type_1 == 2 and type_2 == 15 or type_1 == 15 and type_2 == 2):
		if (move_1_type == 1):
			return -20 # best move cause quad superEffective

		if (move_1_type == 5):
			return -10 # 2* superEffective
		
		if (move_1_type == 13 or move_1_type == 6 or move_1_type == 8 or move_1_type == 14 or move_1_type == 11 or move_1_type == 16 or move_1_type == 9 or move_1_type == 17 or move_1_type == 7 or move_1_type == 18 or move_1_type == 10 or move_1_type == 4 or move_1_type == 12 or move_1_type == 3 or move_1_type == 2):
			return 0 # 1* superEffective
		
		if (move_1_type == 15):
			return 100 # immunity


	### Grass bug
	if (type_1 == 10 and type_1 == 1 or type_1 == 1 and type_1 == 10):
		if (move_1_type == 7 or move_1_type == 8):
			return -20
		
		if (move_1_type == 14 or move_1_type == 16 or move_1_type == 1 or move_1_type == 12):
			return -10
		
		if (move_1_type == 13 or move_1_type == 9 or move_1_type == 17 or move_1_type == 15 or move_1_type == 3 or move_1_type == 2 or move_1_type == 5):
			return 0
		
		if (move_1_type == 6 or move_1_type == 18 or move_1_type == 4):
			return 10
		
		if (move_1_type == 11 or move_1_type == 10):
			return 15


	### Grass ice
	if (type_1 == 10 and type_2 == 12 or type_1 == 12 and type_2 == 10):
		if (move_1_type == 7):
			return -20
		if (move_1_type == 6 or move_1_type == 8 or move_1_type == 14 or move_1_type == 16 or move_1_type == 1 or move_1_type == 17):
			return -10

		if (move_1_type == 13 or move_1_type == 9 or move_1_type == 15 or move_1_type == 12 or move_1_type == 3 or move_1_type == 2 or move_1_type == 5):
			return 0

		if (move_1_type == 11 or move_1_type == 18 or move_1_type == 10 or move_1_type == 4):
			return 10

	
	### Bug flying
	if (type_1 == 1 and type_2 == 8 or type_1 == 8 and type_1 == 1):
		if (move_1_type == 16):
			return -20

		if (move_1_type == 8 or move_1_type == 7 or move_1_type == 4 or move_1_type == 12):
			return -10

		if (move_1_type == 13 or move_1_type == 14 or move_1_type == 9 or move_1_type == 17 or move_1_type == 18 or move_1_type == 15 or move_1_type == 3 or move_1_type == 2 or move_1_type == 5):
			return 0

		if (move_1_type == 1):
			return 10

		if (move_1_type == 6 or move_1_type == 10):
			return 20

		if (move_1_type == 11):
			return 100


	### Ice normal
	if (type_1 == 12 and type_2 == 13):
		if (move_1_type == 6):
			return -20
		
		if (move_1_type == 16 or move_1_type == 17 or move_1_type == 7):
			return -10

		if (move_1_type == 13 or move_1_type == 8 or move_1_type == 14 or move_1_type == 11 or move_1_type == 1 or move_1_type == 18 or move_1_type == 10 or move_1_type == 4 or move_1_type == 15 or move_1_type == 3 or move_1_type == 2 or move_1_type == 5):
			return 0

		if (move_1_type == 12):
			return 10

		if (move_1_type == 9):
			return 100



	### Grass psychic
	if (type_1 == 10 and type_2 == 15 or type_1 == 15 and type_1 == 10):
		if (move_1_type == 1):
			return -20
		
		if (move_1_type == 8 or move_1_type == 14 or move_1_type == 9 or move_1_type == 7 or move_1_type == 12 or move_1_type == 2):
			return -10

		if (move_1_type == 13 or move_1_type == 16 or move_1_type == 17 or move_1_type == 3 or move_1_type == 5):
			return 0

		if (move_1_type == 6 or move_1_type == 11 or move_1_type == 18 or move_1_type == 10 or move_1_type == 4 or move_1_type == 15):
			return 10


	### bug normal
		
	
	### Dark rock
	if (type_1 == 2 and type_2 == 16 or type_1 == 16 and type_1 == 2):
		if (move_1_type == 6):
			return -20

		if (move_1_type == 11 or move_1_type == 1 or move_1_type == 17 or move_1_type == 18 or move_1_type == 10 or move_1_type == 5):
			return -10

		if (move_1_type == 16 or move_1_type == 4 or move_1_type == 12 or move_1_type == 3):
			return 0

		if (move_1_type == 13 or move_1_type == 8 or move_1_type == 14 or move_1_type == 9 or move_1_type == 7 or move_1_type == 2):
			return 10
		
		if (move_1_type == 15):
			return 100

		
	### Fire rock
	if (type_1 == 7 and type_2 == 16 or type_1 == 16 and type_2 == 7):
		if (move_1_type == 11 or move_1_type == 18):
			return -20
		
		if (move_1_type == 6 or move_1_type == 16):
			return -10

		if (move_1_type == 9 or move_1_type == 17 or move_1_type == 10 or move_1_type == 4 or move_1_type == 15 or move_1_type == 3 or move_1_type == 2):
			return 0
		
		if (move_1_type == 13 or move_1_type == 8 or move_1_type == 14 or move_1_type == 1 or move_1_type == 12 or move_1_type == 5):
			return 10

		if (move_1_type == 7):
			return 20

	### Normal poison
	if (type_1 == 13 and type_2 == 14):
		if (move_1_type == 11 or move_1_type == 15):
			return -10
		
		if (move_1_type == 13 or move_1_type == 6 or move_1_type == 8 or move_1_type == 16 or move_1_type == 17 or move_1_type == 7 or move_1_type == 18 or move_1_type == 4 or move_1_type == 12 or move_1_type == 3 or move_1_type == 2):
			return 0

		if (move_1_type == 14 or move_1_type == 1 or move_1_type == 10 or move_1_type == 5):
			return 10

		if (move_1_type == 9):
			return 100

	
	### Bug fighting
	if (type_1 == 1 and type_2 == 6 or type_1 == 6 and type_2 == 1):
		if (move_1_type == 8):
			return -20
		
		if (move_1_type == 7 or move_1_type == 15 or move_1_type == 5):
			return -10

		if (move_1_type == 13 or move_1_type == 14 or move_1_type == 16 or move_1_type == 9 or move_1_type == 17 or move_1_type == 18 or move_1_type == 4 or move_1_type == 12 or move_1_type == 3):
			return 0

		if (move_1_type == 6 or move_1_type == 11 or move_1_type == 1 or move_1_type == 10 or move_1_type == 2):
			return 10

	### normal rock
	if (type_1 == 13 and type_2 == 16 or type_1 == 16 and type_2 == 13):
		if (move_1_type == 6):
			return -20
		
		if (move_1_type == 11 or move_1_type == 17 or move_1_type == 18 or move_1_type == 10):
			return -10
		
		if (move_1_type == 16 or move_1_type == 1 or move_1_type == 4 or move_1_type == 15 or move_1_type == 12 or move_1_type == 3 or move_1_type == 2 or move_1_type == 5):
			return 0
		
		if (move_1_type == 13 or move_1_type == 8 or move_1_type == 14 or move_1_type == 7):
			return 10
		
		if (move_1_type == 9):
			return 20
		
	
	### ground grass
	if (type_1 == 11 and type_2 == 10 or type_1 == 10 and type_2 == 11):
		if (move_1_type == 12):
			return -20
		
		if (move_1_type == 8 or move_1_type == 1 or move_1_type == 7):
			return -10
		
		if (move_1_type == 13 or move_1_type == 6 or move_1_type == 14 or move_1_type == 18 or move_1_type == 17 or move_1_type == 9 or move_1_type == 10 or move_1_type == 15 or move_1_type == 3 or move_1_type == 2 or move_1_type == 5):
			return 0
		
		if (move_1_type == 11 or move_1_type == 16):
			return 10

		if (move_1_type == 4):
			return 100

	
	### ground rock
	if (type_1 == 11 and type_2 == 16 or type_1 == 16 and type_2 == 11):
		if (move_1_type == 18 and move_1_type == 10):
			return -20
		
		if (move_1_type == 6 or move_1_type == 11 or move_1_type == 17 or move_1_type == 12):
			return -10
		
		if (move_1_type == 1 or move_1_type == 9 or move_1_type == 15 or move_1_type == 3 or move_1_type == 2 or move_1_type == 5):
			return 0
		
		if (move_1_type == 13 or move_1_type == 8 or move_1_type == 16 or move_1_type == 7):
			return 10
		
		if (move_1_type == 14):
			return 20
		
		if (move_1_type == 4):
			return 100
	
	### Ice flying
	### pass

	if (type_1 == 1 or type_2 == 1):
		if (node.getBattle.available_moves[i]):
			pass

	### if (poke_env.environment.pokemon.Pokemon.type_1)
	if (len(node.getChildren) < 1):
		# This is the last node of a branch
		# Assign it a value
		pass
	
	else:
		# go to end of each branch recursively
		for i in range(0, len(node.getChildren)):
			minmax(node.getChildren[i])
		# Comes back when all children have a value
		# Get value for node from children based on turn
		if node.player_turn:
			maxVal = -9999
			for child in node.getChildren:
				if child.getValue > maxVal:
					maxVal = child.getValue
			node.setValue = maxVal 
		else: #if opponent turn
			minVal = 9999
			for child in node.getChildren:
				if child.getValue < minVal:
					minVal = child.getValue
			node.setValue = minVal 
	
	# if the node is the root (no parent)
	if node.getParent == None:
		# find best child and return their move
		if node.player_turn: # root should always be player turn
			best_move = None
			maxVal = -9999
			for child in node.getChildren:
				if child.getValue > maxVal:
					maxVal = child.getValue
					best_move = child.getMove()
			return best_move
		else: print("Error: root not player turn")


	
	# assigning the best value to the parent

	# Maybe put this step in it's own function and just return the root here
	# loop through root's children to find matching node value
	# store the best move in the root node
	# return root

async def main():
	start = time.time()
	#Create random
	##could also take one of their implementation examples as our opponent so that it is better than just random
	random_player = RandomPlayer(battle_format="gen8randombattle")
	#Create minMaxPlayer
	minmaxPlayer = minMaxPlayer(battle_format="gen8randombattle")
	
	# run for set number of games
	await minmaxPlayer.battle_against(random_player, n_battles=1)

	# print results 
	print(
        "MinMax player won %d / 1 battles [this took %f seconds]"
        % (
            minmaxPlayer.n_won_battles, time.time() - start
        )
    )

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
