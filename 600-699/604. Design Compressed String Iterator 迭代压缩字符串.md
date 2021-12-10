- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/design-compressed-string-iterator/

## 题目描述

Design and implement a data structure for a compressed string iterator. It should support the following operations: `next` and `hasNext`.

The given compressed string will be in the form of each letter followed by a positive integer representing the number of this letter existing in the original uncompressed string.

- `next()` - if the original string still has uncompressed characters, return the next letter; Otherwise return a white space.
- `hasNext()` - Judge whether there is any letter needs to be uncompressed.

Note:

- Please remember to RESET your class variables declared in StringIterator, as static/class variables are persisted across multiple test cases. Please see here for more details.

Example:

    StringIterator iterator = new StringIterator("L1e2t1C1o1d1e1");
    
    iterator.next(); // return 'L'
    iterator.next(); // return 'e'
    iterator.next(); // return 'e'
    iterator.next(); // return 't'
    iterator.next(); // return 'C'
    iterator.next(); // return 'o'
    iterator.next(); // return 'd'
    iterator.hasNext(); // return true
    iterator.next(); // return 'e'
    iterator.hasNext(); // return false
    iterator.next(); // return ' '


## 题目大意

对于一个压缩字符串，设计一个数据结构，它支持如下两种操作： next 和 hasNext。
给定的压缩字符串格式为：每个字母后面紧跟一个正整数，这个整数表示该字母在解压后的字符串里连续出现的次数。
- next() - 如果压缩字符串仍然有字母未被解压，则返回下一个字母，否则返回一个空格。
- hasNext() - 判断是否还有字母仍然没被解压。


## 解题方法

### 维护当前字符和次数

这个题是很常见的题目，使用变量分别保存当前的字符以及其出现的次数，如果所有的字符都用完则没有下一个字符了。

注意两点：
1. 字符出现的次数可能>=10
2. 最后一个字符用完时才算结束

C++代码如下：

```cpp
class StringIterator {
public:
    StringIterator(string compressedString) {
        str = compressedString;
        index = 0;
        cur = ' ';
        count = 0;
    }
    
    char next() {
        if (!hasNext()) {
            return ' ';
        }
        if (count != 0) {
            count --;
            return cur;
        }
        cur = str[index];
        index ++;
        while (str[index] >= '0' && str[index] <= '9') {
            count = 10 * count + str[index] - '0';
            index ++;
        }
        count --;
        return cur;
    }
    
    bool hasNext() {
        return index < str.size() || count != 0;
    }
private:
    string str;
    int index;
    char cur;
    int count;
};

/**
 * Your StringIterator object will be instantiated and called as such:
 * StringIterator* obj = new StringIterator(compressedString);
 * char param_1 = obj->next();
 * bool param_2 = obj->hasNext();
 */
```

## 日期

2019 年 9 月 19 日 —— 举杯邀明月，对影成三人


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/100977773
