# Odd Character

Into the Odd TTRPG character sheet generator

## Motivation

One of the best things about Mothership TTRPG is its [companion app](https://www.tuesdayknightgames.com/pages/mothership-companion-app).
But Mothership is not the only cool TTRPG in the world.
I really, really like Chris McDowall's [Into The Odd TTRPG](https://freeleaguepublishing.com/games/into-the-odd/).
And I believe it should have as easy entry way for the players as Mothership.
This is a start.

## Quick start

To generate a character run:

```bash
python3 src/odd_character/main.py
```

## Usage

Available generators:

- `character` - (default) generates full Into The Odd character
- `pet` - generates a random pet
- `hire` - generates a random hireling
- `arcana` - generates a random Arcanum

## Example

```bash
python3 src/odd_character/main.py arcana
```
