def to_bits(n: int) -> str:
    return '{0:08b}'.format(n)

def reverse_num_bits(num: int) -> int:
    bnum = to_bits(num)
    bnum = "0"*(32-len(bnum))+bnum
    rbnum = bnum[::-1]
    return int(rbnum,2)

print(reverse_num_bits(1234))