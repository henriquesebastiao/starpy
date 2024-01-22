<p align="center">
    <img src="docs/assets/starpy-slogan-black.svg" alt="Preview" width="400"/>
</p>

<p align="center"><i>Always looking at the sky.</i></p>

# Starpy

Starpy is a CLI for obtaining information from astronomical objects.

So far, the entire CLI is based on NASA's open APIs for getting images and information available.

---

**Documentation:** [https://starpy.henriquesebastiao.com](https://starpy.henriquesebastiao.com)

**Source Code:** [https://github.com/henriquesebastiao/starpy](https://github.com/henriquesebastiao/starpy)

---

## How to install the CLI

To install the cli, I recommend using pipx:

```bash
pipx install starpy
```

But anyway, this is just a recommendation. You can also install using the manager you prefer. Like pip:

```bash
pip install starpy
```

## How to use?

### APOD

#### Requesting the current day's image

You can call APOD (Astronomical Image of the Day) through the command line. Example:

```bash
starpy apod
```

> This was the image of the day on the date January 21, 2024. Which was when this part of the documentation was written 😅

#### Requesting an image from a specific day

```bash
starpy apod -d 2022-01-01
```

## More information about the CLI

You can get more information as stated below, however it is interesting to read the [complete tutorial](tutorial/index.md) to learn starpy superpowers :grin:.

To discover other options, you can use the `--help` flag:

```txt
$ starpy --help

Usage: starpy [OPTIONS] COMMAND [ARGS]...                                   
                                                                             
Starpy is a CLI for obtaining information from astronomical objects.        
                                                                             
╭─ Options ─────────────────────────────────────────────────────────────────╮
│ --version             -v        Returns the version of Starpy             │
│ --help                          Show this message and exit.               │
╰───────────────────────────────────────────────────────────────────────────╯
╭─ Commands ────────────────────────────────────────────────────────────────╮
│ apod   Astronomy Picture of the Day (APOD) https://apod.nasa.gov/apod/    │
╰───────────────────────────────────────────────────────────────────────────╯
```

### More information about subcommands

You can also get information about subcommands by calling the desired subcommand with the `--help` flag:

```txt
$ starpy apod --help

Usage: starpy apod [OPTIONS]                                                
                                                                             
Astronomy Picture of the Day (APOD) https://apod.nasa.gov/apod/             
                                                                             
╭─ Options ─────────────────────────────────────────────────────────────────╮
│ --date        -d      TEXT  Date to search for the image of the day       │
│                             [default: 2024-01-22]                         │
│ --save-image  -s            Download the image                            │
│ --remaining   -r            Tells how many requests remain for the API    │
│ --help                      Show this message and exit.                   │
╰───────────────────────────────────────────────────────────────────────────╯
```