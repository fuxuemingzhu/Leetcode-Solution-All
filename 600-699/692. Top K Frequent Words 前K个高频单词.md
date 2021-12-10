# 【LeetCode】692. Top K Frequent Words 解题报告（Python）

标签： LeetCode

---

题目地址：https://leetcode.com/problems/top-k-frequent-words/description/

## 题目描述：

Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

    Example 1:
    Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
    Output: ["i", "love"]
    Explanation: "i" and "love" are the two most frequent words.
        Note that "i" comes before "love" due to a lower alphabetical order.
    
    Example 2:
    Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
    Output: ["the", "is", "sunny", "day"]
    Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
        with the number of occurrence being 4, 3, 2 and 1 respectively.

Note:

1. You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
1. Input words contain only lowercase letters.

Follow up:
1. Try to solve it in O(n log k) time and O(n) extra space.

## 题目大意

对单词按出现的次数进行排序，如果次数相同，则按照字母序排列，只返回前k个。

## 解题方法

既然看到出现次数，那么那么一般都是使用自带的Counter进行统计的。按出现次数排序这个可以使用most_common()函数，但是这个函数对出现次数相等时不是按照字母序排列的。所以需要自定义排序函数。

```python
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        count = collections.Counter(words)
        def compare(x, y):
            if x[1] == y[1]:
                return cmp(x[0], y[0])
            else:
                return -cmp(x[1], y[1])
        return [x[0] for x in sorted(count.items(), cmp = compare)[:k]]
```

另外一种方法也是排序：

```python
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        count = collections.Counter(words)
        candidates = count.keys()
        candidates.sort(key = lambda w: (-count[w], w))
        return candidates[:k]
```

重要的来了，一般，我们认为找出k个最大最小的问题都是一个使用堆来做的。这个题中，学习了python的堆的用法。

``heapq.heapify(heap)``能在线性时间内，把一个列表转成堆。

``heapq.heappop(heap)``能直接弹出堆的堆顶。

``heappush(heap,5)``向堆中添加元素。

注意，heap是个list，哪怕使用了上述函数之后，这个仍然是list.

python中的堆默认是小根堆，如果想使用大根堆，在添加元素的时候使用负号即可。

```python
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        count = collections.Counter(words)
        heap = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]
```

## 日期

2018 年 3 月 14 日 