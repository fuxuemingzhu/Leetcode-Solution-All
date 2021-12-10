
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/shuffle-an-array/description/


## 题目描述

Shuffle a set of numbers without duplicates.

    Example:
    
    // Init an array with set 1, 2, and 3.
    int[] nums = {1,2,3};
    Solution solution = new Solution(nums);
    
    // Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
    solution.shuffle();
    
    // Resets the array back to its original configuration [1,2,3].
    solution.reset();
    
    // Returns the random shuffling of array [1,2,3].
    solution.shuffle();


## 题目大意

定义两个函数，``shuffle``函数能把数组随机打乱，``reset``函数能返回初始数组。

## 解题方法

### 库函数

直接调用python的``random.shuffle``就行了。C++也有``std::random_shuffle()``函数。

注意都是原地打乱。

Python代码如下：

```python
import random
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        nums_s = self.nums[:]
        random.shuffle(nums_s)
        return nums_s


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
```

C++代码如下：

```cpp
class Solution {
private:
    vector<int> nums_;
    vector<int> toshuffle_;
public:
    Solution(vector<int> nums) {
        nums_ = nums;
        toshuffle_ = nums;
    }
    
    /** Resets the array to its original configuration and return it. */
    vector<int> reset() {
        toshuffle_ = nums_;
        return nums_;
    }
    
    /** Returns a random shuffling of the array. */
    vector<int> shuffle() {
        random_shuffle(toshuffle_.begin(), toshuffle_.end());
        return toshuffle_;
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * vector<int> param_1 = obj.reset();
 * vector<int> param_2 = obj.shuffle();
 */
```

### Fisher–Yates 洗牌

新学习了``Fisher–Yates shuffle`` 洗牌算法。

Fisher–Yates shuffle 的原始版本，最初描述在 1938 年的 Ronald Fisher 和 Frank Yates 写的书中，书名为《Statistical tables for biological, agricultural and medical research》。他们使用纸和笔去描述了这个算法，并使用了一个随机数表来提供随机数。它给出了 1 到 N 的数字的的随机排列，具体步骤如下：

1. 写下从 1 到 N 的数字
1. 取一个从 1 到剩下的数字（包括这个数字）的随机数 k
1. 从低位开始，得到第 k个数字（这个数字还没有被取出），把它写在独立的一个列表的最后一位
2. 重复第 2步，直到所有的数字都被取出
3. 第 3 步写出的这个序列，现在就是原始数字的随机排列

已经证明如果第 2 步取出的数字是真随机的，那么最后得到的排序一定也是。

洗牌的过程可以看看这个文章，看一遍一定就懂！https://gaohaoyang.github.io/2016/10/16/shuffle-algorithm/

这个算法的一句话总结：依次遍历列表中的每一位，并将这一位与``其后面``的随机一位交换顺序。

```python
import random
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        nums_s = self.nums[:]
        _len = len(self.nums)
        for i in xrange(_len):
            rand = random.randrange(i, _len)
            nums_s[i], nums_s[rand] = nums_s[rand], nums_s[i]
        return nums_s


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
```

### 水塘抽样

另外一个抽样算法叫做水塘抽样，其本来的目的是在大数据流中的随机抽样问题，即：当内存无法加载全部数据时，如何从包含未知大小的数据流中随机选取k个数据，并且要保证每个数据被抽取到的概率相等。

1. 当K = 1时，数据流中第i个数被保留的概率为 1/i。只要采取这种策略，只需要遍历一遍数据流就可以得到采样值，并且保证所有数被选取的概率均为 1/N 。
2. 当K > 1时，对于前k个数，我们全部保留，对于第i（i>k）个数，我们以K/i的概率保留第i个数，并以 1/K的概率与前面已选择的k个数中的任意一个替换。

证明过程：https://zhuanlan.zhihu.com/p/29178293

至于这个题的随机打乱，其实就是在长度K的数据中，随机选K个数字的问题，方法变成了和Fisher–Yates 洗牌完全一样了，一句话总结就是：依次遍历列表中的每一位，并将这一位与``其后面``的随机一位交换顺序。

C++代码如下：

```cpp
class Solution {
private:
    vector<int> nums_;
public:
    Solution(vector<int> nums) {
        nums_ = nums;
    }
    
    /** Resets the array to its original configuration and return it. */
    vector<int> reset() {
        return nums_;
    }
    
    /** Returns a random shuffling of the array. */
    vector<int> shuffle() {
        vector<int> res = nums_;
        for (int i = 0; i < res.size(); ++i) {
            int t = i + rand() % (res.size() - i);
            swap(res[i], res[t]);
        }
        return res;
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * vector<int> param_1 = obj.reset();
 * vector<int> param_2 = obj.shuffle();
 */
```

## 日期

2018 年 2 月 27 日 
2019 年 2 月 22 日 —— 这周结束了
