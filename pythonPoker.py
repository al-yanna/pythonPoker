# Poker Hand Evaluator
# Created by: Alyanna Santos


def evaluate(hand):
    givenRanks = ''
    highestRank = ''
    # orderRanks is a string of every possible rank in a poker-hand game in order of value.
    orderRanks = '23456789TJQKA'

    # This loop extracts every even position of the hand and adds it to the givenRanks string.
    for char in hand[0::2]:
        givenRanks += char

    # Full House: This double for loop counts 3 of the same rank then 2 of another same rank and returns full house.
    for rank in givenRanks:
        for otherRank in givenRanks:
            if givenRanks.count(rank) == 3:
                if givenRanks.count(otherRank) == 2:
                    return 'full house'

    # Four of a Kind, Three of a Kind, and Pair: This loop counts 4, 3, and 2 of the same rank in the hand and returns
    # to its corresponding definition.
    for rank in givenRanks:
        if givenRanks.count(rank) == 4:
            return 'four of a kind'
        elif givenRanks.count(rank) == 3:
            return 'three of a kind'
        elif givenRanks.count(rank) == 2:
            return 'pair'

    # Flush: This condition extracts every odd position of the hand (which are the suits) and if all of the positions
    # are the same (which means they are the same suit), it will return flush.
    if hand[1] == hand[3] == hand[5] == hand[7] == hand[9]:
        return 'flush'

    # Highest Rank: This double for loop iterates through every rank in the orderRanks string, then iterates through
    # every rank in the given hand. The last rank in the orderRanks string that is equivalent to a rank in the
    # given hand is the highest rank.
    for orderRank in orderRanks:
        for rank in givenRanks:
            if orderRank == rank:
                highestRank = rank
    return str(highestRank) + str(' high')


evaluate(hand='')

# Testing:
# test = ['Qs7s2s4s5s', '7h8hKsTs8s', '2h4d2d4s4c', 'KsKhKc8sKd', '3s9hTh9s9d', '2s8hThQs9d']
# for hand in test:
#    print(evaluate(hand))

# Expected Output:
# flush
# pair
# full house
# four of a kind
# three of a kind
# Q high
