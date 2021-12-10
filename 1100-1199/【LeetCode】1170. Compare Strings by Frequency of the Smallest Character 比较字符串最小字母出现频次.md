
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/

## 题目描述

Let's define a function `f(s)` over a non-empty string s, which calculates the frequency of the smallest character in `s`. For example, if `s = "dcce"` then `f(s) = 2` because the smallest character is `"c"` and its frequency is 2.

Now, given string arrays queries and words, return an integer array answer, where each `answer[i]` is the number of words such that `f(queries[i]) < f(W)`, where `W` is a word in words.


Example 1:

    Input: queries = ["cbd"], words = ["zaaaz"]
    Output: [1]
    Explanation: On the first query we have f("cbd") = 1, f("zaaaz") = 3 so f("cbd") < f("zaaaz").

Example 2:

    Input: queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]
    Output: [1,2]
    Explanation: On the first query only f("bbb") < f("aaaa"). On the second query both f("aaa") and f("aaaa") are both > f("cc").

Constraints:

1. `1 <= queries.length <= 2000`
1. `1 <= words.length <= 2000`
1. `1 <= queries[i].length, words[i].length <= 10`
1. `queries[i][j], words[i][j]` are English lowercase letters.

 
## 题目大意

定义f(s)为一个字符串中最小的字符(按字母序abcd..xyz)出现的次数。对于每个query的f(query)，求出words中f(word) > f(query)有多少个。

## 解题方法

### 双重循环

第一步，肯定要把每个query和word的f(s)求出来，求每个字符的次数，然后找出最小的字符出现的次数。
第二步，找出words中f(word) > f(query)有多少个时，对于2000*2000的量级，可以暴力两重循环，即对每个query都去遍历一次words的f(word)结果。

时间复杂度O(N^2).

这个题可以优化的地方在，求一个容器中有多少元素大于指定值，可以采用先排序再upper_bound()的方式降低时间度；或者利用题目给的限制：字符串的长度最多是10，因此f(s)一定小于等于10，这样可以用字典保存words中每个f(s)的次数，查找的时候直接在遍历字典中累计次数即可。

C++代码如下：

```cpp
class Solution {
public:
    vector<int> numSmallerByFrequency(vector<string>& queries, vector<string>& words) {
        vector<int> qs, ws;
        for (string& q : queries) {
            qs.push_back(getFrequency(q));
        }
        for (string& w : words) {
            ws.push_back(getFrequency(w));
        }
        vector<int> res;
        for (int q : qs) {
            int count = 0;
            for (int w : ws) {
                if (w > q)
                    count++;
            }
            res.push_back(count);
        }
        return res;
    }
    int getFrequency(string& word) {
        vector<int> counts(26, 0);
        for (char w : word) {
            counts[w - 'a']++;
        }
        for (int i = 0; i < 26; ++i) {
            if (counts[i] != 0)
                return counts[i];
        }
        return 0;
    }
};
```

## 日期

2019 年 8 月 31 日 —— 赶在月底做个题
