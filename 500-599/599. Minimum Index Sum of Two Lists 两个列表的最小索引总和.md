
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/][1]


## 题目描述

Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.

You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.

Example 1:

    Input:
    ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
    Output: ["Shogun"]
    Explanation: The only restaurant they both like is "Shogun".

Example 2:

    Input:
    ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    ["KFC", "Shogun", "Burger King"]
    Output: ["Shogun"]
    Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).

Note:
1. The length of both lists will be in the range of [1, 1000].
1. The length of strings in both lists will be in the range of [1, 30].
1. The index is starting from 0 to the list length minus 1.
1. No duplicates in both lists.

## 题目大意

找出两个列表中相同的元素，并且需要保证输出的是在两个列表中索引和最小的元素。如果这种元素多次出现，那么应该都输出。

## 解题方法

### 方法一：找到公共元素再求索引和

太蠢的想法，直接找出两个列表公共的元素，然后遍历公共元素，把公共元素在两个列表的位置的和求出来。注意题目中是要求如果和相等，那么，把所有和相等的都放到结果列表里。

需要一个变量存储当前的最小的序号和，然后维护这个变量。当变量更新的时候，要初始化结果列表。

这样的做法会反复的调用index方法，时间比较慢，超过14%的提交。

```python
class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        commons = [word for word in list1 if word in list2]
        answer = []
        smallest = 1000000
        for common in commons:
            index1 = list1.index(common)
            index2 = list2.index(common)
            index = index1 + index2
            if smallest > index:
                smallest = index
                answer = [common]
            elif smallest == index:
                answer.append(common)
        return answer
```

方法一就慢在反复的求index，所以可以使用字典保存两个list中的每个元素的序号，然后从字典中查找序号就行。这种做法超过65%的提交。

```python
class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        dic1 = {word:ind for ind,word in enumerate(list1)}
        dic2 = {word:ind for ind,word in enumerate(list2)}
        answer = []
        smallest = 1000000
        for word in dic1:
            if word in dic2:
                _sum = dic1[word] + dic2[word]
                if smallest > _sum:
                    smallest = _sum
                    answer = [word]
                elif smallest == _sum:
                    answer.append(word)
        return answer
```

### 方法二：索引求和，使用堆弹出最小元素

同样使用的是字典，保存的其实是两个里面共同出现的元素，然后求元素的索引和。需要使用小根堆把最小的索引和弹出来。因为可能有多个结果，所以需要保存所有的索引等于最小索引的元素。

```python
class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        interest = dict()
        for i, l in enumerate(list1):
            interest[l] = [i, 100000]
        for j, l in enumerate(list2):
            if l in interest:
                interest[l][1] = j
        heap = [(sum(v), l) for l, v in interest.items()]
        heapq.heapify(heap)
        res = []
        smallest = -1
        while heap:
            cursum, curl = heapq.heappop(heap)
            if smallest == -1:
                smallest = cursum
            if smallest == cursum:
                res.append(curl)
            else:
                break
        return res
```

## 日期

2018 年 1 月 23 日 
2018 年 11 月 16 日 —— 又到周五了！


  [1]: https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/
