from random import randint

from sources import footbal_db


class Bookie:
    def __init__(self):
        pass

    @staticmethod
    def make_random_evaluation(number_of_teams):
        result = []
        number_of_teams = int(number_of_teams)
        for num in range(0, number_of_teams):
            result.append({'teamA': randint(1, 32), 'teamB': randint(1, 32)})

        return Bookie.make_evaluation(result)

    @staticmethod
    def make_evaluation(data):
        results = []
        for team in data:
            team_a = footbal_db.FootballDB.get_team_by_id(team['teamA'])
            team_b = footbal_db.FootballDB.get_team_by_id(team['teamB'])

            if team_a and team_b:

                if team_a == team_b:
                    results.append({'result': ('SAME TEAM %s - 50%%' % team_a)})
                    continue

                team_a_sum = footbal_db.FootballDB.get_wc_titles(team_a) * 200
                team_b_sum = footbal_db.FootballDB.get_wc_titles(team_b) * 200

                team_a_sum += footbal_db.FootballDB.get_ranking(team_b)
                team_b_sum += footbal_db.FootballDB.get_ranking(team_a)

                team_a_sum += footbal_db.FootballDB.get_wc_games_played(team_a)
                team_b_sum += footbal_db.FootballDB.get_wc_games_played(team_b)

                team_a_sum += footbal_db.FootballDB.get_won_wc_games_played(team_a) * 3
                team_b_sum += footbal_db.FootballDB.get_won_wc_games_played(team_b) * 3

                team_a_sum += footbal_db.FootballDB.get_draw_wc_games_played(team_a)
                team_b_sum += footbal_db.FootballDB.get_draw_wc_games_played(team_b)

                team_a_sum -= footbal_db.FootballDB.get_lost_wc_games_played(team_a) * 3
                team_b_sum -= footbal_db.FootballDB.get_lost_wc_games_played(team_b) * 3

                team_a_sum += footbal_db.FootballDB.get_goal_difference_wc_games_played(team_a)
                team_b_sum += footbal_db.FootballDB.get_goal_difference_wc_games_played(team_b)

                team_a_sum += footbal_db.FootballDB.get_wc_points(team_a)
                team_b_sum += footbal_db.FootballDB.get_wc_points(team_b)

                team_a_sum += footbal_db.FootballDB.get_wc_participations(team_a)
                team_b_sum += footbal_db.FootballDB.get_wc_participations(team_b)

                team_a_sum += footbal_db.FootballDB.get_wc_team_player_ratings(team_a)
                team_b_sum += footbal_db.FootballDB.get_wc_team_player_ratings(team_b)

                total_sum = team_a_sum + team_b_sum

                result = '%s : %d %% - %s : %d %%' % (
                    team_a, float(team_a_sum) / float(total_sum) * 100, team_b,
                    float(team_b_sum) / float(total_sum) * 100)
                results.append({'result': result})
            else:
                return 'INVALID TEAM CODE'

        return results

    @staticmethod
    def get_games():
        return footbal_db.FootballDB.get_games()
