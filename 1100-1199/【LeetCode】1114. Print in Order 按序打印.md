
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/print-in-order/

## 题目描述

Suppose we have a class:

    public class Foo {
      public void first() { print("first"); }
      public void second() { print("second"); }
      public void third() { print("third"); }
    }

The same instance of Foo will be passed to three different threads. Thread A will call `first()`, thread B will call `second()`, and thread C will call `three()`. Design a mechanism and modify the program to ensure that `second()` is executed after `first()`, and `third()` is executed after `second()`.

Example 1:

    Input: [1,2,3]
    Output: "firstsecondthird"
    Explanation: There are three threads being fired asynchronously. The input [1,2,3] means thread A calls first(), thread B calls second(), and thread C calls third(). "firstsecondthird" is the correct output.

Example 2:

    Input: [1,3,2]
    Output: "firstsecondthird"
    Explanation: The input [1,3,2] means thread A calls first(), thread B calls third(), and thread C calls second(). "firstsecondthird" is the correct output.
 

Note:

We do not know how the threads will be scheduled in the operating system, even though the numbers in the input seems to imply the ordering. The input format you see is mainly to ensure our tests' comprehensiveness.

## 题目大意

现在三个线程，每个线程分别调用三个函数中的一个。无论线程的产生和调用关系怎么样，最终输出的结果要求都是"firstsecondthird"。如何设计是三个函数。


## 解题方法

### mutex锁

这个是Leetcode的新题型，也就是说并发类型，我觉得很实用，工作中能用到。

一般情况下，最简单的协调不同线程之间的调度关系，都可以使用mutex来做，本质是信号量。

std::mutex 的成员函数有四个：

1. `构造函数`，std::mutex不允许拷贝构造，也不允许 move 拷贝，最初产生的 mutex 对象是处于 unlocked 状态的。
1. `lock()`，调用线程将锁住该互斥量。线程调用该函数会发生下面 3 种情况：
- (1). 如果该互斥量当前没有被锁住，则调用线程将该互斥量锁住，直到调用 unlock之前，该线程一直拥有该锁。
- (2). 如果当前互斥量被其他线程锁住，则当前的调用线程被阻塞住。
- (3). 如果当前互斥量被当前调用线程锁住，则会产生死锁(deadlock)。
1. `unlock()`， 解锁，释放对互斥量的所有权。
1. `try_lock()`，尝试锁住互斥量，如果互斥量被其他线程占有，则当前线程也不会被阻塞。线程调用该函数也会出现下面 3 种情况，
- (1). 如果当前互斥量没有被其他线程占有，则该线程锁住互斥量，直到该线程调用 unlock 释放互斥量。
- (2). 如果当前互斥量被其他线程锁住，则当前调用线程返回 false，而并不会被阻塞掉。
- (3). 如果当前互斥量被当前调用线程锁住，则会产生死锁(deadlock)。

也就是说一个锁能控制两个线程的执行顺序。这个题中我们需要保持三个函数是按顺序执行的，则需要两个锁m1和m2。

在开始的时候，两个锁都锁起来。first()可以直接执行，second()等待m1释放之后执行，third()等待m2释放之后执行。first()结束之后释放m1，second()结束之后释放m2.因此三个的顺序都协调一致了。

C++代码如下：

```cpp
class Foo {
private:
    mutex m1, m2;
public:
    Foo() {
        m1.lock();
        m2.lock();
    }

    void first(function<void()> printFirst) {
        // printFirst() outputs "first". Do not change or remove this line.
        printFirst();
        m1.unlock();
    }

    void second(function<void()> printSecond) {
        m1.lock();
        // printSecond() outputs "second". Do not change or remove this line.
        printSecond();
        m1.unlock();
        m2.unlock();
    }

    
    void third(function<void()> printThird) {
        m2.lock();
        // printThird() outputs "third". Do not change or remove this line.
        printThird();
        m2.unlock();
    }
};

void printFirst() {
    cout << "first";
}

void printSecond() {
    cout << "second";
}

void printThird() {
    cout << "third";
}
```

### promise/future

这也是C++11中的新特性，可以把promise和future当做是在不同线程之间传递值的方式。在某个线程中对promise中生产一个数据，可以在另外一个线程中从future中获取这个数据。

- promise和future是绑定在一起的，可以调用promise::get_future()获取与其绑定的future。
- future.wait()方法对当前的线程进行阻塞，等待与其绑定的promise调用set_value()方法。
- future.get()方法对当前的线程进行阻塞，等待与其绑定的promise调用set_value()方法的返回值。

因此实现线程的同步的方法会很方便。C++代码如下：

```cpp
class Foo {
private:
    std::promise<void> p1;
    std::promise<void> p2;
public:
    Foo() {
    }

    void first(function<void()> printFirst) {
        // printFirst() outputs "first". Do not change or remove this line.
        printFirst();
        p1.set_value();
    }

    void second(function<void()> printSecond) {
        p1.get_future().wait();
        // printSecond() outputs "second". Do not change or remove this line.
        printSecond();
        p2.set_value();
    }

    
    void third(function<void()> printThird) {
        p2.get_future().wait();
        // printThird() outputs "third". Do not change or remove this line.
        printThird();
    }
};

void printFirst() {
    cout << "first";
}

void printSecond() {
    cout << "second";
}

void printThird() {
    cout << "third";
}
```
参考资料：
1. https://www.cnblogs.com/haippy/p/3237213.html
2. http://www.cplusplus.com/reference/future/future/
3. 
## 日期

2019 年 7 月 14 日 —— 第一次做并发的题
