#! usr/bin/env python3
# -*- coding: utf-8 -*-

# Author: Dustin Henry
# Date: 2025-07-05

"""
@file: scoreKeeper.py
@brief: A simple script to keep in game score, highest, lowest and average scores as well as the number of wins and games played.
@version: 1.0
"""

import time
import csvHelper
import Player

def display_menu():
    """Function to display the menu options."""
    print("\n" + "=" * 30)
    print("SCOREKEEPER")
    print("MENU OPTIONS:")
    print(" 1. View Player Stats")
    print(" 2. Play 'May I'")
    print(" 3. Add Player")
    print(" 0. Exit")
    print()

def print_stats(player):
    """Function to display player stats."""
    print()
    print(f"Name: {player.get_player_name()}:")
    print(f"  Wins: {player.get_wins()}")
    print(f"  Games Played: {player.get_games_played()}")
    print(f"  Average Score: {player.get_player_avg()}")
    print(f"  Winning Average: {player.get_winning_avg()}")
    print(f"  High Score: {player.calc_high_score()}")
    print("-" * 30)

def score_edit(playerList):
    """Function to edit player score."""
    while True:
        while True:
            # Prompt user to edit a player's score
            print()
            option = input("Would you like to edit a player's score? (y/n): ").strip().lower()
            if option in ['y', 'yes']:
                break
            elif option in ['n', 'no']:
                print("Moving on to the next round. No score editing will be done.")
                return
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

        # Display player list and prompt for selection
        print()
        print("Select a player to edit their score:")
        for i, player in enumerate(playerList, start=1):
            print(f" {i}. {player.get_player_name()}")
        while True:
            try:
                choice = int(input("Enter player number: "))
                if 1 <= choice <= len(playerList):
                    player = playerList[choice - 1]
                    break
                else:
                    print("Invalid choice, please try again.")
            except ValueError:
                print("Not a valid option. Please enter a number from the list of options.")

        # Confirm player selection and edits player's current score
        print()
        print(f"Editing score for {player.get_player_name()}:")
        print(f"Current Score: {player.get_score()}")
        while True:
            try:
                new_score = int(input("Enter new score: "))
                player.set_score(new_score)
                print(f"Score updated to {player.get_score()}.")
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

def game_option():
    """Prompts user to enter an integer for game option."""
    while True:
        try:
            option = int(input("Enter your choice: "))
            if option in [0, 1, 2, 3]:
               return option
            else:
               print("Invalid choice, please try again.")
        except ValueError:
            print("Not a valid option. Please enter a number from the list of options.")

def display_stats(playerList):
    """Function to display player stats. Takes a list of Player objects."""
    if len(playerList) == 0:
        print("No players found. Please add players first.")
        return
    else:
        print("\n" + "=" * 30)
        print("PLAYER STATS")
        print("-" * 30)
        print("Would you like to view all players or select a specific player?")
        print(" 1. View All Players")
        print(" 2. Select a Player")
        print(" 0. Return to Main Menu")
        print()
        while True:
            try:
                choice = int(input("Enter your choice: "))
                if choice in [0, 1, 2]:
                    break
                else:
                    print("Invalid choice, please try again.")
            except ValueError:
                print("Not a valid option. Please enter a number from the list of options.")

        if choice == 0:
            return
        elif choice == 1:
            print()
            print("All Players Stats:")
            print("-" * 30)
            # Display stats for all players
            if not playerList:
                print("No players found. Please add players first.")
                return
            for player in playerList:
                print_stats(player)
            input("Press Enter to return to the main menu.")
            return
        elif choice == 2:
            print()
            print("Select a player to view their stats:")
            for i, player in enumerate(playerList, start=1):
                print(f" {i}. {player.get_player_name()}")
            while True:
                try:
                    choice = int(input("Enter player number: "))
                    if 1 <= choice <= len(playerList):
                        player = playerList[choice - 1]
                        print_stats(player)
                        input("Press Enter to return to the main menu.")
                        break
                    else:
                        print("Invalid choice, please try again.")
                except ValueError:
                    print("Not a valid option. Please enter a number from the list of options.")  

def add_player(playerList=None):
    """Function to add a new player."""
    if playerList is None:
        playerList = []

    playerName = input("Enter the player's name: ").strip()
    if not playerName:
        print("Player name cannot be empty. Please try again.")
        return

    # Check if player already exists
    for player in playerList:
        if player.get_player_name().lower() == playerName.lower():
            print(f"Player '{playerName}' already exists. Please try again.")
            return

    newPlayer = Player.Player(playerName)
    playerList.append(newPlayer)
    print(f"Player '{playerName}' added successfully.")

    # Write updated player list to file
    playerData = class_to_list(playerList)
    csvHelper.writeFile(playerData)

def class_to_list(playerList):
    """Function to convert player objects to a list of lists for writing to file."""
    playerData = [["Player Name", "Score", "Wins", "Final Score List", "Games Played", "Average Score", "Winning Average"]]
    for player in playerList:
        playerData.append([player.get_player_name(), player.get_score(), player.get_wins(), player.get_final_score_list(), player.get_games_played(), player.get_player_avg(), player.get_winning_avg()])
    return playerData

def list_to_class(playerData):
    """Function to convert a list of lists into Player objects."""
    playerList = []
    if not playerData:
        print("No player data found. Please add players first.")
        return playerList
    
    else:
        playerData = playerData[1:]  # Skip header row
        for data in playerData:
            playerName = data[0]
            score = int(float(data[1]))
            wins = int(float(data[2]))
            finalScoreList = eval(data[3]) if len(data[3]) > 0 else []
            newPlayer = Player.Player(playerName, score, wins, finalScoreList)
            playerList.append(newPlayer)
    return playerList

def split_players(playerFullList, chosenIndices):
    """Function to separate chosen players from the full list."""
    chosenList = []
    notChosenList = []

    for i, player in enumerate(playerFullList):
        if i in chosenIndices:
            chosenList.append(player)
        else:
            notChosenList.append(player)

    return chosenList, notChosenList

def set_rotation(chosenList):
    """Function to set player rotation."""
    while True:
        try:
            print()
            print("Setting dealer rotation...")
            for i, player in enumerate(chosenList, start=1):
                print(f" {i}. {player.name}")

            print()
            order = input("Enter the order of players by their numbers (separated by spaces): ").strip().split()
            order = [int(num) - 1 for num in order if num.isdigit() and 0 < int(num) <= len(chosenList)]
            if len(order) != len(chosenList):
                raise ValueError
            chosenList = [chosenList[i] for i in order]
            break
        except ValueError:
            print("Invalid order input. Try again.")
    return chosenList

def rotate_players(chosenList):
    """Function to rotate players for the next round."""
    return chosenList[1:] + [chosenList[0]]

def mayI(playerFullList):
    """Function to play 'May I' game."""

    # Checks if playerFullList is empty and returns to main menu if so
    if len(playerFullList) == 0:
        print("No players found. Please add players first.")
        return
        
    # If players are already present
    else:
        while True:
            try:
                print()
                print("Players found:")
                for i, player in enumerate(playerFullList, start=1):
                    print(f" {i}. {player.name}")
                print()
                print("Choose players for the game by entering their numbers (separated by spaces):")
                chosenIndices = input("Enter player numbers: ").strip().split()
                chosenIndices = [int(index) - 1 for index in chosenIndices if index.isdigit() and int(index) - 1 < len(playerFullList)]
                if not chosenIndices:
                    print("No valid players selected. Please try again.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter valid player numbers.")
            
        chosenList, notChosenList = split_players(playerFullList, chosenIndices)

    # Game Rounds - Adds scores for each player in each round
    for i in range(7):
        if i == 0:
            print()
            chosenList = set_rotation(chosenList)
            print()
            print("----Round 1 - 2 BOOKS----")
            print()
            print(f"{chosenList[0].name} is the dealer for Round 1.")
            print()
            print("Current Scores:")
            for player in chosenList:
                print(f"{player.name}: {player.score} points")
            print()
            for player in chosenList:
                player.add_score(int(input(f"Enter points for {player.name}: ")))
            score_edit(chosenList)

        elif i == 1:
            print()
            print("----Round 2 - 1 BOOK 1 RUN----")
            print()
            chosenList = rotate_players(chosenList)
            print(f"{chosenList[0].name} is the dealer for Round 2.")
            print()
            print("Current Scores:")
            for player in chosenList:
                print(f"{player.name}: {player.score} points")
            print()
            
            for player in chosenList:
                player.add_score(int(input(f"Enter points for {player.name}: ")))
            score_edit(chosenList)

        elif i == 2:
            print()
            print("----Round 3 - 2 RUNS----")
            print()
            chosenList = rotate_players(chosenList)
            print(f"{chosenList[0].name} is the dealer for Round 3.")
            print()
            print("Current Scores:")
            for player in chosenList:
                print(f"{player.name}: {player.score} points")
            print()
            for player in chosenList:
                player.add_score(int(input(f"Enter points for {player.name}: ")))
            score_edit(chosenList)

        elif i == 3:
            print()
            print("----Round 4 - 3 BOOKS----")
            print()
            chosenList = rotate_players(chosenList)
            print(f"{chosenList[0].name} is the dealer for Round 4.")
            print()
            print("Current Scores:")
            for player in chosenList:
                print(f"{player.name}: {player.score} points")
            print()
            for player in chosenList:
                player.add_score(int(input(f"Enter points for {player.name}: ")))
            score_edit(chosenList)

        elif i == 4:
            print()
            print("----Round 5 - 2 BOOKS 1 RUN----")
            print()
            chosenList = rotate_players(chosenList)
            print(f"{chosenList[0].name} is the dealer for Round 5.")
            print()
            print("Current Scores:")
            for player in chosenList:
                print(f"{player.name}: {player.score} points")
            print()
            for player in chosenList:
                player.add_score(int(input(f"Enter points for {player.name}: ")))
            score_edit(chosenList)

        elif i == 5:
            print()
            print("----Round 6 - 2 RUNS 1 BOOK----")
            print()
            chosenList = rotate_players(chosenList)
            print(f"{chosenList[0].name} is the dealer for Round 6.")
            print()
            print("Current Scores:")
            for player in chosenList:
                print(f"{player.name}: {player.score} points")
            print()
            for player in chosenList:
                player.add_score(int(input(f"Enter points for {player.name}: ")))
            score_edit(chosenList)

        elif i == 6:
            print()
            print("----Round 7 - 3 RUNS----")
            print()
            chosenList = rotate_players(chosenList)
            print(f"{chosenList[0].name} is the dealer for Round 7.")
            print()
            print("Current Scores:")
            for player in chosenList:
                print(f"{player.name}: {player.score} points")
            print()
            for player in chosenList:
                player.add_score(int(input(f"Enter points for {player.name}: ")))
            score_edit(chosenList)

    # Final Score Displays
    print()  
    print("----Final Scores----") 
    print() 
    scoreList = []
    for player in chosenList:
        print(f"{player.name}: {player.score} points")
        scoreList.append(player.score)
    print()

    # Display Winner(s)
    for player in chosenList:
        if player.score == min(scoreList):
            print(f"{player.name} has won 'May I' with {player.score} points!")
            player.add_win()

    # Add final scores to player list and reset scores
    for player in chosenList:
        player.add_final_score_to_list()
        player.reset_score()

    fullPlayerList = chosenList + notChosenList
    playerData = class_to_list(fullPlayerList)
    csvHelper.writeFile(playerData)

def main():
    """Main function to run the score keeper."""
    while True:
        playerList = csvHelper.readFile()
        display_menu()
        choice = game_option()

        if choice == 0:
            print("Exiting SCOREKEEPER. Goodbye!")
            break

        elif choice == 1:
            if not playerList:
                print("No players found. Please add players first.")
                continue
            else:
                display_stats(list_to_class(playerList))

        elif choice == 2:
            mayI(list_to_class(playerList))

        elif choice == 3:
            add_player(list_to_class(playerList))

        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
