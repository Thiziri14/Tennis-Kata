# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 19:13:44 2020

@author: Thiziri BELKHIR
"""

import Tennis as T

playerOne = T.Player()
playerTwo = T.Player()

tennisScore = "Love"

while (T.TennisGame.WinnerIs(T.TennisGame, tennisScore)) == None :
    PlayerOneCurrentScore, PlayerTwoCurrentScore = T.TennisGame.getCurrentScore(playerOne, playerTwo)
    #print(PlayerOneCurrentScore,  PlayerTwoCurrentScore)
    tennisScore = T.TennisGame.getTennisScore(PlayerOneCurrentScore, PlayerTwoCurrentScore)
    #print (tennisScore)  
    
#Final Result
print("Score Player 1:  " + str(PlayerOneCurrentScore) + "  Score Player 2: " + str(PlayerTwoCurrentScore))
print (tennisScore)   
    

