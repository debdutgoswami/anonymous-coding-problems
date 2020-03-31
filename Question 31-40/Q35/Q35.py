
def climbingLeaderboard(scores, alice):
    rank = dict()
    prev = 1
    for score in scores:
        if not rank.get(score, 0):
            rank[score] = prev
            prev+=1
    for al in alice:
        if al>scores[0]:
            yield 1
        elif al<scores[len(scores)-1]:
            yield rank[scores[len(scores)-1]]+1
        else:
            low = 0
            high = len(scores)-1
            while low<=high:
                mid = (low+high)//2
                if scores[mid]==al:
                    yield rank[scores[mid]]
                    break
                elif scores[mid]<al and al<scores[mid-1]:
                    yield rank[scores[mid]]
                    break
                elif scores[mid]>al and al>scores[mid+1]:
                    yield rank[scores[mid]]+1
                    break
                elif scores[mid]<al:
                    high = mid-1
                elif scores[mid]>al:
                    low = mid+1


if __name__ == '__main__':

    scores_count = int(input())
    scores = list(map(int, input().rstrip().split()))
    alice_count = int(input())
    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)
    print(result)
