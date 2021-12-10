
- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/flatten-nested-list-iterator/description/

## 题目描述

Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:
    
    Given the list [[1,1],2,[1,1]],
    
    By calling next repeatedly until hasNext returns false, 
    the order of elements returned by next should be: [1,1,2,1,1].
    
Example 2:
    
    Given the list [1,[4,[6]]],
    
    By calling next repeatedly until hasNext returns false, 
    the order of elements returned by next should be: [1,4,6].


## 题目大意

生成一个嵌套的数组迭代对象的迭代器。

## 解题方法
### 递归+队列
该做法是作弊方法，因为题目想要我们给出的迭代器应该是对原始对象的迭代，而不是对自己新建对象的迭代。

这个做法需要我们设计一个数据结构保存嵌套数组的每个元素，我们选择了队列。

重点是利用递归把整个嵌套的列表迭代器给压平。注意，题目已经给了我们它的数据结构，而不是普通的list。所以我们必须用他的函数。题目中虽然是多重嵌套，但是归根到底，对于每层的嵌套都是一个一维数组而已。因此，不要想复杂，直接循环该一维数组，如果是整数，添加到队列中，如果是嵌套的列表则继续解嵌套。

最后的结果是有按照从左到右有序的，这个可以放心。

Python代码如下：

```python
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.queue = collections.deque()
        def getAll(nests):
            for nest in nests:
                if nest.isInteger():
                    self.queue.append(nest.getInteger())
                else:
                    getAll(nest.getList())
        getAll(nestedList)

    def next(self):
        """
        :rtype: int
        """
        return self.queue.popleft()

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.queue)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
```

### 栈
上面说了事先保存所有对象的方法是个作弊的方法，为了不事先保存所有的对象，而是每次在调用`hasNext()`或者`next()`时迭代器向后移动，我们可以使用栈。用到栈的想法出发点是递归本身是用栈实现的。

栈存储的是NestedInteger类型，这样把vector中的元素倒序放进来，在`hasNext()`的判断过程中，如果看到当前的元素是Integer数据那么直接弹出；如果看到的是`List`类型，那么应该对其进行for循环，把里面的Integer再倒序放进来。

C++代码如下：

```cpp
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {
 *   public:
 *     // Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     bool isInteger() const;
 *
 *     // Return the single integer that this NestedInteger holds, if it holds a single integer
 *     // The result is undefined if this NestedInteger holds a nested list
 *     int getInteger() const;
 *
 *     // Return the nested list that this NestedInteger holds, if it holds a nested list
 *     // The result is undefined if this NestedInteger holds a single integer
 *     const vector<NestedInteger> &getList() const;
 * };
 */
class NestedIterator {
public:
    NestedIterator(vector<NestedInteger> &nestedList) {
        for (int i = nestedList.size() - 1; i >= 0; --i) {
            st.push(nestedList[i]);
        }
    }

    int next() {
        NestedInteger cur = st.top(); st.pop();
        return cur.getInteger();
    }

    bool hasNext() {
        while (!st.empty()) {
            NestedInteger cur = st.top();
            if (cur.isInteger()) {
                return true;
            }
            st.pop();
            for (int i = cur.getList().size() - 1; i >= 0; --i) {
                st.push(cur.getList()[i]);
            }
        }
        return false;
    }
private:
    stack<NestedInteger> st;
};

/**
 * Your NestedIterator object will be instantiated and called as such:
 * NestedIterator i(nestedList);
 * while (i.hasNext()) cout << i.next();
 */
```

## 日期

2018 年 3 月 12 日 
2019 年 10 月 2 日 —— 欢度国庆
