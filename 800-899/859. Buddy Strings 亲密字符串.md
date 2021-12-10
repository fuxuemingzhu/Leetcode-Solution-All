
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/buddy-strings/description/

## 题目描述

Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.

Example 1:

    Input: A = "ab", B = "ba"
    Output: true

Example 2:

    Input: A = "ab", B = "ab"
    Output: false

Example 3:

    Input: A = "aa", B = "aa"
    Output: true

Example 4:

    Input: A = "aaaaaaabc", B = "aaaaaaacb"
    Output: true

Example 5:

    Input: A = "", B = "aa"
    Output: false
 

Note:

- 0 <= A.length <= 20000
- 0 <= B.length <= 20000
- A and B consist only of lowercase letters.

## 题目大意

当且仅当交换两个字符串中的两个字符的时候，看两个字符串能否完全相等。

## 解题方法

### 字典

分析如下：

1. 如果两个字符串长度不等，那么一定不满足条件
2. 如果两个字符串完全相等，如果其中存在至少两个相等字符，那么满足条件
3. 如果两个字符串长度相等且只有两个位置的字符不等，记录下这两个位置，如果这两个字符串的该两个位置字符是恰好错位的，那么满足条件。

代码如下：

```python3
class Solution:
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        diff = 0
        idxs = []
        for i, a in enumerate(A):
            if B[i] != a:
                diff += 1
                idxs.append(i)
        counter = dict()
        if diff == 0:
            for a in A:
                if a in counter and counter[a]:
                    return True
                else:
                    counter[a] = True
        if diff != 2:
            return False
        return A[idxs[0]] == B[idxs[1]] and A[idxs[1]] == B[idxs[0]]
```

C++版本如下：

```cpp
class Solution {
public:
    bool buddyStrings(string A, string B) {
        if (A.size() != B.size()) return false;
        vector<int> ca(26);
        vector<int> cb(26);
        int N = A.size();
        int diff = 0;
        for (int i = 0; i < N; i++) {
            if (A[i] != B[i] && diff++ > 2) return false;
            ca[A[i] - 'a']++;
            cb[B[i] - 'a']++;
        }
        for(int i = 0; i < 26; i++) {
            if (diff == 0 && ca[i] > 1) return true;
            if (ca[i] != cb[i]) return false;
        }
        return diff == 2;
    }
};
```

参考资料：https://zxi.mytechroad.com/blog/string/leetcode-859-buddy-strings/

## 日期

2018 年 7 月 4 日 —— 夏天挺热的，记得吃饭，防止低血糖
2018 年 11 月 30 日 —— 又到了周末
