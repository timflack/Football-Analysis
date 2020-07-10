from eventsTodataframe import load_file, to_dataframe
from pass_analysis import get_pass_df, get_player_passes, get_team_passes
from plottingpitches import plot_pitch
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler



def plot_passes(file, team=None, player=False):
    """
    Function that plots the passes for a team (and player if specified) from the SB events data

    :param file: json file of events data
    :param team: team to plot passes for
    :param player: player to plot passes for
    :return: matplotlib fig, ax objects
    """
    # plot the pitch
    fig, ax = plot_pitch(pitchcolour="#195905", linecolour="#faf0e6",
              orientation="horizontal", view="full")

    # Statsbomb data is given in yards - setting pitch dimensions
    length_x = 120
    length_y = 80

    # load the data
    data = load_file(file + '.json')
    # convert data to df
    full_df = to_dataframe(data)
    # subset data to only passes
    pass_df = get_pass_df(full_df)
    pass_df = get_team_passes(pass_df, 'Sevilla')
    # if a player name is given, subset by that player
    if player:
        pass_df = pass_df[pass_df['player']==player]
    # convert x, y coordinates to yards as my pitch dimensions in meters
    scaler_x = MinMaxScaler(feature_range=(0, 104))
    scaler_y = MinMaxScaler(feature_range=(0, 68))
    x_coords = scaler_x.fit_transform(pass_df['x_coord'].to_numpy().reshape(-1, 1))
    end_x_coords = scaler_x.fit_transform(pass_df['end_x_coord'].to_numpy().reshape(-1, 1))
    y_coords = scaler_y.fit_transform(pass_df['y_coord'].to_numpy().reshape(-1, 1))
    end_y_coords = scaler_y.fit_transform(pass_df['end_y_coord'].to_numpy().reshape(-1, 1))
    x_coords = x_coords.flatten()
    y_coords = y_coords.flatten()
    end_x_coords = end_x_coords.flatten()
    end_y_coords = end_y_coords.flatten()
    completed = ['Success' if val == 'Complete' else 'Failed' for val in pass_df['outcome'].values]

    # plot passes with hue on completed/not-completed
    sns.scatterplot(end_x_coords, end_y_coords, hue=completed, zorder=12)
    plt.plot([x_coords, end_x_coords], [y_coords, end_y_coords], zorder=11, alpha=1, color="black")
    plt.show()

if __name__ == "__main__":
    plot_passes('sb_public_events_data_16029')

