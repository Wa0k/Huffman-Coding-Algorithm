# Huffman-Coding-Algorithm
Created by: Louis ONILLON/@Wa0k

License: MIT License

Published on : 23/02/2021

Version 1.0.0

Contact : wa0k@mailo.com

# Description
Huffman coding is a lossless data compression algorithm. In this algorithm, a variable-length code is assigned to input 
different characters, and the lengths of the assigned codes are based on the frequencies of corresponding characters. 
The most frequent characters have the smallest codes, and the least frequent character gets the largest code.

There are mainly two parts. First one to create a Huffman tree, and another one to traverse the tree to find codes.

You can see an example of compression of the Huffman algorithm in the output.txt file, which is the result of the 
compression of the text in the text.txt file.

More information [here](https://www.geeksforgeeks.org/huffman-coding-greedy-algo-3/).

# Complexity
Complexity for assigning the code for each character according to their frequency is O(n log n).

# Usage
Steps :
1. Write your own text in the text.txt file (be careful to the filename ! If you decided to change the name of this file
   ,make sure that you have also changed it into the script python).
2. Run Huffman_Coding_Algorithm file.
3. See the result of the compression in the output.txt file.

# Example
For an example, consider some string “XYYYZYXYYX”. 

The frequency of character Y is larger than X, and the character Z has the least frequency. So the length of the code 
for Y is smaller than X, and code for X will be smaller than Z. So the code of each character of this string could be :
- Y : 0
- X : 10
- Z : 11
