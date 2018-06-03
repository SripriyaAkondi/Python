import random
import collections
n=10
total_score_player1=0  
total_score_player2=0
total_score=[None]*2
n=10
flag=0
answer='N'
index=0
 
#This class represents the result of the dice when thrown
class Play:
 
 def __init__(self):
   self.die=["red","yellow","yellow","green","green","green"]
   self.total_score_player=0
  
 # This method describes the result of the roll,total score of the player for the current turn and also if the player wants to continue the game or not.
 # flag variable is set to 1 if there are red dice and none is green.Then the players ends his/her turn and next player plays.
 
 
 def game(self):
    #Use of global variables
    global n
    global total_score
    global flag
    global answer
    global index

    
    values= [random.choice(self.die) for a in range(0,n)]
    scores=Currentscore()
    print("The output of each roll is:",values)
    result=scores.score(values)
    print ("The current score of the player after the roll is :",result)
    self.total_score_player+=result
    print("The total score of the player after the current roll is:",self.total_score_player)

    if(flag==1):
          print("The total score of the player for the current turn :",self.total_score_player)
          total_score.insert(index,self.total_score_player)
          self.total_score_player=0
          n=10
          flag=0
          total=Totalscore()
          total.winner()
          index+=1
          if(index>=2):
                index=0
    else:  
        
        answer=input('Do you want to continue or end the game.Press (Y/N):')
          
        if (answer=='Y'):
                 self.game()
         
         
        else:
           print("The total score of the current player is:",self.total_score_player)
           totalscores=Totalscore()
           total_score.insert(index,self.total_score_player)
           self.total_score_player=0
           n=10
           totalscores.winner()
           index+=1
           if(index>=2):
                    index=0
 
#This class calculates the current scores of the players          
class Currentscore:     
          
#This method calculates the current score of the player
 def score(self,values):
    global flag
    global n
    self.current_score_player=0
    green=values.count("green")
    red=values.count("red")
    yellow=values.count("yellow")
    if green==0 and red>=1:
       print("There is a red dice and none are green")
       print("Your turn ends\n")
       self.current_score_player=0
       flag=1
       n=10
       return self.current_score_player
    elif green>0:
       n-=green
       print("The value of number of dices to roll is:",n)
       self.current_score_player+=green
       if(n<1):
               n=10

       return self.current_score_player
       
    elif yellow>0 and green==0:
             print("You can either roll again or end your turn\n")
             if(n<1):
                   n=10
    return self.current_score_player


#This class calculates the total score of the players after their current roll    
class Totalscore: 
 #This method describes the total score of the players
 def winner(self):
                 global total_score
                 global total_score_player1
                 global total_score_player2
                 global index
                 
                 if(index==0):
                        total_score_player1+=total_score[0]
                 elif(index==1):
                        total_score_player2+=total_score[1]
                        

def main():  
  print("This program allows 2 players to play the dice game Toss Up! game")
  print("Each player rolls 10 dice intially and the player gets points for each die that lands on green")
  print("The program allows the players to continue to play additional games of Toss Up! until they choose to quit." )
  print("It also calculates players total score and determines who wins the game first")
  global total_score_player1
  global total_score_player2
  play=Play()

  for i in range(0,200):
      play.game()
      print("The current score of player1",total_score_player1)
      print("The current score of player2",total_score_player2)
      if(total_score_player1>100):
                 print("Congratulations!!! Player 1 is the winner of the game with a total score of:",total_score_player1)
                 break
      elif(total_score_player2>100):
                  print("Congratulations!!! Player 2 is the winner of the game with a total score of:",total_score_player2)              
                  break

if __name__ == "__main__":
    main()
                
 
     
     
