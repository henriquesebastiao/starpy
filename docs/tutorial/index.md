# Intro

If you've made it this far, it means you want to know more about how `starpy` works.

The purpose of this CLI is to help astronomy enthusiasts and science lovers in general (who have a taste for technology :smile:) find information about objects in the cosmos quickly and easily.

{% include "templates/installation.md" %}

## Creating a NASA API Key

By default, you do not need to create an API key to use starpy, however the key used by default is the DEMO_KEY provided by NASA, which has the following limits:

- Hourly Limit: 30 requests per IP address per hour
- Daily Limit: 50 requests per IP address per day

With this in mind, it is much more interesting to create an API key for your use. Having an API key other than DEMO_KEY, fee limits may vary depending on the subcommand, but the defaults are:

- Hourly Limit: 1,000 requests per hour

**To create an api key follow these steps:**

Access the [NASA API website](https://api.nasa.gov/) and create your key using the form and copy it as you will need it later;

Now define an environment variable on the machine with the name `NASA_API_KEY` with the value of the key you generated. You can do this with the following command on a Linux system:

!!! warning
    Remember to replace `your-api-key` in the command with your API key.

```bash
echo 'export NASA_API_KEY="yor-api-key"' | sudo tee -a /etc/profile
```

Now restart your system. After this configuration, `starpy` will be able to read your API key when run.

## General information

### Checking API limit

All subcommands have the `--remaining` flag and its shortened version `-r`, using it is also possible to check the remaining number of requests available to the API using your API key.

Example:

<div class="termy">

```console
$ {{commands.run}} apod -d 2022-01-01 -r
<strong>The Full Moon of <span style="color: cyan">2021</span></strong>
Copyright: Soumyadeep Mukherjee

very Full Moon of 2021 shines in this year-spanning astrophoto project, a composite portrait of the familiar lunar nearside at each brightest lunar phase. Arranged by moonth, the year progresses in stripes beginning at the top. Taken with the same camera and lens the stripes are from Full Moon images all combined at the same pixel scale. The stripes still look mismatched, but they show that the Full Moon's angular size changes throughout the year depending on its distance from Kolkata, India, planet Earth. The calendar month, a full moon name, distance in kilometers, and angular size is indicated for each stripe. Angular size is given in minutes of arc corresponding to 1/60th of a degree. The largest Full Moon is near a perigee or closest approach in May. The smallest is near an apogee, the most distant Full Moon in December. Of course the full moons of May and November also slid into Earth's shadow during 2021's two lunar eclipses.

<strong>Image link:</strong> <a href="https://apod.nasa.gov/apod/image/2201/MoonstripsAnnotatedIG.jpg">https://apod.nasa.gov/apod/image/2201/MoonstripsAnnotatedIG.jpg</a>

// The reported number of remaining requests:
Remain <strong><span style="color: cyan">1997</span></strong> requests
More information at: <a href="https://api.nasa.gov/">https://api.nasa.gov/</a>

```

</div>

## The commands

`starpy` separates each of its features into subcommands that can be executed with or without passing parameters. The objective of this tutorial is to explain how the application works in command line.

**The currently available commands are:**

* [x] apod (Astronomy Picture of the Day)