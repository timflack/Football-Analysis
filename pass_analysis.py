from eventsTodataframe import load_file, to_dataframe
from plotting_pitches import plot_pitch
import matplotlib.pyplot as plt
import numpy as np
import sys

def get_pass_df(match_df):
    """
    Function that returns a dataframe of passes with an added column of distance (euclidean) of the pass
    :param match_df: output from to_dataframe function from eventsTodataframe.py
    :return pass_df: dataframe containing all passes in a match that occur in regular play:
    """
    pass_df = match_df[(match_df['type'] == 'Pass')]
    cols1 = ['x_coord', 'y_coord']
    cols2 = ['end_x_coord', 'end_y_coord']
    pass_df['distance'] = np.linalg.norm(pass_df[cols1].values - pass_df[cols2].values, axis=1)

    return pass_df

def get_team_passes(pass_df, team_name):
    """

    :param pass_df: output from get_pass_df (dataframe)
    :param team_name: name of team you want to get passes for
    :return def_team_passes: dataframe containing open play passes for a particular team
    """
    df_team_passes = pass_df[pass_df['team'] == team_name]

    return df_team_passes


def get_player_passes(pass_df):
    """

    :param pass_df: output from get_pass_df (dataframe)
    :return df_player_passes: dataframe containing open play passes for a particular player
    """
    print(pass_df.player.unique())
    player_name = input('Choose name from list: ')
    df_player_passes = pass_df[pass_df['player'] == player_name]

    return df_player_passes

def plot_player_passes(player_pass_df,length, width, unity, linecolor, type='normal'):
    """

    :param player_pass_df:
    :param length:
    :param width:
    :param unity:
    :param linecolor:
    :return:
    """
    # fig = plt.figure()
    ax = plot_pitch(length=length, width=width, unity=unity, linecolor=linecolor)
    for idx, pass_data in player_pass_df.iterrows():
        x = pass_data['x_coord']
        y = pass_data['y_coord']
        dx = pass_data['end_x_coord'] - x
        dy = pass_data['end_y_coord'] - y
        if type == 'normal':
            if pass_data['outcome'] == 'Complete':
                color = 'green'
            else:
                color = 'red'
            end_circle = plt.Circle((x, width - y), 1, color=color)
            end_circle.set_alpha(.2)
            ax.add_patch(end_circle)

            pass_arrow = plt.Arrow(x, width - y, dx, -dy, width=1, color="black")
            ax.add_patch(pass_arrow)
        elif type == 'distance':
            if pass_data['distance'] <= 15.0:
                color = 'green'
            elif 15.0 < pass_data['distance'] <= 30.0:
                color = 'orange'
            else:
                color = 'red'
            end_circle = plt.Circle((x, width - y), 1, color=color)
            end_circle.set_alpha(.2)
            ax.add_patch(end_circle)

            pass_arrow = plt.Arrow(x, width - y, dx, -dy, width=1, color="black")
            ax.add_patch(pass_arrow)
        else:
            print('You have not entered a correct type')
            sys.exit()

    return ax


if __name__ == "__main__":
    match_data = load_file(input('Input json file: '))
    match_df = to_dataframe(match_data)
    pass_df = get_pass_df(match_df)
    player_df = get_player_passes(pass_df)
    fig = plt.figure()
    ax = plot_player_passes(player_df, 120, 80, 'yards', 'black')
    ax = plot_player_passes(player_df, 120, 80, 'yards', 'black', 'distance')
    plt.show()
