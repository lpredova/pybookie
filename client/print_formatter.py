import json


class PrintFormatter:
    def __init__(self):
        pass

    @staticmethod
    def games(games):
        games = json.loads(games)

        for group in games:
            print '\nGroup:' + group['group']
            for team in group['teams']:
                print "%d. %s" % (team['id'], team['team'])
            print '----------------------------------'

    @staticmethod
    def results(results):
        print '\nBetting suggestions\n'
        for game in results:
            print '%s \n' % game['result']
