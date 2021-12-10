
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/open-the-lock/description/

## 题目描述

You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

The lock initially starts at ``'0000'``, a string representing the state of the 4 wheels.

You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.

Example 1:

    Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
    Output: 6
    Explanation:
    A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
    Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
    because the wheels of the lock become stuck after the display becomes the dead end "0102".

Example 2:

    Input: deadends = ["8888"], target = "0009"
    Output: 1
    Explanation:
    We can turn the last wheel in reverse to move from "0000" -> "0009".

Example 3:

    Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
    Output: -1
    Explanation:
    We can't reach the target without getting stuck.

Example 4:

    Input: deadends = ["0000"], target = "8888"
    Output: -1
    Note:
    The length of deadends will be in the range [1, 500].
    target will not be in the list deadends.
    Every string in deadends and the string target will be a string of 4 digits from the 10,000 possibilities '0000' to '9999'.


## 题目大意

有一个密码锁，上面有四个旋钮，每个旋钮上面是0——9各个连续的数字，然后这个旋钮的0和9是连接着的。下面要去求从起始开始的"0000"扭到target，最少需要多少步。注意，其中有些deadends，表示如果扭到这里之后锁就坏掉。

## 解题方法

典型的搜索题目，可以抽象为一个无向图，在这个图中搜索target。因为求最少需要多少步，所以使用的方法是bfs。

方法很暴力了，属于模板。BFS需要一个队列和visited集合，通过step保存寻找了多少步，使用size保存当前有多少步可以搜素。使用j来遍历4个旋钮，使用k= -1, 1来表示能正向搜索和反向搜索。

这个BFS很暴力，也能过，当做模板背下来不错。


代码如下：

```python
class Solution:
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        deadset = set(deadends)
        if (target in deadset) or ("0000" in deadset): return -1
        que = collections.deque()
        que.append("0000")
        visited = set(["0000"])
        step = 0
        while que:
            step += 1
            size = len(que)
            for i in range(size):
                point = que.popleft()
                for j in range(4):
                    for k in range(-1, 2, 2):
                        newPoint = [i for i in point]
                        newPoint[j] = chr((ord(newPoint[j]) - ord('0') + k + 10) % 10 + ord('0'))
                        newPoint = "".join(newPoint)
                        if newPoint == target:
                            return step
                        if (newPoint in deadset) or (newPoint in visited):
                            continue
                        que.append(newPoint)
                        visited.add(newPoint)
        return -1
```

---

二刷，使用的也是BFS，但是没有使用for循环使得代码比较罗素。

```python
class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        que = collections.deque()
        que.append("0000")
        visited = set(deadends)
        step = 0
        while que:
            size = len(que)
            for _ in range(size):
                node = que.popleft()
                if node in visited:
                    continue
                visited.add(node)
                if node == target:
                    return step
                nodelist = map(int, list(node))
                que.append("".join(map(str, [(nodelist[0] + 1 + 10) % 10, nodelist[1], nodelist[2], nodelist[3]])))
                que.append("".join(map(str, [(nodelist[0] - 1 + 10) % 10, nodelist[1], nodelist[2], nodelist[3]])))
                que.append("".join(map(str, [nodelist[0], (nodelist[1] + 1 + 10) % 10, nodelist[2], nodelist[3]])))
                que.append("".join(map(str, [nodelist[0], (nodelist[1] - 1 + 10) % 10, nodelist[2], nodelist[3]])))
                que.append("".join(map(str, [nodelist[0], nodelist[1], (nodelist[2] + 1 + 10) % 10, nodelist[3]])))
                que.append("".join(map(str, [nodelist[0], nodelist[1], (nodelist[2] - 1 + 10) % 10, nodelist[3]])))
                que.append("".join(map(str, [nodelist[0], nodelist[1], nodelist[2], (nodelist[3] + 1 + 10) % 10])))
                que.append("".join(map(str, [nodelist[0], nodelist[1], nodelist[2], (nodelist[3] - 1 + 10) % 10])))
            step += 1
        return -1
```

C++版本的代码如下：

```cpp
class Solution {
public:
    int openLock(vector<string>& deadends, string target) {
        queue<string> que;
        que.push("0000");
        int step = 0;
        set<string> visited;
        for (string& d : deadends) {
            visited.insert(d);
        }
        while (!que.empty()) {
            int size = que.size();
            for (int i = 0; i < size; i++) {
                string node = que.front(); que.pop();
                if (visited.count(node)) continue;
                if (node == target) return step;
                for (int j = 0; j < 4; j++) {
                    for (int k = -1; k < 2; k += 2) {
                        string next = node;
                        next[j] = '0' + (next[j] - '0' + k + 10) % 10;
                        que.push(next);
                    }
                    
                }
                visited.insert(node);
            }
            step++;
        }
        return -1;
    }
};
```

参考资料：

https://www.youtube.com/watch?v=M7GgV6TJTdc

## 日期

2018 年 9 月 14 日 —— 脚踏实地，不要迷茫了
2018 年 11 月 29 日 —— 时不我待
