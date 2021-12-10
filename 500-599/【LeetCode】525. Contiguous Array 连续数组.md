作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/contiguous-array/description/

## 题目描述

Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:

    Input: [0,1]
    Output: 2
    Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

Example 2:

    Input: [0,1,0]
    Output: 2
    Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
    Note: The length of the given binary array will not exceed 50,000.

## 题目大意

找到一个数组中的一个连续数组，使得这个连续数组中0和1的数字一样多。

## 解题方法

### 累积和

使用的方法是求和+hashmap的方法，首先从头开始遍历，如果当前值是0就sum-1，否则就sum+1.这样如果得到了一个sum就知道在此之前出现了1的个数和0的个数的差值。因此，当后面该sum再次出现的时候，我们就知道了这个差值再次出现，也就是说，从第一次这个差值出现和第二次这个差值出现之间0和1的个数是一样多的。

因此我们需要一个map来保存0和1的差值。如果这个差值没出现过就给它赋值为它出现的索引。我们要求的就是当同样的差值出现的时候，两者之间的最大值。另外注意，当这个差值再次出现的时候不要更新map。即我们的策略是只保存这个差值出现的第一个位置，只有这样我们才知道最长的连续子数组是多少。

这个题的官方解答里面给出了详细的每一步的变化过程，推荐一看。

也可以在刚开始的时候就把nums中的0替换成-1，这样就可以直接使用total_sum加上当地前数值即可。

需要注意的是字典应该有个初始化值，代表在刚开始的时候没有任何元素的位置是-1，否则后面出现0的时不能和最开始的位置求位置差。

![在这里插入图片描述](https://leetcode.com/articles/Figures/535_Contiguous_Array.PNG)

python代码如下：

```python
class Solution:
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        print(nums)
        total_sum = 0
        index_map = dict()
        index_map[0] = -1
        res = 0        
        for i, num in enumerate(nums):
            if num == 0:
                total_sum -= 1
            else:
                total_sum += 1
            if total_sum in index_map:
                res = max(res, i - index_map[total_sum])
            else:
                index_map[total_sum] = i
        return res
```

C++代码如下：

```cpp
class Solution {
public:
    int findMaxLength(vector<int>& nums) {
        const int N = nums.size();
        unordered_map<int, int> m_;
        for (int& num : nums) {
            if (num == 0) {
                num = -1;
            }
        }
        m_.insert({0, -1});
        int sums = 0;
        int res = 0;
        for (int i = 0; i < N; ++i) {
            sums += nums[i];
            if (m_.count(sums)) {
                res = max(res, i - m_[sums]);
            }
                m_.insert({sums, i});
            }
        }
        return res;
    }
};
```


参考资料：

https://leetcode.com/problems/contiguous-array/discuss/99646/Easy-Java-O(n)-Solution-PreSum-+-HashMap
https://leetcode.com/articles/contiguous-array/

## 日期

2018 年 9 月 12 日 ———— 做题还是要有耐心


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/79888528
