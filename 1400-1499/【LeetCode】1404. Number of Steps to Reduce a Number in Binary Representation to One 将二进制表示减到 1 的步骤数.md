- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/

# 题目描述

给你一个以二进制形式表示的数字 `s` 。请你返回按下述规则将其减少到 1 所需要的步骤数：

- 如果当前数字为偶数，则将其除以 2 。

- 如果当前数字为奇数，则将其加上 1 。

题目保证你总是可以按上述规则将测试用例变为 1 。

示例 1：

    输入：s = "1101"
    输出：6
    解释："1101" 表示十进制数 13 。
    Step 1) 13 是奇数，加 1 得到 14 
    Step 2) 14 是偶数，除 2 得到 7
    Step 3) 7  是奇数，加 1 得到 8
    Step 4) 8  是偶数，除 2 得到 4  
    Step 5) 4  是偶数，除 2 得到 2 
    Step 6) 2  是偶数，除 2 得到 1  

示例 2：

    输入：s = "10"
    输出：1
    解释："10" 表示十进制数 2 。
    Step 1) 2 是偶数，除 2 得到 1 

示例 3：

    输入：s = "1"
    输出：0
 

提示：

1. `1 <= s.length <= 500`
2. `s` 由字符 `'0'` 或 `'1'` 组成。
3. `s[0] == '1'`

# 题目大意

二进制表示的数字，经过多少次变化之后能变成1.


# 解题方法

## 转成十进制模拟

第一想法是先转成十进制数字，然后进行模拟。但是看了字符串的长度范围是500，即这个数字估计有 2 ^ 500 那么大。很显然，不能用普通的数字类型进行保存。

但是，可以使用大数类型去做。比如 Python 默认就支持无限大的数字，那么在 Python 中是可以直接转成 十进制 进行模拟的。

在 Java 中，可以使用 BigInteger 类来做。

Python 代码如下。

```python
class Solution:
    def numSteps(self, s: str) -> int:
        step = 0
        s_int = int(s, 2)
        while s_int != 1:
            if s_int % 2 == 0:
                s_int //= 2
            else:
                s_int += 1
            step += 1
        return step
```

## 修改二进制字符串

既然是个二进制字符串，那么可以从最后一位就知道当前的数字是偶数还是奇数。然后根据规则对这个二进制字符串进行操作就好了。类似于字符串表示的数字进行加法。

稍微有点难度的就是二进制进行加一的操作，需要一个进位 carry 表示是否有进位。carry 默认是 1，表示要对当前的二进制字符串加 1.

C++代码如下：

```cpp
class Solution {
public:
    int numSteps(string s) {
        int step = 0;
        while (s != "1") {
            int len = s.size();
            if (s[len - 1] == '1') {
                addOne(s);
            } else {
                s = s.substr(0, len - 1);
            }
            step ++;
        }
        return step;
    }
    void addOne(string& s) {
        int N = s.size();
        int carry = 1;
        for (int i = N - 1; i >= 0; --i) {
            if (s[i] == '1') {
                if (carry == 1) {
                    s[i] = '0';
                    carry = 1;
                }
            } else {
                if (carry == 1) {
                    s[i] = '1';
                    carry = 0;
                }
            }
        }
        if (carry == 1) {
            s = "1" + s;
        }
    }
};
```

 **欢迎关注[负雪明烛的刷题博客](https://blog.csdn.net/fuxuemingzhu)，leetcode刷题800多，每道都讲解了详细写法！**

# 日期

2020 年 4 月 5 日 —— 好久不打周赛了


  [1]: https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/04/04/sample_4_1728.png
  [2]: https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/04/04/sample_2_1728.png
  [3]: https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/04/04/sample_6_1728.png
