# -*- coding: utf-8 -*-
class Board:
  def __init__(self,size):
    self.size=size
    self.boardlist=['*']*size**2

  def display_board(self):
    for i in range(self.size):
      print(self.boardlist[(i*self.size):(i*self.size+self.size)])

  def check_board(self,current_position):
    end=True

# horizontal 
#back
    if current_position%self.size>=2:
      if self.boardlist[current_position]==self.boardlist[current_position-1] and self.boardlist[current_position-1]==self.boardlist[current_position-2]:
        if self.boardlist[current_position]=='O':
          print('O win')
        else:
          print('X win')
        end=False

#middle
    if current_position%self.size>0 and current_position%self.size<self.size-1:
      if self.boardlist[current_position]==self.boardlist[current_position-1] and self.boardlist[current_position]==self.boardlist[current_position+1]:
        if self.boardlist[current_position]=='O':
          print('O win')
        else:
          print('X win')
        end=False
 
#front
    if current_position%self.size<self.size-2:
      if self.boardlist[current_position]==self.boardlist[current_position+1] and self.boardlist[current_position+1]==self.boardlist[current_position+2]:
        if self.boardlist[current_position]=='O':
          print('O win')
        else:
          print('X win')
        end=False

# vertical
#down
    if current_position<self.size*(self.size-2):
      if self.boardlist[current_position]==self.boardlist[current_position+self.size] and self.boardlist[current_position]==self.boardlist[current_position+self.size+self.size]:
        if self.boardlist[current_position]=='O':
          print('O win')
        else:
          print('X win')
        end=False

#up
    if current_position>=self.size+self.size:
      if self.boardlist[current_position]==self.boardlist[current_position-self.size] and self.boardlist[current_position]==self.boardlist[current_position-self.size-self.size]:
        if self.boardlist[current_position]=='O':
          print('O win')
        else:
          print('X win')
        end=False
 
#middle
    if current_position>=self.size and current_position<self.size*(self.size-1):
      if self.boardlist[current_position]==self.boardlist[current_position+self.size] and self.boardlist[current_position]==self.boardlist[current_position-self.size]:
        if self.boardlist[current_position]=='O':
          print('O win')
        else:
          print('X win')
        end=False
# left diag 
#top
    if current_position%self.size<self.size-2 and current_position<self.size*(self.size-2):
      if self.boardlist[current_position]==self.boardlist[current_position+self.size+1] and self.boardlist[current_position]==self.boardlist[current_position+self.size+self.size+2]:
        if self.boardlist[current_position]=='O':
          print('O win')
        else:
          print('X win')
        end=False

#middle
    if current_position%self.size>0 and current_position%self.size<self.size-1 and current_position>=self.size and current_position<self.size*(self.size-1):
      if self.boardlist[current_position]==self.boardlist[current_position+self.size+1] and self.boardlist[current_position]==self.boardlist[current_position-self.size-1]:
        if self.boardlist[current_position]=='O':
          print('O win')
        else:
          print('X win')
        end=False
 
#bottom
    if current_position%self.size>=2 and current_position>=self.size+self.size:
      if self.boardlist[current_position]==self.boardlist[current_position-self.size-1] and self.boardlist[current_position]==self.boardlist[current_position-self.size-self.size-2]:
        if self.boardlist[current_position]=='O':
          print('O win')
        else:
          print('X win')
        end=False

# right diag
#top
    if current_position%self.size>=2 and current_position<self.size*(self.size-2):
      if self.boardlist[current_position]==self.boardlist[current_position+self.size-1] and self.boardlist[current_position]==self.boardlist[current_position-self.size-self.size-2]:
        if self.boardlist[current_position]=='O':
          print('O win')
        else:
          print('X win')
        end=False

#middle
    if current_position%self.size>0 and current_position%self.size<self.size-1 and current_position>=self.size and current_position<self.size*(self.size-1):
      if self.boardlist[current_position]==self.boardlist[current_position+self.size-1] and self.boardlist[current_position]==self.boardlist[current_position-self.size+1]:
        if self.boardlist[current_position]=='O':
          print('O win')
        else:
          print('X win')
        end=False
 
#bottom
    if current_position%self.size<self.size-2 and current_position>=self.size+self.size:
      if self.boardlist[current_position]==self.boardlist[current_position-self.size+1] and self.boardlist[current_position]==self.boardlist[current_position-self.size-self.size+2]:
        if self.boardlist[current_position]=='O':
          print('O win')
        else:
          print('X win')
        end=False

        
    
    elif self.boardlist.count('X')+self.boardlist.count('O')>=self.size**2:
      print('No more space, game over now')
      end=False
    return end

class Player:
  def  __init__(self, symbol):
    self.symbol=symbol

  def __interaction(self):
    player_position=None
    while player_position is None:
      try:
        player_position=int(input ("Enter position for player {} ".format(self.symbol)))
      except:
        print("An integer number is needed")
    return player_position

    
      
  def update_board(self,board):
    try: 
      position=self.__interaction()
      if position<0 or position>board.size*board.size-1:
        raise OutOfBoardRange(position,board.size)    
      if board.boardlist[position] =='*':
        board.boardlist[position]=self.symbol
        return position
      else:
        raise PositionTaken(position)
      
    except OutOfBoardRange:
      print(OutOfBoardRange(position,board.size*board.size))
    except PositionTaken:
      print(PositionTaken(position))
    
    
  
  def __str__(self):
    return self.symbol

class GameState:
  def __init__(self, p1, p2):
    self.player_1=Player(p1)
    self.player_2=Player(p2)


  def turn(self, board):
    if board.boardlist.count(self.player_1.symbol)>board.boardlist.count(self.player_2.symbol):
      return self.player_2
    else:
      return self.player_1
  

  def place(self,player, old_board):
    current_position=None
    while(current_position is None):
      current_position=player.update_board(old_board)
    return current_position
        

 
  def game_loop(self, board):
    next=True
    while next:    
      current_player=self.turn(board)
      current_position=self.place(current_player, board)
      board.display_board()
      next=board.check_board(current_position)

class InvalidInputError(Exception):
  pass

class InvalidMenuChoice(InvalidInputError):
  def __init__(self, usrinput,message="is entered, please choose 1 or 2" ):
    self.usrinput=usrinput
    self.message=message
  def __str__(self):
    return f'{self.usrinput} {self.message}'

class InvalidBoardSize(InvalidInputError):
  def __init__(self, usrinput,message="is not greater than or equal to 3, try again" ):
    self.usrinput=usrinput
    self.message=message
  def __str__(self):
    return f'{self.usrinput} {self.message}'

class OutOfBoardRange(InvalidInputError):
  def __init__(self, usrinput, size ,message="is not between 0 and" ):
    self.usrinput=usrinput
    self.size=size
    self.message=message   
  def __str__(self):
    return f'{self.usrinput} {self.message} {self.size-1}'

class PositionTaken(InvalidInputError):
  def __init__(self,position,message="has been placed" ):
    self.position=position
    self.message=message
  def __str__(self):
    return f'{self.position} {self.message}'

while True:
  print ("Welcome to Tic-Tac-Toe")
  print('1:Begin the game\n2: Quit the game ')
  try:
    userinput=int(input('Please choose: '))
    if userinput==2:
      print("Game Over")
      break
    elif userinput==1:
      while True:
        try:
          inputsize=int(input("Enter size of the board, size should be integer >=3: "))
          if inputsize<3:
            raise InvalidBoardSize(inputsize)
          else:
             break
        except InvalidBoardSize:
          print(InvalidBoardSize(inputsize)) 
        except ValueError:
          print("please enter an integer number") 

      newboard=Board(inputsize)
      newboard.display_board()
      newGameState=GameState('X','O')
      newGameState.game_loop(newboard)
    else:
      raise InvalidMenuChoice(userinput)
   
  except InvalidMenuChoice:
    print(InvalidMenuChoice(userinput))
  except ValueError:
    print("please enter an integer number")
