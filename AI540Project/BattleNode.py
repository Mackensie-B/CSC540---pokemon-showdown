import itertools
class BattleNode:
	'''	Holds information about the turn in a battle. 
		These nodes are part of a tree that is built by considering 
		all possible options. This tree is then parsed through to 
		find the best choice for the move to make.'''

	id_iter = itertools.count()

	def __init__(self, battle, player_turn, parentNode):
		''' player_active = player's active pokemon
			opp_active = opponents active pokemon
			player_turn = true if player turn, false if not, None if root node'''
		self.id = next(BattleNode.id_iter)
		self.battle = battle
		self.player_turn = player_turn
		self.parent = parentNode
		self.children = []
		self.move = None
		self.value = None
		self.level = None
		self.damage = None
		self.state = {}
	
	def addChild(self, child):
		self.children.append(child)

	def  __str__ (self):
		return "PT: {0}  lvl: {1} M: {2}  D: {3} S: {5} V: {4}".format("True" if self.player_turn else "False" , self.level, self.move, self.damage, self.value, self.state)
		 