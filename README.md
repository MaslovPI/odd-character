# Odd Character

Into the Odd TTRPG character sheet generator

## Motivation

One of the best things about Mothership TTRPG is its [companion app](https://www.tuesdayknightgames.com/pages/mothership-companion-app).
But Mothership is not the only cool TTRPG in the world.
I really, really like Chris McDowall's [Into The Odd TTRPG](https://freeleaguepublishing.com/games/into-the-odd/).
And I believe it should have as easy entry way for the players as Mothership.
This is a start.

## Quick start

Install using pip:

```bash
pip install -e .
```

Or uv:

```bash
uv venv
source .venv/bin/activate
uv pip install -e .
```

To generate a character run:

```bash
odd-character
```

## Usage

```bash
odd-character [command]
```

Available generators:

- `character` - (default) generates full Into The Odd character
- `pet` - generates a random pet
- `hire` - generates a random hireling
- `arcana` - generates a random Arcanum

## Example

```bash
odd-character arcana
```
