作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/sort-an-array/

## 题目描述

Given an array of integers nums, sort the array in ascending order.

 

Example 1:

    Input: [5,2,3,1]
    Output: [1,2,3,5]

Example 2:

    Input: [5,1,1,2,0,0]
    Output: [0,0,1,1,2,5]
 

Note:

1. `1 <= A.length <= 10000`
1. `-50000 <= A[i] <= 50000`

## 题目大意

对一个数组进行排序。

## 解题方法

### 库函数排序

最简单的方法使用C++内置的sort函数排序，本质是优化了的快排。

时间复杂度是O(N*log(N))，空间复杂度是O(1).

```cpp
class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        return nums;
    }
};
```

### 桶排序

桶排序就是遍历所有元素，把元素的个数累加到对应的桶上，最后进行一次遍历把统计的数字放到结果中即可。

时间复杂度是O(N)，空间复杂度是O(1)（元素的大小上下限已经固定）.

C++代码如下：

```cpp
class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        vector<int> count(100010, 0);
        for (int num : nums) {
            count[num + 50000]++;
        }
        vector<int> res;
        for (int i = 0; i < count.size(); i ++) {
            while (count[i]-- != 0) {
                res.push_back(i - 50000);
            }
        }
        return res;
    }
};
```

### 红黑树排序

C++的map使用了红黑树结构，也可以达到统计各个元素出现的次数，而且遍历是按照Key有序的。

时间复杂度是O(N*log(N))，空间复杂度是O(N).

```cpp
class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        map<int, int> m;
        for (int num : nums) {
            m[num]++;
        }
        vector<int> res;
        auto it = m.begin();
        while(it != m.end()) {
            res.insert(res.end(), it->second, it->first);
            it ++;
        }
        return res;
    }
};
```

### 归并排序

merge sort是把数组的左右两半部分都排序，然后做一个merge two sorted array的操作。

我写的代码定义区间都是[start, end)，即左开右闭，需要注意一下定义。下同。

时间复杂度是O(N*log(N))，空间复杂度是O(N).

```cpp
class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        return mergeSort(nums, 0, nums.size());
    }
    // sort nums[start, end)
    vector<int> mergeSort(vector<int>& nums, int start, int end) {
        if (start + 1 == end) return vector<int>(1, nums[start]);
        int L = end - start;
        vector<int> A = mergeSort(nums, start, start + L / 2);
        vector<int> B = mergeSort(nums, start + L / 2, end);
        return merge(A, B);
    }
    // merge two sorted array
    vector<int> merge(vector<int>& A, vector<int>& B) {
        int M = A.size(), N = B.size();
        if (M == 0) return B;
        if (N == 0) return A;
        vector<int> res;
        auto ita = A.begin();
        auto itb = B.begin();
        while (ita != A.end() && itb != B.end()) {
            if (*ita < *itb) {
                res.push_back(*ita);
                ++ita;
            } else {
                res.push_back(*itb);
                ++itb;
            }
        }
        if (ita != A.end())
            res.insert(res.end(), ita, A.end());
        if (itb != B.end())
            res.insert(res.end(), itb, B.end());
        return res;
    }
};
```

### 快速排序

快速排序的思想是，找出pivot的位置，使得其左边的元素都比pivot小，右边的元素都比pivot大。然后再对左右两部分进行排序。

最坏时间复杂度是O(N^2)，平均时间复杂度是O(N*log(N))，空间复杂度是O(1).

```cpp
class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        quickSort(nums, 0, nums.size());
        return nums;
    }
    // sort nums[start, end)
    void quickSort(vector<int>& nums, int start, int end) {
        if (end - start <= 1) return;
        // nums[j] in right position
        int j = partition(nums, start, end);
        // sort nums[start, j) 
        quickSort(nums, start, j);
        // sort nums[j + 1, end)
        quickSort(nums, j + 1, end);
    }
    // nums[start, end) partition by nums[start]
    int partition(vector<int>& nums, int start, int end) {
        int pivot = nums[start];
        int i = start, j = end;
        while (true) {
            while (++i < end && nums[i] < pivot);
            while (--j > start + 1 && nums[j] > pivot);
            if (i > j) break;
            swap(nums[i], nums[j]);
        }
        swap(nums[start], nums[j]);
        return j;
    }
};
```

## 日期

2019 年 9 月 16 日 —— 秋高气爽
