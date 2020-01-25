import pandas as pd


def get_lineups_and_formations(data):
    """
    Function that takes a dataframe of match events and outputs the home and away lineup and formation
    :param data: clean dataframe from to_dataframe output (refer to eventsTodataframe.py)
    :return home team lineup, away team lineup , home team formation, away team formation:
    """

    idx = 0

    home_team_formation = data[idx]['tactics']['formation']
    home_team = data[idx]['team']['name']
    home_names = []
    home_player_id = []
    home_positions = []
    home_shirt_numbers = []

    for i in range(0, 11):
        home_shirt_numbers.append(data[idx]['tactics']['lineup'][i]['jersey_number'])
        home_player_id.append(data[idx]['tactics']['lineup'][i]['player']['id'])
        home_names.append(data[idx]['tactics']['lineup'][i]['player']['name'])
        home_positions.append(data[idx]['tactics']['lineup'][i]['position']['name'])

    home_df = pd.DataFrame()
    home_df['player_id'] = home_player_id
    home_df['home_names'] = home_names
    home_df['shirt_number'] = home_shirt_numbers
    home_df['position'] = home_positions
    home_df['team'] = [home_team for n in range(11)]

    idx = 1

    away_team_formation = data[idx]['tactics']['formation']
    away_team = data[idx]['team']['name']
    away_names = []
    away_player_id = []
    away_positions = []
    away_shirt_numbers = []

    for i in range(0, 11):
        away_shirt_numbers.append(data[idx]['tactics']['lineup'][i]['jersey_number'])
        away_player_id.append(data[idx]['tactics']['lineup'][i]['player']['id'])
        away_names.append(data[idx]['tactics']['lineup'][i]['player']['name'])
        away_positions.append(data[idx]['tactics']['lineup'][i]['position']['name'])

    away_df = pd.DataFrame()
    away_df['player_id'] = away_player_id
    away_df['away_names'] = away_names
    away_df['shirt_number'] = away_shirt_numbers
    away_df['position'] = away_positions
    away_df['team'] = [away_team for n in range(11)]

    return home_df, away_df, home_team_formation, away_team_formation

