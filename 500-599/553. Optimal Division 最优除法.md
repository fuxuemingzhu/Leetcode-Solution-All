
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/optimal-division/description/


## 题目描述

Given a list of positive integers, the adjacent integers will perform the float division. For example, [2,3,4] -> 2 / 3 / 4.

However, you can add any number of parenthesis at any position to change the priority of operations. You should find out how to add parenthesis to get the maximum result, and return the corresponding expression in string format. Your expression should NOT contain redundant parenthesis.

    Example:
    Input: [1000,100,10,2]
    Output: "1000/(100/10/2)"
    Explanation:
    1000/(100/10/2) = 1000/((100/10)/2) = 200
    However, the bold parenthesis in "1000/((100/10)/2)" are redundant, 
    since they don't influence the operation priority. So you should return "1000/(100/10/2)". 
    
    Other cases:
    1000/(100/10)/2 = 50
    1000/(100/(10/2)) = 50
    1000/100/10/2 = 0.5
    1000/100/(10/2) = 2

Note:

The length of the input array is [1, 10].
Elements in the given array will be in range [2, 1000].
There is only one optimal division for each test case.

## 题目大意

这个题的意思是在合适的位置添加上括号，使得最后得到的除法表达式值最大。

## 解题方法

这道题非常tricky，我们注意到除了第一个除数之外，后面的数都可以转变为乘积！！！ 

　　拿样例来说： 
　　1000/(100/10/2) == (1000*10*2)/(100) 
　　所以，我们只需要考虑三种情况： 
　　1.只有一个数，直接返回； 
　　2.有两个数，第一个除以第二个返回； 
　　3.有三个及以上的数，把第二个数后面的和第一个数全部乘起来，最后除以第二个数。（因为note当中说明了，给的数字都是[2,1000]的，所以第二个数后面的所有数乘起来都只会让结果变大）。 

所以只要有超过两个的数值，那么最大的结果就是后面的括起来：

    "1000/(100/10/2)"
    "1000/(100/10/200)"
    "1000/(100/1000/2)"
    "1000/(100/10/20000)"

Python解法：

```python
class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = map(str, nums)
        if len(nums) <= 2:
            return '/'.join(nums)
        return '{}/({})'.format(nums[0], '/'.join(nums[1:]))
```

C++版本的代码如下：

```cpp
class Solution {
public:
    string optimalDivision(vector<int>& nums) {
        string res = "";
        const int N = nums.size();
        if (N == 1) return to_string(nums[0]);
        if (N == 2) return to_string(nums[0]) + '/' + to_string(nums[1]);
        res += to_string(nums[0]) + "/(";
        for (int i = 1; i < N - 1; i++) {
            res += to_string(nums[i]) + "/";
        }
        res += to_string(nums[N - 1]) + ")";
        return res;
    }
};
```


## 日期

2018 年 2 月 28 日 
2018 年 12 月 10 日 —— 又是周一！
