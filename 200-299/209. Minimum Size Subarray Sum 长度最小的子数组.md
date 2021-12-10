作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址: https://leetcode.com/problems/minimum-size-subarray-sum/description/

## 题目描述：

Given an array of ``n`` positive integers and a positive integer s, find the minimal length of a ``contiguous`` subarray of which the ``sum ≥ s``. If there isn't one, return 0 instead.

Example: 

    Input: s = 7, nums = [2,3,1,2,4,3]
    Output: 2
    Explanation: the subarray [4,3] has the minimal length under the problem constraint.

Follow up:

- If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 


## 题目大意

找出一个数组中最短连续的子数组，这个子数组的和要>=s.

## 解题方法

### 虫取法

碰巧今天在《挑战程序设计竞赛》一书中看到这个题，解法称之为虫取法，其实就是双指针。其实看到让连续子数组满足一定条件的很多都用了双指针，比如[713. Subarray Product Less Than K][1]。

因为这个题需要求最小值，所以结果初始化为inf，每次移动一下右指针，当和满足条件的时候，更新结果，并移动左指针，同时记得把和删去左边的数字。这里求和的区间是左右都是闭区间。

时间复杂度是O(N)，空间复杂度是O(1)。

```python
class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        l, r = 0, 0
        csum = 0
        res = float('inf')
        while r < N:
            csum += nums[r]
            while csum >= s:
                res = min(res, r - l + 1)
                csum -= nums[l]
                l += 1
            r += 1
        return res if res != float('inf') else 0
```

二刷的时候使用了C++，我同样选择了虫取法，但是对虫取法没有100%的信心，因为很多题目虫取法可能漏掉了解，而不容易发现。还好这个题目只有正整数，比较容易找到移动左右指针的规律，所以虫取法没什么问题。

我定义了两个指针left和right，定义了sum = [left...right)的和，其中区间是左闭右开，这样，right终止条件是right <=N，而满足题目要求的区间的长度是right - left。把这些弄明白之后就很容易写出代码了。

C++代码如下：

```cpp
class Solution {
public:
    // O(N) using two pointer
    int minSubArrayLen(int s, vector<int>& nums) {
        const int N = nums.size();
        if (N == 0) return 0;
        int left = 0, right = 0;
        // sum = sum[left, right)
        long long sum = 0;
        int res = INT_MAX;
        while (right <= N) {
            if (sum >= s) {
                res = min(res, right - left);
                sum -= nums[left++];
            } else {
                sum += nums[right++];
            }
        }
        return res == INT_MAX ? 0 : res;
    }
};
```

### 二分查找

这个题有个follow up，让我们用o(NlogN)的时间复杂度去求解，很明显地，在考察我们二分。

思路很显然，对于每个位置求数组累积和，然后对于累积和的每个位置，去查找sums[i] - pos的位置在sums中的哪里。这样的话，就得到了一个区间，这个区间的累积和是不小于s的，即为题目所求。

这个题我写的二分是查找第一个不小于某个数字的位置，即lower_bound，这样会造成，当要查找的target不在sums中时，返回的结果是它右边的第一个数字。所以需要做个判断，如果查到了，那么区间长度是i - pos，否则区间长度应该+1.


```cpp
class Solution {
public:
    int minSubArrayLen(int s, vector<int>& nums) {
        const int N = nums.size();
        vector<int> sums;
        sums.push_back(0);
        for (int i = 0; i < N; ++i) {
            sums.push_back(nums[i] + sums.back());
        }
        int res = INT_MAX;
        for (int i = 1; i <= N; ++i) {
            int target = sums[i] - s;
            if (target < 0) continue;
            auto pos = binary_search(sums, target);
            if (pos > N) continue;
            if (sums[i] - sums[pos] == s)
                res = min(res, i - pos);
            else if (sums[i] - sums[pos] < s)
                res = min(res, i - pos + 1);
        }
        return res == INT_MAX ? 0 : res;
    }
    int binary_search(vector<int>& sums, int target) {
        const int N = sums.size();
        // [l, r)
        int l = 0, r = N;
        while (l < r) {
            int mid = l + (r - l) / 2;
            if (sums[mid] >= target) {
                r = mid;
            } else {
                l = mid + 1;
            }
        }
        return l;
    }
};
```

参考资料：


## 日期

2018 年 10 月 15 日 —— 美好的周一怎么会出现雾霾呢？
2019 年 1 月 11 日 —— 小光棍节？

  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/83047699
