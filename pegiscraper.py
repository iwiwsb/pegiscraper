from argparse import ArgumentParser
import csv
from typing import List, Dict
import requests
from bs4 import BeautifulSoup
from bs4.element import Tag, ResultSet
from requests.sessions import Session


def main():
    delimiters = {'comma': ",",
                  'tab': "\t",
                  'colon': ":",
                  'semicolon': ";",
                  'pipe': "|"}
    parser: ArgumentParser = ArgumentParser(description="Scrape videogame data from PEGI website")
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

    url = ("https://pegi.info/search-pegi?q=&filter-age%%5B0%%5D=&filter-descriptor%%5B0%%5D=&filter-publisher="
                "&filter-platform%%5B0%%5D=&filter-release-year%%5B0%%5D=&page={}")

    first_page_html = get_page_html(s, url, 1)
    first_page_soup = BeautifulSoup(first_page_html, features="lxml")
    pages_count = get_pages_count(first_page_soup)
    pages_range = range(1, pages_count + 1)

    with open(args.path, "w", encoding="utf8", newline="", buffering=1) as csvfile:
        fieldnames = ['"game_title"',
                      '"publisher"',
                      '"release_dates_and_platforms"',
                      '"rating"',
                      '"descriptors"',
                      '"website"']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=delimiters[args.delimiter])
        writer.writeheader()
        for page in pages_range:
            if page == 1:
                soup = first_page_soup
            else:
                search_results = get_page_html(s, url, page)
                soup = BeautifulSoup(search_results, features="lxml")
            games_list = get_games_list(soup)
            for game in games_list:
                entry = construct_game_entry(fieldnames, game)
                writer.writerow(entry)
            progress_percent = page / pages_count * 100
            print("\rParsed {}/{} pages ({:.2}%)".format(page, pages_count, progress_percent), end="")


def get_page_html(session: Session, url: str, page_number: int) -> str:
    return session.get(url.format(page_number)).text


def get_pages_count(soup: BeautifulSoup) -> int:
    pages_count = int(soup.find("a", {"class": "next"}, text=" >> ")["href"][176:])
    return pages_count


def get_games_list(soup: BeautifulSoup) -> ResultSet:
    return soup.find("div", {"class": "page-content"}).find_all("article", {"class": "game"})


def construct_game_entry(fieldnames: List[str], game: Tag) -> Dict[str, str]:
    game_title = get_title(game)
    publisher = get_publisher(game)
    release_dates_and_platforms = get_release_dates_and_platforms(game)
    rating = get_rating(game)
    descriptors = get_descriptors(game)
    website = get_website(game)
    values = [game_title,
              publisher,
              release_dates_and_platforms,
              rating,
              descriptors,
              website]
    entry = dict(zip(fieldnames, values))
    return entry


def get_title(game: Tag) -> str:
    return game.find("div", {"class": "info"}).find("h3").text


def get_release_dates_and_platforms(game: Tag) -> str:
    release_dates_and_platforms: ResultSet = game.find("span", {"class": "platform"}).ul.find_all("li")

    release_date_platform = []
    for rdnp in release_dates_and_platforms:
        rdnp_str: str = rdnp.text
        day = rdnp_str[:2]
        month = rdnp_str[3:5]
        year = rdnp_str[6:10]
        release_date = "-".join([year, month, day])
        platform = rdnp_str[13:]
        release_date_platform.append(release_date + ": " + platform)
    return ", ".join(release_date_platform)


def get_rating(game: Tag) -> str:
    filepath = game.find("div", {"class": "age-rating"}).find("img").get("src")
    pegi_rating = filepath[65:-4:]
    return pegi_rating


def get_descriptors(game: Tag) -> str:
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
        key = descriptor.get("src")[44:-4:]
        if key not in ("", None):
            descriptors_list.append(pegi_descriptors[key])
        else:
            descriptors_list.append("")
    return ", ".join(descriptors_list)


def get_publisher(game: Tag) -> str:
    return game.find("span", {"class": "publisher"}).text


def get_website(game: Tag) -> str:
    url = ""
    website = game.find("div", {"class": "info"}).find("span", {"class": "website-info"})
    if website is not None:
        url = website.find("a")["href"]
    return url


if __name__ == "__main__":
    main()
