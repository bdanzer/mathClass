## Fill in the blank game
    # High score
    # Ask fill in the blank questions
    # Play until you lose/fail

import random
import os

class MathClass:
    HSP = './highscore.py'
    gameOver = False
    score = 0

    def __init__(self):
        ##Set some vars before game
        self.preGame()

        ##Game Starts
        self.startGame()
    
    def preGame(self):
        self.highScore = self.getHighScore()

    def startGame(self):
        if not self.gameOver:
            userInput = self.getUserInput()
            sanitizedInput = self.sanitizeUserInput(userInput)
            self.validateUserInput(sanitizedInput)

            return self.startGame()
        else:
            print('Game Over. The correct answer is {}. Your score was: {} and high score is {}'.format(self.correctAnswer, self.score, self.highScore))

    def getUserInput(self):
        self.firstNumber = random.randint(0, 100)
        self.answer = random.randint(self.firstNumber, 100)

        # print(self.answer - self.firstNumber)
        
        userInput = raw_input("{} + _ = {}: ".format(self.firstNumber, self.answer))

        return userInput

    def sanitizeUserInput(self, userInput):
        try:
            userInput = int(userInput)
        except ValueError:
            userInput = 0
        
        return userInput

    def validateUserInput(self, sanitizedInput):
        self.correctAnswer = self.answer - self.firstNumber

        if sanitizedInput == self.correctAnswer:
            self.score = self.score + 1
        else:
            self.writeHighScore()
            self.gameOver = True   

    def getHighScore(self):
        exists = os.path.isfile(self.HSP)
        if not exists:
            open(self.HSP, "w+")
            return 0
        else:
            highscore = int(open(self.HSP, 'r').read())
            return highscore

    def writeHighScore(self):
        if self.score > self.highScore:
            self.highScore = self.score
            f = open(self.HSP, "w")
            f.write(str(self.score))
            f.close()

MathClass()