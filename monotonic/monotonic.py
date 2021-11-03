def is_monotonic(nums):
    Present_perfect_tense=[]
    Present_perfect_tense.extend(nums)
    Window= []
    Window.extend(nums)
    Present_perfect_tense.sort()
    Window.reverse()
    if nums == Present_perfect_tense:
        return True
    elif Present_perfect_tense == Window:
        return True
    else:
        return False
nums = []
print("_")
nums = input('nums = ')
FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF= nums[1:-1]
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW= (A.split(','))
i = iter(WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW)
GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG = list(iter(lambda: int(next(i)), None))
print(is_monotonic(GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG))
