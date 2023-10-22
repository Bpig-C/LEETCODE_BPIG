def TwoSum(nums, target):  # 定义测试函数
    """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        通过：O（n^2）
    """
    i = 0
    while i < len(nums):
        j = 0
        while j < len(nums):
            if j == i:
                j+=1
                continue
            sum = nums[i] + nums[j]
            if sum == target:
                return [i, j]
            j += 1
        i += 1



if __name__ == '__main__':
    # 准备数据
    nums = [3, 2, 4]
    target = 6
    rtype=TwoSum(nums, target)
    print(rtype)

    """
       官方题解：
    一、暴力枚举
        最容易想到的方法是枚举数组中的每一个数 x，寻找数组中是否存在 target - x。
    当我们使用遍历整个数组的方式寻找 target - x 时，需要注意到每一个位于 x 之前的元素都已经和 x 匹配过，
    因此不需要再进行匹配。而每一个元素不能被使用两次，所以我们只需要在 x 后面的元素中寻找 target - x。
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
        复杂度分析
            时间复杂度：O(N^2)，其中N是数组中的元素数量。最坏情况下数组中任意两个数都要被匹配一次。
            空间复杂度：O(1)
    
    二、查找表法（哈希表）
        “思路：空间换时间”
        合为定值：target
        其中一个元素：num[i]--->推出另一个元素为：target-num[i]
        方法：
            在遍历的同时记录一些信息，以省去一层循环，这是以“空间换时间”的想法，
            需要记录已经遍历过的数值和它所对应的下标，可以借助查找实现
            查找两个常用的实现：
                哈希表
                平衡二叉树
    """
