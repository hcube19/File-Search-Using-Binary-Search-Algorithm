# File-Search-Using-Binary-Search-Algorithm
Just a fun Prototype

There are two search algorithms which can be implemented if index is not
known:

1. Linear Search :</br>
● Searches all elements one by one from index=0 until the element is
found</br>
● Time complexity for this method is O(n)

2. Binary Search :</br>
● Algorithm :</br>
a. NOTE: This method can only be applied on a sorted list.</br>
b. First the element in the middle position in the list is checked.</br>
c. If middle element is not the desired element(key) then it</br>
compares the key with the middle element
d. If the middle element is greater, it will repeat the steps ‘b’ and
‘c’ on elements which are on the left side of the middle
element and discard the right side and likewise if the middle
element is less than key, it will search on the right side of the
middle element.</br>
● Time complexity for this is O(log n)

MODULES: glob (for getting files from a file path) and webbrowser (to open the file)

Right now you need to enter the correct file name with extension. You can use methods to match the string or pattern so that you donot have to always correctly enter filename. (Give it a TRY)
