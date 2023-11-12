OSINT-Faux is a Python script that I came up with as a challenge to write a program that could be used for Open-Source Intelligence [OSINT](https://www.sans.org/blog/what-is-open-source-intelligence/) applications. 

The program takes a username, looks it up against a list or database of names, performing both a check to see if it is a Palindrome (a word spelled in reverse) or an Anagram (a word in scrambled order) for each name in the list / database. 

Some people use their real first or last name when creating online usernames for various sites and services and with something as simple as this, a real person’s name may be identified which could then be used in phishing campaigns and other social engineering attacks.
This script demonstrates how easy it is to decode and therefore serves to discourage the use of Personally Identifiable Information [PII](https://www.dol.gov/general/ppii#:~:text=Further%2C%20PII%20is%20defined%20as,with%20other%20data%20elements%2C%20i.e.%2C) when creating usernames online.

### THE DATA
In my case I used the free and publicly available [National Records of Scotland](https://www.nrscotland.gov.uk/statistics-and-data/statistics/statistics-by-theme/vital-events/names/babies-first-names) - an official government data source.

The National Records of Scotland provide full lists of babies’ first names for a range of years (in the following formats at the time of writing: CSV, PDF and Excel), in the following breakdown. 

- 1974-1979
- 1980-1989
- 1990-1999
- 2000-2009
- 2010-2019

I had 41 years of data in total from 46 separate `.csv` files. I combined all the data into one new `.csv` using the code in the `csv_append.py` file.
I have included the appended `.csv` [here]().

I then cleaned up the data so that I had a single name on each row to work with. 

After removing duplicates and empty rows, I was left with 64,849 rows.

It is interesting to note that out of forty-one years of data, there are only 64,849 unique names.

For this project I converted my `.csv` into a Python Set format for the names list, which are used to do the reverse lookup, because of the Constant Time Complexity of (O(1)) – meaning that the time it takes to complete the algo-rhythm is independent of the size of the list. It will take the same amount of time to perform a lookup a username if there are 60 or 60,000 names. Additionally, I had no other values and there weren’t any duplicates, so using the Python Set made sense.
 
### NAME DIVERSITY INDEX (NDI)
Out of curiosity, I looked up the population of Scotland in 2019 and it was 5.46 million. 

To work out how many people share on average the same name we can use the NDI to calculated roughly how many people in the population share the same name:
64,584  / 5.46 = 0.01

As an estimate that there is roughly one unique name for every 100 people in Scotland.

This means that unique names account for 1.18% of the total population in 2019. For every 100 people in the population, there are approximately 1.18 unique names.
There are other databases such as the [United States Department of Social Security](https://www.ssa.gov/oact/babynames/limits.html) and the [United States Census Bureau](https://www.census.gov/topics/population/genealogy/data/2000_surnames.html) as well as paid databases but I chose this as it was a manageable size to test and free and publicly available as well as being formatted consistently across the years, so it was easy to work with.

### THE PROGRAM 
I limited the username to 11 digits, as the jump from 11 to 12 characters is an increase in permutation that is gargantuan.
For a username with 11 characters, the number of permutations would be 11! (39,916,800), for or 12 characters, it would be 12! (479,001,600). The factorial grows extremely quickly with each additional character.

In earlier iterations of this program, I noticed that if there were multiple matches of the anagram, then it would only print out one match. For instances of several matches and to catch all of them, I got the results to output to a .txt file showing any palindrome and any anagram matches. This list of matched could then be used for further reconnaissance and OSINT operations.

I ran this on a laptop on battery power that is medium tier and it performed it instantaneously. I couldn’t detect any lag and it felt like it took less than half a second.

### DISCLAIMER
Use this on your own username as a fun exercise and to explore the potential risks. Obey your local laws and regulations. 
