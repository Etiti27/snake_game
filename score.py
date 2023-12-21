from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(x=0, y=270)
        self.update_score_board()
        self.hideturtle()
    def update_score_board(self):
        self.write(f'Score {self.score}', align='center', font=('Aria', 24, 'normal'))
    def update_score(self):
        self.score += 2
        self.clear()
        self.update_score_board()
    def game_over(self):
        self.color('white')
        self.penup()
        self.goto(x=0, y=0)
        self.write(f'GAME OVER!', align='center', font=('Aria', 35, 'normal'))
        self.hideturtle()


