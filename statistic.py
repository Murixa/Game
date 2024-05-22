class Statistic():

    def __init__(self):
        #инициализация статистики
        self.reset_statistic()
        self.run_game = True
        with open('high_score.txt', 'r') as f:
            self.high_score = int(f.readline())

    def reset_statistic(self):
        #изменения во время игры
        self.guns_left = 2
        self.score = 0
