作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址: https://leetcode.com/problems/orderly-queue/description/

## 题目描述：

A string S of lowercase letters is given.  Then, we may make any number of moves.

In each move, we choose one of the first K letters (starting from the left), remove it, and place it at the end of the string.

Return the lexicographically smallest string we could have after any number of moves.

Example 1:

    Input: S = "cba", K = 1
    Output: "acb"
    Explanation: 
    In the first move, we move the 1st character ("c") to the end, obtaining the string "bac".
    In the second move, we move the 1st character ("b") to the end, obtaining the final result "acb".

Example 2:

    Input: S = "baaca", K = 3
    Output: "aaabc"
    Explanation: 
    In the first move, we move the 1st character ("b") to the end, obtaining the string "aacab".
    In the second move, we move the 3rd character ("c") to the end, obtaining the final result "aaabc".
 

Note:

1. 1 <= K <= S.length <= 1000
1. S consists of lowercase letters only.



## 题目大意

给了一个字符串和一个数字K，每次操作可以把字符串的前K个数字中任意抽取一个放到最后，可以做很多次操作。问，经过很多次操作之后，能构成的字母序最小的字符串是什么？

## 解题方法

这是一道智商题。

1. 当``K == 1``的时候，没有什么好说的，每次只能把每个开头的字母放到最后去，进行``S.length``次操作之后求字母序最小的字符串。这个操作是把字符串进行了旋转。

        12345 -> 23451 -> 34512 -> 45123 -> 51234

2. 当``K > 1``的时候，我们可以：
    1). 把字符串进行旋转（相当于``K == 1``）
    2). 把字符串除了第一个字符的其余部分进行旋转

        012345 -> 023451 -> 034512 -> 045123 -> 051234

所以，我们可以使用步骤1里面的操作，把整个字符串最小的数字放到最前面去。然后对字符串后面的部分再旋转使后面部分最小的数字放到前面……以此类推，我们可以得到任何字符串升序排列。

当k > 1的时候，这个过程相当于冒泡排序，所以，我们可以直接排序得到结果。

时间复杂度是O(N ^ 2)，空间复杂度是O(N)。

```python
class Solution(object):
    def orderlyQueue(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        if K == 1:
            res = S
            for i in range(len(S)):
                res = min(res, S[i:] + S[:i])
        else:
            res = "".join(sorted(list(S)))
        return res
```

参考资料：

https://leetcode.com/problems/orderly-queue/discuss/165878/C++JavaPython-Sort-String-or-Rotate-String

## 日期

2018 年 10 月 ４ 日 —— 一个很不容易察觉的小错误，需要总结一下坑了！
