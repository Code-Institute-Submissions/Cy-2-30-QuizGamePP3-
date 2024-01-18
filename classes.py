import gspread
from google.oauth2.service_account import Credentials

class Player:
    """
    Saves the player name as an object to be used every time there is new player
    """
    def __init__(self, name, sheet):
        self.name = name
        self.sheet = sheet
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
        records = self.sheet.get_all_values()
        return self.name in [record[1] for record in records]
        pass

    def save_player_info(self, records, score, question_num, timer_end):
        """
        At the end of the game the statistic is saved
        """
        score_percentage = int(score / question_num * 100)
        new_player = [len(records) + 1, self.name, score, f"{score_percentage}%", f"{timer_end:.2f}"]
        self.sheet.append_row(new_player)
        pass

    #def fetch_all_players(sheet):
        """
        Fetches the player information from google sheets
        """
        #records = sheet.get_all_values()
        #return records
    
    #def get_new_player(self):
        """
        Returns the valid player name
        """
     #   return self.name

       # while len(self.name) <= 3 or not self.name.isalnum() or self.name in scoreboard_names:
        #    if len(player_name) <= 3: 
         #       print("Name must contain at least one number.")
          #  elif not self.name.isalnum():
           #     print("Name must contain both alphabets and numbers")
            #elif self.name in scoreboard_names:
             #   print("Name already exists! Please choose a different name.")
            #self.name = input(f"Please enter your name: ")
         
            #self.name = input(f"Please enter your name: ")   

        #return self.name





#class Statistics:
 #   def __init__(self, name, score, percentage, time, rank):
  #      self.name = name
   #     self.score = score
    #    self.percentage = percentage
     #   self.time = time