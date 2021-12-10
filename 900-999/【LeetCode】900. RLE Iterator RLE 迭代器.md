作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址：https://leetcode.com/problems/rle-iterator/description/

## 题目描述：

Write an iterator that iterates through a run-length encoded sequence.

The iterator is initialized by ``RLEIterator(int[] A)``, where A is a run-length encoding of some sequence.  More specifically, for all even i, A[i] tells us the number of times that the non-negative integer value A[i+1] is repeated in the sequence.

The iterator supports one function: ``next(int n)``, which exhausts the next n elements (n >= 1) and returns the last element exhausted in this way.  If there is no element left to exhaust, next returns -1 instead.

For example, we start with A = [3,8,0,9,2,5], which is a run-length encoding of the sequence [8,8,8,5,5].  This is because the sequence can be read as "three eights, zero nines, two fives".

 

Example 1:

    Input: ["RLEIterator","next","next","next","next"], [[[3,8,0,9,2,5]],[2],[1],[1],[2]]
    Output: [null,8,8,5,-1]
    
    Explanation: 
    
    RLEIterator is initialized with RLEIterator([3,8,0,9,2,5]).
    This maps to the sequence [8,8,8,5,5].
    RLEIterator.next is then called 4 times:
    
    .next(2) exhausts 2 terms of the sequence, returning 8.  The remaining sequence is now [8, 5, 5].
    
    .next(1) exhausts 1 term of the sequence, returning 8.  The remaining sequence is now [5, 5].
    
    .next(1) exhausts 1 term of the sequence, returning 5.  The remaining sequence is now [5].
    
    .next(2) exhausts 2 terms, returning -1.  This is because the first term exhausted was 5,
    but the second term did not exist.  Since the last term exhausted does not exist, we return -1.

Note:

1. 0 <= A.length <= 1000
A.length is an even integer.
0 <= A[i] <= 10^9
There are at most 1000 calls to RLEIterator.next(int n) per test case.
Each call to RLEIterator.next(int n) will have 1 <= n <= 10^9.


## 题目大意

给出了一个数组，这个数组第偶数个位置表示的是其后面的那个数字出现的次数。让我们设计一个函数，能找出后面的第n个数字，如果后面没有数字就返回-1.这个运算的过程中要把偶数位置出现的次数给统计进去。

## 解题方法

这个设计确实类似于python的next()函数，估计next()是这个题的原型吧。

看了下A的规模是1000，那么对时间复杂度的要求并没有那么严格。其实这个题可以直接使用O(N)的时间复杂度求解。

使用index指向我们现在统计到的数组A的位置，这个位置只指向偶数位置。然后每次next()调用同时维护数组A和index。直接遍历就好，如果A[index]的个数>n，就往后去找，直至找到对应的位置，这个时候的位置就代表我们的找到了要弹出的数字。遍历的过程中一定要更新n，也要更新每个位置出现次数。这样就相当于n把原来位置的数字给消耗掉了。

平均时间复杂度是O(n)，空间复杂度是O(1)。

代码如下：

```python
class RLEIterator(object):

    def __init__(self, A):
        """
        :type A: List[int]
        """
        self.A = A
        self.index = 0

    def next(self, n):
        """
        :type n: int
        :rtype: int
        """
        while self.index < len(self.A) and self.A[self.index] < n:
            n -= self.A[self.index]
            self.index += 2
        if self.index >= len(self.A):
            return -1
        self.A[self.index] -= n
        return self.A[self.index + 1]


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)
```

二刷的时候使用C++，思路和上面大致相同。如果当前位置的数字大于等于剩余的n，那么把当前数字-n；如果当前位置的数字小于n，那么必须向后寻找了，需要更新n并且向后走，每次走两步。

如果上面的循环结束的时候，pos已经走到了数组外边，直接返回-1，否则返回pos位置对应的下一个位置。

C++代码如下：

```cpp
class RLEIterator {
public:
    RLEIterator(vector<int> A) : A_(A), pos(0){
    }
    
    int next(int n) {
        while (pos < A_.size() && n > 0) {
            if (A_[pos] >= n) {
                A_[pos] -= n;
                n = 0;
            } else {
                n -= A_[pos];
                A_[pos] = 0;
                pos += 2;
            }
        }
        if (pos >= A_.size() - 1) return -1;
        return A_[pos + 1];
    }
private:
    vector<int> A_;
    int pos;
};

/**
 * Your RLEIterator object will be instantiated and called as such:
 * RLEIterator obj = new RLEIterator(A);
 * int param_1 = obj.next(n);
 */
```

参考资料：

https://leetcode.com/problems/rle-iterator/discuss/168294/Java-Straightforward-Solution-O(n)-time-O(1)-space

## 日期

2018 年 9 月 18 日 —— 铭记这一天
2019 年 2 月 26 日 —— 二月就要完了
