# Traping Rain water

Given an array `arr[]` of `N` non-negative integers representing height of blocks at index `i` as `Ai` where the width of each block is 1. Compute how much can be trapped in between blocks after raining.

## Example 1

### Input

```
3
2 0 2
```

### Output

```
2
```

### Diagram

```
| |
|_|
```

## Example 2

### Input

```
6
3 0 0 2 0 4
```

### Output

```
10 (3+3+1+3)
```

### Diagram

```
     |
|    |
|  | |
|__|_|
```

## Solution

Sum(1 to N-1){min(max of left, max of right) - arr[i]}

Naive: O(N^2)
Optimised: O(N)
