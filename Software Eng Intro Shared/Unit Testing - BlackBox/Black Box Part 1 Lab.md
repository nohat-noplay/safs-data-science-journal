Learning Objectives: 

1. Design test cases using Equivalence Partitioning approach, focusing on following aspects.
a. Identifying test categories considering behavior of a module, adhering to important properties of test categories. 
b. Dealing with numeric (integer, real) import/export data. 
c. Dealing with non-numeric (Boolean, string)import/export data. 
d. Concern about requirements for error handing. 


2. Design test cases using Boundary Value Analysis approach, a. when imports are integers, b. when imports are real numbers.


QUESTIONS:

#### Equivalence Categories
For each of the following submodules, determine the complete set of equivalence categories ( use equivalence partition approach). For each equivalence category, 
(1) give an appropriate test input/import, and 
(2) describe the expected output/export.
 
(a) Submodule calcGrade 
Imports: mark (integer) 
Exports: grade (string) 
Calculates a grade, given a mark. For marks less than 50, the grade is "F". For marks from 50 to 59, the grade is "5". For 60 to 69, the grade is "6", and so on up to "10". If mark is invalid, calcGrade will export the empty string "".

| Categories   | Test Input | Expected Output |
| ------------ | ---------- | --------------- |
| m = 0 > 50   | 48         | "F"             |
| m = 50 =< 60 | 55         | "5"             |
| m = 60 < 70  | 65         | "6"             |
| m = 70 < 80  | 75         | "7"             |
| m = 80 < 90  | 85         | "8"             |
| m = 90 < 100 | 95         | "9"             |
| m = 100      | 100        | "10"            |
| m = < 0      | -1         | ""              |
| m = > 100    | 101        | ""              |

(b) Submodule room
Volume Imports: width, length, height (reals) 
Exports: volume (real) 
Calculates the volume of a room, but only if the imported width, length and height are valid. To be valid, width must be at least 2 (metres), length 2.5, and height 3. For invalid imports, this submodule will return 0.

| Categories                     | Test Input | Expected Output |     |     |
| ------------------------------ | ---------- | --------------- | --- | --- |
| w = <= 2, l = <= 2.5, h = <= 3 | 2, 2.5, 3  | 15              |     |     |
| w = < 2, l = > 2.5, h = <=3    | 2, 1, 3    | "0"             |     |     |
| w = <= 2, l = <= 2.5, h = > 3  | 2, 2.5, 1  | "0"             |     |     |
| w = > 2, l = <= 2.5, h = <= 3  | 1, 2.5, 3  | "0"             |     |     |
| w = > 2, l = > 2.5, h = <= 3   | 1, 1, 3    | "0"             |     |     |
| w = <= 2, l = > 2.5, h = > 3   | 2, 1, 1    | "0"             |     |     |
| w = > 2, l = <= 2.5, h = > 3   | 1, 2.5, 1  | "0"             |     |     |
| w = > 2, l = > 2.5, h = > 3    | 1, 1, 1    | "0"             |     |     |
|                                |            |                 |     |     |

(c) Submodule charCase 
Imports: checkUpper (boolean), ch (character) 
Exports: isCase (boolean) 
Checks whether or not ch is an upper/lowercase letter. If checkUpper is true, the submodule checks whether ch is uppercase, and return true/false accordingly. If checkUpper is false, the submodule instead checks whether ch is lowercase.

![[WhatsApp Image 2024-04-30 at 12.50.05_3e8eab4d.jpg|400]]

| Categories | Test Input | Expected Output |
| ---------- | ---------- | --------------- |
| All Lower  | ch         |                 |
| All Upper  | CH         |                 |
|            | cH         |                 |
|            | Ch         |                 |

(d) Submodule substr 
Imports: str1, str2 (strings) 
Exports: s (string) 
Determines whether one string occurs inside the other. If it does, the submodule returns whichever string is shorter. If not, it returns the the empty string "". Note that the empty string is, by definition, contained inside every string (including itself). For instance, if str1 is "conscience" and str2 is "science", then this submodule returns "science". If both imported strings are "xyz", then the submodule returns "xyz".

![[WhatsApp Image 2024-04-30 at 12.50.12_363cab2a.jpg|500]]

| Categories | Test Input | Expected Output |
| ---------- | ---------- | --------------- |

#### Boundary Value Analysis

(a) BVA 
(a) Submodule calcGrade 
Imports: mark (integer) 
Exports: grade (string) Calculates a grade, given a mark. For marks less than 50, the grade is "F". For marks from 50 to 59, the grade is "5". For 60 to 69, the grade is "6", and so on up to "10". If mark is invalid, calcGrade will export the empty string "".

| Categories              | Test Input | Expected Output |     |
| ----------------------- | ---------- | --------------- | --- |
| Between 0 and 50        | 49         | "F"             |     |
|                         | 50         | "5"             |     |
| Between 50 and 60       | 59         | "5"             |     |
|                         | 60         | "6"             |     |
| Between 60 and 70       | 69         | "6"             |     |
|                         | 70         | "7"             |     |
| Between 70 and 80       | 79         | "7"             |     |
|                         | 80         | "8"             |     |
| Between 80 and 90       | 89         | "8"             |     |
|                         | 90         | "9"             |     |
| Between 90 and 100      | 99         | "9"             |     |
|                         | 100        | "10"            |     |
| Between invalid and 0   | -1         | ""              |     |
| Between 100 and invalid | 101        | ""              |     |

(b)
<span style="color:#ff0000">Submodule uvRating
Imports: index (real) 
Exports: rating (string) 
Determines a rating for ultraviolet radiation risk, based on a real-valued UV index. Ratings below zero are invalid, in which case the submodule returns "-". Otherwise, if the index is below 3, the rating is "low", then up to 6 for "moderate", up to 8 for "high", and up to 11 for "very high". Any rating over 11 is "extreme".
</span>

| Categories              | Test Input | Expected Output |
| ----------------------- | ---------- | --------------- |
| Between 0 and 50        | 49         | "F"             |
|                         | 50         | "5"             |
| Between 50 and 60       | 59         | "5"             |
|                         | 60         | "6"             |
| Between 60 and 70       | 69         | "6"             |
|                         | 70         | "7"             |
| Between 70 and 80       | 79         | "7"             |
|                         | 80         | "8"             |
| Between 80 and 90       | 89         | "8"             |
|                         | 90         | "9"             |
| Between 90 and 100      | 99         | "9"             |
|                         | 100        | "10"            |
| Between invalid and 0   | -1         | ""              |
|                         | 0          | "F"             |
| Between 100 and invalid | 101        | ""              |

reals = floats