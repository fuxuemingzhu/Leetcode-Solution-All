
- 作者：    负雪明烛
- id：      fuxuemingzhu
- 公众号：负雪明烛
- 本文关键词：LeetCode，力扣，算法，算法题，外观数列，Count and Say，刷题群

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/count-and-say/#/description][1]


## 题目描述


The count-and-say sequence is the sequence of integers with the first five terms as following:

	1.     1
	2.     11
	3.     21
	4.     1211
	5.     111221

``1`` is read off as ``"one 1"`` or ``11``.
``11`` is read off as ``"two 1s"`` or ``21``.
``21`` is read off as ``"one 2, then one 1"`` or ``1211``.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.


Example 1:

	Input: 1
	Output: "1"

Example 2:

	Input: 4
	Output: "1211"

## 题目大意

统计连续字符出现的次数，说出这个字符是什么。把一个串就这么统计并且说出来。现在要知道第n个串说出来。

## 解题方法


### 解法一：循环


两重循环的思路是：

- 外层循环 $i$ 负责递增 $1 .. n$；
- 内存循环负责求当取值为 $i$ 时的外观数列。

​

Java 代码如下：

```java
public class Solution {
    public String countAndSay(int n) {
        StringBuilder ans = new StringBuilder("1");
        StringBuilder prev;
        int count;
        char say;
        for(int i = 1; i < n; i++){
            prev = ans;
            ans = new StringBuilder();
            count = 1;
            say = prev.charAt(0);
            for(int j = 1; j < prev.length(); j++){
                if(say != prev.charAt(j)){
                    ans.append(count).append(say);
                    count = 1;
                    say = prev.charAt(j);
                }else{
                    count++;
                }
            }
            ans.append(count).append(say);
        }
        return ans.toString();
    }
}

```

python 代码如下：
```python
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = "1"
        for i in range(n - 1):
            prev = res[0]
            count = 1
            ans = ""
            for j in range(1, len(res)):
                cur = res[j]
                if prev != cur:
                    ans = ans + str(count) + str(prev)
                    prev = cur
                    count = 0
                count += 1
            res = ans + str(count) + str(prev)
        return res

```


- 时间复杂度：$O(n * m)$，$n$ 是输入的数字，$m$ 是「外观数列」的最大长度；
- 空间复杂度：$O(m)$。

​

### 解法二：递归


其实，按照题目描述的话，我们最容易想到的应该就是递归解法。
​

题目描述是：

- `countAndSay(1) = "1"`
- `countAndSay(n)` 是对 `countAndSay(n-1)` 的描述，然后转换成另一个数字字符串。



这个意思就是想求 `countAndSay(n)` 的话，必须先求 `countAndSay(n-1)`，这就是标准的递归。
​

使用递归求解，一定不要用大脑去模拟递归的过程。大脑能压几个栈？
​

正确的做法是：记住递归函数的定义。比如本题中的递归函数 `countAndSay(int n)`含义是当取值为 $n$ 时的外观数列。
​

 那么，必须先求出取值为 $n - 1$ 时的外观数列，怎么求？根据递归函数的定义，就是  `countAndSay(n - 1)`。至于 `countAndSay(n - 1)` 怎么算的，我们不用管。只要知道这个函数能给我们正确的结果就行。
​

我在下面的代码把 `countAndSay(n - 1)` 的结果即为 `before`，然后统计了 `before` 中各个数字出现的次数，就是取值为 $n$ 时的外观数列。
​

C++ 代码如下：


```cpp
class Solution {
public:
    string countAndSay(int n) {
        if (n == 1) {
            return "1";
        }
        string before = countAndSay(n - 1);
        string res;
        char cur = before[0];
        int count = 1;
        for (int i = 1; i < before.size(); ++i) {
            if (before[i] != cur) {
                res += to_string(count) + cur;
                cur = before[i];
                count = 0;
            }
            count ++;
        }
        res += to_string(count) + cur;
        return res;
    }
};
```

- 时间复杂度：$O(n * m)$，$n$ 是输入的数字，$m$ 是「外观数列」的最大长度；
- 空间复杂度：$O(m)$。

## 刷题心得
- 递归是最贴合本题意的解法。
- 递归的时间复杂度和遍历是一样的，因为 $1..n$ 中的每个数字都被计算了一次。

## 日期

2017 年 5 月 11 日 
2018 年 11 月 22 日 —— 感恩节快乐～
2021 年 10 月 15 日

  [1]: https://leetcode.com/problems/count-and-say/#/description
