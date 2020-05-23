# Find the longest river (DFS)

Given a boolean 2D matrix, find the length of the longest river. A group of connected `1`s (horizontal and vertical and not diagonal) forms a river. For example, the below matrix contains 3 rivers, but the longest is `8`.

## Example

### Input

```
mat[][] = [
    [0, 0, 0, 0, 1],
    [0, 1, 0, 0, 1],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 1, 1]
]
```

### Output

```
8
```