
#Author:        Brandon Waldron
#Program:       Summarizer
#Description:   Takes a file name from user then performs analysis of data to determine winner and stats of game.
import os
os.chdir(os.path.dirname(__file__))



def main():
    '''
    This is the main function it calls 3 other functions
    1. user_file() to prompt user for file
    2. logic_func() to perform analysis of data
    3. print_func() to print out summary of game

    '''

    score1 = 0
    score2 = 0

    num_players = []
    players_scored = []

    teams =[]
    file = user_file()
    players_scored, num_players, teams, score1, score2 = logic_func(file, players_scored, num_players,
                                                                    teams, score1, score2)
    print_func(players_scored, num_players, teams, score1, score2)


def logic_func(file,players_scored,num_players,teams,score1,score2):
    '''

    :param file: Input file
    :param players_scored: The function determines the number of players to score by making them into a running list
    :param num_players: Uses the built in function "in" to determine the total number of players without repeats
    :param teams: Makes a list of total teams
    :param score1: Sums the first team to score total points
    :param score2: Sums the second team to score total points
    :return: returns the param to main function
    '''
    for line in file:
        columns = line.split(' ')
       # print(len(line))
       # print(line)

        players_scored.append(columns[1])
        if columns[1] in num_players:
            pass
        else:
            num_players.append(columns[1])
        if columns[0] in teams:
            pass
        else:
            teams.append(columns[0])
        if columns[0] == teams[0]: # team 1 score sum
            score1 += int(columns[2])
        else: # team 2 score sum
            score2 += int(columns[2])
    return players_scored, num_players, teams, score1, score2

def print_func(players_scored, num_players, teams, score1, score2):
    '''
    This function takes the following param listed below and prints
    out the results of the logic function to the terminal
    :param players_scored: list of every player to score in the game
    :param num_players: Total number of players
    :param teams: Teams competing in game
    :param score1: First teams score
    :param score2: Second teams score

    '''
    first_player_score = num_players[0]
    last_player_score = players_scored[-1]
    if score1 > score2:
        print(teams[0]+' won!')
    else:
        print(teams[-1] + ' won!')
    print(teams[0]+' scored',score1,"points.")
    print(teams[-1]+' scored',score2,"points.")
    print(len(num_players), 'players scored.')
    print(first_player_score+' scored first.')
    print(last_player_score+' scored last.')
def user_file():
    '''
    This function asks the user for the name of file reads the file and returns it to main
    '''

    file_name = input("enter gamelog file name:\n")

    file = open(file_name,'r')

    return file


main()