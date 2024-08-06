import os 

def clear_screen():
    os.system("cls" if os.name=="nt" else "clear")
class Player:
    def __init__(self):
        self.name=""
        self.symbol=""
    def choose_name(self):
        while True:
            name=input("Enter Your Name (letters only): ")
            if name.isalpha():
                self.name=name
                break
            else:
                print("Invalid Name. Please Enter a valid name containing (letters only): ")
    def choose_symbol(self):
        while True:
            symbol=input(f"{self.name} Please Enter Your symbol (A single letter): ")
            if symbol.isalpha() and len(symbol)==1:
                self.symbol=symbol.upper()
                break
            else:
                print(f"{self.name} Please Enter Your symbol correctly (one letter only !): ")

class Menu:
    def display_main_menu(self):
        print("Welcome to my X-O Game")
        print("1. Start Game")
        print("2. Quit Game")
        while True:
            choice=input("Please choose Your choice 1 or 2 only: ")
            if choice=='1' or choice=='2':
                return choice
            else:
                print("Please Enter 1 or 2 Only")
    def display_endGame_menu(self):
        menu_text="""
        Game Over!
        1. Restart Game
        2. Quit Game
        Enter Your choice 1 or 2 Only
        """
        choice=input(menu_text)
        while True:
            choice=input("Please choose Your choice 1 or 2 only: ")
            if choice=='1' or choice=='2':
                return choice
            else:
                print("Please Enter 1 or 2 Only")

class Board:
    def __init__(self):
        self.board=[str(i) for i in range(1,10)]
    def display_board(self):
        for i in range(0,len(self.board),3):
            print(" | ".join(self.board[i:i+3]))
            if i!=len(self.board)/2:
                print("- "*5)
    def is_valid_move(self,choice):
        return self.board[choice-1].isdigit()
    def update_board(self,choice,symbol):
        if self.is_valid_move(choice):
            self.board[choice-1]=symbol
            return True
        return False
    def reset_board(self):
        self.board=[str(i) for i in range(1,10)]
        
class Game:
    def __init__(self):
        self.players=[Player(),Player()]
        self.menu=Menu()
        self.board=Board()
        self.current_player_index=0
    def start_game(self):
        choice=self.menu.display_main_menu()
        if choice=="1":
            self.setup_player()
            self.play_game()
        else:
            self.quit_game()
    def setup_player(self):
        for player in range(0,len(self.players)):
            print(f"Player {player+1} Enter Your Details: ")
            self.players[player].choose_name()
            self.players[player].choose_symbol()
    def play_game(self):
        while True:
            self.play_turn()
            if self.check_win() or self.check_draw():
                choice=self.menu.display_endGame_menu()
                if choice=='1':
                    self.restart_game()
                else:
                    self.quit_game()
                    break;
    def restart_game(self):
        self.board.reset_board()
        self.current_player_index=0
        self.play_game()


    def check_win(self):
        win_compinations=[
            [0,1,2],[3,4,5],[6,7,8],
            [0,3,6],[1,4,7],[2,5,8],
            [0,4,8],[2,4,6]

        ]
        for combo in win_compinations:
            if self.board.board[combo[0]]==self.board.board[combo[1]]==self.board.board[combo[2]]:
                return True
        return False
    def check_draw(self):
        return all(not cell.isdigit() for cell in self.board.board)
    def play_turn(self):
        player=self.players[self.current_player_index]
        self.board.display_board()
        print(f"{player.name}'s turn ({player.symbol})")
        while True:
            try:
                cell_choice=int(input("choose a cell (1-9): "))
                if 1<=cell_choice<=9 and self.board.update_board(cell_choice,player.symbol):
                    break;
                else:
                    print("Invalid move, try again !")
            except ValueError:
                print("Please Enter a valid number between 1 to 9 .")
        self.switch_player()
    def switch_player(self):
        self.current_player_index=1-self.current_player_index
    def quit_player(self):
        print("Thank You for Playing!")

game=Game()
game.start_game()