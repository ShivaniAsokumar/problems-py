""" 
!PROMPT: Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

TODO: Understand
? What happens when the needle is an empty string 
    // We will return 0 if the needle is an empty string. 
* Input: Needle (String) and Haystack (String)
* Returns the index of the first occurence of the Needle in the Haystack
* Return -1 if Needle is not found in Haystack
* They are all lowercase letters

? What happens if haystack is an empty string and needle is not empty



TODO: Match
* String.find() 

TODO: Pseuodocode
def strStr(haystack, needle):
    if needle.length == 0:
        return 0
    else:
        return haystack.find(needle)

"""

def strStr(haystack, needle):
    if len(needle) == 0: # Needle is an empty string
        return 0
    if len(haystack) == 0:
        return "Haystack is an empty string"
    else:
        return haystack.find(needle)

print(strStr("shivani", "i"))

