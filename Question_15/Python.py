import sys
import enum
import array
import re

class TeamInfo :
    def __init__(self) :
        self.scoreboard = []
        self.problem_solving_count = 0
        self.penalty_time = 0

class ContestExamine :
    def __init__(self, teams) :
        self.teams = teams

    def contest(self):
        print('')


inputArray = []
while (True) :
    i = input(">")
    if i == 'X' : 
        break
    else :
        inputArray.append(i)