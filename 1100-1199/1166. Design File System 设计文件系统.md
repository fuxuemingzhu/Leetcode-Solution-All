
- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)

题目地址https://leetcode-cn.com/problems/design-file-system/

## 题目描述

You are asked to design a file system which provides two functions:

- `create(path, value)`: Creates a new path and associates a value to it if possible and returns True. Returns False if the path already exists or its parent path doesn't exist.
- `get(path)`: Returns the value associated with a path or returns `-1` if the path doesn't exist.

The format of a path is one or more concatenated strings of the form: `/` followed by one or more lowercase English letters. For example, `/leetcode` and `/leetcode/problems` are valid paths while an empty string and `/` are not.

Implement the two functions.

Please refer to the examples for clarifications.

Example 1:

    Input: 
    ["FileSystem","create","get"]
    [[],["/a",1],["/a"]]
    Output: 
    [null,true,1]
    Explanation: 
    FileSystem fileSystem = new FileSystem();
    
    fileSystem.create("/a", 1); // return true
    fileSystem.get("/a"); // return 1

Example 2:

    Input: 
    ["FileSystem","create","create","get","create","get"]
    [[],["/leet",1],["/leet/code",2],["/leet/code"],["/c/d",1],["/c"]]
    Output: 
    [null,true,true,2,false,-1]
    Explanation: 
    FileSystem fileSystem = new FileSystem();
    
    fileSystem.create("/leet", 1); // return true
    fileSystem.create("/leet/code", 2); // return true
    fileSystem.get("/leet/code"); // return 2
    fileSystem.create("/c/d", 1); // return false because the parent path "/c" doesn't exist.
    fileSystem.get("/c"); // return -1 because this path doesn't exist.
 

Constraints:

The number of calls to the two functions is less than or equal to 10^4 in total.
2 <= path.length <= 100
1 <= value <= 10^9


## 题目大意

你需要设计一个能提供下面两个函数的文件系统：
- `create(path, value)`: 创建一个新的路径，并尽可能将值 value 与路径 path 关联，然后返回 True。如果路径已经存在或者路径的父路径不存在，则返回 False。
- `get(path)`: 返回与路径关联的值。如果路径不存在，则返回 -1。

## 解题方法

### 字典

总体思想：使用字典保存每一个已经创建的路径。

- `create()`：找出其父路径，判断是否已经存在。当父路径存在时，字典保存新路径的值，否则不保存。
- `get()`：判断字典中是否已经存在该路径，如果存在返回对应的值，否则返回-1.

这个做法把所有的路径保存在同一级上，没有下面的目录树科学。

由于leetcode-cn无法提交该题答案，下面的代码没有submit。

C++代码如下：

```cpp
class FileSystem {
public:
    FileSystem() {
    }
    
    bool create(string path, int value) {
        if (path.empty() || path == "/" || path[0] != '/')
            return false;
        int last = path.size();
        while (last >= 1 && path[last] != '/') {
            last --;
        }
        string parent = path.substr(0, last);
        if (!m_.count(parent))
            return false;
        m_[path] = value;
        return true;
    }
    
    int get(string path) {
        return m_.count(path) ? m_[path] : -1;
    }
private:
    unordered_map<string, int> m_;
};

/**
 * Your FileSystem object will be instantiated and called as such:
 * FileSystem* obj = new FileSystem();
 * bool param_1 = obj->create(path,value);
 * int param_2 = obj->get(path);
 */
```

### 目录树

是否有更好的做法？类似于我们系统文件的保存方法？

我们可以创建一个目录树，把每一个路径对应一个叶子，其保存它的所有孩子。查找的时候也依次从目录树获取路径。这个结构类似于字典树。

![此处输入图片的描述][1]

代码没有写，待续。

## 日期

2019 年 9 月 23 日 —— 昨夜睡的早，错过了北京的烟火


  [1]: https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1569261609603&di=82f5df0898bf72cacf91ef738bdd2a9c&imgtype=jpg&src=http://img1.imgtn.bdimg.com/it/u=2382911796,3816115269&fm=214&gp=0.jpg
