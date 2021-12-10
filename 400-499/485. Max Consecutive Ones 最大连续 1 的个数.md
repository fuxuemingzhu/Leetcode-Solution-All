作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

[LeetCode]

题目地址：[https://leetcode.com/problems/max-consecutive-ones/][1]

Difficulty: Easy

## 题目描述


Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:

	Input: [1,1,0,1,1,1]
	Output: 3
	Explanation: The first two digits or the last three digits are consecutive 1s.
	    The maximum number of consecutive 1s is 3.

Note:

1. The input array will only contain 0 and 1.
1. The length of input array is a positive integer and will not exceed 10,000

## 题目大意

找出数组中最多有多少个连续的1。

## 解题方法

### Java解法

找出一个二进制串中最多连续的1的个数。

第一想法就是动态规划。找到目前的连续的串和过去连续的串的最大值，设为曾经最大的串。

故，设置count代表现在连续的串，anwer为过去连续的值得最大值。转移方程就是求两者的最大值。

有个技巧，就是判断count和answer最大值得时候，注意到count要包括末尾的连续的1的个数，而不仅仅是遇到0停止。所以设置的是循环变量到了nums.length，超出了数组的clength，这样的时候就使停止的判断有两个，遇到0和超出数组长度。

好像有人比我的代码更简洁，但是思路大致一样的。

```java
public class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int answer=0;
        int count =0;
        for(int i=0; i<= nums.length; i++){
            if(i != nums.length && nums[i] == 1){
                count++ ;
            }else{
                if(count == 0){
                    continue;
                }
                answer=answer > count ? answer : count;
                count = 0;
            }
        }
        return answer;
    }
}
```

AC: 8 ms

### Python解法

二刷的时候使用的是Python。写起来比较简单了，如果是0的话，更新起始位置，如果是1就更新最大值。

```python
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = -1
        N = len(nums)
        res = 0
        for i, n in enumerate(nums):
            if n == 0:
                index = i
            else:
                res = max(res, i - index)
        return res
```

## 日期

2017 年 1 月 15 日 
2018 年 11 月 ９ 日 —— 睡眠可以

  [1]: https://leetcode.com/problems/max-consecutive-ones/
