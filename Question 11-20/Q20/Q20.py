"""approach:

    Here we have a for loop to go through each character of String e.g. for input "123" this loop will run three times.
    In each iteration, we are making a recursive call to function itself  i.e. permutation(String word, String perm)  method,
    where the second parameter is used to store the result.


After 1st iteration perm (second parameter of permutation() method) will be "" + 1 as we are doing word[i]
and i is zero. Next, we take out that character and pass the remaining characters to permutation method again
e.g. "23" in the first iteration. Recursive call ends when it reaches to base case i.e. when remaining word becomes empty,
at that point "perm" parameter contains a valid permutation to be printed. You can also store it into a List if you want to.
"""
class Solution:
    def permutation(self, word: str, perm: str = ""):
        if(len(word)==0):
            print(perm+word)
        else:
            for i in range(len(word)):
                self.permutation(word[:i]+word[i+1:], perm+word[i])

Solution().permutation("1234")