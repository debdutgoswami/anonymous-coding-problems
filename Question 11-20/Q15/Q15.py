'''
Chef decided to write an infinite sequence. Initially, he wrote 0, and then he started repeating the following process:

Look at the last element written so far (the l-th element if the sequence has length l so far); let's denote it by x.
If x does not occur anywhere earlier in the sequence, the next element in the sequence is 0.
Otherwise, look at the previous occurrence of x in the sequence, i.e. the k-th element, where k<l, this element is equal to x and all elements between the k+1-th and l−1-th are different from x. The next element is l−k, i.e. the distance between the last two occurrences of x.
The resulting sequence is (0,0,1,0,2,0,2,2,1,…): the second element is 0 since 0 occurs only once in the sequence (0), the third element is 1 since the distance between the two occurrences of 0 in the sequence (0,0) is 1, the fourth element is 0 since 1 occurs only once in the sequence (0,0,1), and so on.

Chef has given you a task to perform. Consider the N-th element of the sequence (denoted by x) and the first N elements of the sequence. Find the number of occurrences of x among these N elements.

Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first and only line of each test case contains a single integer N.
Output
For each test case, print a single line containing one integer ― the number of occurrences of the N-th element.

Example Input
1
2
Example Output
2
Explanation
Example case 1: The 2-nd element is 0. It occurs twice among the first two elements, since the first two elements are both 0.
'''


def series(n):
    l = [0,0]
    for i in range(2,n):
        search = l[i-1]
        counter = l.count(search)
        if(counter>1):
            new_l = l[::-1]
            new_l = new_l[1:]
            pos = new_l.index(search)
            print(pos)
            pos = len(l[:i-2])-pos
            #print(pos)
            l.append(i-1-pos)
        else:
            l.append(0)
    return l

N = int(input())
ref = [0, 0, 1, 0, 2, 0, 2, 2, 1, 6, 0, 5, 0, 2, 6, 5, 4, 0, 5, 3, 0, 3, 2, 9, 0, 4, 9, 3, 6, 14, 0, 6, 3, 5, 15, 0, 5, 3, 5, 2, 17, 0, 6, 11, 0, 3, 8, 0, 3, 3, 1, 42, 0, 5, 15, 20, 0, 4, 32, 0, 3, 11, 18, 0, 4, 7, 0, 3, 7, 3, 2, 31, 0, 6, 31, 3, 6, 3, 2, 8, 33, 0, 9, 56, 0, 3, 8, 7, 19, 0, 5, 37, 0, 3, 8, 8, 1, 46, 0, 6, 23, 0, 3, 9, 21, 0, 4, 42, 56, 25, 0, 5, 21, 8, 18, 52, 0, 6, 18, 4, 13, 0, 5, 11, 62, 0, 4, 7]
l = []

for i in range(N):
    l.append(int(input()))

for i in l:
    element = ref[i-1]
    print(ref[:i].count(element))