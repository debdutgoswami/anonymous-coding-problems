# Stock Buy and Sell

Given an array of prices, find the maximum profit one can make by buying and selling at various intances of time.

## Example 1

### Input

```
5
1 5 3 8 12
```

### Output

```
13
```

### Explaination

We buy the stock when it is first `1` then sell it at `5` making a profit of `4`. Again, we buy the stock when it is `3` and sell it when it is `12` thus making the profit to be `9`. So, the total profit adds up to be `13`.

## Solution

The idea is to find the local maxima and local minima and then subtract pair wise local minima from local maxima.

## Complexity

Time: O(N)
Space: O(N)
