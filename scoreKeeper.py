#! usr/bin/env python3
# -*- coding: utf-8 -*-

# Author: Dustin Henry
# Date: 2025-07-05

"""
@file: scoreKeeper.py
@brief: A simple script to keep in game score, highest, lowest and average scores as well as the number of wins and games played.
@version: 1.0
"""

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
    print()
    if len(playerList) == 0:
        print("No players found. Please add players first.")
        return
    else:
        print()
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
                print(f"Name: {player.get_player_name()}")
                print(f"  Score: {player.get_score()}")
                print(f"  Wins: {player.get_wins()}")
                print(f"  Final Scores: {player.get_final_score_list()}")
                print(f"  Games Played: {player.get_games_played()}")
                print(f"  Average Score: {player.get_player_avg()}")
                print(f"  Winning Average: {player.get_winning_avg()}")
                print(f"  High Score: {player.calc_high_score()}")
                print("-" * 30)
            input("Press Enter to return to the main menu.")
            return
        elif choice == 2:
            print("Select a player to view their stats:")
            for i, player in enumerate(playerList, start=1):
                print(f" {i}. {player.get_player_name()}")
            while True:
                try:
                    choice = int(input("Enter player number: "))
                    if 1 <= choice <= len(playerList):
                        player = playerList[choice - 1]
                        print(f"Stats for {player.get_player_name()}:")
                        print(f"  Score: {player.get_score()}")
                        print(f"  Wins: {player.get_wins()}")
                        print(f"  Games Played: {player.get_games_played()}")
                        print(f"  Average Score: {player.get_player_avg()}")
                        print(f"  Winning Average: {player.get_winning_avg()}")
                        print(f"  High Score: {player.calc_high_score()}")
                        print("-" * 30)
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
    playerData = []
    for player in playerList:
        playerData.append([player.get_player_name(), player.get_score(), player.get_wins(), player.get_final_score_list()])
    return playerData

def list_to_class(playerData):
    """Function to convert a list of lists back to Player objects."""
    playerList = []
    if not playerData:
        print("No player data found. Please add players first.")
        return playerList
    
    else:
        for data in playerData:
            playerName = data[0]
            score = float(data[1])
            wins = float(data[2])
            finalScoreList = eval(data[3]) if len(data) > 0 else []
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

def mayI(playerFullList):
    """Function to play 'May I' game."""

    # Checks if playerFullList is empty and returns to main menu if so
    if len(playerFullList) == 0:
        print("No players found. Please add players first.")
        return
        
    # If players are already present
    else:
        print("Players found:")
        for i, player in enumerate(playerFullList, start=1):
            print(f" {i}. {player.name}")

        print("Choose players for the game by entering their numbers (separated by spaces):")
        while True:
            try:
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
            print("")
            print("----Round 1 - 2 BOOKS----")
            print("")
            print("Current Scores:")
            for player in chosenList:
                print(f"{player.name}: {player.score} points")
            print("")
            for player in chosenList:
                player.add_score(float(input(f"Enter points for {player.name}: ")))

        elif i == 1:
            print("")
            print("----Round 2 - 1 BOOK 1 RUN----")
            print("")
            print("Current Scores:")
            for player in chosenList:
                print(f"{player.name}: {player.score} points")
            print("")
            for player in chosenList:
                player.add_score(float(input(f"Enter points for {player.name}: ")))

        elif i == 2:
            print("")
            print("----Round 3 - 2 RUNS----")
            print("")
            print("Current Scores:")
            for player in chosenList:
                print(f"{player.name}: {player.score} points")
            print("")
            for player in chosenList:
                player.add_score(float(input(f"Enter points for {player.name}: ")))

        elif i == 3:
            print("")
            print("----Round 4 - 3 BOOKS----")
            print("")
            print("Current Scores:")
            for player in chosenList:
                print(f"{player.name}: {player.score} points")
            print("")
            for player in chosenList:
                player.add_score(float(input(f"Enter points for {player.name}: ")))

        elif i == 4:
            print("")
            print("----Round 5 - 2 BOOKS 1 RUN----")
            print("")
            print("Current Scores:")
            for player in chosenList:
                print(f"{player.name}: {player.score} points")
            print("")
            for player in chosenList:
                player.add_score(float(input(f"Enter points for {player.name}: ")))

        elif i == 5:
            print("")
            print("----Round 6 - 2 RUNS 1 BOOK----")
            print("")
            print("Current Scores:")
            for player in chosenList:
                print(f"{player.name}: {player.score} points")
            print("")
            for player in chosenList:
                player.add_score(float(input(f"Enter points for {player.name}: ")))

        elif i == 6:
            print("")
            print("----Round 7 - 3 RUNS----")
            print("")
            print("Current Scores:")
            for player in chosenList:
                print(f"{player.name}: {player.score} points")
            print("")
            for player in chosenList:
                player.add_score(float(input(f"Enter points for {player.name}: ")))

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
