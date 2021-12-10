
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/custom-sort-string/description/


## 题目描述

S and T are strings composed of lowercase letters. In S, no letter occurs more than once.

S was sorted in some custom order previously. We want to permute the characters of T so that they match the order that S was sorted. More specifically, if x occurs before y in S, then x should occur before y in the returned string.

Return any permutation of T (as a string) that satisfies this property.

Example :

    Input: 
    S = "cba"
    T = "abcd"
    Output: "cbad"
    Explanation: 
    "a", "b", "c" appear in S, so the order of "a", "b", "c" should be "c", "b", and "a". 
    Since "d" does not appear in S, it can be at any position in T. "dcba", "cdba", "cbda" are also valid outputs.
 

Note:

1. S has length at most 26, and no character is repeated in S.
2. T has length at most 200.
3. S and T consist of lowercase letters only.

## 题目大意

S是一个自定义的字母表顺序，现在要把T中的字符按照S的顺序进行排序。如果T中有S中不存在的字符，那么可以处在结果的任何位置。

## 解题方法

### 按顺序构造字符串

使用字典保存T中的每个字母出现的次数，然后遍历S中的每个字符，查表构建新的结果字符串，并且把已经遍历了的字符的次数设为0。最后把count中剩余的字符放到最后。

这里用到了一个技巧，Counter中使用不存在的索引会返回0.

如：

    from collections import Counter
    count = Counter("Hello World!")
    print count['8']
    ##输出0

代码：

```python
from collections import Counter
class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        count = Counter(T)
        answer = ''
        for s in S:
            answer += s * count[s]
            count[s] = 0
        for c in count:
            answer += c * count[c]
        return answer
```

C++代码如下：

d.count(c)只会返回0或者1，想要得到次数使用d[c]，但是这个在不存在的情况下会新增key=c。最好使用find()返回的是迭代器。

```cpp
class Solution {
public:
    string customSortString(string S, string T) {
        map<char, int> d;
        for (char c : T) d[c]++;
        string res;
        for (char c : S) {
            for (int i = 0; i < d[c]; i++) {
                res += c;
            }
            d[c] = 0;
        }
        for (auto k : d) {
            if (k.second) {
                for (int i = 0; i < k.second; i++) {
                    res += k.first;
                }
            }
        }
        return res;
    }
};
```

学习到C++的string有构造方法以下构造方法：
```
(6) fill constructor
	string (size_t n, char c);
	Fills the string with n consecutive copies of character c.
```

注意第一个位置是字符重复次数，第二个参数是字符。代码如下：

```cpp
class Solution {
public:
    string customSortString(string S, string T) {
        map<char, int> d;
        for (char c : T) d[c]++;
        string res = "";
        for (char c : S) {
            res += string(d[c], c);
            d[c] = 0;
        }
        for (auto k : d) {
            res += string(k.second, k.first);
        }
        return res;
    }
};
```

### 排序

这个题目里面说了，在S中没有出现的字符可以出现在任意位置，所以这个题本质上上也是一个排序问题。对于排序问题，我们就必须明白，按照什么排序。在string中默认的排序方式是ASCII，但是这个题相当于给了我们一个新的排序方法：按照在S出现的位置排序。

所以，使用字典保存S中字符出现的每个位置索引，然后对T进行排序，排序的key就是该字符在S中的位置索引。由于使用的字典是defaultdict，因此如果T中的字符在S中没有出现，那么位置会是0，这个无所谓了，题目不关心。

python代码如下：


```python
class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        pos = collections.defaultdict(int)
        for i in range(len(S)):
            pos[S[i]] = i
        res = sorted(T, key = lambda x : pos[x])
        return "".join(res)
```


## 日期

2018 年 2 月 26 日 
2018 年 12 月 4 日 —— 周二啦！
2019 年 1 月 6 日 —— 打球打的腰酸背痛

  [1]: http://bpic.588ku.com/element_pic/00/00/07/125784e23ebbd9a.jpg
