
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

 - Difficulty: Easy

## 题目描述


Given two arrays, write a function to compute their intersection.

Example 1:

	Input: nums1 = [1,2,2,1], nums2 = [2,2]
	Output: [2,2]

Example 2:

	Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
	Output: [4,9]

Note:

- Each element in the result should appear as many times as it shows in both arrays.
- The result can be in any order.

Follow up:

- What if the given array is already sorted? How would you optimize your algorithm?
- What if nums1's size is small compared to nums2's size? Which algorithm is better?
- What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?


## 解题方法

### Java排序+双指针

题目的意思是找出两个数组中相同的元素，这个题目前面题使用HashSet去除的重复元素，这个题里边直接用ArrayList存储相同元素即可。

所以可以参考前面的，创建一个Arraylist，然后对两个数组进行排序，这样才能比较，根据不同的比较结果采取不同的措施。

对了，双指针的方法节省了不少空间。高票答案用的HashMap，效率明显没有双指针高。


```java
public class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
		ArrayList<Integer> arraylist = new ArrayList<Integer>();
		//一定写上<Integer>，否则没法自动拆包装包
		Arrays.sort(nums1);
		Arrays.sort(nums2);
		int index1 = 0;
		int index2 = 0;
		while (index1 < nums1.length && index2 < nums2.length) {
			if (nums1[index1] == nums2[index2]) {
				arraylist.add(nums1[index1]);
				index1++;
				index2++;
			} else if (nums1[index1] < nums2[index2]) {
				index1++;
			} else {
				index2++;
			}
		}
		int answer[] = new int[arraylist.size()];
		for (int i = 0; i < arraylist.size(); i++) {
			answer[i] = arraylist.get(i);
		}
		return answer;
    }
}
```

AC: 3 ms 超过96.76%

### Python排序+双指针

看到题目说了如果已经排序了会怎么样，这是一个很明显的需要排序的提示，告诉我们先排序。下面的操作就像merge两个有序链表差不多，分别从两个的起始位置判断是否相等即可。

需要注意的是题目要求的是结果中的出现次数等于两个数组交集部分的次数，所以当两个数组元素相等的时候需要把两个指针同时右移。

时间复杂度O(NlogN)，空间复杂度O(1).

```python
class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        l1, l2 = 0, 0
        N1, N2 = len(nums1), len(nums2)
        res = []
        while l1 != N1 and l2 != N2:
            if nums1[l1] == nums2[l2]:
                res.append(nums1[l1])
                l1 += 1
                l2 += 1
            elif nums1[l1] < nums2[l2]:
                l1 += 1
            else:
                l2 += 1
        return res
```

### Python解法使用字典

使用字典对两个数组出现的数字进行统计，然后直接判断数字是否在另一个字典里出现过，把结果直接拼接上两个的最小次数个当前数字。

时间复杂度O(N)，空间复杂度O(N).打败了98%的提交。

```python
class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        count1 = collections.Counter(nums1)
        count2 = collections.Counter(nums2)
        res = []
        for k, v in count1.items():
            if k in count2:
                res += [k] * min(v, count2[k])
        return res
```


## 日期

2017 年 1 月 11 日 
2018 年 11 月 6 日 —— 腰酸背痛要废了
2018 年 11 月 16 日 —— 又到周五了！

  [1]: https://leetcode.com/problems/intersection-of-two-arrays-ii/
