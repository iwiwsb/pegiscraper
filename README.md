# PEGI Scraper

PEGI Scraper is python script that extracts information about videogames from [PEGI](https://pegi.info) website.
Unfortunately, very slow.

The script parses:
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

## Example result
A csv file with following columns and entries:

|game_title|publisher|release_dates_and_platforms |rating|descriptors|website|
|----------|---------|----------------------------|------|-----------|-------|
|...|...|...|...|...|...|
|Stardew Valley|505 Games S.p.A|2018-05-24: PlayStation&nbsp;4|12|Gambling|https://www.stardewvalley.net/|
|Serious Sam 4|Devolver Digital|2020-08-13: Stadia, 2020-08-13: PC|18|Violence, Bad Language| |
|Alphaset by POWGI|Lightwood Consultancy Ltd (trading as Lightwood Games)|2020-08-17: PlayStation Vita|3| |//www.lightwoodgames.com
|...|...|...|...|...|...|


