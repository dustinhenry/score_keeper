class Player:
    """Class to represent a player."""
    def __init__(self, name, score=0, wins=0, final_score_list=None):
        self.name = name
        self.score = score
        self.wins = wins
        self.final_score_list = final_score_list if final_score_list is not None else []
        self.games_played = len(self.final_score_list)
        self.player_avg = self.calc_avg()
        self.win_avg = self.calc_win_avg()
        self.high_score = self.calc_high_score()
    
    # Methods to calculate averages
    def calc_avg(self):
        """Calculate the player's average score."""
        try:
            avg = round(sum(self.final_score_list) / float(len(self.final_score_list)), 1)
        except ZeroDivisionError:
            avg = 0.0
        return avg
    
    def calc_win_avg(self):
        """Calculate the player's winning average."""
        try:
            win_avg = round(self.wins / float(self.games_played), 3)
        except ZeroDivisionError:
            win_avg = 0
        return win_avg
    
    def calc_high_score(self):
        """Return the highest score from the final score list."""
        if self.final_score_list:
            return int(max(self.final_score_list))
        return 0
    
    # Methods to manage player's score and stats
    def add_score(self, points):
        """Add points to the player's score."""
        self.score += points

    def set_score(self, score):
        """Set the player's score to a specific value."""
        self.score = score

    def reset_score(self):
        """Reset the player's score to zero."""
        self.score = 0

    def add_win(self):
        """Increment the number of wins."""
        self.wins += 1

    def add_final_score_to_list(self):
        """Add the final score to the player's final score list."""
        self.final_score_list.append(self.score)

    # Methods to retrieve player's information
    def get_final_score_list(self):
        """Return the player's final score list."""
        return self.final_score_list

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
        return self.player_avg
    
    def get_winning_avg(self):
        """Return the player's winning average."""
        return self.win_avg
    
    # String representation of the player
    def __str__(self):
        """Return a string representation of the player."""
        return f"Player: {self.name}\n   Wins: {self.wins}\n   Games Played: {self.games_played}\n   Average Score: {self.player_avg}\n   Winning Average: {self.win_avg * 100}%\n   High Score: {self.high_score}"
