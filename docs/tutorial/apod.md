# Astronomy Picture of the Day (APOD)

APOD highlights an interesting astronomical image or photograph every day, accompanied by a brief description written by a professional astronomer. These images can encompass a variety of celestial objects, such as stars, galaxies, nebulae, planets, and other cosmic phenomena.

The apod subcommand provides information about the image of the current day or a specific day, and can also download the image of the day by passing a flag that we will see later.

## Requesting the current day's image

You can call APOD (Astronomical Image of the Day) through the command line. Example:

<div class="termy">

```console
$ {{commands.run}} apod
<strong>The Upper Michigan Blizzard of <span style="color: cyan">1938</span></strong>

Yes, but can your blizzard do this? In the Upper Peninsula of Michigan's Storm of the Century in 1938, some snow drifts reached the level of utility poles. Nearly a meter of new and unexpected snow fell over two days in a storm that started 86 years ago this week.  As snow fell and gale-force winds piled snow to surreal heights, many roads became not only impassable but unplowable; people became stranded, cars, school buses and a train became mired, and even a dangerous fire raged. Two people were killed and some students were forced to spend several consecutive days at school.  The featured image was taken by a local resident soon after the storm. Although all of this snow eventually melted, repeated snow storms like this help build lasting glaciers in snowy regions of our planet Earth.

<strong>Image link:</strong> <a href="https://apod.nasa.gov/apod/image/2401/snowpoles_brinkman_960.jpg">https://apod.nasa.gov/apod/image/2401/snowpoles_brinkman_960.jpg</a>
```

</div>

!!! note
    This was the image of the day on the date January 21, 2024. Which was when this part of the documentation was written 😅

## Requesting an image from a specific day

| Flag   | Short | Argument |
|--------|-------|----------|
|`--date`|`-d`|AAAA-MM-DD| 

Through this flag, it is possible to specify a specific day in the past to consult the image of the day. The date must be passed in [ISO 8601](https://pt.abcdef.wiki/wiki/ISO_8601) format (YYYY-MM-DD), example: 2021-10-29.

Example:

<div class="termy">

```console
$ {{commands.run}} apod -d 2022-01-01
<strong>The Full Moon of <span style="color: cyan">2021</span></strong>
Copyright: Soumyadeep Mukherjee

very Full Moon of 2021 shines in this year-spanning astrophoto project, a composite portrait of the familiar lunar nearside at each brightest lunar phase. Arranged by moonth, the year progresses in stripes beginning at the top. Taken with the same camera and lens the stripes are from Full Moon images all combined at the same pixel scale. The stripes still look mismatched, but they show that the Full Moon's angular size changes throughout the year depending on its distance from Kolkata, India, planet Earth. The calendar month, a full moon name, distance in kilometers, and angular size is indicated for each stripe. Angular size is given in minutes of arc corresponding to 1/60th of a degree. The largest Full Moon is near a perigee or closest approach in May. The smallest is near an apogee, the most distant Full Moon in December. Of course the full moons of May and November also slid into Earth's shadow during 2021's two lunar eclipses.

<strong>Image link:</strong> <a href="https://apod.nasa.gov/apod/image/2201/MoonstripsAnnotatedIG.jpg">https://apod.nasa.gov/apod/image/2201/MoonstripsAnnotatedIG.jpg</a>
```

</div>

## Downloading the image

You can also download the image by adding the `--save-image` flag or its shortened version `-s`

<div class="termy">

```console
$ {{commands.run}} apod -d 2022-01-01 -s
<strong>The Full Moon of <span style="color: cyan">2021</span></strong>
Copyright: Soumyadeep Mukherjee

very Full Moon of 2021 shines in this year-spanning astrophoto project, a composite portrait of the familiar lunar nearside at each brightest lunar phase. Arranged by moonth, the year progresses in stripes beginning at the top. Taken with the same camera and lens the stripes are from Full Moon images all combined at the same pixel scale. The stripes still look mismatched, but they show that the Full Moon's angular size changes throughout the year depending on its distance from Kolkata, India, planet Earth. The calendar month, a full moon name, distance in kilometers, and angular size is indicated for each stripe. Angular size is given in minutes of arc corresponding to 1/60th of a degree. The largest Full Moon is near a perigee or closest approach in May. The smallest is near an apogee, the most distant Full Moon in December. Of course the full moons of May and November also slid into Earth's shadow during 2021's two lunar eclipses.

<strong>Image link:</strong> <a href="https://apod.nasa.gov/apod/image/2201/MoonstripsAnnotatedIG.jpg">https://apod.nasa.gov/apod/image/2201/MoonstripsAnnotatedIG.jpg</a>
<strong><span style="color: #258e5e">Image saved as image.jpg</span></strong>
```

</div>

## Getting help

You can also get help for the apod subcommand with the `--help` flag:

```{ .txt .no-copy }
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


