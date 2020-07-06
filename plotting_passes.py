from eventsTodataframe import load_file, to_dataframe
from pass_analysis import get_pass_df, get_player_passes, get_team_passes
from plottingpitches import plot_pitch
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler



def plot_passes(file, player=False):
    """
    # ToDo add docstring

    :param file:
    :param player:
    :return:
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

    # plot passes as arrows
    # ToDo separate passes into different sections using colours/arrow tpyes - too simple atm
    for x, y, x_end, y_end in zip(x_coords, y_coords, end_x_coords, end_y_coords):
        diff_x = x_end - x
        diff_y = y_end - y
        pass_arrow = plt.Arrow(x, length_y-y, diff_x, diff_y)
        ax.add_artist(pass_arrow)

    plt.show()

if __name__ == "__main__":
    plot_passes('sb_public_events_data_16029', "Nélson Cabral Semedo")

