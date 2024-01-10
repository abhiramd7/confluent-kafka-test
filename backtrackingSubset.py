

def subsetsWithoutDuplicates(nums):
    subsets, curSet = [], []
    helper(0, nums, curSet, subsets)
    return subsets


def helper(i, nums, curSet, subsets):
    if i >= len(nums):
        subsets.append(curSet.copy())
        return
    
    #decision to include nums[i]
    ## 0 (0, [1, 2, 3], [], [])  
    #--> 1 (1, [1, 2, 3], [1], []) 
    curSet.append(nums[i])
    helper(i + 1, nums, curSet, subsets)
    curSet.pop()

    #decision not to include nums[i]
    helper(i + 1, nums, curSet, subsets)


if __name__ == "__main__":
    print(subsetsWithoutDuplicates([1, 2, 3]))

