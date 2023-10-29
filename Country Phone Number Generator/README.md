## Country phone number generator 
This country phone number generator is a python script to audit passwords for businesses, with possible OSINT applications. 

### Definitions:
Mobile Prefix: These are the 3 or 4 digits at the beginning of a mobile phone number, after the country code. It helps identify the specific mobile carrier or network to which the number belongs. The exact terminology might vary by country or region, but as this project is based on Mauritian data, we will use the term “Mobile Prefix”.

### Problem: 
Network administrators struggle to always enforce secure password policies and enforcing them is not always possible, due to management guidelines. However, in such situations the administrator may still want to know whether employees are using phone numbers as their passwords. This tool generates every possible* mobile phone number (in this case for Mauritius) and outputs the generated numbers to a .txt file which can then be used to present to management and make a case for changing password policy or to use in purple team exercises.
*I say “possible” because some numbers will not be currently in use - and may likely never be used. 

As the numbers are often reused once a subscriber cancels their contract. They are often assigned to someone else shortly thereafter. Secondly, it is likely that some numbers are not disclosed publicly and may be reserved for law and order or military, for example. Still, it is quite a comprehensive range of valid and potentially in use mobile phone numbers, which can be used to audit password in the business.

### System:
This system can be applied to other countries as well. Firstly, find out what entity in the country is the “numbering authority”. 

This is a government or private entity (depending on the country) that is assigned the responsibility of assigning all number spaces for the entire country. The terms differ from country to country, but numbering authority is a common designation. Another phrase that may help when doing a search include “communications authority”. 

Secondly, if the numbering authority has made the mobile prefixes publicly available this is a best-case scenario – otherwise you will need to research what are some mobile prefixes that are known.
In the case of Mauritius, the [Information and Communication Technologies Authority](https://www.icta.mu/mobile-prefixes/) (ICTA) lists the mobile prefixes and offers them in a variable of formats such as CSV and Excel and even breaks them down by network provider, this is quite helpful and impressive. 

Mauritius mobile numbers are 8 digits long, and all begin with the number 5. 

I wrote a Python script that takes a dictionary containing all the network providers in Mauritius and their mobile prefixes (network numbers), and for each one will generate every possible 8 digit mobile phone number, without modifying the prefixes.

Here is a screenshot example output:
![example](https://github.com/rubileandro/Python-Projects/assets/93342175/8186d1b6-2436-4383-a0db-2eabd18b3ae6)

Generating all of the possible numbers gave me a list of 4,290,000 numbers.

As an aside, the population size of the Republic of Mauritius is 1,262,523.

### Permutation Space
- Cellplus Mobile Communications Ltd will generate 1,750,000 numbers.
- Emtel Ltd will generate 1,730,000 numbers.
- Mahanagar Telephone (Mauritius) Ltd will generate 810,000 numbers.

The total number of phone numbers generated for all providers is 4,290,000 numbers.

Since each 4-digit number can be followed by 4 more digits to make up the 8 digits for a phone number, each 4-digit network number will have 10,000 possible phone numbers (10^4). The 3-digit network numbers will each have 100,000 possible phone numbers (10^5).

Total numbers for 5 four-digit network numbers: 
- 5 x 10,000 = 50,000

Total numbers for 17 three-digit network numbers:
- 17 x 100,000 = 1,700,000

Total numbers for Cellplus Mobile Communications Ltd:
- 50,000 + 1,700,000 = 1,750,000

**1. Cellplus Mobile Communications Ltd**
- 5 network numbers with 4 digits
- 17 network numbers with 3 digits

**2. Emtel Ltd**
- 23 network numbers with 4 digits
- 15 network numbers with 3 digits

Total numbers for 23 four-digit network numbers: 
- 23 x 10,000 = 230,000

Total numbers for 15 three-digit network numbers:
- 15 x 100,000 = 1,500,000

Total numbers for Emtel Ltd:
- 230,000 + 1,500,000 = 1,730,000

**3. Mahanagar Telephone (Mauritius) Ltd**
- 1 network number with 4 digits
- 8 network numbers with 3 digits

Total numbers for 1 four-digit network number: 
- 1 x 10,000 = 10,000

Total numbers for 8 three-digit network numbers:
- 8 x 100,000 = 800,000

Total numbers for Mahanagar Telephone (Mauritius) Ltd:
- 10,000 + 800,000 = 810,000
