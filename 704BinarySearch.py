def traverse(nums, target):  # 定义遍历函数函数
    """
        :type nums: List[int]
        :type target: int
        :rtype: int
        描述：给定序列为升序
    """
    n = len(nums)
    for i in range(n):
        if nums[i] == target:
            return i
    return -1


def BinarySearch(nums, target):
    n = len(nums)
    low, high = 0, n - 1
    while low <= high:
        mid = int((low + high) / 2)
        if low > high:
            return -1
        else:
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            elif nums[mid] == target:
                return mid
    return -1


if __name__ == '__main__':
    # 准备数据
    nums = [-1,0,3,5,9,12]
    target = 9
    # rtype = traverse(nums, target)
    rtype = BinarySearch(nums, target)
    print(rtype)

"""
        三个边界条件：
            right=numsize（还是numsize-1）
            while（left<（还是<=）right）
            right=middle（还是middle-1）
        判断遍历的范围（循环不变量）：左闭右闭[left,right]，左闭右开[left,right)
        *所有边界处理都要基于边界的定义来判断
            1.左闭右闭[left,right]：
                right = numsize - 1
                while(left <= right)
                right = middle - 1
            2.左闭右开[left,right)：
                right = numsize
                while(left < right)
                right = middle   
"""
