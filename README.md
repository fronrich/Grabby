
<div align="center">

![project logo](https://github.com/fronrich/Grabby/blob/main/Grabby.png?raw=true)

# Grabby - the Google Fonts Downloader

## Created by Fronrich Puno

### Disclaimer, this is not an offical Google Product.

### It is an open-source alternative to the manual installation of Google Fonts.

</div>

This program was inspired by Andrewsomething's TypeCatcher, a gui based program to install google fonts https://github.com/andrewsomething/typecatcher . Although this program is functionally similar to TypeCatcher, Grabby is able to run on newer versions of python, and will automatically download all the latest google fonts at once.

# Installation

Before installing this program, make sure you have the following packages:

- git
- python3
- pip3

Clone the repo in the directory you want to install. `cd` into target directory and then use the command `git clone https://github.com/fronrich/Grabby.git` or `gh repo clone fronrich/Grabby` if you have the GitHub cli.

`cd` into the Grabby directory using the command `cd Grabby/`, and run `setup` in the terminal. `setup` does not to be run as root, although the script will ask you to run a few commands as root user in order to install fonts to your system and add the grabby command to your `PATH`.

And that's it! You now have the latest Google Fonts. Whenever new fonts come out, just run `grabby` in the terminal to update your font library.