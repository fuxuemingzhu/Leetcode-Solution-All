# 【LeetCode】137. Single Number II 解题报告（Python）

标签： LeetCode

---

题目地址：https://leetcode.com/problems/single-number-ii/description/

## 题目描述：

Given an array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

## 题目大意

有一个数组，每个数字都出现了3次，除了其中的某一个只出现了1次。找出这个只出现了1次的数字。

## 解题方法

这个题本身不是很难，注意，不能使用异或运算搞定了。这个题的做法是把32位的二进制数进行遍历，统计每个数字的每一位出现的和。因为每个数字出现了3次或者1次，所以如果某一位出现的次数不是3次，那么这个位置一定是因为那个只出现1次的数字导致的。用来保存结果的res是0，因此使用或操作，就能把这个位置的数字变成1.

需要注意的是：python的整型方便是方便了，但是由于其没有最大值，所以，当输入是一堆负数的时候，会导致认为结果是个整数！因为32位有符号的被认为成了无符号的，所以这就是Python的一个坑。。

注意一下结论，以后出现位运算的时候，需要对结果进行判断一下最好。如果不在这个范围内，说明了结果被认为是无符号的数了，需要减去2 ^ 32。

> 16位整数中-32768到32767
> 
> 32位整数中-2147483648到2147 483 647
> 
> 
> 最高位为符号位 ，请您计算2的15次方以及2的31次方，就可以得到以上结果
> 
> 16位整数-2^15~2^15-1
> 
> 32位整数-2^31~2^31-1

```python
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in range(32):
            cnt = 0
            mask = 1 << i
            for num in nums:
                if num & mask:
                    cnt += 1
            if cnt % 3 == 1:
                res |= mask
        if res >= 2 ** 31:
            res -= 2 ** 32
        return res
```

## 日期

2018 年 3 月 14 日 --霍金去世日