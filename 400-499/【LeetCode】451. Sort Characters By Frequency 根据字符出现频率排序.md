
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/sort-characters-by-frequency/description/

## 题目描述

Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:
    
    Input:
    "tree"
    
    Output:
    "eert"
    
    Explanation:
    'e' appears twice while 'r' and 't' both appear once.
    So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
    
Example 2:
    
    Input:
    "cccaaa"
    
    Output:
    "cccaaa"
    
    Explanation:
    Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
    Note that "cacaca" is incorrect, as the same characters must be together.
    
Example 3:
    
    Input:
    "Aabb"
    
    Output:
    "bbAa"
    
    Explanation:
    "bbaA" is also a valid answer, but "Aabb" is incorrect.
    Note that 'A' and 'a' are treated as two different characters.


## 题目大意

很喜欢这种题目很短，而栗子很多的题目~

题意就是把字符串按照字符出现的次数重新排列。

## 解题方法

### 字典

用python真的超级简单呀~使用Counter类就能统计每个字符出现的次数，使用most_common函数就能按次序排列，最后字符与其出现的次数相乘就得到了字符串~

下面是使用的一个例子的结果：

    count = collections.Counter('abbdfas').most_common()
    print count
    
    # 输出
    [('a', 2), ('b', 2), ('s', 1), ('d', 1), ('f', 1)]

代码：

```python
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = collections.Counter(s).most_common()
        res = ''
        for c, v in count:
            res += c * v
        return res
```

### 优先级队列

C++默认的priority_queue是大顶堆。

C++构造把字符重复多次的新字符串的一个方法是append方法，第一个参数是整形表示重复次数，第二个参数是字符。

C++代码如下：

```cpp
class Solution {
public:
    string frequencySort(string s) {
        string res;
        unordered_map<char, int> count;
        for (char c : s) count[c]++;
        priority_queue<pair<int, char>> q;
        for (auto a : count) q.push({a.second, a.first});
        while (!q.empty()) {
            auto t = q.top(); q.pop();
            res.append(t.first, t.second);
        }
        return res;
    }
};
```

### 排序

参考Grandyang的解法：http://www.cnblogs.com/grandyang/p/6231504.html

我们也可以使用STL自带的sort来做，关键就在于重写comparator，由于需要使用外部变量，记得中括号中放入＆，然后我们将频率大的返回，注意一定还要处理频率相等的情况，要不然两个频率相等的字符可能穿插着出现在结果res中，这样是不对的。参见代码如下。

```cpp
class Solution {
public:
    string frequencySort(string s) {
        unordered_map<char, int> m;
        for (char c : s) ++m[c];
        sort(s.begin(), s.end(), [&](char& a, char& b){
            return m[a] > m[b] || (m[a] == m[b] && a < b);
        });
        return s;
    }
};
```

## 日期

2018 年 3 月 4 日 
2018 年 12 月 11 日 —— 双十一已经过去一个月了，真快啊。。
