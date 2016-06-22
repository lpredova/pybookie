import os
import random


class Evaluator:
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))

    path = BASE_DIR + '/client/results'

    def __init__(self):
        pass

    @staticmethod
    def find_result(data):
        if os.path.isfile(Evaluator.path):
            f = open(Evaluator.path)

            for game in data:
                team_a = game['result'].split(' ')[0]
                team_b = game['result'].split(' ')[5]

                for line in f:
                    compare_a = line.split(' ')[0]
                    compare_b = line.split(' ')[2]

                    if (str(team_a.strip()) == str(compare_b.strip()) or str(team_a.strip()) == str(compare_a.strip())) \
                            and (str(team_b.strip()) == str(compare_b.strip()) or str(team_b.strip()) == str(
                                compare_a.strip())):
                        print line

    @staticmethod
    def make_bet(mood, data):
        bets = []
        # risky
        try:

            if mood == 1:
                print "\nI'm gonna play it risky\n"
                for game in data:
                    team_a = game['result'].split(' ')[0]
                    team_a_rating = int(game['result'].split(' ')[2])
                    team_b = game['result'].split(' ')[5]
                    team_b_rating = int(game['result'].split(' ')[7])

                    if team_a_rating > team_b_rating or (team_b_rating - team_a_rating < 10):
                        bet = '%s - %d' % (team_a, 1)
                        bets.append(bet)

                    elif team_a_rating < team_b_rating or (team_a_rating - team_b_rating < 10):
                        bet = '%s - %d' % (team_b, 2)
                        bets.append(bet)

                    elif team_a_rating == team_b_rating:
                        bet = '%s - %s - %s' % (team_a, 'X', team_b)
                        bets.append(bet)

            # sure
            if mood == 2:
                print "\nHmmm... I'm gonna play it safe\n"
                for game in data:
                    team_a = game['result'].split(' ')[0]
                    team_a_rating = int(game['result'].split(' ')[2])
                    team_b = game['result'].split(' ')[5]
                    team_b_rating = int(game['result'].split(' ')[7])

                    if team_a_rating > team_b_rating:
                        bet = '%s - %d' % (team_a, 1)
                        bets.append(bet)

                    elif team_a_rating < team_b_rating:
                        bet = '%s - %d' % (team_b, 2)
                        bets.append(bet)

                    elif team_a_rating == team_b_rating:
                        bet = '%s - %s - %s' % (team_a, 'X', team_b)
                        bets.append(bet)

            # random
            if mood == 3:
                print "\nDon't have an idea what I'm doing\n"
                for game in data:
                    team_a = game['result'].split(' ')[0]
                    team_b = game['result'].split(' ')[5]

                    bet = '%s - %d' % (random.choice([team_a, team_b]), random.choice([1, 2, 3]))
                    bets.append(bet)
        except:
            pass

        Evaluator.print_bets(bets)

    @staticmethod
    def print_bets(bets):

        for bet in bets:
            print bet
