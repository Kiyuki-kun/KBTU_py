def spy_game(nums):
    for i in range(len(nums) - 2):
        if nums[i] == 0:
            for  j in range(i + 1, len(nums)):
                if nums[j] == 0:
                    for  k in range(j + 1, len(nums)):
                        if nums[k] == 7:
                            print("True")
                            return True
    print("False")
    return False

spy_game([1,2,4,0,0,7,5]) 
spy_game([1,0,2,4,0,5,7]) 
spy_game([1,7,2,0,4,5,0]) 