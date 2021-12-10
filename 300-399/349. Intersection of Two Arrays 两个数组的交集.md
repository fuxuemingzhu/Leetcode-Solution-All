
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

[LeetCode]

题目地址：[https://leetcode.com/problems/intersection-of-two-arrays/][1]

 - Difficulty: Easy

## 题目描述


Given two arrays, write a function to compute their intersection.

Example 1:

	Input: nums1 = [1,2,2,1], nums2 = [2,2]
	Output: [2]

Example 2:

	Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
	Output: [9,4]

Note:

1. Each element in the result must be unique.
2. The result can be in any order.

## 题目大意

找出两个数组中共同出现的数字，保证结果中返回的数字是唯一的，返回结果的顺序无所谓。

## 解题方法

### 方法一：Java解法，HashSet

每次都要看解析啊摔！用HashSet去除每个数组的重复元素，统计重复出现的元素即可。java只有元素的个数确定了才能新建数组，所以这里注意一下。

```java
public class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        HashSet<Integer> set1=new HashSet<Integer>();
        for(int i : nums1){
            set1.add(i);
        }
        HashSet<Integer> set2=new HashSet<Integer>();
        for(int i: nums2){
            if(set1.contains(i)){
                set2.add(i);
            }            
        }
        int answer[]=new int[set2.size()];
        int i=0;
        for(int n:set2){
            answer[i++]=n;
        }
        return answer;
    }
}
```

AC:8 ms

### 方法二：Python解法，set

还是python对于这种多种数据结构的题处理来方便。打败96%的提交。

```python
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1) & set(nums2))
```

## 日期

2017 年 1 月 8 日 
2018 年 11 月 11 日 —— 剁手节快乐

  [1]: https://leetcode.com/problems/intersection-of-two-arrays/
