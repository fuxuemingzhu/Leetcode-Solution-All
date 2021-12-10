
作者： 负雪明烛
id：	fuxuemingzhu
公众号：负雪明烛
本文关键词：数组，array，非递减，遍历，python，C++

---
@[TOC](目录)

题目地址：https://leetcode-cn.com/problems/non-decreasing-array/

## 题目描述
给你一个长度为 n 的整数数组，请你判断在 最多 改变 1 个元素的情况下，该数组能否变成一个非递减数列。

我们是这样定义一个非递减数列的： 对于数组中所有的 `i (0 <= i <= n-2)` ，总满足 `nums[i] <= nums[i + 1]`。

示例 1:

	输入: nums = [4,2,3]
	输出: true
	解释: 你可以通过把第一个4变成1来使得它成为一个非递减数列。

示例 2:

	输入: nums = [4,2,1]
	输出: false
	解释: 你不能在只改变一个元素的情况下将其变为非递减数列。
	 

说明：

- 1 <= n <= 10 ^ 4
- -10 ^ 5 <= nums[i] <= 10 ^ 5

## 题目大意

最多只能修改一个数字，使得给出的数组变为非递减的数组。


## 解题方法

各位题友大家好，今天是**负雪明烛**坚持日更的第 **14** 天。今天力扣上的每日一题是「[665. 非递减数列](https://leetcode-cn.com/problems/non-decreasing-array/)」。


### 一、错误代码

拿到今天这个题，看到是个 Easy，就没有想太多了。直接判断是不是只出现了一次下降！迅速写出下面的代码，题目给的两个测试用例都通过了，那么就提交！


没想到，啪！直接来了个**解答错误**，很快啊！

```python
class Solution(object):
    def checkPossibility(self, nums):
        count = 0
        N = len(nums)
        for i in range(N):
            if i > 0 and nums[i] < nums[i - 1]:
                count += 1
        return count <= 1
```


题目说该代码没有通过测试用例 `[3,4,2,3]` 。仔细一想还真是，虽然该数组中只出现了一次下降，但是无论调整其中的一个数字都不能得到一个单调上升的数组。


那么，这题就有讲究了。下面我举了例子，相信我，下面的分析不难，你看完一定能懂。


### 二、举例分析


首先，看下面的几个测试用例，它们都因为数字 2 的出现，导致数组是非单调递增的。


- 例①： `4, 2, 5` 
- 例②： `1, 4, 2, 5`
- 例③： `3, 4, 2, 5` 



当数组中出现 2 时，破坏了数组的单调递增。为了让数组有序，我们需要对 2 或者 4 进行调整：


第①个用例，我们可以 `把 4 调小到 <= 2`  或者 `把 2 调大到 4、5` ，使数组有序。


![655-1.gif](https://img-blog.csdnimg.cn/img_convert/d1d904c6d76374ad0da4497eee12e48a.gif)

第②个用例，我们可以 `把 4 调小到 1、2`  或者 `把 2 调大到 4、5` ，使数组有序。

![655-2.gif](https://img-blog.csdnimg.cn/img_convert/5a1c9b390455af8f829e04eb0842b97c.gif)


第③个用例，我们必须 `把 2 调大到 4、5`，才能使数组有序：我们不能把 4 调整为一个 `<= 2` 的数字，因为 4 前面的元素是 3.

![655-3.gif](https://img-blog.csdnimg.cn/img_convert/05146d8e8fd4bb85f05f16adce5c8415.gif)


### 三、归纳总结


当 `nums[i]`  破坏了数组的单调递增时，即 `nums[i] < nums[i - 1]`  时，为了让数组有序，我们发现一个规律（在上面三个例子中， `nums[i]` 都为 2， `nums[i -1]` 都为 4）：


1. 如例①的情况，当 `i = 1` ，那么修改 `num[i- 1]` ，不要动 `nums[i]` ，因为`nums[i]`后面的元素是啥我们还不知道呢，少动它为妙。
2. 如例②的情况，当 `i > 1` 时，我们应该优先考虑把 `nums[i - 1]` 调小到 `>= nums[i - 2] 并且 <= nums[i]`。同样尽量不去修改 `nums[i]` ，理由同上。
3. 如例③的情况，当 `i > 1` 且 `nums[i] < nums[i - 2]` 时，我们无法调整 `nums[i - 1]` ，我们只能调整 `nums[i]` 到 `nums[i - 1]` 。



## 代码


使用 Python 和 C++ 写的代码如下。

```python
class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        N = len(nums)
        count = 0
        for i in range(1, N):
            if nums[i] < nums[i - 1]:
                count += 1
                if i == 1 or nums[i] >= nums[i - 2]:
                    nums[i - 1] = nums[i]
                else:
                    nums[i] = nums[i - 1]
        return count <= 1
```

C++ 代码如下：

```cpp
class Solution {
public:
    bool checkPossibility(vector<int>& nums) {
        int count = 0;
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] < nums[i - 1]) {
                if (i == 1 || nums[i] >= nums[i - 2]) {
                    nums[i - 1] = nums[i];
                } else {
                    nums[i] = nums[i - 1];
                }
                count ++;
            }
        }
        return count <= 1;
    }
}
```


## 刷题心得

1. 别小看 easy 题，它也能给我们带来收获，特别是easy题可能帮助我们练习某一种思路。
2. 这题看分析那么一大截，其实只是当发现有下降的时候，多判断了一次 `nums[i]` 和 `nums[i - 2]`，本身没那么难。

OK，以上就是 [@负雪明烛](/u/fuxuemingzhu/) 写的今天题解的全部内容了，如果你觉得有帮助的话，**求赞、求关注、求收藏**。我们明天再见！

## 日期

2018 年 2 月 5 日 
2018 年 11 月 31 日 —— 11月结束了
2021 年 2 月 7 日 —— 今天这个题解发在了力扣上，半天收获了5k阅读
