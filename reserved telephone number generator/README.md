# Proof of Concept: Generate “reserved”/ “protected” telephone numbers.

### Introduction
In a [previous project](https://github.com/rubileandro/Python-Projects/tree/main/Country%20Phone%20Number%20Generator) I put together a program and laid out a method to generate every single possible mobile phone number in for a given country.

In this project the code is an example that can be applied to many different countries. In my case, I used my own country, South Africa.

This program will generate every possible* telephone/landline number that is “protected”, also referred to as “reserved” numbers. These are numbers that are not available to the public, such as emergency medical services, military, and government lines. 

Under this category are also numbers that have not been released. However, these usually are demarcated “unallocated”, rather than “protected” or “reserved”.

This information at the time of writing this program was publicly available and free. The government gazette of 2016 lists the “protected” prefixes of the numbering plans, and even distinguishes between “private” of which there are 12 reserved number ranges as “protected”, and one “unallocated” that is also “protected”.

The Numbering Plan Regulations can be found [here](https://www.ellipsis.co.za/wp-content/uploads/2016/03/Numbering-Plan-Regulations-2016.pdf) and [here](https://www.icasa.org.za/legislation-and-regulations/numbering-plan-regulations) at the Independent Communications Authority of South Africa, they are also published in the government gazette of 2016. At the time of writing it had 16 saves on archive.org.

*I say “possible” because some numbers may not be in use yet.

### Why?
Why generate these? A network administrator with the proper authorization and permissions could use these to audit the passwords used by staff to ensure that they are not using phone numbers as passwords, this is a potential vulnerability and testing for these would be part of securing these communication channels. 
I have not included the generated numbers, to prevent abuse. 

Here are the output metrics: 
- Total number of phone numbers generated: 120,000,000
- Size of 'numbers.txt': 1.3GB
- Time taken: 3 minutes and 48 seconds

  ![2023-11-05 08_23_02-telephone_number – main py](https://github.com/rubileandro/Python-Projects/assets/93342175/0b7a8fcf-d1e4-4133-b322-660eaa3e1c96)


This was run on a laptop on battery power with Ryzen 7, RTX3050, 2021 model.

### How?
This is just a simple script that will read through a list of area codes (private). I chose to use a .txt file and had one area code on each line, but you could use JSON, CSV or other options. Then for each area  code, generate every possible 10 digit number, area code included, without modifying the area codes. The program pads with zeros so that there are zeros and no blank spaces for numbers like:
011-0000001 

### Math
The Cartesian product is as follows; since we have 12 3-digit area codes, we multiply this 7-dimensional space (7 digits remaining after the prefix) by 12 to account for the 12 fixed starting points provided by each area code. Therefore, the entire combinatorial space encompassing all 12 area codes is calculated as 12×10^7.



 
### Considerations
-	If indeed these are meant to be private but are still contactable from any other number then they should be put on a closed network like PBX, if they are not already in combination with other access control measures.
-	If the above is not an option, then for future publication “protected” prefixes should be omitted.
-	It could be questioned whether “protected” and “unallocated” should be published in the gazette, as this reduces subset size. 
-	Assuming that the numbers are contactable, it would not take too much work to find in-use private numbers.

Here is a theoretical scenario to understand the risks and implication of publishing these prefixes:

While the completed list is 120,000,000 numbers, someone does not need to try every single one. They would only need to pick for example 5 numbers at random, per private area code, and then through trial and error phone them and see if there is an answer, which would open the door for further reconnaissance and phishing attack vectors.
Therefore, as previously mentioned, unless there some sort of measure in place to prevent abuse, prefixes should not be made publicly available. 
Even in the case of 14-digit numbers which take around 1.5 Petabytes, one could generate manageable sample sizes of potential numbers per each area code. 

Additionally, I speculate that one could make the assumption, which could be entirely wrong, that there is a similar pattern to existing numbers or known services, such as police station phone numbers, government departments, or even allocated mobile phone numbers, and using predictive modelling, one could take a sample of these known numbers to enumerate numbers based on statistical inference techniques. 

Even without these sophisticated techniques one could exclude options that would be hard to remember as Telecommunications Service Providers as known to allocate numbers based on ease of use. Sometimes repeating numbers and patterns are considered premium, this would further help narrow down “protected” numbers in use.

Therefore, the total combinatorial space by itself is not enough to rely on these “protected” numbers remaining private.

I suspect that the prefixes are made public because it is considered too difficult to guess the right one. 

### Disclaimer
Use this program responsibly and within the bounds of the law. The script and information are provided here to help each other better secure networks where there is the proper and legal authorization to perform such audits. Consult your legal regulation and laws if unsure.
