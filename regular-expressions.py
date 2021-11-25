# Regular expressions


# import re

# s = 'GeeksforGeeks: A computer science portal for geeks'

# match = re.search(r'portal', s)

# print('start index:', match.start())
# print('end index:', match.end())

'''
Note: Here r character (r’portal’) stands for raw, not regex. The raw string is slightly different from a regular string, it won’t interpret the \ character as an escape character. This is because the regular expression engine uses \ character for its own escaping purpose

MetaCharacters	Description
\	Used to drop the special meaning of character following it
[]	Represent a character class
^	Matches the beginning
$	Matches the end
.	Matches any character except newline
|	Means OR (Matches with any of the characters separated by it.
?	Matches zero or one occurrence
*	Any number of occurrences (including 0 occurrences)
+	One or more occurrences
{}	Indicate the number of occurrences of a preceding regex to match.
()	Enclose a group of Regex
'''

# using \
'''
The backslash (\) makes sure that the character is not treated in a special way. This can be considered a way of escaping metacharacters. 
'''
# import re 


# s = 'geeks.forgeeks'

# match = re.search(r'.', s)
# print(match)

# match = re.search(r'\.', s)
# print(match)


# [] – Square Brackets
'''
Square Brackets ([]) represents a character class consisting of a set of characters that we wish to match.

[0, 3] is sample as [0123]
[a-c] is same as [abc]

Invert the character class using the caret(^) symbol
[^0-3] means any number except 0, 1, 2, or 3
[^a-c] means any character except a, b, or c

^ – Caret
Caret (^) symbol matches the beginning of the string i.e. checks whether the string starts with the given character(s) or not.
^g will check if the string starts with g such as geeks, globe, girl, g, etc.
^ge will check if the string starts with ge such as geeks, geeksforgeeks,

$ – Dollar
Dollar($) symbol matches the end of the string i.e checks whether the string ends with the given character(s) or not.
s$ will check for the string that ends with a such as geeks, ends, s,
ks$ will check for the string that ends with ks such as geeks, geeksforgeeks, ks, etc.

. – Dot
Dot(.) symbol matches only a single character except for the newline character (\n).
a.b will check for the string that contains any character at the place of the dot such as acb, acbd, abbb, etc
.. will check if the string contains at least 2 characters

| – Or
Or symbol works as the or operator meaning it checks whether the pattern before or after the or symbol is present in the string or not. 
a|b will match any string that contains a or b such as acd, bcd, abcd, 

? – Question Mark
Question mark(?) checks if the string before the question mark in the regex occurs at least once or not at all.
ab?c will be matched for the string ac, acb, dabc but will not be matched for abbc because there are two b.

* – Star
Star (*) symbol matches zero or more occurrences of the regex preceding the * symbol.
ab*c will be matched for the string ac, abc, abbbc, dabc, etc. but will not be matched for abdc because b is not followed by c.

+ – Plus
Plus (+) symbol matches one or more occurrences of the regex preceding the + symbol.
ab+c will be matched for the string abc, abbc, dabc, but will not be matched for ac, abdc because there is no b in ac and d is not followed by c in abdc.

{m, n} – Braces
Braces match any repetitions preceding regex from m to n both inclusive.
a{2, 4} will be matched for the string aaab, baaaac, gaad, but will not be matched for strings like abc, bc because there is only one a or no a in both the cases.

(<regex>) – Group
Group symbol is used to group sub-patterns. 
(a|b)cd will match for strings like acd, abcd, gacd, 

Special Sequences
Special sequences do not match for the actual character in the string instead it tells the specific location in the search string where the match must occur. 


Special Sequence	Description	Examples
\A	Matches if the string begins with the given character	\Afor 	for geeks
for the world
\b	Matches if the word begins or ends with the given character. \b(string) will check for the beginning of the word and (string)\b will check for the ending of the word.	\bge	geeks
get
\B	It is the opposite of the \b i.e. the string should not start or end with the given regex.	\Bge	together
forge
\d	Matches any decimal digit, this is equivalent to the set class [0-9]	\d	123
gee1
\D	Matches any non-digit character, this is equivalent to the set class [^0-9]	\D	geeks
geek1
\s	Matches any whitespace character.	\s	gee ks
a bc a
\S	Matches any non-whitespace character	\S	a bd
abcd
\w	Matches any alphanumeric character, this is equivalent to the class [a-zA-Z0-9_].	\w	123
geeKs4
\W	Matches any non-alphanumeric character.	\W	>$
gee<>
\Z	Matches if the string ends with the given regex	ab\Z	abcdab

'''


