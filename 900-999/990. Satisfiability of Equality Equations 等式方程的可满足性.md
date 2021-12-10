作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/satisfiability-of-equality-equations/


## 题目描述

Given an array equations of strings that represent relationships between variables, each string ``equations[i]`` has length 4 and takes one of two different forms: ``"a==b"`` or ``"a!=b"``.  Here, a and b are lowercase letters (not necessarily different) that represent one-letter variable names.

Return ``true`` if and only if it is possible to assign integers to variable names so as to satisfy all the given equations.


Example 1:

    Input: ["a==b","b!=a"]
    Output: false
    Explanation: If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second.  There is no way to assign the variables to satisfy both equations.

Example 2:

    Input: ["b==a","a==b"]
    Output: true
    Explanation: We could assign a = 1 and b = 1 to satisfy both equations.

Example 3:

    Input: ["a==b","b==c","a==c"]
    Output: true

Example 4:

    Input: ["a==b","b!=c","c==a"]
    Output: false

Example 5:

    Input: ["c==c","b==d","x!=z"]
    Output: true
 
Note:

1. 1 <= equations.length <= 500
1. equations[i].length == 4
1. equations[i][0] and equations[i][3] are lowercase letters
1. equations[i][1] is either '=' or '!'
1. equations[i][2] is '='


## 题目大意

给了一连串的等式和不等式，判断这些等式和不等式能否同时都成立。

## 解题方法

### DFS

这题最难的部分就是数据抽象，其实并不难：把每个字母当做一个节点，把等号代表两个节点之间有连接，把不等号代表两个节点之间没有连接。判断这样的图是否存在。

由此可见，我们首先可以根据等号关系，把这个网的所有节点之间的连接构成一个无向图。然后对于不等号，我们记性dfs搜索，判断等号两边的节点能不能有路。如果有路代表两者通过一定的等号关系能够相互转化，那么就不符合不等号关系，返回false；如果所有不等号两边的节点都没有路，那么返回true.

这个题直接搜索的话会超时，可以把已经访问过的节点保存下来，这样的话，等我们在搜索下一条路的时候不会走已经搜索过的节点。

python代码如下：

```python
class Solution(object):
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
        self.m = collections.defaultdict(list)
        for eq in equations:
            if eq[1] == '=':
                self.m[eq[0]].append(eq[3])
                self.m[eq[3]].append(eq[0])
        for eq in equations:
            if eq[1] == '!':
                if self.find(set(), eq[0], eq[3]) or self.find(set(), eq[3], eq[0]):
                    return False
        return True
        
    def find(self, visited, begin, end):
        if begin in visited:
            return False
        visited.add(begin)
        if begin == end:
            return True
        for n in self.m[begin]:
            if self.find(visited, n, end):
                return True
        return False
```

### 并查集

判断两个点直接是否有连接的一个更为简单的方法就是使用并查集。如果两个节点的祖先相同，说明两者之间有路。

下面是一种并查集的写法，这个写法在查找某个节点的祖先的时候做了路径压缩，使得被查找节点直接挂载到了祖先上，这样下次查找的时候就不用搜索那么多了。而合并的这一步骤，是直接查找到两个节点的左右祖先，把其中一个的祖先设置成为了另一个。

不要太纠结，记住，对于``a==b``，无论是a的祖先设置成b、还是把b的祖先设置成a，都不想影响查找出来的a和b的祖先是同一个元素。

python代码如下：

```python
class Solution(object):
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
        dsu = DSU()
        for eq in equations:
            if eq[1] == '=':
                dsu.u(ord(eq[0]) - ord('a'), ord(eq[3]) - ord('a'))
        for eq in equations:
            if eq[1] == '!':
                if dsu.f(ord(eq[0]) - ord('a')) == dsu.f(ord(eq[3]) - ord('a')):
                    return False
        return True
                
class DSU(object):
    def __init__(self):
        self.m = range(26)
    
    def f(self, x):
        if self.m[x] != x:
            self.m[x] = self.f(self.m[x])
        return self.m[x]
    
    def u(self, x, y):
        px = self.f(x)
        py = self.f(y)
        self.m[px] = py
```

C++代码如下：

```cpp
class Solution {
public:
    bool equationsPossible(vector<string>& equations) {
        init();
        for (string& s : equations) {
            if (s[1] == '=') {
                u(s[0] - 'a', s[3] - 'a');
            }
        }
        for (string& s : equations) {
            if (s[1] == '!') {
                if (f(s[0] - 'a') == f(s[3] - 'a'))
                    return false;
            }
        }
        return true;
    }
private:
    int _fa[26];
    
    void init() {
        for (int i = 0; i < 26; ++i) {
            _fa[i] = i;
        }
    }
    int f(int x) {
        if (_fa[x] == x) return x;
        return _fa[x] = f(_fa[x]);
    }
    void u(int a, int b) {
        int pa = f(a);
        int pb = f(b);
        _fa[pa] = pb;
    }
};
```

## 日期

2019 年 2 月 21 日 —— 一放假就再难抓紧了


  [1]: https://leetcode.com/problems/add-two-numbers/
