

- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/design-phone-directory/

## 题目描述

Design a Phone Directory which supports the following operations:

- `get`: Provide a number which is not assigned to anyone.
- `check`: Check if a number is available or not.
- `release`: Recycle or release a number.

Example:

    // Init a phone directory containing a total of 3 numbers: 0, 1, and 2.
    PhoneDirectory directory = new PhoneDirectory(3);
    
    // It can return any available phone number. Here we assume it returns 0.
    directory.get();
    
    // Assume it returns 1.
    directory.get();
    
    // The number 2 is available, so return true.
    directory.check(2);
    
    // It returns 2, the only number that is left.
    directory.get();
    
    // The number 2 is no longer available, so return false.
    directory.check(2);
    
    // Release number 2 back to the pool.
    directory.release(2);
    
    // Number 2 is available again, return true.
    directory.check(2);


## 题目大意

设计一个电话目录管理系统，让它支持以下功能：

- `get`: 分配给用户一个未被使用的电话号码，获取失败请返回 -1
- `check`: 检查指定的电话号码是否可用
- `release`: 释放掉一个电话号码，使其能够重新被分配

## 解题方法

### 数组

这个题比较简单，可以直接用最简单的做法，使用一个数组保存所有的数字是否被使用过。

- `get`: 每次分配的时候从左向右依次遍历，找到第一个可用的数字并且把状态设置为已用。
- `check`: 检查指定的电话号码是否可用
- `release`:设置电话号码的状态为没有被使用过。

C++代码如下：

```cpp
class PhoneDirectory {
public:
    /** Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory. */
    PhoneDirectory(int maxNumbers) {
        used = vector<bool>(maxNumbers, false);
    }
    
    /** Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available. */
    int get() {
        for (int i = 0; i < used.size(); ++i) {
            if (!used[i]) {
                used[i] = true;
                return i;
            }
        }
        return -1;
    }
    
    /** Check if a number is available or not. */
    bool check(int number) {
        return !used[number];
    }
    
    /** Recycle or release a number. */
    void release(int number) {
        used[number] = false;
    }
private:
    vector<bool> used;
};

/**
 * Your PhoneDirectory object will be instantiated and called as such:
 * PhoneDirectory* obj = new PhoneDirectory(maxNumbers);
 * int param_1 = obj->get();
 * bool param_2 = obj->check(number);
 * obj->release(number);
 */
 ```


## 日期

2019 年 9 月 21 日 —— 莫生气，我若气病谁如意


  [1]: https://assets.leetcode.com/uploads/2018/10/12/bstdlloriginalbst.png
  [2]: https://assets.leetcode.com/uploads/2018/10/12/bstdllreturndll.png
  [3]: https://assets.leetcode.com/uploads/2018/10/12/bstdllreturnbst.png
  [4]: https://blog.csdn.net/fuxuemingzhu/article/details/79294461
