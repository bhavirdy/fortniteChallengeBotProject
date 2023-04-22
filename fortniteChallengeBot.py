import requests
import config


def get_current_challenges():
    headers = {
        'accept': 'application/json',
        'Authorization': config.key,
    }

    params = {
        'lang': 'en',
    }

    response = requests.get('https://fortniteapi.io/v3/challenges', params=params, headers=headers)

    challenge_category = response.json()['bundles']

    category_results = []
    for entry in challenge_category:
        category_name = entry['name']
        category_results.append(category_name)

    print('Choose a challenge category:')
    for i in category_results:
        print(category_results.index(i), end=' ')
        print(" ", i)

    keyboard = int(input('\nEnter the number of the desired challenge category:\n'))

    challenge_subcategories = challenge_category[keyboard]['bundles']
    challenge_results = []
    for entry in challenge_subcategories:
        subcategory = entry['quests']
        for entry2 in subcategory:
            challenge = entry2['name']
            challenge_results.append(challenge)

    print('Here is a list of all the challenges in this category:\n')
    challenge_results = list(dict.fromkeys(challenge_results))  # removing duplicates
    for i in challenge_results:
        print(challenge_results.index(i), end=' ')
        print(" ", i)


def main():
    get_current_challenges()


if __name__ == "__main__":
    main()
