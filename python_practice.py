#two strings s & goal are given, return true if and only if s can become goal after any number of shifts on s
def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)
        for i in range(n): 
            shifted_s = s[i:] + s[:i]  # i to end and start to i
            if shifted_s == goal:
                return True
        return False 
def main():
    result=rotateString(s,goal)
    print(result)

########################################################################

#logic to compress word
    def compressedString(self, word: str) -> str:
       comp = ""
       count = 1  
       for i in range(1, len(word)):
            if word[i] == word[i - 1] and count<9:  # If current char matches previous, increment count
                count += 1
            else:
                comp +=  str(count) + word[i - 1]   # Append char and count
                count = 1  # Reset count for new character
        
       comp += str(count) + word[-1]  # Append last character count
       return comp

########################################################################

