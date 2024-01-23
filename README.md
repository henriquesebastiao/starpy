<p align="center">
    <img src="docs/assets/skyport-slogan-white.svg" alt="Preview" width="400"/>
</p>

<p align="center"><i>Always looking at the sky.</i></p>

<p align="center">
    <a href="https://github.com/henriquesebastiao/skyport/actions/workflows/ci.yml">
        <img src="https://github.com/henriquesebastiao/skyport/actions/workflows/ci.yml/badge.svg" alt="CI status"/>
    </a>
    <a href="https://codecov.io/gh/henriquesebastiao/skyport" > 
        <img src="https://codecov.io/gh/henriquesebastiao/skyport/graph/badge.svg?token=EG2ZrqIKiH" alt="Codecov status"/> 
    </a>
    <a href="https://github.com/henriquesebastiao/skyport/blob/main/LICENSE">
        <img alt="LICENSE" src="https://img.shields.io/badge/license-BEER_WARE-red"/>
    </a>
</p>

# Skyport

Skyport is a CLI for obtaining information from astronomical objects.

So far, the entire CLI is based on NASA's open APIs for getting images and information available.

---

**Documentation:** [https://skyport.henriquesebastiao.com](https://skyport.henriquesebastiao.com)

**Source Code:** [https://github.com/henriquesebastiao/skyport](https://github.com/henriquesebastiao/skyport)

---

## How to install the CLI

To install the cli, I recommend using pipx:

```bash
pipx install skyport
```

But anyway, this is just a recommendation. You can also install using the manager you prefer. Like pip:

```bash
pip install skyport
```

## How to use?

### APOD

#### Requesting the current day's image

You can call APOD (Astronomical Image of the Day) through the command line. Example:

```bash
skyport apod
```

> This was the image of the day on the date January 21, 2024. Which was when this part of the documentation was written 😅

#### Requesting an image from a specific day

```bash
skyport apod -d 2022-01-01
```

## More information about the CLI

You can get more information as stated below, however it is interesting to read the [complete tutorial](tutorial/index.md) to learn skyport superpowers :grin:.

To discover other options, you can use the `--help` flag:

```txt
$ skyport --help

Usage: skyport [OPTIONS] COMMAND [ARGS]...                                   
                                                                             
Skyport is a CLI for obtaining information from astronomical objects.        
                                                                             
╭─ Options ─────────────────────────────────────────────────────────────────╮
│ --version             -v        Returns the version of Skyport            │
│ --help                          Show this message and exit.               │
╰───────────────────────────────────────────────────────────────────────────╯
╭─ Commands ────────────────────────────────────────────────────────────────╮
│ apod   Astronomy Picture of the Day (APOD) https://apod.nasa.gov/apod/    │
╰───────────────────────────────────────────────────────────────────────────╯
```

### More information about subcommands

You can also get information about subcommands by calling the desired subcommand with the `--help` flag:

```txt
$ skyport apod --help

Usage: skyport apod [OPTIONS]                                                
                                                                             
Astronomy Picture of the Day (APOD) https://apod.nasa.gov/apod/             
                                                                             
╭─ Options ─────────────────────────────────────────────────────────────────╮
│ --date        -d      TEXT  Date to search for the image of the day       │
│                             [default: 2024-01-22]                         │
│ --save-image  -s            Download the image                            │
│ --remaining   -r            Tells how many requests remain for the API    │
│ --help                      Show this message and exit.                   │
╰───────────────────────────────────────────────────────────────────────────╯
```