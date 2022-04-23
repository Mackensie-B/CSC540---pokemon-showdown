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

	def __init__(self, player_active, opp_active, player_turn, parentNode):
		''' player_active = player's active pokemon
			opp_active = opponents active pokemon
			player_turn = true if player turn, false if not, None if root node'''
		self.player_active = player_active 
		self.opp_active = opp_active
		self.player_turn = player_turn
		self.parent = parentNode
		self.children = []
		self.move = None
	
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

	

class minMaxPlayer(Player):
	
	def choose_move(self, battle):
		if battle.available_moves:
			# send in battle object so all properties are available
			rootNode = buildTree(battle) #send battle, returns root node
			best_node = minmax(rootNode) # send in root node(current battle), get node with chosen move
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
		

def buildTree(battle):
	'''	Builds a 2 or 3 level tree of possible moves for the current battle state.
		Returns root node which is the current battle state. '''
	# simple start, only one choice for testing
	rootNode = BattleNode(battle.active_pokemon, battle.opponent_active_pokemon, None, None)
	print("battle.available_moves: ", battle.available_moves)
	nodeOne = BattleNode(battle.active_pokemon, battle.opponent_active_pokemon, True, rootNode)
	nodeOne.setMove(battle.available_moves[0])	
	rootNode.addChild(nodeOne)
	return rootNode

def minmax(root):
	'''	Goes through the battle tree to evaluate the nodes.
		Then chooses a best move and sends that node back to choose_move.'''
	# simple start, returns the first child node
	return root.getChildren()[0]

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