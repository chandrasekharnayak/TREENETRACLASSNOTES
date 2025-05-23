#Regular Expression?- regex or regexp-- string search pattern

'''
is a sequence of chacters that define a search pattern. it is used for matching , locating and manupulating text based on spesific patterns.
Regex is powerfull module or tools for text processing  and text editing and data validating.

work?

1.searching :- Find patterns in string or text (ip address, email, format)
2.Validation :- Check if a string machtes a specific format or not.
3.Extraction :- Extract spesific data from a string
4.Substituion :- Replace specific patterns with new text.
5.Splitting :- Divide a string into part based on a delimeter

create own pattern
Create Symbols, Anchors, Quantifiers, Logical Operators Special Chars, Greedy and Lazy Matching
Lookaheads abd Lookbehinds
Escape Sequence


Char Symbols

.       Matches any single char expect a newline  ---> a.b matches aab,acb
\w      Matches any alphanumeric charc(letters,digit and _) --->\w+ mtaches hi_123
\W      Matches any non-aplhanumeric char ------------------->\W matches @,#,$ or a space
\d      Matches any digit(0-9) ------------------------------>\d+ matches 123
\D      Matches any non-digit---------------------->\D+ abc
\s      Matches while space(space,tab,newline) ------------------>\s+ matches space in hello world
\S      Matches any non-whitespace charcter----------------> \S+ matches hello
\t      Matches a tab
\n      Matche a newline


Anchors

^       Matches the beginning of a string ----> ^hello-(hello world)  not match(world hello)
$       Matches the end of string------------> world$ matches (hello world)--- not matches (world hello)
\b      Matches a word boundry  ---------> \bcat ---- cat--- not match(catepillar)
\B      Matches a non-word boundary ---> \Bcat ---- matches(catepillar)--not cat

Quantifiers
-----------

*       Matche 0 or more occurrence of the preceding chactaer or group ----->a* mtache aaaa,aaa,a or empty string
+       Matche 1 or more occurrence of the preceding  charc or grp ---> a+ mtache aaaa,aaa,a or not empty string
?       Matche 0 or 1 Ocuurence of preceding char or group -----------> a? single chr or empty
{n}     Matche exactly n occurance of the preceding char or grp --- >a{3} --- aaa
{n,}    Matches at least n occurrence of the preceding charc or group --- a{2,} --aa,aaa,aaaa
{n,m}   matches between n and m occ -------------------------------------> a{2,3}---aa,aaa

Logical operator
------------------
()      groups patterns or creates capture the group  ---- (abc)+ --abcabc
(?:)    Non-Capaturing group  ----------------------------(?:abc)+ matches abcabc but does not capture


Special Ch
\       Escapes special ch to treat them a literl----------> \. ---- ., ..
[]      Matches any charcter inside  the brackets --------> [abc] ----matches , a, b,c
[^]     Matches aby char not inside the brackets----------> [^abc] --- x,y,w,u--- not a,b,c

-       Specifies a range of char -----------------------[a-z] -- macyes any lowerscase char


'''

import re

from pandas.io.formats.format import return_docstring

# print(dir(re))

'''email ---
username ---- Upper,lower,digit,_.
@
char----upper,lower,digit,-
.
char [upper,lower][2,]

'''
'''email = input('Enter your email:-')

pattern = r'^[a-zA-z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-z]{2,}$'

if re.match(pattern,email):
    print(True)
else:
    print(False)'''


ipv4--- what is ipv4





