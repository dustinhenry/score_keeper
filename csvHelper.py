#!usr/bin/env python3
import csv

FILENAME = "mayIPlayerStats.csv"

def writeFile(players):
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(players)

def readFile():
    try:
        players = []
        with open(FILENAME, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                players.append(row)
        return players
    except FileNotFoundError:
        print("Team data file count not be found.")
        print("You can create a new one if you want.")