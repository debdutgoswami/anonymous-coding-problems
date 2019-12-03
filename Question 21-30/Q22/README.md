# Problem

Given a string, return the first recurring letter that appears. If there are no recurring letters, return None.

## complexity

The most naive approach will be to search each element on the same string over and over again which gives it a complexity of ```O(n)```

The next approach is to sort the input string and then match every character with it's immediate next character. So, here the minimum sorting technique is ```O(n log n)```

And now the best approach is to use hashing to solve this problem. This reduces the complexity to ```O(n)```

## Example

```
Input: qwertty
Output: t

Input: qwerty
Output: None
```