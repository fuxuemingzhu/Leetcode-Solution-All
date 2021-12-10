
- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)
- 个人公众号：负雪明烛
- 本文关键词：电话号码, 字母组合，回溯法，题解，leetcode, 力扣，Python, C++, Java

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/generate-parentheses/description/


## 题目描述


Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

![在这里插入图片描述](https://img-blog.csdnimg.cn/img_convert/373139be54a2234a583eea9709c841fd.png)

Example:

	Input: "23"
	Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.

## 题目大意

在拨号键盘上按下了几个键，问能打出来的字符串的所有组合是多少。

## 解题方法

### 回溯法

依然是回溯法。要求所有的可能的字符串的组合。

有点类似784. Letter Case Permutation，不需要对index进行for循环，因为对index进行for循环产生的是所有可能的组合。而这两个题要求的组合的长度是固定的，每个位置都要有字母。

另外就是要判断一下``path != ''``，原因是当 digits 为`""`的要求的结果是 `[]` ，而不是 `[""]` 。

Python代码如下：

```python
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        kvmaps = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        res = []
        self.dfs(digits, 0, res, '', kvmaps)
        return res
    
    def dfs(self, string, index, res, path, kvmaps):
        if index == len(string):
            if path != '':
                res.append(path)
            return
        for j in kvmaps[string[index]]:
            self.dfs(string, index + 1, res, path + j, kvmaps)
```

如果不新增函数，而是直接使用题目给出的函数，也可以很快写出代码。唯一要注意的是，当题目输入为``""``的时候，要返回{}，那么for循环就没法遍历，所以我给他添加成了``{""}``，这样循环就能进行了。

```cpp
class Solution {
public:
    vector<string> letterCombinations(string digits) {
        if (digits.size() == 0) return {};
        vector<string> res;
        for (char d : board[digits[0]]) {
            auto next = letterCombinations(digits.substr(1));
            if (next.size() == 0)
                next.push_back("");
            for (string n : next) {
                res.push_back(d + n);
            }
        }
        return res;
    }
private:
    unordered_map<char, string> board = {{'2', "abc"}, {'3', "def"}, {'4', "ghi"}, {'5', "jkl"}, {'6', "mno"}, {'7', "pqrs"}, {'8', "tuv"}, {'9', "wxyz"}};
};
```

### 内置函数

使用python 自带的product笛卡尔乘积函数。

```python
from itertools import product
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        kvmaps = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        answer = []
        for each in product(*[kvmaps[key] for key in digits]):
            answer.append(''.join(each))
        return answer
```

### 循环

使用循环也能轻松把这个题目给搞定。使用结果数组res表示遍历到当前的位置已有的结果，那么再遍历下一个位置的时候，把这个位置能形成的所有结果和原来的进行两两组合。

python代码如下：

```python
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "": return []
        d = {'2' : "abc", '3' : "def", '4' : "ghi", '5' : "jkl", '6' : "mno", '7' : "pqrs", '8' : "tuv", '9' : "wxyz"}
        res = ['']
        for e in digits:
            res = [w + c for c in d[e] for w in res]
        return res
```

## 日期

2018 年 2 月 24 日 
2018 年 12 月 21 日 —— 一周就要过去了
2019 年 1 月 8 日 —— 别熬夜，我都开始有黑眼圈了。。


  [1]: http://img.blog.csdn.net/20150926195427474
