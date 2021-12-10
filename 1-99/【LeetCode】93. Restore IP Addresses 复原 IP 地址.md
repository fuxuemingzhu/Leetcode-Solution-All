
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/restore-ip-addresses/description/

## 题目描述

Given a string containing only digits, restore it by returning all possible valid IP address combinations.

Example:
    
    Input: "25525511135"
    Output: ["255.255.11.135", "255.255.111.35"]

## 题目大意

题目中给了一个仅有数字组成的字符串，要求这个字符串能构成的合法IP组合。

## 解题方法

### 回溯法

我是按照Tag刷的，当然知道这个题是回溯法了。。其实只要看到所有的组合，一般都是用回溯。

第一遍超时，原因是没有找到合理的剪枝！！这就是回溯法最难的地方：剪枝！

当然了，看出了测试用例是一个特别长的由1组成的字符串，仅仅这一个测试用例超时，所以我加上了len(s)和12的判断就ok了。所以有了下面的版本：

代码如下：

```python
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) > 12:
            return []
        res = []
        self.dfs(s, [], res)
        return res
        
    def dfs(self, s, path, res):
        if not s and len(path) == 4:
            res.append('.'.join(path))
            return
        for i in range(1, 4):
            if i > len(s):
                continue
            number = int(s[:i])
            if str(number) == s[:i] and number <= 255:
                self.dfs(s[i:], path + [s[:i]], res)
```

看到了题目中有别的同学的剪枝方法特别好，那就是每次dfs的时候都去检查一下所有的字符串的长度是不是能满足在最多4个3位数字组成，果然速度提升了很多：


```python
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        self.dfs(s, [], res)
        return res
        
    def dfs(self, s, path, res):
        if len(s) > (4 - len(path)) * 3:
            return
        if not s and len(path) == 4:
            res.append('.'.join(path))
            return
        for i in range(min(3, len(s))):
            curr = s[:i+1]
            if (curr[0] == '0' and len(curr) >= 2) or int(curr) > 255:
                continue
            self.dfs(s[i+1:], path + [s[:i+1]], res)
```


二刷的时候，使用的C++，同样需要使用合理的剪枝，提交的时候有一次WA，原因是没有考虑0开头的整数是不合法的。代码如下：

```cpp
class Solution {
public:
    vector<string> restoreIpAddresses(string s) {
        if (s.size() > 12) return {};
        vector<string> res;
        helper(s, res, {}, 0);
        return res;
    }
    void helper(const string& s, vector<string>& res, vector<string> path, int start) {
        if (start > s.size() || path.size() > 4) return;
        if (start == s.size() && path.size() == 4) {
            res.push_back(path[0] + '.' + path[1] + '.' + path[2] + '.' + path[3]);
            return;
        }
        for (int i = 1; i <= 3; i++) {
            string sub = s.substr(start, i);
            if (sub.size() == 0 || (sub.size() > 1 && sub[0] == '0') || stoi(sub) > 255) continue;
            path.push_back(sub);
            helper(s, res, path, start + i);
            path.pop_back();
        }
    }
};
```

## 日期

2018 年 6 月 11 日 —— 今天学科三在路上跑的飞快～
2018 年 12 月 22 日 —— 今天冬至
