- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/confusing-number/

## 题目描述

Given a number `N`, return true if and only if it is a confusing number, which satisfies the following condition:

We can rotate digits by 180 degrees to form new digits. When `0, 1, 6, 8, 9` are rotated 180 degrees, they become `0, 1, 9, 8, 6` respectively. When `2, 3, 4, 5 and 7` are rotated 180 degrees, they become invalid. A confusing number is a number that when rotated 180 degrees becomes a different number with each digit valid.

Example 1:

    Input: 6
    Output: true
    Explanation: 
    We get 9 after rotating 6, 9 is a valid number and 9!=6.

Example 2:

    Input: 89
    Output: true
    Explanation: 
    We get 68 after rotating 89, 86 is a valid number and 86!=89.

Example 3:
    
    Input: 11
    Output: false
    Explanation: 
    We get 11 after rotating 11, 11 is a valid number but the value remains the same, thus 11 is not a confusing number.

Example 4:

    Input: 25
    Output: false
    Explanation: 
    We get an invalid number after rotating 25.

Note:

1. `0 <= N <= 10^9`
1. After the rotation we can ignore leading zeros, for example if after rotation we have 0008 then this number is considered as just 8.


## 题目大意

给定一个数字 N，当它满足以下条件的时候返回 true：
原数字旋转 180° 以后可以得到新的数字。
如 0, 1, 6, 8, 9 旋转 180° 以后，得到了新的数字 0, 1, 9, 8, 6 。
2, 3, 4, 5, 7 旋转 180° 后，得到的不是数字。
易混淆数 (confusing number) 在旋转180°以后，可以得到和原来不同的数，且新数字的每一位都是有效的。

## 解题方法

### 字典

使用字典保存每个可以翻转的字符翻转后会变成谁，然后对每一位数字进行翻转，看翻转后的数字和原来的数字是否相等。

C++代码如下：

```cpp
class Solution {
public:
    bool confusingNumber(int N) {
        unordered_map<int, int> m{{0, 0}, {1, 1}, {6, 9}, {8, 8}, {9, 6}};
        int rotate = 0;
        int temp = N;
        while (temp != 0) {
            int mod = temp % 10;
            if (!m.count(mod))
                return false;
            rotate = 10 * rotate + m[mod];
            temp /= 10;
        }
        return rotate != N;
    }
};
```

## 日期

2019 年 9 月 18 日 —— 今日又是九一八


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/100977773
