Here's a comprehensive list of coding problems related to prefix sum that are appropriate for an easy to medium level of difficulty:

1. [Subarray Sum Equals K - LeetCode](https://leetcode.com/problems/subarray-sum-equals-k/): Given an array of integers `nums` and an integer `k`, return the total number of subarrays whose sum equals to `k`. A subarray is a contiguous non-empty sequence of elements within an array.

   Approach:
   Use a hash map to store the prefix sums of the subarrays. For each subarray ending at the current index, check if its prefix sum minus the target value `k` exists in the hash map. If it does, increment the count of subarrays with a sum of `k` by one.

2. [Prefix Sum - LeetCode Discuss](https://leetcode.com/discuss/study-guide/4023666/prefix-sum-questions-to-practice): This LeetCode discussion post provides a list of prefix sum problems to practice, including:

   - [Maximum Sum of 3 Non-Overlapping Subarrays - LeetCode](https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/)
   - [Minimum Size Subarray Sum - LeetCode](https://leetcode.com/problems/minimum-size-subarray-sum/)

   Tips:
   - Practice different types of prefix sum problems, including 1D and 2D prefix sums.
   - Be aware of common variations of prefix sum problems, such as range sum queries and finding subarrays with a specific sum.
   - Make sure to optimize your prefix sum implementation for specific problems, as the pre-computation of prefix sums can be time-consuming for large arrays.
   - Don't forget to consider edge cases when implementing prefix sum solutions, such as empty arrays or arrays with negative values.

3. [Prefix Sum | LeetCode The Hard Way](http://leetcodethehardway.com/tutorials/basic-topics/prefix-sum): This tutorial explains the prefix sum technique and provides examples of how to implement it. It covers:

   - One-dimensional prefix sums
   - Two-dimensional prefix sums
   - Range sum queries

   Tips:
   - Practice the prefix sum technique on a variety of problems to build your intuition.
   - Make sure to understand the problem statement and consider if prefix sum can help simplify the problem.
   - When solving problems with prefix sum, try to optimize the pre-computation of prefix sums.

4. [Prefix Sum Problems - LeetCode Discuss](https://leetcode.com/discuss/general-discussion/563022/prefix-sum-problems): This LeetCode discussion post provides a list of prefix sum problems to practice, including:

   - [Count of Smaller Numbers After Self - LeetCode](https://leetcode.com/problems/count-of-smaller-numbers-after-self/)
   - [Longest Subarray of 1's After Deleting One Element - LeetCode](https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/)

   Tips:
   - Practice different types of prefix sum problems, including 1D and 2D prefix sums.
   - Be aware of common variations of prefix sum problems, such as range sum queries and finding subarrays with a specific sum.
   - Make sure to optimize your prefix sum implementation for specific problems, as the pre-computation of prefix sums can be time-consuming for large arrays.
   - Don't forget to consider edge cases when implementing prefix sum solutions, such as empty arrays or arrays with negative values.

5. [Prefix Sum + HashMap is quite tricky to implement, it's definitely harder than recursion + memo - Reddit](https://www.reddit.com/r/leetcode/comments/1dmz00j/prefix_sum_hashmap_is_quite_tricky_to_implement/): This Reddit thread discusses the challenges of implementing prefix sum with a hash map. It covers:

   - How to use a hash map to store prefix sums
   - How to handle edge cases with negative numbers
   - How to optimize the hash map implementation

   Tips:
   - Make sure to understand how prefix sum with a hash map works.
   - Practice implementing prefix sum with a hash map on a variety of problems.
   - Optimize the hash map implementation for specific problems.

6. [Prefix Sum | Summary with practice questions Sheet (1D, 2D) on LeetCode - Medium](https://mohitaunni.medium.com/all-about-prefix-sum-technique-90764fa91007): This Medium article summarizes the prefix sum technique and provides practice questions for both 1D and 2D prefix sums. It covers:

   - How to compute prefix sums
   - How to use prefix sums to solve range queries
   - How to optimize the prefix sum implementation for specific problems

   Tips:
   - Practice the prefix sum technique on a variety of problems.
   - Make sure to understand the problem statement and consider if prefix sum can help simplify the problem.
   - Optimize the prefix sum implementation for specific problems.

7. [Special Array II - LeetCode](https://leetcode.com/problems/special-array-ii/): Given an integer array `nums`, return the smallest `k` such that the number of elements strictly less than `k` in the array is equal to `k`.

   Approach:
   Use a hash map to store the number of elements in the array that are less than or equal to each prefix sum. For each prefix sum, check if the number of elements less than or equal to it is equal to the number of elements that are strictly less than it. If it is, return the prefix sum.

8. [Mediums are so much harder than Easies - Reddit](https://www.reddit.com/r/leetcode/comments/18368y5/mediums_are_so_much_harder_than_easies/): This Reddit thread discusses the challenges of solving medium-level LeetCode problems. It provides tips on how to improve problem-solving skills, including:

   - Practice, practice, practice
   - Understand the problem statement and consider all edge cases
   - Break down the problem into smaller sub-problems

   Tips:
   - Practice prefix sum problems at a variety of levels to build your skills.
   - Pay attention to the problem statement and consider all edge cases.
   - Break down the problem into smaller sub-problems and solve each one individually.

8. [More on Prefix Sums - USACO Guide](https://usaco.guide/silver/more-prefix-sums): This USACO guide provides an overview of prefix sums and how to use them to solve competitive programming problems. It covers:

   - One-dimensional prefix sums
   - Two-dimensional prefix sums
   - Range sum queries
   - Counting subarrays with a specific sum

   Tips:
   - Practice prefix sum problems at a variety of levels.
   - Understand the different types of prefix sums and when to use them.
   - Optimize the prefix sum implementation for specific problems.

9. [Prefix Sums Problem - AtCoder ABC 89 D: Practical Skill Test - Reddit](https://www.reddit.com/r/algorithms/comments/lzxvbz/prefix_sums_problem_atcoder_abc_89_d_practical/): This Reddit thread discusses a prefix sum problem from the AtCoder ABC 89 D contest. It covers:

   - How to use prefix sums to solve the problem
   - How to handle edge cases
   - How to optimize the prefix sum implementation

   Tips:
   - Understand the problem statement and consider all edge cases.
   - Use prefix sums to solve the problem.
   - Optimize the prefix sum implementation for specific problems.

10. [B - Inverse Prefix Sum - AtCoder](https://atcoder.jp/contests/abc280/tasks/abc280_b): Given an array `A` of integers, find the minimum number of swaps required to make the inverse prefix sum of the array non-decreasing. The inverse prefix sum of an array `A` is the array `B` where `B[i]` is the sum of the elements in `A` from index `i` to the end of the array.

   Approach:
   Use a hash map to store the number of elements in the array that have a specific inverse prefix sum. For each inverse prefix sum, check if the number of elements with a smaller inverse prefix sum is non-increasing. If it is, continue to the next inverse prefix sum. Otherwise, find the maximum number of elements that can be swapped to make the inverse prefix sum non-increasing and update the hash map accordingly.

11. [IPVCE Practice Prefix Sums [easy - medium] - Virtual Judge](https://vjudge.net/contest/595816): This Virtual Judge contest provides a variety of prefix sum problems to practice, including:

    - [Prefix Sum - Codeforces](https://codeforces.com/blog/entry/59915)
    - [Prefix Sum - Codeforces](<https://codeforces.com/blog/entry/105782>)
    - [Where should I practice prefix sum problems - Codeforces](<https://codeforces.com/blog/entry/94598>)
    - [Prefix sum (aka cumulative sum) related problems - Codeforces](<https://codeforces.com/blog/entry/90592>)
    - [Problem - 1303G - Codeforces](<https://codeforces.com/problemset/problem/1303/G>)
    - [Problem - 1738B - Codeforces](<https://codeforces.com/problemset/problem/1738/B>)
    - [Prefix Sum Addicts | Codeforces Global round 22 - YouTube](<https://www.youtube.com/watch?v=bHPUXqI-EI4>)
    - [Problem - 1779C - Codeforces](<https://codeforces.com/problemset/problem/1779/C>)

   Tips:
   - Practice prefix sum problems at a variety of levels.
   - Understand the problem statement and consider all edge cases.
   - Break down the problem into smaller sub-problems and solve each one individually.

Remember, practice is key when it comes to improving your problem-solving skills. By practicing prefix sum problems at a variety of levels and understanding the different types of prefix sums, you can become more proficient in solving these types of problems. Good luck!