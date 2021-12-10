作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址: https://leetcode.com/problems/repeated-dna-sequences/description/

## 题目描述：

All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

Example:

    Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    
    Output: ["AAAAACCCCC", "CCCCCAAAAA"]


## 题目大意

在一个字符串中找出连续的十个字符，这十个字符不止在一个地方出现过。

## 解题方法

遍历+set。

做法简单了，需要一个长度是10的字符串切片，从头到尾把字符遍历一遍，然后不停的判断以这个位置开头的10个字符构成的字符串是否看到过，如果看到过就放到另外一个set里。为什么不直接放入list返回呢？因为一个字符串可能会重复多次，为了防止重复添加到结果里，必须set一下。

时间复杂度是O(N)，空间复杂度是O(N)。

```python
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        seen = set()
        repeated = set()
        N = len(s)
        for i in range(N):
            cur = s[i : i+ 10]
            if cur in seen:
                repeated.add(cur)
            else:
                seen.add(cur)
        return list(repeated)
```


参考资料：

https://leetcode.com/problems/repeated-dna-sequences/discuss/53855/7-lines-simple-Java-O(n)

## 日期

2018 年 10 月 11 日 —— 做Hard题真的很难
