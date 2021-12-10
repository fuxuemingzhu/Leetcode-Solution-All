作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/longest-absolute-file-path/description/

## 题目描述：

Suppose we abstract our file system by a string in the following manner:

The string ``"dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"`` represents:

    dir
        subdir1
        subdir2
            file.ext

The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.

The string ``"dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"`` represents:

    dir
        subdir1
            file1.ext
            subsubdir1
        subdir2
            subsubdir2
                file2.ext

The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.

We are interested in finding the longest (number of characters) absolute path to a file within our file system. For example, in the second example above, the longest absolute path is ``"dir/subdir2/subsubdir2/file2.ext"``, and its length is 32 (not including the double quotes).

Given a string representing the file system in the above format, return the length of the longest absolute path to file in the abstracted file system. If there is no file in the system, return 0.

Note:

1. The name of a file contains at least a ``.`` and an extension.
1. The name of a directory or sub-directory will not contain a ``.``.
1. Time complexity required: O(n) where n is the size of the input string.

Notice that ``a/aa/aaa/file1.txt`` is not the longest file path, if there is another path ``aaaaaaaaaaaaaaaaaaaaa/sth.png``.

## 题目大意

给出了一个字符串表示的文件夹目录，现在需要求出最长的文件路径。文件的深度有``\t``个数标识，文件夹开始和终止有``\n``标识，有``.``的是文件否则是文件夹。注意文件路径长度是指拼成的绝对地址的长度，包括切割符``/``.

## 解题方法

第一个感觉DFS、或者栈。估计这两种方法都可以，我是使用栈做的，没想到这么简单就过了，难度在哪里。。

使用一个栈同时保存目录的深度，当前总的字符串长度，那么：

计算当前目录的深度，如果当前深度小于栈的深度，那么把栈弹出来到比当前浅为止。如果当前遍历到的是目录，如果大于栈中最上面目录的深度，那么进栈；如果当前遍历的是文件，那么统计总的深度即可。

需要注意的是，目录是需要分隔符的，所以目录进栈的深度应该是目录深度+1。

时间复杂度是O(N)，空间复杂度是O(N). N为input按照"\n"分割后的个数。

代码如下：

```python
class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        stack = [(-1, 0)] # 目录的深度，当前总的字符串长度
        max_len = 0
        for p in input.split("\n"):
            depth = p.count('\t')
            p = p.replace('\t', '')
            while stack and depth <= stack[-1][0]: # 一样深，或者当前目录更浅
                stack.pop()
            if '.' not in p: # 目录
                stack.append((depth, len(p) + stack[-1][1] + 1))
            else: # 文件
                max_len = max(max_len, len(p) + stack[-1][1])
        return max_len
```


## 日期

2018 年 9 月 25 日 —— 美好的一周又开始了，划重点，今天是周二
2019 年 3 月 13 日 —— 周赛进了第一页！
