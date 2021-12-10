
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/random-pick-index/description/

## 题目描述

Given an array of integers with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.

Note:
The array size can be very large. Solution that uses too much extra space will not pass the judge.

Example:

int[] nums = new int[] {1,2,3,3,3};
Solution solution = new Solution(nums);

// pick(3) should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(3);

// pick(1) should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(1);


## 题目大意

在一个数组中寻找一个数字的索引位置。如果有多个，等概率的随机返回其中的任何一个。

## 解题方法

### 每次遍历索引

使用了一个比较讨巧的方法，用O(n)的时间复杂度，对整个数组进行遍历，这样如果有数字和target相等就保存下其索引位置。再从这些索引位置中等概率返回任意一个即可。

python代码如下：

```python
class Solution(object):

    def __init__(self, nums):
        """
        
        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        idxs = []
        for i, num in enumerate(self.nums):
            if num == target:
                idxs.append(i)
        return idxs[random.randint(0, len(idxs) - 1)]

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
```

### 字典保存索引

上面的做法每次pick的时候都要遍历一次，时间复杂度太高。一个利用空间换时间的方法就是提前使用字典把每个数字在哪些数字出现都保存好，然后随机一个返回就行。每次Pick的时间复杂度是O(1)。

C++代码如下：

```cpp
class Solution {
public:
    Solution(vector<int> nums) {
        for (int i = 0; i < nums.size(); ++i) {
            m_[nums[i]].push_back(i);
        }
    }
    
    int pick(int target) {
        auto v = m_[target];
        int s = v.size();
        int i = rand() % s;
        return v[i];
    }
private:
    unordered_map<int, vector<int>> m_;
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * int param_1 = obj.pick(target);
 */
```

### 蓄水池抽样

看到这个题，想到[382. Linked List Random Node][1]，知道它考察的是蓄水池抽样算法。[384. Shuffle an Array](https://blog.csdn.net/fuxuemingzhu/article/details/79391342)也有用到。

蓄水池采样算法（Reservoir Sampling）是说在一个流中，随机选择k个数字，保证每个数字被选择的概率相等。

算法的过程：

假设数据序列的规模为 n，需要采样的数量的为 k。

首先构建一个可容纳 k 个元素的数组，将序列的前 k 个元素放入数组中。

然后从第 k+1 个元素开始，以 k/cnt 的概率来决定该元素是否被替换到数组中（数组中的元素被替换的概率是相同的）。 当遍历完所有元素之后，数组中剩下的元素即为所需采取的样本。

这个题中k = 1。

C++代码如下：

```cpp
class Solution {
public:
    Solution(vector<int> nums) : nums_(nums) {
    }
    
    int pick(int target) {
        int cnt = 0;
        int res = -1;
        for (int i = 0; i < nums_.size(); ++i)  {
            int n = nums_[i];
            if (n != target) continue;
            ++cnt;
            if (rand() % cnt == 0)
                res = i;
        }
        return res;
    }
private:
    vector<int> nums_;
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * int param_1 = obj.pick(target);
 */
```


参考资料：

http://www.cnblogs.com/grandyang/p/5875509.html
https://www.cnblogs.com/snowInPluto/p/5996269.html

## 日期

2018 年 3 月 13 日 
2019 年 2 月 26 日 —— 二月就要完了

  [1]: http://blog.csdn.net/fuxuemingzhu/article/details/79488113
