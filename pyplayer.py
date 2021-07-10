import math
import random

class player:
  def __init__(self,letter):
    #weather 'x' or 'O'
    self.letter=letter
  #we want all player to select there next move
  def get_move(self,game):
    pass
  
  
class randomcomputerplayer(player):
  def __init__(self,letter):
    super().__init__(letter)

  def get_move(self,game):
    square = random.choice(game.available_moves())
    return square
    

class humanplayer(player):
  def __init__(self,letter):
    super().__init__(letter)

  def get_move(self,game):
    valid_square= False
    val=None
    while not valid_square:
      square=input(self.letter + '\'s turn.input move(0-8):')
      #we check the corret value by giving the integer
      #if the integer is not in range we return invalid 
      #if the spot is not availbe we return invalid

      try:
        val= int(square)
        if val not in game.available_move():
          raise ValueError
        valid_square= True
      except ValueError:
        print('invalid square try again')
    return val