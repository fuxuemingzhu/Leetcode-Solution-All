
- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)
- 个人公众号：负雪明烛
- 本文关键词：two sum, 两数之和，题解，leetcode, 力扣，Python, C++, Java

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/two-sum/#/description][1]


## 题目描述

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

    Given nums = [2, 7, 11, 15], target = 9,
    
    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].

## 题目大意

找出两个索引，这两个索引对应的数组的数字之和等于target.

## 解题方法

### 字典+两次遍历

第一次遍历保存每个数字和索引的对应关系，第二次遍历nums找到target - num是不是在字典中，如果在的话还要保证同样的数字不能用两次。需要注意的是，如果有相同的数字在nums中出现，那么字典中只会保存后面的那个数字的位置，因此第二次遍历的时候一定只能从左到右的走。

```python
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i, num in enumerate(nums):
            dic[num] = i
        for i, num in enumerate(nums):
            if target - num in dic and dic[target - num] != i:
                return [i, dic[target - num]]
```

### 字典+一次遍历

这个遍历的方法其实就是只保存已经出现了的数字的方式。当遍历的过程中发现了目标在已经遍历过的字典中出现了，那么就停止，这样的题实在是太多了。

这个题首先想到的是时间复杂度O(n^2)的遍历，但是肯定会超时，所以想到用HashMap保存已经有的数据出现的位置，这样可以使如果要求的数字出现的时候不再继续遍历，及时停止即可。有个技巧就是判断差是否在HashMap中，而不是遍历一遍HashMap来求和。

```java
public class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        for(int i = 0; i < nums.length; i++){
            if(map.containsKey(target - nums[i])){
                return new int[]{map.get(target - nums[i]), i};
            }else{
                map.put(nums[i], i);
            }
        }
        return new int[2];
    }
}
```

python解法如下，打败100%的提交。

```python
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        N = len(nums)
        pos = dict()
        for i, num in enumerate(nums):
            if target - num in pos:
                return [pos[target - num], i]
            else:
                pos[num] = i
        return [0, 0]
```

### 双指针

另外有一个种解法是双指针解法，对nums进行排序，然后使用双指针分别从左边和右边向中间走，如果两者的和相加是target说明已经找到。再返回其在数组中的位置。

C++代码如下：

```cpp
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> copy = nums;
        sort(nums.begin(), nums.end());
        int left = 0;
        int right = nums.size() - 1;
        while (left != right) {
            if (nums[left] + nums[right] == target)
                break;
            else if (nums[left] + nums[right] > target)
                right --;
            else 
                left ++;
        }
        vector<int> res(2, -1);
        for (int i = 0; i < copy.size(); ++i) {
            if (copy[i] == nums[left] && res[0] == -1) {
                res[0] = i;
            } else if (copy[i] == nums[right]) {
                res[1] = i;
            }
        }
        return res;
    }
};
```

## 日期

2017 年 5 月 18 日 
2018 年 11 月 22 日 —— 感恩节快乐～

  [1]: https://leetcode.com/problems/two-sum/#/description
