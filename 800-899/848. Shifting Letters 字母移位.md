# 【LeetCode】848. Shifting Letters 解题报告（Python）

标签（空格分隔）： LeetCode

作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.me/

---

题目地址：https://leetcode.com/problems/shifting-letters/description/

## 题目描述：

We have a string S of lowercase letters, and an integer array shifts.

Call the ``shift`` of a letter, the next letter in the alphabet, (wrapping around so that 'z' becomes 'a'). 

For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.

Now for each shifts[i] = x, we want to shift the first i+1 letters of S, x times.

Return the final string after all such shifts to S are applied.

Example 1:
    
    Input: S = "abc", shifts = [3,5,9]
    Output: "rpl"
    Explanation: 
    We start with "abc".
    After shifting the first 1 letters of S by 3, we have "dbc".
    After shifting the first 2 letters of S by 5, we have "igc".
    After shifting the first 3 letters of S by 9, we have "rpl", the answer.

Note:

1. 1 <= S.length = shifts.length <= 20000
1. 0 <= shifts[i] <= 10 ^ 9

## 题目大意

（这个题本身简单，但是读懂题目很重要）

给出了一个字符串S，以及和这个字符串等长的数组shifts。定义了一个shift操作：把某个字符在字母表上移动某位（字母'z'再向右移得到'a'）。现在遍历shifts，每个操作都是把**当前位数之前的所有字符**移动shift位。求最后得到的字符串。

## 解题方法

坑还是挺明显的：需要把当前位数之前的所有字符串都去shift操作。看出题目给的字符串挺长的，如果普通的遍历，在每次遍历的时候再把之前所有shift过的再次shift，那么就会超时。

所以正确的做法是先求出每个字符串需要shift的次数。即对shifts进行位置之后的求和。得出要shift的位数之后，按照题目给的那种循环去操作就好了。

（应该没有人傻到真的去循环，而不是用求余操作吧233，逃……）

```python
class Solution(object):
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        _len = len(S)
        shifts_sum = sum(shifts)
        shifts_real = []
        for shift in shifts:
            shifts_real.append(shifts_sum)
            shifts_sum -= shift
        def shift_map(string, shift_time):
            shifted = ord(s) + (shift_time % 26)
            return chr(shifted if shifted <= ord('z') else shifted - 26)
        ans = ''
        for i, s in enumerate(S):
            ans += shift_map(s, shifts_real[i])
        return ans
```


## 日期

2018 年 6 月 10 日 ———— 等了两天的腾讯比赛复赛B的数据集，结果人家在复赛刚开始就给了。。