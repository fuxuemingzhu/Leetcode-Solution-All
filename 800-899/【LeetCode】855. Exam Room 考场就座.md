作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址: https://leetcode.com/problems/exam-room/description/

## 题目描述：

In an exam room, there are ``N`` seats in a single row, numbered ``0, 1, 2, ..., N-1``.

When a student enters the room, they must sit in the seat that maximizes the distance to the closest person.  If there are multiple such seats, they sit in the seat with the lowest number.  (Also, if no one is in the room, then the student sits at seat number 0.)

Return a class ``ExamRoom(int N)`` that exposes two functions: ``ExamRoom.seat()`` returning an int representing what seat the student sat in, and ``ExamRoom.leave(int p)`` representing that the student in seat number ``p`` now leaves the room.  It is guaranteed that any calls to ``ExamRoom.leave(p)`` have a student sitting in seat ``p``.

 

Example 1:

    Input: ["ExamRoom","seat","seat","seat","seat","leave","seat"], [[10],[],[],[],[],[4],[]]
    Output: [null,0,9,4,2,null,5]
    Explanation:
    ExamRoom(10) -> null
    seat() -> 0, no one is in the room, then the student sits at seat number 0.
    seat() -> 9, the student sits at the last seat number 9.
    seat() -> 4, the student sits at the last seat number 4.
    seat() -> 2, the student sits at the last seat number 2.
    leave(4) -> null
    seat() -> 5, the student sits at the last seat number 5.

Note:

1. 1 <= N <= 10^9
1. ExamRoom.seat() and ExamRoom.leave() will be called at most 10^4 times across all test cases.
1. Calls to ExamRoom.leave(p) are guaranteed to have a student currently sitting in seat number p.

## 题目大意

有一个考场里面有N个座位排成一条线，现在每次有个学生进来需要给他安排座位，要求是他的座位和左右两个人的间隔最远。如果有多个满足要求的座位，需要安排在满足要求且序号最小的位置上。第一个进来的人会坐在第一个位置上。

## 解题方法

看了寒神的做法，直接对这个过程进行模拟。使用一个数组保存现在已经做了的位置的坐标。如果数组是空，那么就坐在0位置上，否则的话需要遍历查找离两边最端的位置在哪。毫无疑问，如果坐在两个位置之间的话，一定需要是坐在正中间才行。但是还需要注意最后一个位置模拟，因为右边没有人做了，坐在最右端的话，和最后一个人的距离是直接相减。找出了位置然后用二分查找进行插入。

这个走人的办法是直接查找出p的位置，然后移走就好。

时间复杂度是O(N)，空间复杂度是O(N)。

```python
class ExamRoom(object):

    def __init__(self, N):
        """
        :type N: int
        """
        self.N, self.L = N, list()

    def seat(self):
        """
        :rtype: int
        """
        N, L = self.N, self.L
        if not self.L: res = 0
        else:
            d, res = L[0], 0
            # d means cur distance, res means cur pos
            for a, b in zip(L, L[1:]):
                if (b - a) / 2 > d:
                    d = (b - a) / 2
                    res = (b + a) / 2
            if N - 1 - L[-1] > d:
                res = N - 1
        bisect.insort(L, res)
        return res
        

    def leave(self, p):
        """
        :type p: int
        :rtype: void
        """
        self.L.remove(p)


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)
```



参考资料：

https://leetcode.com/problems/exam-room/discuss/139862/C++JavaPython-Straight-Forward

## 日期

2018 年 10 月 18 日 —— 做梦都在科研


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/83115850
