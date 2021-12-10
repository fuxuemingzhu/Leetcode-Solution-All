# 【LeetCode】556. Next Greater Element III 解题报告（Python）

标签（空格分隔）： LeetCode

作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址：https://leetcode.com/problems/next-greater-element-iii/description/

## 题目描述：

Given a positive ``32-bit`` integer n, you need to find the smallest ``32-bit`` integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive ``32-bit`` integer exists, you need to return -1.

Example 1:

    Input: 12
    Output: 21
     

Example 2:

    Input: 21
    Output: -1


## 题目大意

同样的数字进行重新排列组合，找出下一个更大组合方式情况下，比当前的数字更大一点的那个。

注意是个32位的正数。

## 解题方法

和[31. Next Permutation][1]解题方式基本一模一样，先找到从后向前数，第一个降序的位置，把此位置后面的翻转。再把这个降序数字和后面第一个比它大的位置交换即可。

> 如果从第n个数字到最后都是递减的并且第n-1个数字小于第n个，说明从第n个数字开始的这段序列是字典序组合的最后一个，在下一个组合中他们要倒序变为字典序第一个，然后从这段序列中找出第一个大于第n-1个数字的数和第n-1个数字交换就可以了。
> 
> 举个栗子，当前组合为12431，可以看出431是递减的，同时4>2，这样我们把431倒序，组合就变为12134，然后从134中找出第一个大于2的数字和2交换，这样就得到了下一个组合13124。对于完全递减的组合例如4321在倒序之后就可以结束了。

大体和Leetcode的这个解答方式类似：

![此处输入图片的描述][2]

十分需要注意的是，找到了下一个更大的数字，有可能超出了题目中所说的32位的正数。需要额外注意。

代码如下：

```python
class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = list(str(n))
        n = len(nums)
        i = n - 1
        while i > 0 and nums[i] <= nums[i - 1]:
            i -= 1
        if i == 0:
            return -1
        self.reverse(nums, i, n - 1)
        for j in range(i, n):
            if nums[j] > nums[i-1]:
                self.swap(nums, i-1, j)
                break
        ans = int("".join(nums))
        if ans > 1 << 31:
            return -1
        else:
            return ans
        
    def reverse(self, nums, i, j):
        """
        contains i and j.
        """
        for k in range(i, (i + j) / 2 + 1):
            self.swap(nums, k, i + j - k)

        
    def swap(self, nums, i, j):
        """
        contains i and j.
        """
        nums[i], nums[j] = nums[j], nums[i]
```

参考资料：

1. https://leetcode.com/articles/next-permutation/
1. https://blog.csdn.net/tstsugeg/article/details/50261517

## 日期

2018 年 8 月 27 日 ———— 就要开学了！


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/82113409
  [2]: https://leetcode.com/media/original_images/31_Next_Permutation.gif