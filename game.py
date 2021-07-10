class tictactoe:
  def __init__(self):
    self.board=[" "for _ in range(9) ]
    self.winner= None

  def print_board(self):
    #creation of row
    for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
      print('|' + '|'.joint(row) +'|')

  @statismeathod
  #|0|1|2|
  def print_board_num():
    for row in [self.board[j*3:(j+1)*3] for j in range(3)]:
      print('|' + '|'.join(row) +'|')

  def available_move(self):
    return[i for i,spot in  enumerate(self.board) if spot==' ']
    #move[]
    #for(i,spot) in enumerate self.board():
      #if spot==' ':
        #move.append(i)
        #return move

  
  def empty_square(self):
    return ' ' in self.board 

  def _num_empty_square():
    return self.board.count(' ')

  def make_move(self,square,letter):
    if self.board[square]==' ':
      self.board[square]= letter
      return True
    return False

    
  def play(game,x_player,o_player,print_game=true):
    if print_game:
      game.print_board_num()

  letter='x'    
  while game.emty_square():
    if letter == 'o':
      square= o_player.get_move(game)
    else:
      square= x_player.get_move(game)

    if game.make_move(square,letter):
      if print_game:
        print(letter+ f'make a move to square {square}')
        game.print_board
        print(' ')#just empty space

      letter='o' if letter=='x' else letter='x'#switching players







