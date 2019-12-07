# Problem

Chef has a sequence A1,A2,…,AN. He needs to find the number of pairs (i,j) (1 ≤ i < j ≤ N ) such that Ai+Aj=Ai⋅Aj. However, he is busy, so he asks for your help.

## Input

The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains a single integer N.
The second line contains N space-separated integers A1,A2,…,AN.

## Output

For each test case, print a single line containing one integer ― the desired number of pairs.

# Example Input

```
2
3
2 4 2
3
0 2 3
```

## Example Output

```
1
0
```

## Explanation

```
Example case 1: The only valid pair is (1,3).

Example case 2: We can see that no valid pair exists.
```

## Complexity

O(n)
