import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from eventsTodataframe import load_file, to_dataframe

def get_pass_df(match_df):
    """

    :param match_df: output from to_dataframe function from eventsTodataframe.py
    :return pass_df: dataframe containing all passes in a match that occur in regular play:
    """
    pass_df = match_df[(match_df['type'] == 'Pass')]

    return pass_df

def get_team_passes(pass_df, team_name):
    """

    :param pass_df: output from get_pass_df (dataframe)
    :param team_name: name of team you want to get passes for
    :return def_team_passes: dataframe containing open play passes for a particular team
    """
    df_team_passes = pass_df[pass_df['team'] == team_name]

    return df_team_passes


def get_player_passes(pass_df, player_name):
    """

    :param pass_df: output from get_pass_df (dataframe)
    :param player_name: name of player you want to get passes for
    :return df_player_passes: dataframe containing open play passes for a particular player
    """
    df_player_passes = pass_df[pass_df['player'] == player_name]

    return df_player_passes

