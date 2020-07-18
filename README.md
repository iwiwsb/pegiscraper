# PEGI Scraper

:warning: <b>WARNING!</b> :warning:<br />
:radioactive: :scream: <b>DO NOT USE THIS PROGRAM.</b> :scream: :radioactive:<br />
This program is not a program of honor.

No highly esteemed function is executed here.

What is here is dangerous and repulsive to us.

The danger is still present, in your time, as it was in ours,
without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE.

This program is best shunned and left unused (but it is free software,
and you are welcome to redistribute it under certain conditions).
:radioactive: :scream: <b>DO NOT USE THIS PROGRAM.</b> :scream: :radioactive:

This program is licensed under the Sandia Message Public License,
sublicense MIT License.
This may be abbreviated as <b>sandia-mit</b>.
You may obtain a copy of the License(s) at
https://github.com/cdanis/sandia-public-license/blob/main/LICENSE.md and
https://github.com/iwiwsb/pegi-scraper/blob/master/LICENSE

## Description
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

## Example result
A csv file with following columns and entries:

|game_title|publisher|release_date|platforms |rating|descriptors|website|
|----------|---------|------------|----------|------|-----------|-------|
|...|...|...|...|...|...|...|
|Frostpunk: The Last Autumn|Merge Games|2020-06-11|"PC, PlayStation&nbsp;4, Xbox&nbsp;One"|16|Bad Language|http://www.frostpunkgame.com/|
|Arcade Archives SUNSETRIDERS|HAMSTER Corporation|2020-06-11|PlayStation&nbsp;4|12|Violence| |
|Many Faces|Eastasiasoft Limited|2020-06-10|PlayStation&nbsp;4|3| |http://www.eastasiasoft.com|
|...|...|...|...|...|...|...|

## Speed
Very slow.

