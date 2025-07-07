class Player:
    """Class to represent a player."""
    def __init__(self, name, score=0, wins=0, finalScoreList=None):
        self.name = name
        self.score = score
        self.wins = wins
        self.finalScoreList = finalScoreList if finalScoreList is not None else []
        self.games_played = len(self.finalScoreList)
        self.playerAvg = self.calcAvg()
        self.winningAvg = self.calcWinAvg()
        self.highScore = self.highScore()
    
    # Methods to calculate averages
    def calcAvg(self):
        """Calculate the player's average score."""
        try:
            avg = round(sum(self.finalScoreList) / len(self.finalScoreList), 3)
        except ZeroDivisionError:
            avg = 0.0
        return avg
    
    def calcWinAvg(self):
        """Calculate the player's winning average."""
        try:
            win_avg = round(self.wins / self.games_played, 3)
        except ZeroDivisionError:
            win_avg = 0.0
        return win_avg
    
    def highScore(self):
        """Return the highest score from the final score list."""
        if self.finalScoreList:
            return max(self.finalScoreList)
        return 0
    
    # Methods to manage player's score and stats
    def add_score(self, points):
        """Add points to the player's score."""
        self.score += points

    def reset_score(self):
        """Reset the player's score to zero."""
        self.score = 0

    def add_win(self):
        """Increment the number of wins."""
        self.wins += 1

    def add_final_score_to_list(self):
        """Add the final score to the player's final score list."""
        self.finalScoreList.append(self.score)

    # Methods to retrieve player's information
    def get_final_score_list(self):
        """Return the player's final score list."""
        return self.finalScoreList

    def get_player_name(self):
        """Return the player's name."""
        return self.name

    def get_score(self):
        """Return the player's score."""
        return self.score

    def get_wins(self):
        """Return the number of wins."""
        return self.wins

    def get_games_played(self):
        """Return the number of games played."""
        return self.games_played
    
    def get_player_avg(self):
        """Return the player's average score."""
        return self.playerAvg
    
    def get_winning_avg(self):
        """Return the player's winning average."""
        return self.winningAvg
    
    # String representation of the player
    
    def __str__(self):
        """Return a string representation of the player."""
        return f"Player: {self.name}\n   Wins: {self.wins}\n   Games Played: {self.games_played}\n   Average Score: {self.playerAvg}\n   Winning Average: {self.winningAvg}\n   High Score: {self.highScore}"
