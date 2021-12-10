# 【LeetCode】373. Find K Pairs with Smallest Sums 解题报告（Python）

标签： LeetCode

---

题目地址：https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/

## 题目描述：

You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u,v) which consists of one element from the first array and one element from the second array.

Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

    Example 1:
    Given nums1 = [1,7,11], nums2 = [2,4,6],  k = 3
    
    Return: [1,2],[1,4],[1,6]
    
    The first 3 pairs are returned from the sequence:
    [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
    
    Example 2:
    Given nums1 = [1,1,2], nums2 = [1,2,3],  k = 2
    
    Return: [1,1],[1,1]
    
    The first 2 pairs are returned from the sequence:
    [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
    
    Example 3:
    Given nums1 = [1,2], nums2 = [3],  k = 3 
    
    Return: [1,3],[2,3]
    
    All possible pairs are returned from the sequence:
    [1,3],[2,3]

## 题目大意

从两个数组中各拿出一个数字，求两个数字的和最小的k个组合。如果和相等的时候，出现的顺序是不在乎的。

## 解题方法

看到全排列，于是我用了笛卡尔积，结果遇到特别长的两个数组时，内存超了。。代码还是很简单的。

```python
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        pairs = list(itertools.product(nums1, nums2))
        return sorted(pairs, key = lambda x: sum(x))[:k]
```

方法二：

使用堆。说实话，这个堆的使用我是感觉真是不令人满意啊。我们一般用这种数据结构都是把结构里的内容正好用完的。这个题中堆的使用很随意，也是直接把“可能成为和最小的一组数”直接进堆，不用管这个数字是不是真的是最小的k个之一。

注意，不用保证每次进堆的元素是和最小！相对较小即可！

> 首先将（nums1[i] + nums2[0], i, 0）加入堆，i取值范围[0, size1)
> 
> 弹出堆顶元素sum, i, j，将(nums1[i], nums2[j])加入结果集ans
> 
> 若j + 1 < size2，则将(nums1[i] + nums2[j + 1], i, j + 1)加入堆
> 
> 循环直到结束

参考：http://bookshadow.com/weblog/2016/07/07/leetcode-find-k-pairs-with-smallest-sums/

```python
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        len1, len2 = len(nums1), len(nums2)
        if not len1 or not len2: return res
        heap = []
        for x in range(len1):
            heapq.heappush(heap, (nums1[x] + nums2[0], x, 0))
        while len(res) < min(k, len1 * len2):
            sum, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])
            if j + 1 < len2:
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
        return res
```

## 日期

2018 年 3 月 14 日 --霍金去世日


  [1]: http://blog.csdn.net/fuxuemingzhu/article/details/79559645