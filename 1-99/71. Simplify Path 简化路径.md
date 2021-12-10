# 【LeetCode】71. Simplify Path 解题报告（Python）

标签（空格分隔）： LeetCode

作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.me/

---

题目地址：https://leetcode.com/problems/simplify-path/description/

## 题目描述：

Given an absolute path for a file (Unix-style), simplify it.

For example,

    path = "/home/", => "/home"
    path = "/a/./b/../../c/", => "/c"

Corner Cases:

- Did you consider the case where path = "/../"?
In this case, you should return "/".

- Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".


## 题目大意

简化linux路径。

## 解题方法

看到这种来来回回，增增删删的题，一般都想到用栈。

我们把字符串按照/分割之后就得到了每个文件的目录，然后判断路径是添加还是向上层进行返回。这个题很简单了。

有一个地方犯了小错误，不能写成if dir == '..' and stack: stack.pop()。这样的话如果栈是空的，就把..进栈了。
                   

```python
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = list()
        dirs = path.split('/')
        for dir in dirs:
            if not dir or dir == '.':
                continue
            if dir == '..':
                if stack:
                    stack.pop()
            else:                
                stack.append(dir)
        return '/' + '/'.join(stack)
```

## 日期

2018 年 6 月 26 日 ———— 早睡早起