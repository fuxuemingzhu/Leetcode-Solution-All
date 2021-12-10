
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/self-dividing-numbers/description/][1]


## 题目描述

You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.

Example 1:

    Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
    Output: [-1,3,-1]
    Explanation:
        For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
        For number 1 in the first array, the next greater number for it in the second array is 3.
        For number 2 in the first array, there is no next greater number for it in the second array, so output -1.

Example 2:

    Input: nums1 = [2,4], nums2 = [1,2,3,4].
    Output: [3,-1]
    Explanation:
        For number 2 in the first array, the next greater number for it in the second array is 3.
        For number 4 in the first array, there is no next greater number for it in the second array, so output -1.
    Note:
    All elements in nums1 and nums2 are unique.
    The length of both nums1 and nums2 would not exceed 1000.

## 题目大意

给了一个数组nums2，以及它的一个子集nums1，找出nums1中的每个数字在nums2中的位置右边第一个比该数字大的数。如果没有就返回-1。

## 解题方法

### 直接遍历查找

想法比较淳朴：先从nums2中找到对应的nums1数值的序号，然后从这个序号往又找，看有没有比nums1数字大的。

如果有，把这个数字放到结果里；如果没有，就把-1放到结果里。


```python
class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = []
        for num1 in findNums:
            index = -1
            for i,nums2 in enumerate(nums):
                if num1 == nums[i]:
                    index = i
                    break
            while index < len(nums) and num1 >= nums[index]:
                index += 1
            if index == len(nums):
                answer.append(-1)
            else:
                answer.append(nums[index])            
        return answer
```

### 字典保存位置

注意，题目说的是没有重复，那么可以使用字典保存每个数字出现的位置，这样就能直接定位到要寻找的数字在nums中的位置了，然后我们从这个位置向后寻找第一个比他大的数字即可。

```cpp
class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& findNums, vector<int>& nums) {
        unordered_map<int, int> pos;
        const int N = nums.size();
        for (int i = 0; i < N; i++) {
            pos[nums[i]] = i;
        }
        vector<int> res;
        for (int f : findNums) {
            int i = pos[f];
            for (; i < N; i++) {
                if (nums[i] > f) {
                    res.push_back(nums[i]);
                    break;
                }
            }
            if (i == N) {
                res.push_back(-1);
            }
        }
        return res;
    }
};
```

## 日期

2018 年 1 月 16 日 
2018 年 11 月 ９ 日 —— 睡眠可以
2018 年 12 月 28 日 —— 元旦假期到了

  [1]: https://leetcode.com/problems/next-greater-element-i/description/
