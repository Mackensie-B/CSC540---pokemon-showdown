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