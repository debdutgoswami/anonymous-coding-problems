def divide(product: int, divisor: int) -> tuple:
    """this function returns the quotient and remainder of division between two numbers.

    Arguments:
        product {int} -- dividend
        divisor {int} -- divisor

    Returns:
        tuple -- pair of quotient and remainder
    """

    sign = -1 if(product<0 or divisor<0) else 1

    product = abs(product)
    divisor = abs(divisor)

    quotient = 0
    while(product>=divisor):
        product -= divisor
        quotient += 1

    quotient = sign*quotient
    remainder = product

    return (quotient, remainder)

print(divide(10,3))