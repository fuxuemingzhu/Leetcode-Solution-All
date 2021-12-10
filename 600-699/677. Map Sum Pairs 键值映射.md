
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/map-sum-pairs/description/

## 题目描述

Implement a MapSum class with insert, and sum methods.

For the method insert, you'll be given a pair of (string, integer). The string represents the key and the integer represents the value. If the key already existed, then the original key-value pair will be overridden to the new one.

For the method sum, you'll be given a string representing the prefix, and you need to return the sum of all the pairs' value whose key starts with the prefix.

Example 1:

    Input: insert("apple", 3), Output: Null
    Input: sum("ap"), Output: 3
    Input: insert("app", 2), Output: Null
    Input: sum("ap"), Output: 5


## 题目大意

定义了两个元素，添加和求和。添加是输入字符串和数字的键值对，求和是对所有具有相同前缀的字符串的值求和。

## 解题方法

### 字典

使用字典有两种方法，第一种是在插入的时候保留完整字符串，在查找的时候才遍历所有子串；第二种是在插入的时候把所有前缀就进行计数，在查找的时候直接返回前缀的数目即可。

下面的做法是在插入的时候直接插入数值，在查找的时候才遍历子串的方式， C++代码如下：

```cpp
class MapSum {
public:
    /** Initialize your data structure here. */
    MapSum() {
        
    }
    
    void insert(string key, int val) {
        m_[key] = val;
    }
    
    int sum(string prefix) {
        int count = 0;
        const int N = prefix.size();
        for (auto a : m_) {
            if (a.first.substr(0, N) == prefix) {
                count += a.second;
            }
        }
        return count;
    }
private:
    unordered_map<string, int> m_;
};

/**
 * Your MapSum object will be instantiated and called as such:
 * MapSum obj = new MapSum();
 * obj.insert(key,val);
 * int param_2 = obj.sum(prefix);
 */
```

同样地一个巧妙的做法是，使用有序字典，然后用lower_bound找出prefix的位置，然后向后遍历，直到不等于prefix为止，然后把这部分进行求和就得到了前缀的数目。事实上，没有我上面的一种做法快。

```cpp
class MapSum {
public:
    /** Initialize your data structure here. */
    MapSum() {
        
    }
    
    void insert(string key, int val) {
        m_[key] = val;
    }
    
    int sum(string prefix) {
        int res = 0, n = prefix.size();
        for (auto it = m_.lower_bound(prefix); it != m_.end(); ++it) {
            if (it->first.substr(0, n) != prefix) break;
            res += it->second;
        }
        return res;
    }
private:
    map<string, int> m_;
};

/**
 * Your MapSum object will be instantiated and called as such:
 * MapSum obj = new MapSum();
 * obj.insert(key,val);
 * int param_2 = obj.sum(prefix);
 */
```


### 前缀树

还是使用前缀树。只不过这次是在每个经过的节点都保存了以此节点为前缀的字符串的值的和。这样，求和操作就变得很简单，只需找出相应的前缀对应的和即可。

需要注意的一点是，如果是相同的字符串的插入操作，是进行覆盖的。

```python
class Node(object):
    def __init__(self, count = 0):
        self.children = collections.defaultdict(Node)
        self.count = count
        
class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()
        self.keys = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        curr = self.root
        delta = val - self.keys.get(key, 0)
        # 更新保存键值对的keys
        self.keys[key] = val
        
        curr = self.root
        # 更新节点的count
        curr.count += delta
        for char in key:
            curr = curr.children[char]
            curr.count += delta

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return 0
            curr = curr.children[char]
        return curr.count


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
```

C++版本的前缀树实现如下，注意需要手写析构函数。

```cpp
class MapSum {
public:
    /** Initialize your data structure here. */
    MapSum() {}
    
    void insert(string key, int val) {
        int inc = val - vals_[key];
        Trie* p = &root;
        for (const char c : key) {
            if (!p->children[c])
                p->children[c] = new Trie();
            p->children[c]->sum += inc;
            p = p->children[c];
        }
        vals_[key] = val;
    }
    
    int sum(string prefix) {
        Trie* p = &root;
        for (const char c : prefix) {
            if (!p->children[c])
                return 0;
            p = p->children[c];
        }
        return p->sum;
    }
private:
    struct Trie {
        Trie():children(128, nullptr), sum(0){}
        ~Trie(){
            for (auto child : children)
                if (child) delete child;
            children.clear();
        }
        vector<Trie*> children;
        int sum;
    };
    
    Trie root;
    unordered_map<string, int> vals_;
};

/**
 * Your MapSum object will be instantiated and called as such:
 * MapSum obj = new MapSum();
 * obj.insert(key,val);
 * int param_2 = obj.sum(prefix);
 */
```

参考资料：

http://www.cnblogs.com/grandyang/p/7616525.html
https://zxi.mytechroad.com/blog/tree/leetcode-677-map-sum-pairs/

## 日期

2018 年 3 月 4 日 
2018 年 12 月 15 日 —— 今天四六级
