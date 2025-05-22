
####  Module 1a.1-V2: askUserDate()

| Categories     | Test Input | Expected Output |
| -------------- | ---------- | --------------- |
| below 1        | "0"        | "0"             |
| between 1 - 31 | "15"       | "15"            |
| above 31       | "32"       | "0"             |
|                |            |                 |

#### Module 1a.2-V2 askUserMonth()

| Categories                          | Test Input | Expected Output |
| ----------------------------------- | ---------- | --------------- |
| below 1                             | "0"        | "00"            |
| between 1 - 12                      | "6"        | "6"             |
| above 12                            | "13"       | "00"            |
| JANUARY                             | january    | "01"            |
| FEBRUARY                            | february   | "02"            |
| MARCH                               | march      | "03"            |
| APRIL                               | april      | "04"            |
| MAY                                 | may        | "05"            |
| JUNE                                | june       | "06"            |
| JULY                                | july       | "07"            |
| AUGUST                              | august     | "08"            |
| SEPTEMBER                           | september  | "09"            |
| OCTOBER                             | october    | "10"            |
| NOVEMBER                            | november   | "11"            |
| DECEMBER                            | december   | "12"            |
| JAN                                 | jan        | "01"            |
| FEB                                 | feb        | "02"            |
| MAR                                 | mar        | "03"            |
| APR                                 | apr        | "04"            |
| JUN                                 | jun        | "06"            |
| JUL                                 | jul        | "07"            |
| AUG                                 | aug        | "08"            |
| SEP                                 | sep        | "09"            |
| OCT                                 | oct        | "10"            |
| NOV                                 | nov        | "11"            |
| DEC                                 | dec        | "12"            |
| Not month name or abbreviated month | " "        | "00"            |


#### Module 1a.3-V2 askUserYear()

| Categories          | Test Input | Expected Output |
| ------------------- | ---------- | --------------- |
| below 1901          | "1900"     | "0000"          |
| between 1901 - 2025 | "1960"     | "1960"          |
| above 2025          | "2026"     | "0000"          |

#### Module 1a.4-V2 dateString()

| Categories     | Test Input       | Expected Output |
| -------------- | ---------------- | --------------- |
| DD MM YYYY     | "07" "10" "1988" | "07 10 1988"    |
| Not DD MM YYYY | "100" " " "0"    | "00 00 0000"    |

#### Module 1a.5-V3 printDateGen()

| Categories     | Test Input       | Expected Output |
| -------------- | ---------------- | --------------- |
| DD MM YYYY     | "07" "10" "1988" | "07 10 1988"    |
| Not DD MM YYYY | "100" " " "0"    | "00 00 0000"    |

#### Module 1b  month2MM()

| Categories                       | Test Input | Expected Output |
| -------------------------------- | ---------- | --------------- |
| Month name or Month Abbreviation | "October"  | "10"            |
| Not a Month or Abbreviation      | "Blue"     | "0"             |

#### Module 1c dateLister()

| Categories   | Test Input   | Expected Output      |
| ------------ | ------------ | -------------------- |
| DD MM YYYY   | "07 10 1988" | ["07", "10", "1988"] |
| Empty string | ""           | [""]                 |
| One Space    | " "          | ["",""]              |

#### Module 1d calcList()

| Categories                                                        | Test Input           | Expected Output |
| ----------------------------------------------------------------- | -------------------- | --------------- |
| List of integers                                                  | ["07", "10", "1988"] | 16              |
| Empty string                                                      | [""]                 | 0               |
| One Space                                                         | ["",""]              | 0               |
| Master Number                                                     | ["11"]               | 11              |
| MN + MN = MN                                                      | ["11", "22"]         | 33              |
| int+int = MN (master number is made by D+D (2+9 =11, 11+1+6 = 18) | ["29", "01", "2004"] | 18              |


#### Module 1e lifePathNum()

| Categories                          | Test Input | Expected Output |
| ----------------------------------- | ---------- | --------------- |
| Single digit integer                | 5          | 5               |
| Multi digit integer                 | 44         | 8               |
| Empty String                        | ""         | 0               |
| Master Number                       | 11         | 11              |
| Integer that leads to Master Number | 29         | 11              |

***Note LifePathNum() failed on Integer that leads to Master NUmber
#### Module 1f addDigits()

| Categories                                    | Test Input | Expected Output |
| --------------------------------------------- | ---------- | --------------- |
| string of Single digit integer                | "5"        | 5               |
| string of Multi digit integer                 | "44"       | 8               |
| String of Master Number                       | "11"       | 11              |
| String of Integer that leads to Master Number | "29"       | 11              |
***Note addDigits() failed on Integer that leads to Master NUmber

#### Module 1g checkMaster()
| Categories          | Test Input | Expected Output |
| ------------------- | ---------- | --------------- |
| Master Number "11"  | "11"       | True            |
| Master Number "22"  | "22"       | True            |
| Master Number "33"  | "33"       | True            |
| Not a Master Number | "15"       | False           |


 #### Module 2a path2Colour()

| Categories        | Test Input | Expected Output |
| ----------------- | ---------- | --------------- |
| Below 1           | 0          | None            |
| Between 1 and 9   | 5          | "Sky Blue"      |
| 10                | 10         | None            |
| 11                | 11         | "Silver"        |
| Between 12 and 21 | 15         | None            |
| 22                | 22         | "White"         |
| Between 23 and 32 | 25         | None            |
| 33                | 33         | "Crimson"       |
| Above 33          | 34         | None            |

#### Module 3a printifPathMaster()

| Categories          | Test Input | Expected Output                                |
| ------------------- | ---------- | ---------------------------------------------- |
| Master Number "11"  | "11"       | "Life Path Number 11 is a MASTER NUMBER!"      |
| Master Number "22"  | "22"       | "Life Path Number 22 is a MASTER NUMBER!"      |
| Master Number "33"  | "33"       | "Life Path Number 33 is a MASTER NUMBER!"      |
| Not a Master Number | "7361"     | "Life Path Number 7361 is not a Master Number" |

#### Module 4a askUser2ndDate()

| Categories               | Test Input | Expected Output |
| ------------------------ | ---------- | --------------- |
| "Y" or "y"               | "Y"        | "Y"             |
| "N" or "n"               | "n"        | "N"             |
| Not "Y", "y" or "N", "n" | "e"        | "0"             |

#### Module 4b printLPReport()

| Categories  | Test Input | Expected Output                                                                             |
| ----------- | ---------- | ------------------------------------------------------------------------------------------- |
| any integer | 11         | "Life Path Number:  11\nLife Path Number 11 is a MASTER NUMBER!\nLife Path Colour:  Silver" |


#### Module 4c printCompare()

| Categories                              | Test Input | Expected Output                                                                   |
| --------------------------------------- | ---------- | --------------------------------------------------------------------------------- |
| any integer = any integer               | 11, 11     | "It's a match! \nBoth birthdates have the same Life Path Number and Colour!"      |
| any integer not equal any other integer | 5, 11      | "It's not a match. \nEach birthdate has a different Life Path Number and Colour." |



#### Module 5a year2Gen()

| Categories            | Test Input | Expected Output     |
| --------------------- | ---------- | ------------------- |
| less than 1901        | 1900       | None                |
| between 1901 and 1945 | 1915       | "Silent Generation" |
| between 1946 and 1964 | 1950       | "Baby Boomers"      |
| between 1965 and 1979 | 1975       | "Generation X"      |
| between 1980 and 1994 | 1985       | "Millenials"        |
| between 1995 and 2009 | 2005       | "Generation Z"      |
| between 2010 and 2024 | 2015       | "Generation Alpha"  |
| 2025                  | 2025       | "Generation Beta"   |
| Above 2025            | 2026       | None                |

#### Module 5b printGen()

| Categories            | Test Input | Expected Output           |
| --------------------- | ---------- | ------------------------- |
| less than 1901        | 1900       | "Generation:  None"       |
| between 1901 and 2025 | 1988       | "Generation:  Millenials" |
| Above 2025            | 2050       | "Generation:  None"       |





| Module Name                   | BB (EP) | BB (BVA) | WB  | Data Type/s | Form of IO | EP Results        | BVA Results | WB Results |
| ----------------------------- | ------- | -------- | --- | ----------- | ---------- | ----------------- | ----------- | ---------- |
| Module 1a.2-V2 askUserMonth() |         |          |     |             |            |                   |             |            |
| Module 1a.3-V2 askUserYear()  |         |          |     |             |            |                   |             |            |
| Module 1a.4-V2 dateString()   |         |          |     |             |            |                   |             |            |
| Module 1a.5-V3 printDateGen() |         |          |     |             |            |                   |             |            |
| Module 1b  month2MM()         |         |          |     |             |            |                   |             |            |
| Module 1c dateLister()        |         |          |     |             |            |                   |             |            |
| Module 1d calcList()          |         |          |     |             |            |                   |             |            |
| Module 1e lifePathNum()       |         |          |     |             |            | FAIL - see RETEST |             |            |
| Module 1f addDigits()         |         |          |     |             |            | FAIL - see RETEST |             |            |
| Module 1g checkMaster()       |         |          |     |             |            |                   |             |            |

#### <span style="color:#00b050">Module 5c importgen()</span>

| Categories                               | Test Input                           | Expected Output        |
| ---------------------------------------- | ------------------------------------ | ---------------------- |
| import file that doesn't exist           | testnonexist.csv                     | "File not found"       |
| import csv file with 3 columns           | generationmap.csv                    | {valid gen dictionary} |
| import empty file                        | testdatafiles/testemptyfile.csv      | {}                     |
| import csv file with less than 3 columns | testdatafiles/testunfinishedfile.csv | {}                     |
| import non-csv file                      | testdatafiles/testtextfile.csv       | "File not found"       |
| import csv file with more than 3 columns | testdatafiles/test5columnfile.csv    | {valid gen dictionary} |


#### <span style="color:#00b050">Module 6a clearReport()</span>
| Categories                          | Test Input            | Expected Output |
| ----------------------------------- | --------------------- | --------------- |
| write to report that doesn't exist* | testwritenonexist.csv | ""              |
| write to report that does exist     | testwritetoexist.csv  | ""              |
\* requires teardown() to remove created file
  
#### <span style="color:#00b050">Module 6b exportReport()</span>

| Categories                          | Test Input                 | Expected Output |
| ----------------------------------- | -------------------------- | --------------- |
| write empty string to report*       | testexportfile.csv, ""     | ""              |
| write string to report*             | testexportfile.csv, "x"    | ""              |
| write newline to report*            | testexportfile.csv, "x\ny" | "x,\ny,"        |
| write to report that doesn't exist* | testnoexportfile.csv, "x"  | ""              |

\* requires teardown() to either clear or remove created file








BVA

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

#### Module 1a.1-V2 askUserDate() 

| Categories             | Test Input | Expected Output |
| ---------------------- | ---------- | --------------- |
| between invalid and 1  | "0"        | "0"             |
| between 1 - 31         | "1"        | "1"             |
|                        | "31"       | "31"            |
| between 31 and invalid | "32"       | "0"             |
#### Module 1a.2-V2 askUserMonth()

| Categories             | Test Input | Expected Output |
| ---------------------- | ---------- | --------------- |
| between invalid and 1  | "0"        | "0"             |
| between 1 - 12         | "1"        | "1"             |
|                        | "12"       | "12"            |
| between 12 and invalid | "13"       | "0"             |

#### Module 1a.3-V2 askUserYear()

| Categories               | Test Input | Expected Output |
| ------------------------ | ---------- | --------------- |
| between invalid and 1901 | "1900"     | "0000"          |
| between 1901 - 2025      | "1901"     | "1901"          |
|                          | "2025"     | "2025"          |
| between 2025 and invalid | "2026"     | "0000"          |

#### Module 2a path2Colour()

| Categories             | Test Input | Expected Output |
| ---------------------- | ---------- | --------------- |
| between invalid and 1  | 0          | None            |
| Between 1 and 9        | 1          | "Red"           |
|                        | 9          | "Gold"          |
| 10                     | 10         | None            |
| 11                     | 11         | "Silver"        |
| Between 12 and 21      | 12         | None            |
|                        | 21         | None            |
| 22                     | 22         | "White"         |
| Between 23 and 32      | 23         | None            |
|                        | 32         | None            |
| 33                     | 33         | "Crimson"       |
| between 33 and invalid | 34         | None            |

#### Module 5a year2Gen()

| Categories               | Test Input | Expected Output     |
| ------------------------ | ---------- | ------------------- |
| between invalid and 1901 | 1900       | None                |
| between 1901 and 1945    | 1901       | "Silent Generation" |
|                          | 1945       | "Silent Generation" |
| between 1946 and 1964    | 1946       | "Baby Boomers"      |
|                          | 1964       | "Baby Boomers"      |
| between 1965 and 1979    | 1965       | "Generation X"      |
|                          | 1979       | "Generation X"      |
| between 1980 and 1994    | 1980       | "Millenials"        |
|                          | 1994       | "Millenials"        |
| between 1995 and 2009    | 1995       | "Generation Z"      |
|                          | 2009       | "Generation Z"      |
| between 2010 and 2024    | 2010       | "Generation Alpha"  |
|                          | 2024       | "Generation Alpha"  |
| 2025                     | 2025       | "Generation Beta"   |
| between 2025 and invalid | 2026       | None                |






# White Box Testing

Due to having to showcase my ability to test a wide variety of situations, I have chosen modules that test different data types, various forms of inputs and outputs. I have also conducted white box testing on one module that has while loops, for loops and if statements to prove ability to test complexity.

<span style="color:#ff0000">ProdCode.py does not have textfiles inputs or textfile outputs so I have simulated a module (not used in program) to be able to be fully assessed. 
</span>

(1f) addDigits()
Input: Parameter Passing
Output: Return Value
Data Type/s: integer, string, boolean

| Path                                                                | Test Data | Expected Result |
| ------------------------------------------------------------------- | --------- | --------------- |
| 1. if CM is False, while len is not 1, if CM is False, if len is 1: | "12"      | 3               |
| 2. if CM is False, while len is not 1, if CM is not False (else):   | "1901"    | 11              |
| 3. if CM is False, while len is 1 (else):                           | "5"       | 5               |
| 4. if CM is True (else):                                            | "11"      | "11"            |


(1g) CheckMaster()
Input: Parameter Passing
Output: Return Value
Data Type/s: String and Boolean

| Path                                          | Test Data  | Expected Result |
| --------------------------------------------- | ---------- | --------------- |
| 1. if number is ["11", "22", "33]:            | "11"       | True            |
| 2. if number is not ["11", "22", "33] (else): | "FLATTERS" | False           |


(4a) askUser2ndDate()
Input: Keyboard Input
Output: Return Value
Data Type: String

| Path                             | Test Data | Expected Result |
| -------------------------------- | --------- | --------------- |
| 1. if input is not in "Y or N"   | "e"       | "0"             |
| 2. if input is "Y" or "N" (else) | "Y"       | "Y"             |

(3a) printifPathMaster()
Input: Parameter passing
Output: console outputs
Data Type/s: Integer, String

| Path                          | Test Data | Expected Result                                |
| ----------------------------- | --------- | ---------------------------------------------- |
| 1. If checkmaster:            | 11        | "Life Path Number 11 is a MASTER NUMBER!"      |
| 2. if not checkmaster (else): | 7361      | "Life Path Number 7361 is not a Master Number" |
|                               |           |                                                |


**<span style="color:#00b050">(5c) importgen()** <br></span>
Input: File
Output: Parameter passing
Data Type/s: Integer, String, Dictionary

  

| Path                                              | Test Data                            | Expected Result        |
| ------------------------------------------------- | ------------------------------------ | ---------------------- |
| 1. if file found: if len(line) > 3:               | generationmap.csv                    | {valid gen dictionary} |
| 2. if file found: if len(line) is not > 3 (else): | testdatafiles/testunfinishedfile.csv | {}                     |
| 3. if file not found (else):                      | testnonexist.csv                     | "File not found"       |

  

<span style="color:#00b050">***(6b) exportReport()** </span><br>
Input: String, File
Output: File
Data Type/s: String

| Path                                 | Test Data | Expected Result |
| ------------------------------------ | --------- | --------------- |
| 1. if printedoutput is not '\n':     | "x"       | "x,"            |
| 2. if printedoutput is  '\n' (else): | "\n"      | "\n"            |
