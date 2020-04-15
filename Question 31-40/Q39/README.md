# Problem

Chef owns N cars `(numbered 1 through N)`. He wishes to sell all of them over N years by selling exactly one car per year. For each valid i, the initial price of the `i-th` car is `Pi`. Due to depreciation, the price of each car decreases by `1 unit per year` until it is sold.

Note that the price of a car cannot drop below 0 no matter how many years have passed, i.e. when the price of a car reaches `0` in some year, it remains `0` in all subsequent years.

Find the maximum profit Chef can make if he sells his cars in an optimal way. Since this number may be large, compute it modulo `1,000,000,007` (10^9+7).

## Example

### Input

```
2
3
6 6 6
3
0 1 0
```

### Output

```
15
1
```

### Explanation

**Example case 1**:

1. During the first year, Chef's profit so far is 0 and the prices of the cars are [6,6,6]. Chef sells one of these cars.

2. During the second year, Chef's profit so far is 6 and the prices of the remaining cars are [5,5]. Again, Chef sells one of these cars.

3. During the third year, Chef's profit so far is 11 and there is one car with price 4. Chef sells this car.

4. In the fourth year, Chef has sold all of his cars and his profit is 15. This is the maximum profit he can make.


**Example case 2**:

1. During the first year, Chef's profit so far is 0 and the prices of the cars are [0,1,0]. Chef sells the second car.

2. During the second year, Chef's profit so far is 1 and the prices of the remaining cars are [0,0]. Chef sells one of these cars.

3. During the third year, Chef's profit so far is 1 and there is one car with price 0. Chef sells this car.

4. During the fourth year, Chef has sold all his cars and his profit is 1.
