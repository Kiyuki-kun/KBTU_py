def spy_game(nums):
    for i in range(len(nums)-2):
        if nums[i] == 0 :
            for k in range(i, len(nums)-1):
                if nums[k] == 0 :
                    for j in range(k, len(nums)):
                        if nums[j] == 7 : 
                            return True
    return False

'''
spy_game([1,2,4,0,0,7,5]) => True
spy_game([1,0,2,4,0,5,7]) => True
spy_game([1,7,2,0,4,5,0]) => False
'''