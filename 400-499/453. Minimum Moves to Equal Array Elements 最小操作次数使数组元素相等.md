
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

[LeetCode]

题目地址：[https://leetcode.com/problems/minimum-moves-to-equal-array-elements/][1]

 - Difficulty: Easy

## 题目描述

Given a non-empty integer array of size n, find the minimum number of moves required to make all array elements equal, where a move is incrementing n - 1 elements by 1.

    Example:

    Input:
    [1,2,3]
    
    Output:
    3
    
    Explanation:
    Only three moves are needed (remember each move increments two elements):
    
    [1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]

## 题目大意

数组长度是n，每次把n-1个数字加1，问需要多少次才能让所有的数字都相等。

## 解题方法

### 方法一：模拟过程

我用的直接的方法，每次把数组排序，然后把前n-1个元素++，再排序，知道首尾元素相等即可。

根据测试用例，这个方法应该对的，但这个方法时间超出。

```java
public class Solution {
    public int minMoves(int[] nums) {
        int count=0;
        Arrays.sort(nums);
        while(nums[0] != nums[nums.length-1]){
            for(int i=0; i<nums.length-1; i++){
                nums[i]++;                
            }
            Arrays.sort(nums);
            count++;
        }
        return count;
    }
}
```

### 方法二：求和-n*最小值

看了高票答案之后，才明白，把其中最小的n-1个元素都++ 相当于 把最大的元素--；

我们的目标是把所有的元素搞相等，也就是每次把最大的元素-1 直到所有元素都等于最小元素即可。

故总的运算次数等于 所有元素与最小元素 的差  的和： sum(array) - n * minimum

```java
public class Solution {
    public int minMoves(int[] nums) {
        int count=0;
        int min=nums[0];
        for(int num : nums){
            min=Math.min(min,num);
        }
        for(int num : nums){
            count += num - min;
        }
        return count;
    }
}
```

AC:	14 ms

python的代码如下：

```python
class Solution:
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums) - len(nums) * min(nums)
```

C++代码如下：

```cpp
class Solution {
public:
    int minMoves(vector<int>& nums) {
        int mn = INT_MAX;
        long long s = 0;
        for (int n : nums) {
            if (n < mn) mn = n;
            s += n;
        }
        return s - nums.size() * mn;
    }
};
```

### 方法三：排序

受到上面的想法的启发，反思方法一，没必要每次循环都排下序，按照相减的策略，排序后，第一个元素就是最小元素，再求出其他元素与最小元素的差的和即可。

排序算法的时间复杂度是O(nlog(n))

```java
public class Solution {
    public int minMoves(int[] nums) {
        int count=0;
        Arrays.sort(nums);
        for(int num : nums){
            count += num - nums[0];
        }
        return count;
    }
}
```

AC:53 ms

python代码如下：

```python
class Solution:
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        res = 0
        for num in nums:
            res += num - nums[0]
        return res
```

官网给的解答很好，很全面而且配了视频。好评。[https://leetcode.com/articles/minimum-moves-to-equal-array-elements/][2]


## 日期

2017 年 1 月 7 日 
2018 年 11 月 14 日 —— 很严重的雾霾
2018 年 12 月 14 日 —— 12月过半，2019就要开始

  [1]: https://leetcode.com/problems/minimum-moves-to-equal-array-elements/
  [2]: https://leetcode.com/articles/minimum-moves-to-equal-array-elements/
