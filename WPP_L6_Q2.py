import random
class Rock_paper_scissors:
    def __init__(self, num_rounds):
        self.num_rounds = num_rounds
        self.current_round = 0
        self.user_wins = 0
        self.computer_wins = 0
    def get_computer_choice(self):
        choices = ["rock", "paper", "scissors"]
        return random.choice(choices)
    def play_round(self, user_choice):
        self.current_round += 1
        computer_choice = self.get_computer_choice()
        winner = self.determine_winner(user_choice, computer_choice)
        if winner == "user":
            self.user_wins += 1
        elif winner == "computer":
            self.computer_wins += 1
        return user_choice, computer_choice, winner
    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "draw"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            return "user"
        else:
            return "computer"
    def game_over(self):
        return self.current_round >= self.num_rounds or self.user_wins > self.num_rounds // 2 or self.computer_wins > self.num_rounds // 2
    def get_final_winner(self):
      if self.user_wins > self.computer_wins:
        return "user"
      elif self.computer_wins > self.user_wins:
        return "computer"
      else:
        return "draw"
    def display_results(self):
        print(f"\n--- Game Results ---")
        print(f"Rounds played: {self.current_round}")
        print(f"User wins: {self.user_wins}")
        print(f"Computer wins: {self.computer_wins}")
        final_winner = self.get_final_winner()
        if final_winner != "draw":
            print(f"The final winner is: {final_winner}!")
        else:
            print("draw!")
num_rounds = 5  
game = Rock_paper_scissors(num_rounds)

while not game.game_over():
    while True:
      user_choice = input(f"Round {game.current_round + 1}: Enter choice (rock, paper, scissors): ").lower()
      if user_choice in ["rock", "paper", "scissors"]:
        break
      else:
        print("Invalid choice.")
    user_choice, computer_choice, winner = game.play_round(user_choice)
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    print(f"Round winner: {winner}")
game.display_results()