import gspread
from google.oauth2.service_account import Credentials


SCOPE = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive"
        ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('quizgamepp3') 
ScoreBoard = SHEET.worksheet('gameresults') 
records = ScoreBoard.get_all_values()

class Player:
    """
    Saves the player name as an object to be used every time there is new player
    """
    def __init__(self, name, ScoreBoard):
        self.name = name
        self.ScoreBoard = ScoreBoard
        self.validate_name()
    
    def validate_name(self):
        """
        Returns valid verified 3 charectors
        Returns valid verified number and alphabet
        Returns valid verified player name already nonexistant from Google Sheets
        """
        return (
            self.validate_len()
            and self.validate_alnum()
            and not self.name_in_scoreboard()
        )
        pass
    
    def validate_len(self):
        """
        Checks if the player name has more than 3 charectors
        """
        return len(self.name) > 3

    def validate_alnum(self):
        """
        Checks if the player name has number and alphabet
        """
        return any(char.isalpha() or char.isdigit() for char in self.name)

    def name_in_scoreboard(self):
        """
        Checks if the player name already exist from previous players scoreboard in the Google Sheets
        """
        records = self.ScoreBoard.get_all_values()
        return self.name in [record[1] for record in records]
        pass

    def save_player_info(self, ScoreBoard, score, question_num, timer_end):
        """
        At the end of the game the statistic is saved
        """
        score_percentage = int(score / question_num * 100)
        new_player = [len(records) + 1, self.name, score, f"{score_percentage}%", f"{timer_end:.2f}"]
        self.ScoreBoard.append_row(new_player)
        pass
