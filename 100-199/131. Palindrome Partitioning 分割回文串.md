
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/palindrome-partitioning/description/

## 题目描述


Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

	Input: "aab"
	Output:
	[
	  ["aa","b"],
	  ["a","a","b"]
	]

## 题目大意

找出一个字符串可以构成的所有可能回文子字符串。

## 解题方法

### 回溯法

看到所有可能的结果的时候，一般想到回溯。

这个题和之前的回溯有个差别，那就是继续开始回溯的条件是目前的结果已经是回文串。然后从后面的字符开始继续回溯。感觉回溯都是套路，80%的代码可以通用的，最好背下来。

特别注意切片的位置，以及path + [s[:i]]产生了新的list中，所以append时候才有效。

```python
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.isPalindrome = lambda s : s == s[::-1]
        res = []
        self.helper(s, res, [])
        return res
        
    def helper(self, s, res, path):
        if not s:
            res.append(path)
            return
        for i in range(1, len(s) + 1): #注意起始和结束位置
            if self.isPalindrome(s[:i]):
                self.helper(s[i:], res, path + [s[:i]])
```

和上面思想相同的经典C++回溯法写法如下：

```cpp
class Solution {
public:
    vector<vector<string>> partition(string s) {
        vector<vector<string>> res;
        helper(s, res, {});
        return res;
    }
    void helper(string s, vector<vector<string>>& res, vector<string> path) {
        if (s.size() == 0) {
            res.push_back(path);
            return;
        }
        for (int i = 1; i <= s.size(); i++) {
            string pre = s.substr(0, i);
            if (isPalindrome(pre)) {
                path.push_back(pre);
                helper(s.substr(i), res, path);
                path.pop_back();
            }
        }
    }
    bool isPalindrome(string s) {
        if (s.size() == 0) return true;
        int start = 0, end = s.size() - 1;
        while (start <= end) {
            if (s[start] != s[end])
                return false;
            start ++;
            end --;
        }
        return true;
    }
};
```

如果不使用新的函数，只是用题目给的函数也能通过，唯一需要注意的是，当字符串长度是0的时候返回的是空，那么我们没办法在for循环里面进行遍历，所以新增上一个空字符串，最后再去掉。

```cpp
class Solution {
public:
    vector<vector<string>> partition(string s) {
        vector<vector<string>> res;
        if (s.size() == 0) return res;
        for (int i = 1; i <= s.size(); i++) {
            string pre = s.substr(0, i);
            if (isPalindrome(pre)) {
                vector<vector<string>> next = partition(s.substr(i));
                if (next.size() == 0)
                    next.push_back({""});
                for (vector<string> vs : next) {
                    vector<string> path;
                    path.push_back(pre);
                    for (string s : vs) {
                        if (s == "")
                            continue;
                        path.push_back(s);
                    }
                    res.push_back(path);
                }
            }
        }
        return res;
    }
    bool isPalindrome(string s) {
        if (s.size() == 0) return true;
        int start = 0, end = s.size() - 1;
        while (start <= end) {
            if (s[start] != s[end])
                return false;
            start ++;
            end --;
        }
        return true;
    }
};
```

## 日期

2018 年 3 月 15 日 ——雾霾消散，春光明媚
2018 年 12 月 21 日 —— 一周就要过去了

  [1]: http://blog.csdn.net/fuxuemingzhu/article/details/79573621
