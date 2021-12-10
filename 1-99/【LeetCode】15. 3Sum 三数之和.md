
- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)
- 个人公众号：负雪明烛
- 本文关键词：3sum, 三数之和，题解，leetcode, 力扣，Python, C++, Java

---

题目地址: https://leetcode.com/problems/3sum/description/

## 题目描述：

Given an array ``nums`` of n integers, are there elements a, b, c in ``nums`` such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

    Given array nums = [-1, 0, 1, 2, -1, -4],
    
    A solution set is:
    [
      [-1, 0, 1],
      [-1, -1, 2]
    ]



## 题目大意

在给定的数组中判断是否存在三个数的和是0，返回所有的组合，但是返回的组合中不能有重复。

## 解题方法

### 方法一：统计频率+双指针

我的做法和大多数人不一样，我看了很多人的做法是对原数组排序后进行的左右指针向中间合并。而我这个做法使用的是先进行次数统计、元素去重然后做的双指针。

我的这个思路是在[923. 3Sum With Multiplicity][1]中使用的，同样地两重循环，然后查找第三个值是否在给出的数字set中，然后判断3个数字相同的有多少，可能存在三个都相同，两个相同，三个都不同的情况，这个时候需要注意的是还需要对原来的数组中该数字出现的次数进行判断。另外题目说了防止同样的组合多次返回，那么我是用了一个笨方法就是用set保存已经使用了的组合，这样能判断是否已经出现过。

时间复杂度是O(N^2)，空间复杂度是O(N)。看似操作复杂，实际上还是超过了48%的提交。

```python
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        count = collections.Counter(nums)
        values = count.keys()
        values.sort()
        print(values)
        N = len(values)
        l, r = 0, N - 1
        res = list()
        visited = set()
        for l in range(N):
            for r in range(l, N):
                t = 0 - values[l] - values[r]
                if t in count:
                    if (t == 0 and count[t] >= 3) \
                    or (((t == values[l] and t != values[r]) or (t == values[r] and t != values[l])) and count[t] >= 2) \
                    or (l == r and values[l] != t and count[values[l]] >= 2) \
                    or (t != values[l] and t != values[r] and l != r):
                        curlist = sorted([values[l], t, values[r]])
                        finger = "#".join(map(str, curlist))
                        if finger not in visited:
                            res.append(curlist)
                            visited.add(finger)
        return res
```

### 方法二：原数组排序+双指针

这个方法就是上面说的对原数组排序的做法，这个做法思路比较简单，对于排序后的数组遍历，对每个位置都从它的后一个元素和末尾一个元素向中间集中，如果和为0就添加到结果数组中。这里需要注意的地方是需要跳过相同的数字，因为同样的数字组合只能出现一次嘛。也就是两个while，注意判断相等的条件：i是向前面判断，j是向后面判断。

这个方法不用使用set来保存已经遍历过的数字组合，因为对于原数组来说每次向后遍历的过程中，同样的组合只能出现一次。

时间复杂度是O(N^2)，空间复杂度是O(1)。代码很清晰简短，实际上只超过了24%的提交。

```python
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        N = len(nums)
        nums.sort()
        res = []
        for t in range(N - 2):
            if t > 0 and nums[t] == nums[t - 1]:
                    continue
            i, j = t + 1, N - 1
            while i < j:
                _sum = nums[t] + nums[i] + nums[j]
                if _sum == 0:
                    res.append([nums[t], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
                elif _sum < 0:
                    i += 1
                else:
                    j -= 1
        return res
```



参考资料：


## 日期

2018 年 10 月 17 日 —— 今又重阳，战地黄花分外香


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/83045983
