
def gcdOfStrings(str1: str, str2: str) -> str:
    if(str1=="" or str2 ==""):
        return ""

    if len(str1) <= len(str2): #standardize which string will be the divisor
        smallString = str1
        bigString = str2
    else:
        smallString = str2
        bigString = str1
    #check if lengths of strings have GCD. this is needed to determine the size of the GCD string.
    numerator = len(bigString)
    denominator = len(smallString) #this is really a search function if you think about it. We're trying to find the smaller string in the larger string.
    #Then step through larger string and compare it's ith value to the (i mod len(GCD))th value of the smaller string
    smallNum = len(smallString)
    bigNum = len(bigString)
    GCDLength = 0
    for ii in range(smallNum,0,-1):
        if((smallNum%ii==0) & (bigNum%ii==0)):
            GCDLength = ii
            break   
    
    def checkString(entry: str, mod: int) -> bool:#check if string is a repeatable unit of size mod(i.e. the GCD size)
        for ii in range (0, len(entry)):
            if(entry[ii] != entry[ii%mod]):
                return 0
        return 1
    
    def compare2strings(string1: str, string2: str, mod: int) -> bool:#compare the first mod number of characters of each string
        for ii in range (0, mod):
            if(string1[ii] != string2[ii]):
                return 0
        return 1
    if(checkString(smallString,GCDLength) & checkString(bigString,GCDLength) & compare2strings(smallString, bigString, GCDLength)):
        return smallString[0:GCDLength]
    else:
        return ""

print(gcdOfStrings("ABCABC","ABC"))




#     '''For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

# Example 1:

# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"
# Example 2:

# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"
# Example 3:

# Input: str1 = "LEET", str2 = "CODE"
# Output: ""
 

# Constraints:

# 1 <= str1.length, str2.length <= 1000
# str1 and str2 consist of English uppercase letters.'''