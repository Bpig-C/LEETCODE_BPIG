def removeElement1(nums, val):
    # 暴力解法
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    暴力法：
    两层循环：一层循环遍历数组；另一层更新数组
    问题
        为什么一定要用while:for i in range() 函数会自动将i加一，这样就不能控制遍历指针，故一定要使用while
        遍历指针前移与否的前提：遍历指针一定要前移，因为在遍历过程中，该结点在覆盖之后会向后遍历，该点会被忽略
        为什么覆盖是i到n-1而不是到n：如果到n的话，没有第n+1个元素与其对应，故[<range(i, n-1)>:<nums[j] = nums[j+1]>][<range(i+1, n)>:<nums[j-1] = nums[j]>]

    """
    n = len(nums)
    i = 0
    while i < n:
    # for i in range(n):
        if nums[i] == val:
            for j in range(i, n-1):
                nums[j] = nums[j+1]
            n -= 1
            i -= 1
        i += 1
    return n



def removeElement2(nums, val):
    # 双指针法
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    双指针法
    问题：
        FastIndex < n-1
        while nums[FastIndex] == val:
            FastIndex += 1
    """
    n = len(nums)
    SlowIndex = 0
    FastIndex = 0
    # 遍历数组
    if n == 1:
        if nums[FastIndex] == val:
            return SlowIndex
        else:
            nums[SlowIndex] = nums[FastIndex]
            return SlowIndex+1
    while FastIndex < n-1:
        # 判断指定元素
        while nums[FastIndex] == val:
            # 若快指针不是最后一个时，则将快指针向后移动继续判断其值
            FastIndex += 1
        # 将快指针所指需要的元素，放入慢指针所指位置形成新的序列
        nums[SlowIndex] = nums[FastIndex]
        # 快慢指针后移
        FastIndex += 1
        SlowIndex += 1
    return SlowIndex


if __name__ == '__main__':
    # 准备数据
    nums = [3,3]
    val = 5
    # len = removeElement1(nums, val)
    len = removeElement2(nums, val)
    print(len)
    print('[', end='')
    for i in range(len):
        print(nums[i], end='\t')
    print(']', end='')


