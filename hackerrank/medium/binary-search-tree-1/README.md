# Binary Tree Nodes

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given a table, <em>BST</em>, containing two columns: <em>N&nbsp;</em>and <em>P,</em>&nbsp;where <em>N</em> represents the value of a node in <em>Binary Tree</em>, and <em>P</em> is the parent of <em>N</em>.

<img src="https://s3.amazonaws.com/hr-challenge-images/12888/1443818507-5095ab9853-1.png" />

Write a query to find the node type of <em>Binary Tree</em> ordered by the value of the node. Output one of the following for each node:

<ul>
	<li><em>Root</em>: If node is root node.</li>
	<li><em>Leaf</em>: If node is leaf node.</li>
	<li><em>Inner</em>: If node is neither root nor leaf node.</li>
</ul>

__Sample Input__

<img src="https://s3.amazonaws.com/hr-challenge-images/12888/1443818467-30644673f6-2.png" />

__Sample Output__

    1 Leaf
    2 Inner
    3 Leaf
    5 Root
    6 Leaf
    8 Inner
    9 Leaf

<br>
__Explanation__

The <em>Binary Tree</em> below illustrates the sample:

<img src="https://s3.amazonaws.com/hr-challenge-images/12888/1443773633-f9e6fd314e-simply_sql_bst.png" />

**Input Format**

 

**Constraints**

 

**Output Format**

## Solution

**Language:** SQL  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-18T09:37:51.501Z  

```sql
/*
Enter your query here.
*/

SELECT N,
       CASE 
           WHEN P IS NULL THEN 'Root'
           WHEN N IN (SELECT DISTINCT P FROM BST WHERE P IS NOT NULL) THEN 'Inner'
           ELSE 'Leaf'
       END AS NodeType
FROM BST
ORDER BY N;

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/binary-search-tree-1/problem)