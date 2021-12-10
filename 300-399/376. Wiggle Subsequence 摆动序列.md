# 【LeetCode】376. Wiggle Subsequence 解题报告（Python）

作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址: https://leetcode.com/problems/wiggle-subsequence/description/

## 题目描述：

A sequence of numbers is called a wiggle sequence if the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with fewer than two elements is trivially a wiggle sequence.

For example, [1,7,4,9,2,5] is a wiggle sequence because the differences (6,-3,5,-7,3) are alternately positive and negative. In contrast, [1,4,7,2,5] and [1,7,4,5,5] are not wiggle sequences, the first because its first two differences are positive and the second because its last difference is zero.

Given a sequence of integers, return the length of the longest subsequence that is a wiggle sequence. A subsequence is obtained by deleting some number of elements (eventually, also zero) from the original sequence, leaving the remaining elements in their original order.

Example 1:

    Input: [1,7,4,9,2,5]
    Output: 6
    Explanation: The entire sequence is a wiggle sequence.

Example 2:

    Input: [1,17,5,10,13,15,10,5,16,8]
    Output: 7
    Explanation: There are several subsequences that achieve this length. One is [1,17,10,13,10,16,8].

Example 3:

    Input: [1,2,3,4,5,6,7,8,9]
    Output: 2

Follow up:

Can you do it in O(n) time?

## 题目大意

如果一个数组里面，相邻的两个数字的差是正负交替的，那么认为这个是波动序列。求输入的数组里面最长的波动序列长度。

## 解题方法

明显的DP问题，本来的想法是用个二维DP，可是提交了几遍只通过了部分测试用例。才去看的别人的两个DP数组的解法。

定义了一个记录递增的DP数组inc，一个记录递减的DP数组dec，这两个DP数组分别保存的是开头元素是递增、递减的最长波动序列长度。对于每个位置，从头遍历，如果当前的元素比前面的元素大，应该更新递增数组，否则，如果比前面的数字小，那么应该更新递减数组。

时间复杂度是O(N^2)，空间复杂度是O(N).

```python
class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1:
            return n
        inc, dec = [1] * n, [1] * n
        for x in range(n):
            for y in range(x):
                if nums[x] > nums[y]:
                    inc[x] = max(inc[x], dec[y] + 1)
                elif nums[x] < nums[y]:
                    dec[x] = max(dec[x], inc[y] + 1)
        return max(inc[-1], dec[-1])
```

其实不需要从头遍历，只需要知道前面元素对应的最长递增和递减数组即可。

时间复杂度是O(N)，空间复杂度是O(N).

```python
class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1:
            return n
        inc, dec = [1] * n, [1] * n
        for x in range(1, n):
            if nums[x] > nums[x - 1]:
                inc[x] = dec[x - 1] + 1
                dec[x] = dec[x - 1]
            elif nums[x] < nums[x - 1]:
                inc[x] = inc[x - 1]
                dec[x] = inc[x - 1] + 1
            else:
                inc[x] = inc[x - 1]
                dec[x] = dec[x - 1]
        return max(inc[-1], dec[-1])
```

简单分析代码就可以看出，每个元素都只和它之前的元素相关，因此，只需要使用两个变量即可。

时间复杂度是O(N)，空间复杂度是O(1).

```python
class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1:
            return n
        inc, dec = 1, 1
        for x in range(1, n):
            if nums[x] > nums[x - 1]:
                inc = dec + 1
            elif nums[x] < nums[x - 1]:
                dec = inc + 1
        return max(inc, dec)
```

参考资料：

https://leetcode.com/articles/wiggle-subsequence/
http://www.cnblogs.com/grandyang/p/5697621.html
http://bookshadow.com/weblog/2016/07/21/leetcode-wiggle-subsequence/

## 日期

2018 年 9 月 29 日 —— 国庆9天长假第一天！


  [1]: https://www.hrwhisper.me/leetcode-guess-number-higher-lower-ii/
