作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址: https://leetcode.com/problems/rearrange-string-k-distance-apart

## 题目描述：

Given a non-empty string str and an integer k, rearrange the string such that the same characters are at least distance k from each other.

All input strings are given in lowercase letters. If it is not possible to rearrange the string, return an empty string ``""``.

Example 1:

    str = " ", k = 3
    
    Result: "abcabc"
    
    The same letters are at least distance 3 from each other.

Example 2:

    str = "aaabc", k = 3
    
    Answer: ""

    It is not possible to rearrange the string.

Example 3:

    str = "aaadbbcc", k = 2

    Answer: "abacabcd"

    Another possible answer is: "abcabcda"

    The same letters are at least distance 2 from each other.


## 题目大意

判断给出的字符串能不能构成一个新的排列，在这个排列中，所有的相同字符之间的间距最少是k.

## 解题方法

使用Counter统计每个字符出现的次数，然后使用大根堆，每次弹出出现次数最多的字符，添加到生成结果字符串的末尾。如果剩余的不同字符个数不够k，那么说明不能满足题目的要求，返回空字符串。另外，每次弹出出现次数最多的字符之后，不能直接放入堆中，因为直接放入堆中可能下次又被弹出来，所以应该放入一个临时的数组中，在单次操作结束之后再重新插入堆中。

时间复杂度是O(N)，空间复杂度是O(N)。

```python
class Solution:
	def rearrangeString(self, words, k):
		_len = len(words)
		words_count = collections.Counter(words)
		que = []
		heapq.heapify(que)
		for w, v in words_count.items():
			heapq.heappush(que, (-v, w))
		res = ""
		while que:
			cnt = min(_len, k)
			used = []
			for i in range(cnt):
				if not que:
					return ""
				v, w = heapq.heappop(que)
				res += w
				if -v > 1:
					used.append((v + 1, w))
				_len -= 1
			for use in used:
				heapq.heappush(que, use)
		return res
```


参考资料：

http://www.cnblogs.com/grandyang/p/5586009.html

## 日期

2018 年 10 月 13 日 —— 这个题没有用OJ测试
