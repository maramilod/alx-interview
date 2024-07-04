#!/usr/bin/python3
"""
0-prime_game.py
"""


def is_winner(x, nums):
    def is_prime(n):
        """Check if n is a prime number."""
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    maria_wins = 0
    ben_wins = 0

    for _ in range(x):
        current_nums = nums.copy()
        
        while len(current_nums) > 1:
            for num in sorted(current_nums, reverse=True):
                if is_prime(num):
                    current_nums = [n for n in current_nums if n % num != 0]
                    break
        
        if len(current_nums) == 1:
            if is_prime(current_nums[0]):
                maria_wins += 1
            else:
                ben_wins += 1
        elif len(current_nums) > 1:
            raise ValueError("Invalid state: More than one number should remain at the end of a round.")


    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None
