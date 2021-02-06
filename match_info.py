import pickle


def get_all_team_matches(team_name):
    with open('data.pickle', 'rb') as f:
        matches = pickle.load(f)

    new_dict = {}

    for key, value in matches.items():
        for match in value:
            if team_name in match:
                new_dict[key] = match

    string = ''
    for key, value in new_dict.items():
        string += f'{key}: {value} \n'

    return string


def get_all_matches():
    with open('data.pickle', 'rb') as f:
        data_new = pickle.load(f)

    string = ''
    for key, value in data_new.items():
        string += f'{key}: {value} \n'

    return string


if __name__ == '__main__':
    for key, value in get_all_team_matches('Liverpool').items():
        print(f'{key}: {value}')
