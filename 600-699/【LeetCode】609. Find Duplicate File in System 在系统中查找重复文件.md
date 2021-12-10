
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/find-duplicate-file-in-system/description/

## 题目描述

Given a list of directory info including directory path, and all the files with contents in this directory, you need to find out all the groups of duplicate files in the file system in terms of their paths.

A group of duplicate files consists of at least two files that have exactly the same content.

A single directory info string in the input list has the following format:

    "root/d1/d2/.../dm f1.txt(f1_content) f2.txt(f2_content) ... fn.txt(fn_content)"

It means there are n files (f1.txt, f2.txt ... fn.txt with content f1_content, f2_content ... fn_content, respectively) in directory root/d1/d2/.../dm. Note that n >= 1 and m >= 0. If m = 0, it means the directory is just the root directory.

The output is a list of group of duplicate file paths. For each group, it contains all the file paths of the files that have the same content. A file path is a string that has the following format:

"directory_path/file_name.txt"

Example 1:

    Input:
    ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
    Output:  
    [["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]

Note:

1. No order is required for the final output.
1. You may assume the directory name, file name and file content only has letters and digits, and the length of file content is in the range of [1,50].
1. The number of files given is in the range of [1,20000].
1. You may assume no files or directories share the same name in the same directory.
1. You may assume each given directory info represents a unique directory. Directory path and file info are separated by a single blank space.

Follow-up beyond contest:

1. Imagine you are given a real file system, how will you search files? DFS or BFS?
1. If the file content is very large (GB level), how will you modify your solution?
1. If you can only read the file by 1kb each time, how will you modify your solution?
1. What is the time complexity of your modified solution? What is the most time-consuming part and memory consuming part of it? How to optimize?
1. How to make sure the duplicated files you find are not false positive?

## 题目大意

把不同文件夹中所有文件内容相同的文件放到一起。

## 解题方法

这个题很简单，只需要使用字典进行``内容==>目录``的对应保存即可。因为要得到内容相同的目录的列表，所以把内容作为键，把目录列表作为值。最后的结果要目录列表内容长度>1才行。

Python代码：

```python
class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        filemap = collections.defaultdict(list)
        for path in paths:
            roads = path.split()
            directory, files = roads[0], roads[1:]
            for file in files:
                file_s = file.split('(')
                name, content = file_s[0], file_s[1][:-1]
                full = directory + '/' + name
                filemap[content].append(full)
        return [full for full in filemap.values() if len(full) > 1]
```

这个题的C++解法让我学习到了istringstream的用法，istringstream是一个比较有用的c++的输入输出控制类。

C++引入了ostringstream、istringstream、stringstream这三个类，要使用他们创建对象就必须包含<sstream>这个头文件。
istringstream类用于执行C++风格的串流的输入操作。
ostringstream类用于执行C风格的串流的输出操作。
strstream类同时可以支持C风格的串流的输入输出操作。

和常见的iostream有点类似，可以对应理解。


C++代码如下：

```cpp
class Solution {
public:
    vector<vector<string>> findDuplicate(vector<string>& paths) {
        unordered_map<string, vector<string>> m;
        vector<vector<string>> res;
        for (string& path : paths) {
            istringstream is(path);
            string pre = "", t = "";
            is >> pre;
            while (is >> t) {
                int idx = t.find_last_of("(");
                string dir = pre + "/" + t.substr(0, idx);
                string content = t.substr(idx + 1, t.size() - idx - 2);
                m[content].push_back(dir);
            }
        }
        for (auto a : m) 
            if (a.second.size() > 1)
                res.push_back(a.second);
        return res;
    }
};
```

参考资料：

http://www.cnblogs.com/grandyang/p/7007974.html
https://blog.csdn.net/longzaitianya1989/article/details/52909786

## 日期

2018 年 3 月 4 日 
2018 年 12 月 12 日 —— 双十二

  [1]: http://blog.csdn.net/fuxuemingzhu/article/details/79359540
