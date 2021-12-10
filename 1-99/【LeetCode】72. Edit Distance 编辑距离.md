

作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/edit-distance/description/


## 题目描述

Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

1. Insert a character
1. Delete a character
1. Replace a character

Example 1:

    Input: word1 = "horse", word2 = "ros"
    Output: 3
    Explanation: 
    horse -> rorse (replace 'h' with 'r')
    rorse -> rose (remove 'r')
    rose -> ros (remove 'e')

Example 2:

    Input: word1 = "intention", word2 = "execution"
    Output: 5
    Explanation: 
    intention -> inention (remove 't')
    inention -> enention (replace 'i' with 'e')
    enention -> exention (replace 'n' with 'x')
    exention -> exection (replace 'n' with 'c')
    exection -> execution (insert 'u')

## 题目大意

给了两个字符串，现在有三种操作，问最少做多少次操作，能使word1变成word2。三种操作是：

1. 插入一个字符
2. 删除一个字符
3. 替换一个字符

## 解题方法
程序的世界真是其妙无穷。

很多人的解法直接上来就是动态规划，其实少了这个动态规划怎么想出来的过程。动态规划的思路就是 `递归 => 记忆化搜索 => 动态规划`，一步步提升转化出来的，大家都在讲动态规划，其实少了前两步的思考过程。

我现在详细讲解下`递归 => 记忆化搜索 => 动态规划`的优化过程。

### 递归

这个题和最长公共子序列非常相似，需要判断**最后的一个字符**是否相等：

- 如果相等，则最后一个字符不用做任何操作，那么只用计算除去最后一个字符外的前面的子串的编辑距离即可。
- 如果不等，则最后一个字符需要进行替换操作，那么只用计算除去最后一个字符外的前面的子串的编辑距离 ，再 +1（最后一个字符的替换操作），即可把word1变成word2。


图源花花酱：

![此处输入图片的描述][1]

代码比较简单，需要注意的是初始化的数组大小是 `L1 + 1` 和 `L2 + 1`，因为函数的意义是 `[0, L1], [0, L2]` 区间变成相等的最小操作次数，闭区间。

可以按照上面的思路，进行暴力的求解。但是会超时 TLE。

C++代码如下：

```cpp
class Solution {
public:
    int minDistance(string word1, string word2) {
        // cout << "word1: " << word1 << " word2: " << word2 << endl;
        int M = word1.size();
        int N = word2.size();
        if (M == 0) return N;
        if (N == 0) return M;
        if (word1[M - 1] == word2[N - 1]) {
            return minDistance(word1.substr(0, M - 1), word2.substr(0, N - 1));
        }
        return 1 + min(min(minDistance(word1.substr(0, M - 1), word2),
                      minDistance(word1, word2.substr(0, N - 1))),
                       minDistance(word1.substr(0, M - 1), word2.substr(0, N - 1)));
    }
};
```

### 记忆化搜索

上面的超时的原因是会有重复的计算，同样的一个状态会被不同的分支走多次，因此可以使用记忆化搜索，保存一下走过的状态的结果，如果另外一个分支走到了这个状态，那么可以直接查找之前的计算结果。

Python代码如下：

```python
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        L1, L2 = len(word1), len(word2)
        dp = [[-1] * (L2 + 1) for _ in range(L1 + 1)]
        return self.getDistance(word1, word2, dp, L1, L2)
    
    def getDistance(self, word1, word2, dp, pos1, pos2):
        if pos1 == 0: return pos2
        if pos2 == 0: return pos1
        if dp[pos1][pos2] >= 0: return dp[pos1][pos2]
        
        res = 0
        if word1[pos1 - 1] == word2[pos2 - 1]:
            res = self.getDistance(word1, word2, dp, pos1 - 1, pos2 - 1)
        else:
            res = min(self.getDistance(word1, word2, dp, pos1 - 1, pos2 - 1),
                      self.getDistance(word1, word2, dp, pos1, pos2 - 1),
                      self.getDistance(word1, word2, dp, pos1 - 1, pos2)) + 1
        dp[pos1][pos2] = res
        return res
```

C++代码如下：

```cpp
class Solution {
public:
    int minDistance(string word1, string word2) {
        const int L1 = word1.size();
        const int L2 = word2.size();
        dp_ = vector<vector<int>>(L1 + 1, vector<int>(L2 + 1, -1));
        return getDistance(word1, word2, L1, L2);
    }
private:
    vector<vector<int>> dp_;
    int getDistance(string& word1, string& word2, int l1, int l2) {
        if (l1 == 0) return l2;
        if (l2 == 0) return l1;
        if (dp_[l1][l2] >= 0) return dp_[l1][l2];
        
        int res = 0;
        if (word1[l1 - 1] == word2[l2 - 1])
            res = getDistance(word1, word2, l1 - 1, l2 - 1);
        else
            res = min(getDistance(word1, word2, l1 - 1, l2 - 1),
                     min(getDistance(word1, word2, l1 - 1, l2),
                     getDistance(word1, word2, l1, l2 - 1))) + 1;
        dp_[l1][l2] = res;
        return res;
    }
};
```

### 动态规划

**记忆化搜索**是自顶向下的操作，即如果求 word1 和 word2 的编辑距离 需要求除掉最后一个字符外的字符串的 编辑距离，依次递归下去。是个把问题规模逐渐变小的过程。

**动态规划**是自底向上的操作，即先求出最开始的边界条件，然后一步步添加字符，直到添加成 word1 和 word2 的时候，最后的编辑距离。是个把问题规模逐渐变大的过程。

知道了记忆化搜索之后，很容易改成动态规划。这两者的边界是一样的，只不过从递归转成了循环。

python代码如下：

```python
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        L1, L2 = len(word1), len(word2)
        dp = [[0] * (L2 + 1) for _ in range(L1 + 1)]
        for i in range(L1 + 1):
            dp[i][0] = i
        for j in range(L2 + 1):
            dp[0][j] = j
        for i in range(1, L1 + 1):
            for j in range(1, L2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        return dp[L1][L2]
```

C++代码如下：

```cpp
class Solution {
public:
    int minDistance(string word1, string word2) {
        const int L1 = word1.size();
        const int L2 = word2.size();
        vector<vector<int>> dp(L1 + 1, vector<int>(L2 + 1, -1));
        for (int i = 0; i <= L1; i++)
            dp[i][0] = i;
        for (int j = 0; j <= L2; j++)
            dp[0][j] = j;
        for (int i = 1; i <= L1; i++) {
            for (int j = 1; j <= L2; j++) {
                if (word1[i - 1] == word2[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1];
                } else {
                    dp[i][j] = min(dp[i - 1][j - 1], min(dp[i - 1][j], dp[i][j - 1])) + 1;
                }
            }
        }
        return dp[L1][L2];
    }
};
```

## 日期

2018 年 12 月 10 日 —— 又是周一！
2020 年 4 月 6 日 —— 又是周一！


  [1]: https://zxi.mytechroad.com/blog/wp-content/uploads/2017/10/72-ep87.png
