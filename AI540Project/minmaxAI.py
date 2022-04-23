# Following this guide for general idea on using a custom player
# https://poke-env.readthedocs.io/en/latest/max_damage_player.html#max-damage-player
import asyncio
from poke_env.player.player import Player
from poke_env.player.random_player import RandomPlayer

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
	'''Holds information about the turn in a battle. 
	These nodes are part of a tree that is built by considering 
	all possible options. This tree is then parsed through to 
	find the best choice for the move to make.'''

	def __init__(self, player_active, opp_active, player_turn, parentNode):
		''' player_active = player's active pokemon
			opp_active = opponents active pokemon
			player_turn = true if player turn, false if not'''
		self.player_active = player_active 
		self.opp_active = opp_active
		self.player_turn = player_turn
		self.parent = parentNode
		self.children = []
		self.move 
	
	def setMove(self, move):
		'''Set the chosen move for this node'''
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
		self.children.push(child)

	

class minMaxPlayer(Player):
	pass
	def choose_move(self, battle):
		

		# send in battle object so all properties are available
		tree = buildTree(battle)
		best_node = minmax(tree) # send in tree object, get chosen node
		# make move
		move = best_node.getMove()
		# research move object and how to make a move
		# https://poke-env.readthedocs.io/en/latest/move.html 
		pass

def buildTree(battle):
	'''Builds a 2 or 3 level tree of possible moves for the current battle state.'''
	# simple start, only one choice for testing
	node = BattleNode(battle.active_pokemon, battle.opponent_active_pokemon, True)
	
	pass

def minmax(tree):
	'''Goes through the battle tree to evaluate the nodes.
	Then chooses a best move and sends it back to choose_move.'''

	pass

async def main():

	#Create random
	##could also take one of their implementation examples as our opponent so that it is better than just random
	random_player = RandomPlayer(battle_format="gen8randombattle")
	#Create minMaxPlayer
	minmaxPlayer = minMaxPlayer(battle_format="gen8randombattle")
	
	# run for set number of games

	# print results 
	pass

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())