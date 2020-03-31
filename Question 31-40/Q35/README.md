# Problem

Alice is playing an arcade game and wants to climb to the top of the leaderboard and wants to track her ranking. The game uses Dense Ranking, so its leaderboard works like this:

1. The player with the highest score is ranked number 1 on the leaderboard.

2. Players who have equal scores receive the same ranking number, and the next player(s) receive the immediately following ranking number.

---

## Example

### Input

```
7
100 100 50 40 40 20 10
4
5 25 50 120
```

### Output

```
6
4
2
1
```

---

## Complexity

### Time

```
O(n*log(n))
```