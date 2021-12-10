
- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/two-sum-iii-data-structure-design/

## 题目描述

Design and implement a `TwoSum` class. It should support the following operations: `add` and `find`.

- `add` - Add the number to an internal data structure.
- `find` - Find if there exists any pair of numbers which sum is equal to the value.

Example 1:

    add(1); add(3); add(5);
    find(4) -> true
    find(7) -> false

Example 2:

    add(3); add(1); add(2);
    find(3) -> true
    find(6) -> false

## 题目大意

设计并实现一个 TwoSum 的类，使该类需要支持 add 和 find 的操作。

## 解题方法

### 数组+字典

使用字典保存每个数字出现的位置，并且另外使用一个数组按照顺序保存出现的数字。查找的时候从左向右遍历数组中的每个数字left，查找value - left是否在字典中，并且和left位置不同。

C++代码如下：

```cpp
class TwoSum {
public:
    /** Initialize your data structure here. */
    TwoSum() {
    }
    
    /** Add the number to an internal data structure.. */
    void add(int number) {
        nums.push_back(number);
        m[number] = nums.size() - 1;
    }
    
    /** Find if there exists any pair of numbers which sum is equal to the value. */
    bool find(int value) {
        for (int i = 0; i < nums.size(); ++i) {
            int left = nums[i];
            int right = value - left;
            if (m.count(right) && m[right] != i)
                return true;
        }
        return false;
    }
private:
    map<int, int> m;
    vector<int> nums;
};

/**
 * Your TwoSum object will be instantiated and called as such:
 * TwoSum* obj = new TwoSum();
 * obj->add(number);
 * bool param_2 = obj->find(value);
 */
```

### 平衡查找树+双指针

这个题和[1. Two Sum][1]是类似的，我使用的双指针的方法，那么要求已经插入的数据是有序的，所以使用了平衡查找树（红黑树，在C++中是map），保存每个数字出现的次数。

每次find的时候，从左右两个位置向中间走，如果左右指针的和是target说明找到了；如果和比target大，右指针向左移动；如果和比target小，左指针向右移动。

由于可能会存在重复的数字，所以map中是保存的数字出现的次数。查找到target的条件是：左右指针不相等且和等于target 或者 左右指针相等且和等于target且该数字出现的次数不止1次。


C++代码如下：

```cpp
class TwoSum {
public:
    /** Initialize your data structure here. */
    TwoSum() {
    }
    
    /** Add the number to an internal data structure.. */
    void add(int number) {
        m[number] ++;
    }
    
    /** Find if there exists any pair of numbers which sum is equal to the value. */
    bool find(int value) {
        if (m.empty()) return false;
        auto left = m.begin();
        auto right = m.end();
        right --;
        while (left != right) {
            int cur_sum = left->first + right->first;
            if (cur_sum == value 
                && (left != right || left->second > 1))
                return true;
            else if (cur_sum > value)
                right --;
            else
                left ++;
        }
        return left->first + right->first == value && (left != right || left->second > 1);
    }
private:
    map<int, int> m;
};

/**
 * Your TwoSum object will be instantiated and called as such:
 * TwoSum* obj = new TwoSum();
 * obj->add(number);
 * bool param_2 = obj->find(value);
 */
```


## 日期

2019 年 9 月 19 日 —— 举杯邀明月，对影成三人


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/72465759
