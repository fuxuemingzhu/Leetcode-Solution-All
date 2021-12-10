- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/design-browser-history/


# 题目描述

你有一个只支持单个标签页的 浏览器 ，最开始你浏览的网页是 `homepage` ，你可以访问其他的网站 `url` ，也可以在浏览历史中后退 `steps` 步或前进 `steps` 步。

请你实现 `BrowserHistory` 类：

- `BrowserHistory(string homepage)` ，用 homepage 初始化浏览器类。
- `void visit(string url)` 从当前页跳转访问 `url` 对应的页面。执行此操作会把浏览历史前进的记录全部删除。
- `string back(int steps)` 在浏览历史中后退 `steps` 步。如果你只能在浏览历史中后退至多 `x` 步且 `steps > x` ，那么你只后退 `x` 步。请返回后退 至多 `steps` 步以后的 `url` 。
- `string forward(int steps)` 在浏览历史中前进 `steps` 步。如果你只能在浏览历史中前进至多 `x` 步且 `steps > x` ，那么你只前进 `x` 步。请返回前进 至多 `steps` 步以后的 `url` 。
 

示例：

    输入：
    ["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]
    [["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]
    输出：
    [null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"]
    
    解释：
    BrowserHistory browserHistory = new BrowserHistory("leetcode.com");
    browserHistory.visit("google.com");       // 你原本在浏览 "leetcode.com" 。访问 "google.com"
    browserHistory.visit("facebook.com");     // 你原本在浏览 "google.com" 。访问 "facebook.com"
    browserHistory.visit("youtube.com");      // 你原本在浏览 "facebook.com" 。访问 "youtube.com"
    browserHistory.back(1);                   // 你原本在浏览 "youtube.com" ，后退到 "facebook.com" 并返回 "facebook.com"
    browserHistory.back(1);                   // 你原本在浏览 "facebook.com" ，后退到 "google.com" 并返回 "google.com"
    browserHistory.forward(1);                // 你原本在浏览 "google.com" ，前进到 "facebook.com" 并返回 "facebook.com"
    browserHistory.visit("linkedin.com");     // 你原本在浏览 "facebook.com" 。 访问 "linkedin.com"
    browserHistory.forward(2);                // 你原本在浏览 "linkedin.com" ，你无法前进任何步数。
    browserHistory.back(2);                   // 你原本在浏览 "linkedin.com" ，后退两步依次先到 "facebook.com" ，然后到 "google.com" ，并返回 "google.com"
    browserHistory.back(7);                   // 你原本在浏览 "google.com"， 你只能后退一步到 "leetcode.com" ，并返回 "leetcode.com"
 

提示：

1. `1 <= homepage.length <= 20`
1. `1 <= url.length <= 20`
1. `1 <= steps <= 100`
1. `homepage` 和 `url` 都只包含 `'.'` 或者小写英文字母。
1. 最多调用 5000 次 `visit`， `back` 和 `forward` 函数。

# 题目大意

本题是模拟浏览器的前进和后退操作。
`forward()`和`back()`函数分别代表前进和后退。
`visit()`函数会访问一个新界面，同时会把之前回退的页面都清空。


# 解题方法

## 模拟法

需要有个数据结构能够很快的前进和后退 `n` 步，第一感觉是**栈**，但是一般认为栈中的数据弹出之后就不存在了，因此后退了之后就不能前进。故最终使用数组来模拟。

使用一个数组`his`保存所有的访问记录，使用`cur`保存当前处于数组中的哪个位置。

1. `__init__(str)`函数：初始化时把`homepage`放入数组中。
2. `forward(steps)`函数：会让`cur`前进`steps`步，但是注意不能超出数组的右边界。
3. `back(steps)`函数：会让`cur`后退`steps`步，但是注意不能少于数组的左边界。
4. `visit(url)`函数：会先把`cur`位置以后的所有历史记录清空，然后把`url`放到`his`数组的后面。


Python 代码如下：

```python
class BrowserHistory:

    def __init__(self, homepage: str):
        self.his = [homepage]
        self.cur = 0


    def visit(self, url: str) -> None:
        while self.his and len(self.his) - 1 > self.cur:
            self.his.pop()
        self.his.append(url)
        self.cur += 1


    def back(self, steps: int) -> str:
        self.cur -= min(self.cur, steps)
        return self.his[self.cur]
        

    def forward(self, steps: int) -> str:
        self.cur += steps
        self.cur = min(self.cur, len(self.his) - 1)
        return self.his[self.cur]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
```

**欢迎关注[负雪明烛的刷题博客](https://blog.csdn.net/fuxuemingzhu)，leetcode刷题800多，每道都讲解了详细写法！**


# 日期

2020 年 6 月 28 日 —— 端午节快乐


  [1]: https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/05/30/leetcode_max_area_2.png
  [2]: https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/05/30/leetcode_max_area_3.png
