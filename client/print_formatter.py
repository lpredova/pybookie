import json


class PrintFormatter:
    def __init__(self):
        pass

    @staticmethod
    def games(games):
        games = json.loads(games)

        for group in games:
            print '\n----------------------------------'
            print '\nGroup:' + group['group']
            print '\t1. ' + group['teams']['team1'] + '\n'
            print '\t2. ' + group['teams']['team2'] + '\n'
            print '\t3. ' + group['teams']['team3'] + '\n'
            print '\t4. ' + group['teams']['team4'] + ''
