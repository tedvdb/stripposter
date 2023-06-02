### Purpose ###

Stripbot is a reddit bot which posts comics to reddit. It scrapes various comic sites, and posts to discover comics. If a new comic is discovered, it attempts to post it to ~~Reddit~~ Lemmy. 

This is a fork of the nice [bot made by @ondergetekende](https://github.com/ondergetekende/stripposter/). 

### Contributing ###

Please feel free to suggest comics by posting an [issue](https://github.com/tedvdb/stripposter/issues). Note that the stripbot hosted by /u/tedvdb will only post Dutch comics to `https://feddit.nl/c/strips`. If you want to post to a different community, you'll need to fork the repo, and host the bot yourself.

### Installation ###

You'll need:

* A lemmy account for the bot
* Linux with Python 3 (windows may work too, but this guide will not be applicable)
* The dependencies in `requirements.txt`

First you'll need to create a configuration file. Stripbot is configured using environment variables or an `.env` file, so the configuration file is simply:

```
LEMMY_BASEURL=https://feddit.nl
LEMMY_USERNAME=stripbot
LEMMY_PASSWORD=<your password here>
LEMMY_COMMUNITY_ID=<community id here>
```
Then you can run the bot once by running `./update` or repeating every 6 hours with `./update-continuous`.


