def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    time complexity: O(n)
    space complexity: O(n)
    """
    hashmap={};
    for i in range(len(nums)):
        complement = target-nums[i];
        if complement in hashmap:
            return [i,hashmap[complement]];
        hashmap[nums[i]]=i;

def main():
    """
    twoSum:
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.
    """
    nums = [2,7,11,15]
    target = 9
    res = twoSum(nums,target)
    print (res)




main();