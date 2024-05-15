#!/usr/bin/python3

"""
Prime Game Module

This module provides functionality to determine the winner of a
game played between two players, Maria and Ben, using a set of
consecutive integers starting from 1 up to and including n.
They take turns choosing a prime number from the set and
removing that number and its multiples from the set.
The player who cannot make a move loses the game.
The module includes a function to determine the overall
winner after playing multiple rounds.

Function:
    isWinner(x, nums): Determines the winner after
                    playing x rounds of the game.

"""


def isWinner(x, nums):

    """
    Determines the winner of the prime game after x rounds.

    Parameters:
    x (int): The number of rounds to be played.
    nums (list of int): A list of integers where each integer n
    represents the set {1, 2, ..., n} for a round.

    Returns:
    str: The name of the player who won the most rounds ("Maria" or "Ben").
    Returns None if there is no overall winner.
    """
    max_n = max(nums) if nums else 0

    sieve = [True] * (max_n + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes

    for start in range(2, int(max_n**0.5) + 1):
        if sieve[start]:
            for multiple in range(start*start, max_n + 1, start):
                sieve[multiple] = False

    primes = [i for i, is_prime in enumerate(sieve) if is_prime]

    prime_count_up_to = [0] * (max_n + 1)
    count = 0
    for i in range(1, max_n + 1):
        if sieve[i]:
            count += 1
        prime_count_up_to[i] = count

    results = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        if prime_count_up_to[i] % 2 == 1:
            results[i] = 1
        else:
            results[i] = 0

    maria_wins = 0
    ben_wins = 0
    for n in nums:
        if results[n] == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
