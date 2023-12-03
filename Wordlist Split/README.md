# Wordlist Split

## Description

A simple Python script to split large wordlists.

I tested it on the 2013 RockYou wordlist which has over 14,000,000 entries.

The script reads the wordlist and counts the lines. Instead of loading the entire file in memory it reads and writes, one line at time. This allows for large wordlists to be run that exceed available memory.

At the end the script displays how long the operation took. It also prints out the line count in the original wordlist as well as the line count of the split wordlists.

## Output Preview

![2023-12-03 10_26_37-main py - split_wordlist - Visual Studio Code](https://github.com/rubileandro/Python-Projects/assets/93342175/f540ea90-eb21-4534-a736-f42322bc1f4d)

## Things to Consider:
- I haven’t implemented any error handling but if there are non-utf8 characters then it may not work properly.
- The line count may be slightly different depending on the what tool is being used and the OS.
