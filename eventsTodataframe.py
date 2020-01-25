import pandas as pd
import json

def load_file(json_file):
    """
    Function that takes a json file and returns a list of dicts
    :param json_file: json_file of events data for match
    :return list of dicts:
    """
    with open(json_file) as f:
        data = json.load(f)
        f.close()
    return data


def to_dataframe(data):
    """
    Function that takes a list of dicts returned from load_file and returns a clean dataframe
    :param data: list of dicts - output from load_file
    :return dataframe:
    """

    # initialise an index
    idx = 0

    # initialise empty lists to populate with data from list of dicts
    index = []
    period = []
    duration = []
    t = []
    player = []
    minute = []
    second = []
    x_coord = []
    y_coord = []
    end_x_coord = []
    end_y_coord = []
    play_pattern = []
    recipient = []
    outcome = []
    team = []
    poss_team = []
    height = []

    # populate the lists with data from list of dicts
    for idx in range(0, len(data)):
        if ("index" in data[idx]):
            index.append(data[idx]['index'])
        else:
            index.append(0)
        if ("period" in data[idx]):
            period.append(data[idx]['period'])
        else:
            period.append(None)

        if ("duration" in data[idx]):
            duration.append(data[idx]['duration'])
        else:
            duration.append(0)

        if ("type" in data[idx]):
            t.append(data[idx]['type']['name'])
        else:
            t.append(None)

        if ("player" in data[idx]):
            player.append(data[idx]['player']['name'])
        else:
            player.append(None)

        if ("minute" in data[idx]):
            minute.append(data[idx]['minute'])
        else:
            minute.append(None)

        if ("second" in data[idx]):
            second.append(data[idx]['second'])
        else:
            second.append(None)

        if ("location" in data[idx]):
            x_coord.append(data[idx]['location'][0])
            y_coord.append(data[idx]['location'][1])
        else:
            x_coord.append(None)
            y_coord.append(None)

        if ("pass" in data[idx]):
            if ("end_location" in data[idx]['pass']):
                end_x_coord.append(data[idx]['pass']['end_location'][0])
                end_y_coord.append(data[idx]['pass']['end_location'][1])
            else:
                end_x_coord.append(None)
                end_y_coord.append(None)
        elif ("shot" in data[idx]):
            if ("end_location" in data[idx]['shot']):
                end_x_coord.append(data[idx]['shot']['end_location'][0])
                end_y_coord.append(data[idx]['shot']['end_location'][1])
            else:
                end_x_coord.append(None)
                end_y_coord.append(None)
        else:
            end_x_coord.append(None)
            end_y_coord.append(None)

        if ("play_pattern" in data[idx]):
            play_pattern.append(data[idx]['play_pattern']['name'])
        else:
            play_pattern.append(None)

        if ("pass" in data[idx]):
            if ("recipient" in data[idx]['pass']):
                recipient.append(data[idx]['pass']['recipient']['name'])
            else:
                recipient.append(None)
        else:
            recipient.append(None)

        if ("pass" in data[idx]):
            if ("outcome" in data[idx]['pass']):
                outcome.append(data[idx]['pass']['outcome']['name'])
            elif ("outcome" not in data[idx]['pass']):
                outcome.append("Complete")
        else:
            outcome.append(None)

        if ("team" in data[idx]):
            team.append(data[idx]['team']['name'])
        else:
            team.append(None)

        if ("possession_team" in data[idx]):
            poss_team.append(data[idx]['possession_team']['name'])
        else:
            poss_team.append(None)

        if ("pass" in data[idx]):
            if ('height' in data[idx]['pass']):
                height.append(data[idx]['pass']['height']['name'])
            else:
                height.append(None)
        else:
            height.append(None)

    # construct dataframe from set of lists
    df = pd.DataFrame()
    df['index'] = index
    df['period'] = period
    df['duration'] = duration
    df['minute'] = minute
    df['second'] = second
    df['type'] = t
    df['player'] = player
    df['team'] = team
    df['poss_team'] = poss_team
    df['x_coord'] = x_coord
    df['y_coord'] = y_coord
    df['end_x_coord'] = end_x_coord
    df['end_y_coord'] = end_y_coord
    df['play_pattern'] = play_pattern
    df['recipient'] = recipient
    df['height'] = height
    df['outcome'] = outcome

    return df