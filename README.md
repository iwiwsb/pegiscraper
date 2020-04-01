# PEGI Scraper

PEGI Scraper is the python script that extracts videogames data from [PEGI](https://pegi.info) website, such as:
- Game title
- Release date
- Platforms
- Raiting
  - 3+
  - 7+
  - 12+
  - 16+
  - 18+
- Content descriptors
  - Bad language
  - Discrimination
  - Drugs
  - Fear
  - Gambling
  - In-Game Purchases
  - Sex
  - Violence

The extracted data is saved to a csv file.

### Algorithm
1. Download first page from [PEGI Search](https://pegi.info/search-pegi?q=&op=Search&filter-age%5B%5D=&filter-descriptor%5B%5D=&filter-publisher=&filter-platform%5B%5D=&filter-release-year%5B%5D=&page=1)
2. Extract information about videogames
3. Append extracted information to a csv file. 
4. Download next page
5. GOTO 2

### Example result
A csv file with following columns and entries:
|game_title|release_date|platform|rating|descriptors|
|----------|------------|--------|------|-----------|
|...|...|...|...|...|
|Just Cause 4|04/12/2018|PC \| Xbox&nbsp;One \| PlayStation&nbsp;4|18|Violence \| Bad&nbsp;Language|
|Mutant Year Zero: Road to Eden|04/12/2018|PC \| PlayStation&nbsp;4 \| Xbox&nbsp;One|16|Violence \| Bad&nbsp;Language |
|Atelier Meruru: The Apprentice of Arland DX|04/12/2018|PlayStation&nbsp;4 \| PC|12|Violence \| Bad&nbsp;Language \| Sex |
|Hellblade: Senua's Sacrifice|04/12/2018|Xbox&nbsp;One \| PlayStation&nbsp;4|18|Violence \| Bad&nbsp;Language |
|...|...|...|...|...|

### Speed
Very slow, because it downloads and parses pages one at a time. So far it needs to download 31346 pages (by March 2020).

