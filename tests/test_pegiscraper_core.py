# coding: utf8

import pegiscraper
from bs4 import BeautifulSoup


class TestPegiscraper:
    text = '''<article class="game">
              <div class="game-content"><div class="description"><div class="age-rating">
              <img src="https://pegi.info/themes/pegi/public-images/pegi/pegi18.png" alt="" />
              </div><div class="info">
              <h3>Hitman: Blood Money</h3>
              <span class="publisher">Warner Brothers Entertainment UK Ltd</span>
              <span class="content-info">This is an action game in which players control Agent 47, a master assassin 
              tasked with eliminating targets while evading an organization known as the Franchise. Players use machine 
              guns, sniper rifles,...</span></div><div class="technical-info">
              <span class="platform"><span class="feature-label">System:</span>PlayStation 4, Xbox One</span>
              <span class="release-date"><span class="feature-label">Release Date:</span>25/09/2018</span></div></div>
              <div class="descriptors"><img src="https://pegi.info/themes/pegi/public-images/violence.png" alt="" />
              <img src="https://pegi.info/themes/pegi/public-images/bad_language.png" alt="" />
              <img src="https://pegi.info/themes/pegi/public-images/drugs.png" alt="" /></div>
              </div><div class="advice"><div class="consumer-advice"><h3><span>Consumer advice</span></h3>
              <div class="content-wrap"><div class="content-arrow"></div><div class="content-main"><p>This game has 
              received a PEGI 18 which restricts availability to ADULTS ONLY. This rating has been given due to violence
              against vulnerable and defenceless characters, strong violence, glamorisation of the use of illegal drugs 
              and the use of sexual expletives. Not suitable for persons below 18 years of age.</p></div></div></div>
              </article>'''
    soup = BeautifulSoup(text, features="lxml")
    games_list = soup.find_all('article', {'class': 'game'})

    def test_get_pages_count(self):
        text = '''<h1><span property="schema:name">Search results</span></h1>
                  <div class="page-content">
                  <div class="results-count">
                  <span>Found <strong>30131 results</strong> from your query</span>
                  </div><div property="schema:text" class="body text-with-summary">'''
        assert pegiscraper.get_pages_count(text) == 3014

    def test_get_title(self):
        assert pegiscraper.get_title(self.games_list[0]) == 'Hitman: Blood Money'

    def test_get_release_date(self):
        assert pegiscraper.get_release_date(self.games_list[0]) == '25/09/2018'

    def test_get_platform(self):
        assert pegiscraper.get_platform(self.games_list[0]) == 'PlayStation 4 Xbox One'

    def test_get_rating(self):
        assert pegiscraper.get_rating(self.games_list[0]) == 18

    def test_get_descriptors_list(self):
        assert set(pegiscraper.get_descriptors_list(self.games_list[0])) == {'Bad Language', 'Violence', 'Drugs'}

    def test_get_games_list(self):
        with open('./search_page_1.html', 'rb') as search_results_file:
            search_data = search_results_file.read()

        soup = BeautifulSoup(search_data)
        print(pegiscraper.get_games_list(soup))

    def test_parse_search_results_file(self):
        search_results_file = './search_page_1.html'
        result = pegiscraper.parse_search_results_file(search_results_file)
        print(result)
