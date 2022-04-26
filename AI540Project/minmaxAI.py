# Following this guide for general idea on using a custom player
# https://poke-env.readthedocs.io/en/latest/max_damage_player.html#max-damage-player
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
			best_node = minmax(rootNode, 0) # send in root node(current battle), get root node with the chosen move stored
			# make move
			move = best_node.getMove()
			print("move: ", move)
			# From max damage example:
				# Now that we have selected a move, we need 
				# to return a corresponding order, which takes
				# the form of a string. Fortunately, Player 
				# provides a method designed to craft such strings 
				# directly: create_order. It takes a Pokemon 
				# (for switches) or Move object as argument, 
				# and returns a string corresponding to the order.
			return self.create_order(move)
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
	if (len(node.getChildren) < 1):
		# This is the last node of a branch
		pass
	
	else:
		# go to end of each branch recursively
		for i in range(0, len(node.getChildren)):
			minmax(node.getChildren[i])
			# Comes back when all children have a value
			# Get value for node from children
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
