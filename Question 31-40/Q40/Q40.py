CURRENCY = {
    100.00: 'ONE HUNDRED',
    50.00: 'FIFTY',
    20.00: 'TWENTY',
    10.00: 'TEN',
    5.00: 'FIVE',
    2.00: 'TWO',
    1.00: 'ONE',
    0.50: 'HALF DOLLAR',
    0.25: 'QUARTER',
    0.10: 'DIME',
    0.05: 'NICKEL',
    0.01: 'PENNY',
}

DENOMINATION = [100.00, 50.00, 20.00, 10.00, 5.00, 2.00, 1.00, 0.50, 0.25, 0.10, 0.05, 0.01, None]

PP, CH = tuple(map(int, input().split()))

if CH<PP:
    print("ERROR")
elif CH==PP:
    print("ZERO")
else:
    diff = CH-PP

    current = 0
    final = set()
    while DENOMINATION[current]:
        if diff==DENOMINATION[current]:
            final.add(CURRENCY[DENOMINATION[current]])
            break
        elif diff>DENOMINATION[current]:
            final.add(CURRENCY[DENOMINATION[current]])
            diff-=DENOMINATION[current]
        else:
            current+=1

    for element in list(final)[:len(final)-1]:
        print(element, end=";")
    print(list(final)[len(final)-1])