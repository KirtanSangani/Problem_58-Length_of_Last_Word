# Problem 58: Length of Last Word

7/19/2025

## Thought Process
My initial thought process was to traverse through a while loop until there is a space. When the space is found, the while loop would end and it would return a count variable counting everytime the while loop ran. This wouldn't work for strings with spaces at the end. So in this case, I decided to count the letters instead. 

##  Initial Solution
I created an i variable which would start at len(s) - 1. I then lowercased all letters so that I can see if the characters in the string s are within the ASCII values of "a" and "z". I then created a count variable to count all the letters within the last word. I created the while loop going until i is less than 0. If s[i] is between a and z, I would add 1 to count. If count is greater than 0 and the first if statement is false, the while loop breaks. Through each iteration of the while loop, I subtract 1 from i. After the while loop, I returned count. 

Initial solution - 1 ms 

Complexity - O(n)

## Another Solution
Another solution I saw was using .split() and .strip() on s. This way, you just get a List of all the words in the String s. You would then just return the len(s[-1]), giving you the length of the last word. 

Final Solution - 0 ms

Complexity - O(1)

## Takeaways
I learned about .strip() and .split() for strings, which are really good methods for splitting strings apart by the words so you can work with a specific word if necessary. 