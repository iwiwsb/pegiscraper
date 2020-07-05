from argparse import ArgumentParser
import csv
import os
import requests
from bs4 import BeautifulSoup


def main():
    delimiters = {'comma': ",",
                  'tab': "\t",
                  'colon': ":",
                  'semicolon': ";",
                  'pipe': "|"}
    parser = ArgumentParser(description="Scrape videogame data from PEGI website")
    parser.add_argument("--delimiter",
                        default="comma",
                        type=str,
                        choices=delimiters.keys(),
                        required=False,
                        help="Delimiter will be used in csv file. The default is comma.")
    parser.add_argument("path", type=str, help="Path where to save file.")

    args = parser.parse_args()
    s = requests.Session()
    s.headers.update({
        "Referer": "https://pegi.info/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:68.0) Gecko/20100101 Firefox/68.0"
    })

    data = load_search_results(page=1, session=s)
    pages_count = get_pages_count(data)
    pages_range = range(1, pages_count + 1)

    with open(args.path, "w", encoding="utf8", newline="", buffering=1) as csvfile:
        fieldnames = ['"game_title"',
                      '"publisher"',
                      '"release_date"',
                      '"platforms"',
                      '"rating"',
                      '"descriptors"',
                      '"website"']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=delimiters[args.delimiter])
        writer.writeheader()
        for page in pages_range:
            search_results: str = load_search_results(page=page, session=s)
            soup = BeautifulSoup(search_results, features="lxml")
            games_list = get_games_list(soup)
            for game in games_list:
                game_title = get_title(game)
                publisher = get_publisher(game)
                release_date = get_release_date(game)
                platforms = get_platforms(game)
                rating = get_rating(game)
                descriptors = get_descriptors(game)
                website = get_website(game)
                values = [game_title,
                          publisher,
                          release_date,
                          platforms,
                          rating,
                          descriptors,
                          website]
                entry = dict(zip(fieldnames, values))
                writer.writerow(entry)
            progress_percent = page / pages_count * 100
            print("\rParsed {}/{} pages ({:.2}%)".format(page, pages_count, progress_percent), end="")


def get_pages_count(text):
    soup = BeautifulSoup(text, features="lxml")
    count = int(soup.find("div", {"class": "results-count"}).find("strong").text.strip("results"))
    return count // 10 + 1


def load_search_results(page, session):
    url = ("https://pegi.info/search-pegi?q=&filter-age%%5B0%%5D=&filter-descriptor%%5B0%%5D=&filter-publisher="
           "&filter-platform%%5B0%%5D=&filter-release-year%%5B0%%5D=&page={0}".format(page))
    request = session.get(url)
    assert isinstance(request.text, str)
    return request.text


def get_filename(path):
    return os.path.split(path)[1]


def get_games_list(soup):
    return soup.find("div", {"class": "page-content"}).find_all("article", {"class": "game"})


def get_title(game):
    return game.find("div", {"class": "info"}).find("h3").text


def get_release_date(game):
    date = game.find("span", {"class": "release-date"}).text.lstrip("\nRelease Date:")
    day, month, year = date.split("/")
    return str(year + '-' + month + '-' + day)


def get_platforms(game):
    return game.find("span", {"class": "platform"}).text.split(":")[1]


def get_rating(game):
    pegi_ratings = {"pegi3": 3,
                    "pegi7": 7,
                    "pegi12": 12,
                    "pegi16": 16,
                    "pegi18": 18}
    filepath = game.find("div", {"class": "age-rating"}).find("img").get("src")
    key = get_filename(filepath).rstrip(".png")
    return pegi_ratings[key]


def get_descriptors(game):
    pegi_descriptors = {"bad_language": "Bad Language",
                        "discrimination": "Discrimination",
                        "drugs": "Drugs",
                        "fear": "Fear",
                        "horror": "Horror",
                        "gambling": "Gambling",
                        "in-game_purchases": "In-Game Purchases",
                        "sex": "Sex",
                        "violence": "Violence"}

    descriptors_list = []
    descriptors = game.find("div", {"class": "descriptors"}).find_all("img")

    for descriptor in descriptors:
        key = get_filename(descriptor.get("src")).split(".")[0]
        if key not in ("", None):
            descriptors_list.append(pegi_descriptors[key])
        else:
            descriptors_list.append("")
    return ", ".join(descriptors_list)


def get_publisher(game):
    return game.find("span", {"class": "publisher"}).text


def get_website(game):
    url = ""
    website = game.find("div", {"class": "info"}).find("span", {"class": "website-info"})
    if website is not None:
        url = website.find("a")["href"]
    return url


if __name__ == "__main__":
    main()
