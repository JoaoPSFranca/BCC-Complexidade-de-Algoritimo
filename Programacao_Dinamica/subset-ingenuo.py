from itertools import combinations
import time

def subset_sum_brute_force(nums, target):
    for r in range(len(nums) + 1):
        for subset in combinations(nums, r):
            if sum(subset) == target:
                return True, subset
    return False, []

start = time.time()
#print(subset_sum_brute_force([1, 2, 3, 4, 5,6], 15))
print(subset_sum_brute_force(list(range(1, 25)), 200))

end = time.time()
print('{:.4f}'.format(end-start))

