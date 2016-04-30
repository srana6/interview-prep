"""
1) Write an algorithm to determine how similar/different two strings are. I was able to interpret this question 
any way I wanted. (percentage difference, character difference) 


2) Working together to design an elevator with the interviewer.  


3) Binary tree serialization/deserialization


4) Uber Pool System design (walk from signup process to how to get the nearest drivers)


5) Find overlapping meeting times


6) Implement autocomplete system  


7) Given a message "one two three four five six seven eight nine", chop it in 
chunks(no exceed the give buffer size) and print out to the screen. Need to maintain 
the word and do not chop it off.

I.E.: buffer size is 15
one two three (1/4)
four five six (2/4)
seven eight (3/4)
nine (4/4)  

	Solution:
		Find the number of words (no of empty spaces) , substring each word and add it to the buffer 
		until it reaches the limit , if it exceeds the limit do not add the current word. print the 
		buffer and re-initialize and start from the word you left off.


		That's not really the answer because you will not be able to print out the (1/4), (2/4) and ...
		You will need to loop through it the very first time and construct the Array of phrases which contains words within the buffer limits.
		Then loop through the Array the very second time and print out all the required phrases.
		I.E.: [one two three][four five six][seven eight][nine], then you loop through the array and print them out with ith/sizeOfArray


		http://www.geeksforgeeks.org/dynamic-programming-set-32-word-break-problem/


8) Design a streaming service 


9) Also had a derivative of the TwoSum question and a Knapsack problem in disguise as something else.  


10) reverse a linked list or implement longest common subsequence.  


11) Implement an LRU cache.  


12) Using Object Oriented Design principles, design a method to check if 
a Sudoku board is valid (skeleton code was provided which was initially passed in through a 2-d array).  

http://www.geeksforgeeks.org/backtracking-set-7-suduku/

13) Print all permutations of 3 pair of parens. ()()(), (()()), (())(),,,. etc  


14) Build a simplified YELP-like service.  

15 )

"""