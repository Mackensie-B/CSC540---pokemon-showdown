# Following this guide for general idea on using a custom player
# https://poke-env.readthedocs.io/en/latest/max_damage_player.html#max-damage-player
import asyncio
from poke_env.player.player import Player
from poke_env.player.random_player import RandomPlayer
# List of avilable properties for a pokemon object
	# https://poke-env.readthedocs.io/en/latest/pokemon.html
class BattleNode:
	'''Holds information about the turn in a battle. 
	These nodes are part of a tree that is built by considering 
	all possible options. This tree is then parsed through to 
	find the best choice for the move to make.'''
	def __init__(self):
		pass

class minMaxPlayer(Player):
	pass
	def choose_move(self, battle):
		# battle has properties: 
			# active_pokemon
			# available_moves
			# available_switches
			# opponent_active_pokemon
			# opponent_team 
			# team
			# some others 

		# send in battle object so all properties are available
		tree = buildTree(battle)
		move = minmax(tree) # send in tree object
		# make move
		pass

def buildTree(battle):
	'''Builds a 2 or 3 level tree of possible moves for the current battle state.'''
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