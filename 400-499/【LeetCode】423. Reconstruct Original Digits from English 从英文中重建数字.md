# 【LeetCode】423. Reconstruct Original Digits from English 解题报告（Python）

标签： LeetCode

---

题目地址：https://leetcode.com/problems/reconstruct-original-digits-from-english/description/

## 题目描述：

Given a non-empty string containing an out-of-order English representation of digits 0-9, output the digits in ascending order.

Note:

1. Input contains only lowercase English letters.
1. Input is guaranteed to be valid and can be transformed to its original digits. That means invalid inputs such as "abc" or "zerone" are not permitted.
1. Input length is less than 50,000.

    Example 1:
    Input: "owoztneoer"
    
    Output: "012"
    
    Example 2:
    Input: "fviefuro"
    
    Output: "45"

## 题目大意

根据一个打乱了的英文表示的字符串以升序重构出阿拉伯数字。

## 解题方法

刚开始就做错了，都怪我太年轻，以为从0~9把所有能够成的都提前构成，最后就是结果了。这样不对，因为可能会有剩余的字符了。这个题说了，不会有剩余字符。

这个题不是很好，并没有考编程的思想，而是考的找规律。。面试应该不会问的。

错误代码：

```python
class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        number = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        count = collections.Counter(s)
        res = ''
        for i, num in enumerate(number):
            while True:
                word_count = 0
                for c in num:
                    if count[c] > 0:
                        word_count += 1
                if word_count == len(num):
                    res += str(i)
                    count.subtract(collections.Counter(num))
                else:
                    break
        return res
```

正确做法如下：

选自：http://bookshadow.com/weblog/2016/10/16/leetcode-reconstruct-original-digits-from-english/

> 统计字符串s中各字符的个数，需要注意的是，在枚举英文字母时，需要按照特定的顺序方可得到正确答案。
> 
> 例如按照顺序：6028745913，这个顺序可以类比拓扑排序的过程。
> 
> 观察英文单词，six, zero, two, eight, seven, four中分别包含唯一字母x, z, w, g, v,
> u；因此6, 0, 2, 8, 7, 4需要排在其余数字之前。
> 
> 排除这6个数字之后，剩下的4个数字中，按照字母唯一的原则顺次挑选。
> 
> 由于剩下的单词中，只有five包含f，因此选为下一个单词；
> 
> 以此类推，可以得到上面所述的顺序。

在上文代码的基础上，我进行了一点点的技巧性的改变，就是Counter()自带的有subtract()方法，直接从字典中减去了新字典。。

```python
class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        cnts = collections.Counter(s)
        nums = ['six', 'zero', 'two', 'eight', 'seven', 'four', 'five', 'nine', 'one', 'three']
        numc = [collections.Counter(num) for num in nums]
        digits = [6, 0, 2, 8, 7, 4, 5, 9, 1, 3]
        ans = [0] * 10
        for idx, num in enumerate(nums):
            cntn = numc[idx]
            t = min(cnts[c] /  cntn[c] for c in cntn)
            ans[digits[idx]] = t
            for i in range(t):
                cnts.subtract(cntn)
        return ''.join(str(i) * n for i, n in enumerate(ans))
```


## 日期

2018 年 3 月 13 日 


  [1]: http://blog.csdn.net/fuxuemingzhu/article/details/79541501