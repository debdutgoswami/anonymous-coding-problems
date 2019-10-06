# Problem:</br>

Chef is really interested in the XOR operation. He wants to take a sequence A0,A1,…,AN−1 and for each i from 0 to K−1 inclusive (in this order, one by one), perform the following operation:</br>

1. Let's denote a=Ai%N and b=AN−(i%N)−1 before this operation.</br>
2. Change Ai%N to a⊕b, i.e. a XOR b.</br>
Since Chef is busy, he asked you to find the final sequence he should get after performing these operations.</br>

## Example Input</br>
1</br>
2 2</br>
1 2</br>
## Example Output</br>
3 1</br>
