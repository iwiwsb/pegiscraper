import csv
import os
import requests
from bs4 import BeautifulSoup


def main():
    s = requests.Session()
    s.headers.update({
        'Referer': 'https://pegi.info/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'
    })

    data = load_search_results(page=1, session=s)
    pages_count = get_pages_count(data)
    pages_range = range(1, pages_count + 1)

    if not os.path.exists('./pages/'):
        os.makedirs('./pages/')

    with open('./games.csv', 'w', encoding='utf8', newline='') as csvfile:
        fieldnames = ["\"game_title\"", 
                      "\"release_date\"", 
                      "\"platform\"", 
                      "\"rating\"", 
                      "\"descriptors\""]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for page in pages_range:
            if not os.path.exists('./pages/search_page_%d.html' % page):
                print("Downloading file \"search_page_{0}.html\"...".format(page))
                data = load_search_results(page, s)
                with open('./pages/search_page_%d.html' % page, 'wb') as output_file:
                    output_file.write(data.encode('utf8'))
                    print("File \"search_page_{0}.html\" successfully downloaded".format(page))

                print("Writing content of ./search_page_{0}.html to ./games.csv".format(page))
            else:
                print("File ./search_page_{0}.html already exists. Writing content to ./games.csv".format(page))
            writer.writerows(parse_search_results_file('./pages/search_page_%d.html' % page))
            print("Done!")


def read_file(filename):
    with open(filename, mode='rb') as input_file:
        text = input_file.read()
    return text


def get_pages_count(text):
    soup = BeautifulSoup(text, features="lxml")
    count = int(soup.find('div', {'class': 'results-count'}).find('strong').text.strip("results"))
    return count // 10 + 1


def load_search_results(page, session):
    url = '''https://pegi.info/search-pegi?q=&filter-age%%5B0%%5D=&filter-descriptor%%5B0%%5D=&filter-publisher=&filter-platform%%5B0%%5D=&filter-release-year%%5B0%%5D=&page=%d''' % page
    request = session.get(url)
    assert isinstance(request.text, str)
    return request.text


def get_filename(path):
    return os.path.split(path)[1]


def get_games_list(soup):
    return soup.find('div', {'class': 'page-content'}).find_all('article', {'class': 'game'})


def get_title(game):
    return game.find('div', {'class': 'info'}).find('h3').text


def get_release_date(game):
    return game.find('span', {'class': 'release-date'}).text.lstrip('\nRelease Date:')


def get_platform(game):
    return game.find('span', {'class': 'platform'}).text.lstrip('System:').replace(",", "")


def get_rating(game):
    pegi_ratings = {'pegi3': 3,
                    'pegi7': 7,
                    'pegi12': 12,
                    'pegi16': 16,
                    'pegi18': 18}
    filepath = game.find('div', {'class': 'age-rating'}).find('img').get('src')
    key = get_filename(filepath).rstrip('.png')
    return pegi_ratings[key]


def get_descriptors_list(game):
    pegi_descriptors = {'bad_language': 'Bad Language',
                        'discrimination': 'Discrimination',
                        'drugs': 'Drugs',
                        'fear': 'Fear',
                        'gambling': 'Gambling',
                        'in-game_purchases': 'In-Game Purchases',
                        'sex': 'Sex',
                        'violence': 'Violence'}
    
    descriptors_list = []
    descriptors = game.find('div', {'class': 'descriptors'}).find_all('img')

    for descriptor in descriptors:
        key = get_filename(descriptor.get('src')).split('.')[0]
        if key is not '':
            descriptors_list.append(pegi_descriptors[key])
        else:
            descriptors_list.append('')
    return descriptors_list


def parse_search_results_file(filename):
    results = []
    text = read_file(filename)

    soup = BeautifulSoup(text, features="lxml")
    games_list = get_games_list(soup)
    for game in games_list:
        game_title = get_title(game)
        release_date = get_release_date(game)
        platform = get_platform(game)
        rating = get_rating(game)
        descriptors = '|'.join(get_descriptors_list(game))

        results.append({
            '\"game_title\"': game_title,
            '\"release_date\"': release_date,
            '\"platform\"': platform,
            '\"rating\"': rating,
            '\"descriptors\"': descriptors
        })

    return results


if __name__ == "__main__":
    main()
