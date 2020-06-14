# PEGI Scraper

PEGI Scraper is the python script that extracts information about videogames from [PEGI](https://pegi.info) website, such as:
- Game title
- Publisher
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
  - Horror
  - Gambling
  - In-Game Purchases
  - Sex
  - Violence
- Website

The extracted data is saved to a csv file.

### Example result
A csv file with following columns and entries:

|game_title|publisher|release_date|platforms |rating|descriptors|website|
|----------|---------|------------|----------|------|-----------|-------|
|...|...|...|...|...|...|...|
|Frostpunk: The Last Autumn|Merge Games|11/06/2020|"PC, PlayStation&nbsp;4, Xbox&nbsp;One"|16|Bad Language|http://www.frostpunkgame.com/|
|Arcade Archives SUNSETRIDERS|HAMSTER Corporation|11/06/2020|PlayStation&nbsp;4|12|Violence| |
|Many Faces|Eastasiasoft Limited|10/06/2020|PlayStation&nbsp;4|3| |http://www.eastasiasoft.com|
|...|...|...|...|...|...|...|

### Speed
Very slow.

