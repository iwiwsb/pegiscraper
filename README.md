# PEGI Scraper

PEGI Scraper is the python script that extracts information about videogames from [PEGI](https://pegi.info) website, such as:
<ul>
  <li>Game title</li>
  <li>Publisher</li>
  <li>Release date</li>
  <li>Platforms</li>
  <li>
    <details>
      <summary>Rating</summary>
      <ul>
        <li>3+</li>
        <li>7+</li>
        <li>12+</li>
        <li>16+</li>
        <li>18+</li>
      </ul>
    </details>
  </li>
  <li>
    <details>
      <summary>Content descriptors</summary>
      <ul>
        <li>Bad language</li>
        <li>Discrimination</li>
        <li>Drugs</li>
        <li>Fear</li>
        <li>Horror</li>
        <li>Gambling</li>
        <li>In-Game Purchases</li>
        <li>Sex</li>
        <li>Violence</li>
      </ul>
    </details>
  </li>
  <li>Website</li>
</ul>

The extracted data is saved to a csv file.

### Example result
A csv file with following columns and entries:

|game_title|publisher|release_date|platforms |rating|descriptors|website|
|----------|---------|------------|----------|------|-----------|-------|
|...|...|...|...|...|...|...|
|Frostpunk: The Last Autumn|Merge Games|2020-06-11|"PC, PlayStation&nbsp;4, Xbox&nbsp;One"|16|Bad Language|http://www.frostpunkgame.com/|
|Arcade Archives SUNSETRIDERS|HAMSTER Corporation|2020-06-11|PlayStation&nbsp;4|12|Violence| |
|Many Faces|Eastasiasoft Limited|2020-06-10|PlayStation&nbsp;4|3| |http://www.eastasiasoft.com|
|...|...|...|...|...|...|...|

### Speed
Very slow.

