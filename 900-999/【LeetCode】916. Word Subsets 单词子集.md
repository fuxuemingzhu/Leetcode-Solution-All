作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址: https://leetcode.com/problems/word-subsets/description/

## 题目描述：

We are given two arrays A and B of words.  Each word is a string of lowercase letters.

Now, say that word b is a subset of word a if every letter in b occurs in a, including multiplicity.  For example, "wrr" is a subset of "warrior", but is not a subset of "world".

Now say a word a from A is universal if for every b in B, b is a subset of a. 

Return a list of all universal words in A.  You can return the words in any order.

 

Example 1:

    Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","o"]
    Output: ["facebook","google","leetcode"]

Example 2:

    Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["l","e"]
    Output: ["apple","google","leetcode"]

Example 3:

    Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","oo"]
    Output: ["facebook","google"]

Example 4:

    Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["lo","eo"]
    Output: ["google","leetcode"]

Example 5:

    Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["ec","oc","ceo"]
    Output: ["facebook","leetcode"]

Note:

1. ``1 <= A.length, B.length <= 10000``
1. ``1 <= A[i].length, B[i].length <= 10``
1. ``A[i]`` and ``B[i]`` consist only of lowercase letters.
1. All words in ``A[i]`` are unique: there isn't ``i != j`` with ``A[i] == A[j]``.


## 题目大意

如果B中的每一个元素中的每个字符都能在A中的某个字符串中找到，那么这个是个符合要求的字符串。求A中所有满足要求的字符串。

## 解题方法

如果按照题目要求的意思去直接做，那么要遍历B的每个元素的每个字符与A对应，这个时间复杂度肯定过不了OJ。所以，采用了一个很巧妙的方法，把B当做一个限制条件，直接求解这个限制条件。

对B的每个元素遍历，然后统计每个元素中每个字符串出现的次数，更新整体限制条件为每个元素在字符串中出现的次数的最大值。

统计结束之后，对A遍历的时候，只要看A是否满足这个限制条件就行了，所以挺快的。

时间复杂度是O(N)，空间复杂度是O(N)。

```python
class Solution(object):
    def wordSubsets(self, A, B):
        """
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        """
        B = set(B)
        res = []
        count = collections.defaultdict(int)
        for b in B:
            cb = collections.Counter(b)
            for c, v in cb.items():
                count[c] = max(count[c], v)
        res = []
        for a in A:
            ca = collections.Counter(a)
            isSuccess = True
            for c, v in count.items():
                if v > ca[c]:
                    isSuccess = False
                    break
            if isSuccess:
                res.append(a)
        return res
```

参考资料：

https://leetcode.com/problems/word-subsets/discuss/175854/C++JavaPython-Straight-Forward

## 日期

2018 年 9 月 30 日 —— 9月最后一天啦！


  [1]: https://blog.csdn.net/likewind1993/article/details/78473302
