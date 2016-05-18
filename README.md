# Project1
#MinimumRooms


After a long time, Chef has finally decided to renovate his house. Chef's house has N rooms in it numbered from 1 to N. Each room is currently painted in one of the red, blue or green colors. Your are given configuration of colors of his house by a string S consisting of N characters. In this string, color red will be denoted by 'R', green by 'G' and blue by 'B'.
Chef does not like current painting configuration that much and would like to repaint the house such that each room has same color.
For painting, Chef has all the 3 color paints available and mixing any 2 color paints will result into 3rd color paint i.e
R + B = G
B + G = R
G + R = B
For example, painting a room having red color before with green color paint will make the color of room blue.
Also, Chef has many buckets of paint of each color. Simply put, you can assume that he will not run out of paint.
Being extraordinary lazy, our little chef does not want to work much and therefore, he has asked you to find the minimum number of rooms he has to repaint (possibly zero) in order to have all the rooms with same color. Can you please help him?
Input

First line of input contains a single integer T denoting the number of test cases. First line of each test case contains an integer N denoting the number of rooms in the chef's house. Next line of each test case contains a string S denoting the current color configuration of rooms.
Output

For each test case, Print the minimum number of rooms need to be painted in order to have all the rooms painted with same color i.e either red, blue or green.
Constraints

1 ≤ T ≤ 10

1 ≤ N ≤ 105

Si = {'R','G','B'}
Scoring

Subtask 1 (40 points) : 1 ≤ N ≤ 10
Subtask 2 (60 points) : original constraints
Example

Input
3
3
RGR
3
RRR
3
RGB
Output
1
0
2
Explanation:

Test 1: Chef prefers to paint room 2 with blue color such that the resulting color will be red and all the rooms have same color i.e red.
Test 2: Given configuration has all the rooms painted with red color and therefore, chef does not need to do painting work at all.
Test 3: One possible way of renovation is to paint room 1 with green color, room 2 with red color such that all rooms have same color i.e blue.


#ArrayElementDeletion



	
You have an array A1 containing N objects. You have another array A2 containing numbers that represent indexes into the first array. You need to remove elements from A1 for which indexes are there in A2 and produce the compacted array. The order in A1 needs to be retained. For example:

A1 = [ a, b, c, d, e, f, g ] // N elements and N is large
A2 = [ 5, 1 ] // k elements and k is small (and constant)
Answer = [ a, c, d, e, g, _, _ ]

Write a working program to do this in a language of your preference. The expected time complexity = O(N)



