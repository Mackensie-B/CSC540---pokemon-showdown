# Following this guide for general idea on using a custom player
# https://poke-env.readthedocs.io/en/latest/max_damage_player.html#max-damage-player
import asyncio
from poke_env.player.player import Player
from poke_env.player.random_player import RandomPlayer

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
		
		pass
def minmax():
# List of avilable properties for a pokemon object
	# https://poke-env.readthedocs.io/en/latest/pokemon.html
# move options for min max are to check types and pick best move for the type
# tree branches:
	####? when do we check if we are low on health?
	# check if opponent is low on health
		# low -> best damage move to defeat that pokemon
		# too high
			# check type compatibility
				# opposing type -> choose best damage move against that type
				####? is it possible for us to be at a big enough type 
				##### disadvantage that we would want to switch?
				# neutral type -> choose max damage move 
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