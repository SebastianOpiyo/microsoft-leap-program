
# Brute force approach.
def firstPalindrome(words: list[str]) -> str:
        for word in words:
            if word == word[::-1]:
                return word
        return ""


# Using two pointer technique
def isPalindrome(string:str)->str:
     '''A function that checks if a string is a palindrome or not. 
     A palindrome is phrase that reads the same when reversed.
     '''
     start, end = 0, len(string)-1
     
     while start < end:          
          if string[start] != string[end]:
               return False
          start += 1
          end -= 1
          return True
     return (-1)

string = "aba"
print(isPalindrome(string)) 