# Find Words That Can Be Formed by Characters !!

# You are given a list of strings called `words` and a string called `chars`.

# A string is "nice" if it can be formed by characters from `chars` (each character can only be used once).

# Write a function that returns the sum of lengths of all "nice" strings in `words`.

# e.g.: if we have word = ['cat', 'dog', 'rabbit'], char = 'dborciwagt'. Then we check the first string in char, which is 'cat'.  'cat' is a "nice" string because it can be formed by using 'c', 'a' and 't' in string char. And then we check the second string 'dog', too. As for the last one, 'rabbit', we cannot form it from char, because 'rabbit' has two 'b' in it, but there is only 1 'b' in char. Finally, we count the lengths of all the "nice" strings in words, which are 'cat' and 'dog'. So we return 6 (= len('cat') + len('dog'))

# You can try to solve this problem from scratch by yourself, or you may want to follow the instructions below.

# Write your code here:



# first, let's define the function we want:

def findWordsByChar(words, chars):

    # Now think about how to design this function. The solution will be quite straight-forward: just use a loop to iterate through every string in words. And for every string, we check whether it is a "nice" string. If it is, then we add the length of the string to the final returned value; if not, we just ignore it and goes on.

    # So first we initiate the returned value, I usually use "ans" or "res" as the variable name, but you can choose whatever you want. And obviously, its initial value should be 0.
    ans = 0

    # Then we write our loop. Let's just use a simple for-loop here
    for i in range(len(words)):

        # As we iterate through every element in words, we check if it is a "nice" string.

        # How to check whether one string is a "nice" one or not? It seems to be a complicated problem now, so you may want to write another function to handle this problem.

        # Imagine you now have a "magic" function called "isNiceString()". It takes a string and char as input and return True if the input string is "nice" (the string can be formed from char), otherwise it will return False. We will implement it later, but we just use it here
        if isNiceString(words[i], chars):
            
            # As we analyzed before, if a string is "nice", we will add its length to the final answer, so
            ans = ans + len(words[i]) # or you can write ans += len(words[i])

        # Do we have to write else: ... here? 

        # Not really. Because for strings that are not "nice", we just ignore them and do nothing. So you do not have to consider other situations.

    # The loop is over. So finally we just return our answer!
    return ans

def isNiceString(string, chars):
    # As described before, this function is a "magic" function that return True if string is a "nice" string. And now we are going to implement it. 

    # Let's recap what the problem says about a "nice" string: a string is "nice" if it can be formed by characters from `chars` (each character can only be used once). 

    # e.g. if a string is composed of 2 'a' and 3 'b', then it is a "nice" one only if chars has at least 2 'a' and 3 'b'. In other words, a string is "nice" only if the frequency of every character in the string is no greater than the frequency of the same characters in chars.

    # In order to check this, we may want to know the frequency of all characters in string and chars. Generally, we use a hash table (which is dictionary in Python) to achieve this. The key of the hash table will be the character, and the value will br the frequency of the value.

    # How to obtain such hash table (dictionary)? Let's imagine, again, that we have another "magic" function called countFreq(). This countFreq() takes a string as input and return a hash table recording the frequency of each character in the input string. And we will implement it later.

    # We need 2 dictionarise for both string and chars, so:
    freqString = countFreq(string)
    freqChars = countFreq(chars)

    # And then, for every character in string, we check if its frequency in string is no greater than its frequency in chars.
    for i in range(len(string)):

        if freqString[string[i]] > freqChars[string[i]]:
            # if the frequency of one character in string is larger than that in chars, then the string is definitely not a "nice" one. So we can just return False.
            return False
        
    # After checking all the characters is OK, then we know it is a "nice" one, so we can return True.
    return True

def countFreq(string):
    # In this function, we will count the frequency of each character in the input string and record the information in a hash table.

    # So first, we initiate a dictionary first.
    freq = {}

    # Then we iterate every character in string, and increament its frequency by 1.
    # I believe you can do this part by yourself!


    # Finally, we return the resulting dictionary.
    return freq

# Here are some test cases, you can use them to check whether your code is right.

ans = findWordsByChar(['cat', 'dog', 'rabbit'], 'dborciwagt') # ans should be 6
# ans = findWordsByChar(["cat","bt","hat","tree"], "atach") # ans should be 6
# ans = findWordsByChar(["hello","world","leetcode"], "welldonehoneyr") # ans should be 10
print(ans)