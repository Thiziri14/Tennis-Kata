# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 19:08:43 2020

@author: Thiziri BELKHIR
"""

class Player:

    def __init__(self):
        self.point = 0



class TennisGame:

    def __init__(self):
        self.winner = None

        
    def getCurrentScore(playerOne, playerTwo):
        point = input("Tapez 1 si le joueur 1 a marqué sinon 2 : ")

        if (point == '1'):
            playerOne.point += 1
    
        if (point == '2'):
            playerTwo.point += 1
 
        return playerOne.point , playerTwo.point  
    

    def getTennisScore(PlayerOneCurrentScore, PlayerTwoCurrentScore ):
        
        if(PlayerOneCurrentScore == PlayerTwoCurrentScore):
            tennisScore = "Equality"
            
        if(PlayerOneCurrentScore == 0 and PlayerTwoCurrentScore == 0):
            tennisScore = "Love"
        if(PlayerOneCurrentScore - PlayerTwoCurrentScore == 1):
            tennisScore = "Player One is the first in the course"
            
        if(PlayerTwoCurrentScore - PlayerOneCurrentScore == 1):
            tennisScore = "Player Two is the first in the course"
            
        if(PlayerOneCurrentScore - PlayerTwoCurrentScore == 2):
            tennisScore = "Player One is the first in the course "
            
        if(PlayerTwoCurrentScore - PlayerOneCurrentScore == 2):
            tennisScore = "Player Two is the first in the course"
    
        if(PlayerOneCurrentScore == 1) and (PlayerTwoCurrentScore == 0):
            tennisScore = "Fifteen - zero"
            
        if(PlayerOneCurrentScore == 2) and (PlayerTwoCurrentScore == 0):
            tennisScore = "Thirty - zero"
            
        if(PlayerOneCurrentScore == 3) and (PlayerTwoCurrentScore == 0):
            tennisScore = "Fourty - zero"
            
        if(PlayerOneCurrentScore == 0) and (PlayerTwoCurrentScore == 1):
            tennisScore = "zero - Fifteen"
            
        if(PlayerOneCurrentScore == 0) and (PlayerTwoCurrentScore == 2):
            tennisScore = "zero - Thirty"
            
        if(PlayerOneCurrentScore == 0) and (PlayerTwoCurrentScore == 3):
            tennisScore = "zero - Fourty "
            
            
        if(PlayerOneCurrentScore > 3 and PlayerTwoCurrentScore > 3):
            if(PlayerOneCurrentScore == PlayerTwoCurrentScore):
                tennisScore = "Deuce"
            
            if(PlayerOneCurrentScore - PlayerTwoCurrentScore == 1):
                tennisScore = "Advantage Player One"
            
            if(PlayerTwoCurrentScore - PlayerOneCurrentScore == 1):
                tennisScore = "Advantage Player Two"
            
        elif (PlayerOneCurrentScore > 3):
            tennisScore = "Player One Win"
        
        elif(PlayerTwoCurrentScore > 3):
            tennisScore =  "Player Two Win"
    
        return tennisScore  
    
    def WinnerIs(player, tennisScore):
        if (tennisScore == "Player One Win"):
            player.winner = "Player One"
        
        elif (tennisScore == "Player Two Win"):
            player.winner = "Player Two"
            
        else :
            player.winner = None
            
        return  player.winner  
    