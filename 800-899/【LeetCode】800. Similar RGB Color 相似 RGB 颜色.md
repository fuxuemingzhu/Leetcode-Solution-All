
- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/similar-rgb-color/

## 题目描述

In the following, every capital letter represents some hexadecimal digit from 0 to f.

The red-green-blue color `"#AABBCC"` can be written as "#ABC" in shorthand.  For example, "#15c" is shorthand for the color `"#1155cc"`.

Now, say the similarity between two colors "#ABCDEF" and "#UVWXYZ" is `-(AB - UV)^2 - (CD - WX)^2 - (EF - YZ)^2`.

Given the color "#ABCDEF", return a 7 character color that is most similar to #ABCDEF, and has a shorthand (that is, it can be represented as some "#XYZ"

Example 1:

    Input: color = "#09f166"
    Output: "#11ee66"
    Explanation:  
    The similarity is -(0x09 - 0x11)^2 -(0xf1 - 0xee)^2 - (0x66 - 0x66)^2 = -64 -9 -0 = -73.
    This is the highest among any shorthand color.

Note:

1. color is a string of length 7.
1. color is a valid RGB color: for i > 0, color[i] is a hexadecimal digit from 0 to f
1. Any answer which has the same (highest) similarity as the best answer will be accepted.
All inputs and outputs should use lowercase letters, and the output is 7 characters.


## 题目大意

RGB 颜色用十六进制来表示的话，每个大写字母都代表了某个从 0 到 f 的 16 进制数。
RGB 颜色 "#AABBCC" 可以简写成 "#ABC" 。例如，"#15c" 其实是 "#1155cc" 的简写。
现在，假如我们分别定义两个颜色 "#ABCDEF" 和 "#UVWXYZ"，则他们的相似度可以通过这个表达式 -(AB - UV)^2 - (CD - WX)^2 - (EF - YZ)^2 来计算。
那么给定颜色 "#ABCDEF"，请你返回一个与 #ABCDEF 最相似的 7 个字符代表的颜色，并且它是可以被简写形式表达的。（比如，可以表示成类似 "#XYZ" 的形式）

## 解题方法

### 遍历

这个题的解法写的比较长，首先写了个十六进制和十进制转换函数，然后对R、G、B三个位置进行排列组合，看哪个组合和给出的color最相似。

需要注意的是这个相似函数是负数，因此最相似的时候是相似度最大。

C++代码如下：

```cpp
class Solution {
public:
    string similarRGB(string color) {
        vector<string> hexs = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", 
                               "a", "b", "c", "d", "e", "f"};
        int R = hex2dec(color.substr(1, 2));
        int G = hex2dec(color.substr(3, 2));
        int B = hex2dec(color.substr(5, 2));
        int mostSimilar = INT_MIN;
        string res;
        for (int i = 0; i < hexs.size(); ++i) {
            for (int j = 0; j < hexs.size(); ++j) {
                for (int k = 0; k < hexs.size(); ++k) {
                    string newR = hexs[i] + hexs[i];
                    string newG = hexs[j] + hexs[j];
                    string newB = hexs[k] + hexs[k];
                    int intR = hex2dec(newR);
                    int intG = hex2dec(newG);
                    int intB = hex2dec(newB);
                    int curSimilar = - (R - intR) * (R - intR) - (G - intG) * (G - intG) - (B - intB) * (B - intB);
                    if (curSimilar > mostSimilar) {
                        res = "#" + newR + newG + newB;
                        mostSimilar = curSimilar;
                    }
                }
            }
        }
        return res;
    }
    int hex2dec(string hex) {
        int res = 0;
        for (int i = 0; i < hex.size(); ++i) {
            if (hex[i] >= 'a') {
                res = 16 * res + (hex[i] - 'a' + 10);
            } else {
                res = 16 * res + (hex[i] - '0');
            }
        }
        return res;
    }
};
```

## 日期

2019 年 9 月 18 日 —— 今日又是九一八


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/100977773
