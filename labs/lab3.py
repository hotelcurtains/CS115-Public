def change(amount, coins):
    '''
    change(amount, coins) returns the lowest number of elements from list coins it takes 
    to add up to amount. this is not destructive, which allows each element to be
    used multiple times if necessary.
    '''
    if coins == []:
        if amount == 0:
            return 0
        else:
            return float("inf")
    elif amount < 0:
        return float("inf")
    else:
        use_it = 1 + change(amount - coins[0], coins[1:])
        lose_it = change(amount, coins[1:])
        double_it = 1 + change(amount - coins[0], coins)
        return min(use_it, lose_it, double_it)

