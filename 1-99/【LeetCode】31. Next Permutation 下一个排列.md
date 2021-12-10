
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/next-permutation/description/

## 题目描述

Implement ``next permutation``, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be ``in-place`` and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

    1,2,3 → 1,3,2
    3,2,1 → 1,2,3
    1,1,5 → 1,5,1


## 题目大意

找到一个排列按照字母表顺序的情况下，下一个更大的排列是多少。如果已经是最大的，那么应该翻转。必须原地翻转。

## 解题方法

### 逆序数字交换再翻转

很有技巧的题目。

先找到从后向前数，第一个降序的位置，把此位置后面的翻转。再把这个降序数字和后面第一个比它大的位置交换即可。

首先说一下这题怎么想到的。有如下的一个数组

1　　2　　7　　4　　3　　1

下一个排列为：

1　　3　　1　　2　　4　　7

观察可以发现，再给出的数组中，2之后的数字都是降序排列的，我们把2后面第一个比2大的数字放到最前面，然后让3后面的数字升序排列。

简单思路的证明：从7开始是降序的，也就是说7 4 3 1不可能通过重新排列构成更大的数字。如果要得到next permutation，那么必须把2这个位置的数字给换掉才行，而且只能换成比2大的数字在才能使next permutation > current permutation.至于换成多大的数字，很明显的需要换成在2后面的数字中刚好比2大的数字，证明可以使用反证法来说明换成其他数字要么比当前数字小，要么大于正确的next permutation. 

下面这个做法是先逆序再交换，本质和上面的证明一样：

如果从第n个数字到最后都是递减的并且第n-1个数字小于第n个，说明从第n个数字开始的这段序列是字典序组合的最后一个，在下一个组合中他们要倒序变为字典序第一个，然后从这段序列中找出第一个大于第n-1个数字的数和第n-1个数字交换就可以了。
 
举个栗子，当前组合为12431，可以看出431是递减的，同时4>2，这样我们把431倒序，组合就变为12134，然后从134中找出第一个大于2的数字和2交换，这样就得到了下一个组合13124。对于完全递减的组合例如4321在倒序之后就可以结束了。



代码如下：

```python
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 1
        while i > 0 and nums[i] <= nums[i - 1]:
            i -= 1
        self.reverse(nums, i, n - 1)
        if i > 0:
            for j in range(i, n):
                if nums[j] > nums[i-1]:
                    self.swap(nums, i-1, j)
                    break
        
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

也可以先进行交换，然后再翻转。比如Leetcode的这个解答方式：

![此处输入图片的描述][1]


C++代码如下：

```cpp
class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        const int N = nums.size();
        int i = N - 2;
        while (i >= 0 && nums[i] >= nums[i + 1]) --i;
        int j = N - 1;
        if (i >= 0) {
            while (nums[j] <= nums[i]) --j;
            swap(nums[i], nums[j]);
        }
        reverse(nums.begin() + i + 1, nums.end());
    }
};
```

### 库函数

这个算我第一次觉得C++让人惊呆吧，有next_permutation函数，而且是原地操作。

```cpp
class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        next_permutation(nums.begin(), nums.end());
    }
};
```

参考资料：

1. https://leetcode.com/articles/next-permutation/
1. https://blog.csdn.net/tstsugeg/article/details/50261517
1. http://www.cnblogs.com/grandyang/p/4428207.html

## 日期

2018 年 8 月 27 日 ———— 就要开学了！
2019 年 1 月 14 日 —— 凛冬将至

  [1]: https://leetcode.com/media/original_images/31_Next_Permutation.gif
