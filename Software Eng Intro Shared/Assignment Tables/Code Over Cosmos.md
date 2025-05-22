
    A journey into Modularity, Test Design and Version Control

    Author: Saf Flatters

  
## Contents
[Introduction](#introduction)  
[Module Descriptions](#module-descriptions)  
[Modularity](#modularity)  
[Black Box Test Design](#black-box-test-design)  
[White Box Test Design](#white-box-test-design)  
[Test Implementation & Test Execution](#test-implementation-and-test-execution)  
[Summary of Work (Traceability Matrix)](#summary-of-work-traceability-matrix)  
[Run Program](#run-program)  
[Version Control](#version-control)  
[Discussion](#discussion)  


  
  
  
  
  
  
  
  

## Introduction

In this project, I developed a Python program centered around numerology principles, aimed at converting birthdates to Life Path numbers, Life Path colours, identifying Master Numbers and the associated generation the birthdate is in. It then gives the option for a user to compare the result with a second birthdate input. These results are also exported to a csv file for further analysis.   

To design this program, I first planned how I was going to Version Control the entire project. I created a repository and mapped out an intended Version Control plan (see Version Control section). I split the branches by different features my program was going to have.

  To split into Features (and therefore Branches), I came up with an associated User Story.

  *(It's important to note that Feature 6 and alterations to Feature 5 were created at a later stage in the project when I found I had missed a specification during planning - a separate Version Control Branch was used for implementation and testing of these changes before merging with master branch)

  

**Feature 1** -

    User Story 1: "As a numerologist, I want to convert a inputted birthday date to a Life Path Number, to conduct further analysis"

  

**Feature 2** -

        User Story 2: "As a numerologist, I want to convert a Life Path Number to a Lucky Colour, to conduct further analysis"

  

**Feature 3** -

     User Story 3: "As a numerologist, I want to confirm if a Life Path Number is a Master Number, to add to my report"

  

**Feature 4** -

        User Story 4: "As a numerologist, I want to compare 2 birthday dates to see if the Life Path Numbers are the same or not"

  

**Feature 5** -

      User Story 5: "As a numerologist, I want to find what generation a person is from, from their birthday to add it to my analysis report"

  

**Feature 6** -

    User Story 6: "As a numerologist, I want to export some of these results to a csv file, to use for further analysis programs"

  

Splitting into features allowed for easier planning of Version Control branching and also working on one feature at a time, made the project easier to design and manage. It also allowed me to iteratively plan modules and implement code by focusing on one feature at a time. I will be referring to these features throughout this report.

  

I then visually mapped out what modules a feature would need, write the module descriptions and then implement the code based on that description. Once I completed all modules for that feature, I then checked them against my Modularity Checklist, assessed the results and then refactored when required. This would take up to 3 iterations of a feature to pass the Modularity Checklist (see Checklist in Modularity section). I then moved onto the next feature (and Git Branch).

  

Once the code was merged and completed (checked for syntax errors etc), I then started designing a Black Box Testing Framework. Then I tested each feature one by one,  fixing errors (fails) and then testing the entire code again to ensure that any changes didn't create other issues.  I noted down my results on the Traceability Matrix and in this report as I went. I completed White Box testing the same way but by indentifying all possible paths.

  

This report describes in detail my process, results, issues I came across and details how to use this code.

  

## Module Descriptions

  

Modules have been planned visually before I documented them so I could ensure that every module was absolutely required (and the code was tight and easy to read/maintain). These modules were designed with Modularity Principles (described in the next section).   These modules were designed with naming conventions.

- "ask" in the module name meant they require user input in the form of typing (keyboard input).

- "2" & "map" - modules using dictionary have the number "2" in their names and the variable "map" is used in every dictionary used as it 'maps' from an element to another element.

- "print" in the module title means that the function prints to the screen (console output). Many of these only have this task and no exports. The idea was to reduce the amount of tasks in it's parent module (the module that calls it).

- "import" or "export" in the module name referred to it working with an external file (csv).

 I have also assigned each module a number. (eg. 2a) I use this throughout this report, code and Traceability Matrix.

- The first digit is which Feature (refer to Introduction) it is made for, the letter is then to itemise the modules within that feature.  

- Some modules will then have another number after the decimal - this is modules that may have been split up when refactored during the modularity checklist process. I have also written a V2 or V3 next to them - to let the reader know Version 2 or Version 3, as one module was refactored twice (eg. 1a.5-V3)

  

### Feature 1:  

(1a) <---- *Post Modularity Review: askUser() has been Refactored! (see 1a.1-V2, 1a.2-V2, 1a.3-V2, 1a.4-V2) for Feature 1 replacement Modules*

**Module**: askUser

**Imports**:

**Exports**: day + " " + month + " " year (string)

*Input: keyboard input Output: return value*

**Task**: Asks user for input of day, month, year and exports it as a string seperated by spaces. All inputs check if integer and if within a specified valid range (DD is between 0 and 32, MM is between 0 and 13 and YYYY is between 1901 and 2025). When Month input checks for integer and if not: calls Module 'month2MM' to allow for different formats of month to be entered by user without returning ValueError.

**Names**: Module is called "askUser" because its what it does, variables called "day", "month" and "year" because thats what they are

  

(1b)

**Module**: month2MM

**Imports**: monthname (string)

**Exports**: monthmap[month] OR 0  (string)

*Input: para pass      Output: return value*

**Task**: A string (month name) is imported, it is changed to all uppercase (to be mapped regardless of case), string to be found in dictionary items and then returns the month number associated with the month name (or shorthand month name). If not found, returns a 0 (to be picked up by exception handling in askUser)  

**Names**: Module is called "month2MM" because it converts month name (or shorthand month name) to a two digit number (string). Variables called "monthUP" - for month name once converted to uppercase, monthmap is name of dictionary because it maps the name to the number.  

  

(1c)  

**Module**: dateLister  

**Imports**: datestring (string)

**Exports**: datelist (list)

*Input: para pass      Output: return value*

**Task**: A string in the format of "DD MM YYYY" is imported (from askUser), a list called datelist is created by splitting string by " ".  

**Names**: Module is called "dateLister" because it makes a list from a string. Variable is named "datelist" because it is a list of components from a date.  

  

(1d)

**Module**: calcList  

**Imports**: datelist (list)

**Exports**: sumofdate (int)

*Input: para pass      Output: return value*

**Task**: Calculates (D+D) + (M+M) + (Y+Y+Y+Y) by sending each item of datelist to be calculated (by addDigits) and then sum them all together  

**Names**: Module is called "calcList" because it adds all items of the list together (once summing each character of that item together in addDigits). Variable "sumofdate" is called that because it is the addition of all numbers in a date. Variable "listitem" is to acknowledge that it is an element of the datelist.  

  

(1e)  

**Module**: lifePathNum  

**Imports**: sumofdate (int)

**Exports**: finalsum (int)

*Input: para pass      Output: return value*

**Task**: Sum of date could still be more than 1 character long so need to add characters again until only 1 left (using addDigits)  

**Names**: Module is called "lifePathNum" because it adds all characters together (for the last time) to get the final Life Path Number.  

  

(1f)  

**Module**: addDigits

**Imports**: listitem (string)

**Exports**: sumofchar  (int)  

*Input: para pass      Output: return value*

**Task**: Adds all digits (characters) of a date list item together until there is only 1 digit left (unless it a Master Number)  

**Names**: Module is called "addDigits" because its adding all characters (that are digits) together. "sumofchar" is because its the final result of adding characters (digits) together until there is only 1 character (digit) to go (unless it a Master Number).  

  

(1g)  

**Module**: checkMaster  

**Imports**: number (string)

**Exports**: True or False (boolean)

*Input: para pass      Output: return value*

**Task**: Checks if number is Master Number (11, 22 or 33)  

**Names**: Module is called "checkMaster" because it's checking if a number is the "Master Number".  

### Feature 1 Refactored (Additonal) Modules

(1a.1-V2)  

**Module**: askUserDate  

**Imports**:  

**Exports**: day (string)

*Input: keyboard input Output: return value*

**Task**: Asks user for input of day. Input is checked if integer and if within a specified valid range (DD is between 0 and 32).  

**Names**: Module is called "askUserDate" because its what it does, variables called "day" because thats what it is.

  

(1a.2-V2)  

**Module**: askUserMonth  

**Imports**:  

**Exports**: month (string)

*Input: keyboard input Output: return value*

**Task**: Asks user for input of month. Input is checked if integer and if not: calls Module 'month2MM' to allow for different formats of month to be entered by user without returning ValueError. Also checked if within a specified valid range (MM is between 0 and 13).  

**Names**: Module is called "askUserMonth" because its what it does, variables called "month" because thats what it is.

  

(1a.3-V2)  

**Module**: askUserYear  

**Imports**:  

**Exports**: year (string)

*Input: keyboard input Output: return value*

**Task**: Asks user for input of year. Input is checked if integer and if within a specified valid range (YYYY is between 1901 and 2025).  

**Names**: Module is called "askUserYear" because its what it does, variables called "year" because thats what it is.

  

(1a.4-V2)  

**Module**: dateString  

**Imports**:  

**Exports**: datestr (string)

*Input: keyboard input Output: return value*

**Task**: Imports from askUserDate(), askUserMonth and askUserYear and then returns it into a string with spaces. Then calls printDateGen().    

**Names**: Module is called "dateString" because it makes a string joining all the date variables. Variable called "datestr" is just a shortened term.

  

(1a.5-V3)  <------------This is Version 3, a change made to Feature 1 after Feature 5 was implemented and merged. This is to increase Cohesion of 1a.4-V2 dateString()  

**Module**: printDateGen  

**Imports**: datestr (string)

**Exports**:  

*Input: para pass      Output: console outp*

**Task**: Imports date string from dateString() and prints Birthday (as confirmation to user) and calls for PrintGen.  

**Names**: Module is called "printDateGen" because I want all printout modules to have "print" in their title. Import variable "datestr" referring to it coming from in dateString and is a date in a string format.

### Feature 2:

(2a)  

**Module**: path2Colour  

**Imports**: lifepathnum (int)  

**Exports**: colour (string)

*Input: para pass      Output: console outp*

**Task**: Returns colour associated with Life Path Number

**Names**:  Module is called "path2Colour" to represent Life Path Number converting to a colour. Dictionary called "colourmap" is because a number is mapped to a colour. Import variable "lifepathnum" is to represent the Life Path number returned from lifePathNum()

### Feature 3: - Refactored

(3a)  

**Module**: printifPathMaster  

**Imports**: lifepathnum (int)  

**Exports**:  

*Input: para pass      Output: console outp*

**Task**: ~~checks if Number is "11", "22" or "33"~~ (Refactored!) Gets checkMaster() to check if lifepathnum is a master number - if so, it prints to screen "Life Path Number is Master Number" (called by lifePathNum)

**Names**:  Module is called printifPathMaster() because I want all printout modules to have "print" in their title. Import variable is lifepathnum to refer to where the number has come from and what it is

### Feature 4:

(4a)  

**Module**: askUser2ndDate  

**Imports**:  

**Exports**: "Y" or "N" (string)

*Input: keyboard input Output: return value*

**Task**: Asks User if they want to compare Life Path with another date

**Names**:  Module is called "askUser2ndDate" because I wanted to keep all functions that require a user input to have "ask user" in their title. This keeps it clear. Input variable is called "ask2ndDate" as it is asking does the user want to input a 2nd date? "Y" is shortened for Yes and "N" is shortened for No. I felt this was clearer than True or False.

  

(4b)  

**Module**: printLPReport  

**Imports**: LPnum

**Exports**:  

*Input: para pass      Output: console outp*

**Task**: This function is to print Life Path Number, call for isPathMaster print out and print Life Path Colour. This function has more than 2 sequentially ordered tasks but this function exists to avoid duplication in the main() code.  

**Names**:  Module is called "printLPReport" because I wanted to keep all functions that require a printout to have "print" in their title. This keeps it clear. Input variable is called "LPnum" as it the Life Path number imported from Main().

  

(4c)  

**Module**: printCompare  

**Imports**: Lifepath1 and Lifepath2

**Exports**:  

*Input: para pass      Output: console outp*

**Task**: This function is to print whether the Life Path numbers of the two birthdates are a match or not.  

**Names**:  Module is called "printCompare" because I wanted to keep all functions that require a printout to have "print" in their title. This keeps it clear. Input variable is called "LPnum" as it the Life Path number imported from Main().

### Feature 5:

(5a)  

**Module**: year2Gen  

**Imports**: year (string)  

**Exports**: generationname (string)  

*Input: para pass      Output: return value*

**Task**: Looks for date range in dictionary and returns name of generation  

**Names**:  Module is called "year2Gen()" because it converts the year date to a generation name. Import variable is "year" because thats what it is. "Date range" is what the interval is called and "genmap" is the dictionary name - following the naming convention of other dictionaries in this code - using "map" in their titles.

  

(5b)  

**Module**: printGen  

**Imports**: year (string)  

**Exports**:  

*Input: para pass      Output: console outp*

**Task**: Prints the result of year2gen to user  

**Names**:  Module is called "printGen" following a naming convention that I am following that all modules that print results to screen have the word "print" in them.

  

(5c)  

**Module**: importGen        ((Added late-stage in the project))

**Imports**: csvfile  

**Exports**: genmap (dict)  

*Input: csvfile   Output: return value*

**Task**: Imports dates, generation name from a csv file and turns this data into a dictionary of date ranges mapping to a generation name  

**Names**:  Module is called "importGen" to show its importing externally from file. "genmap" is the dictionary name - following the naming convention of other dictionaries in this code - using "map" in their titles.

### Feature 6: ((Added late-stage in the project))

(6a)

**Module**: clearReport  

**Imports**: csvfile  

**Exports**: csvfile (file)  

*Input: csvfile    Output: csvfile*

**Task**: Opens existing LifePathReport.csv file and clears any data  

**Names**:  Module is called "clearReport" because thats what it does. The Report is refering to name of the csv file LifePathReport.csv

  

(6b)

**Module**: exportReport  

**Imports**: string  

**Exports**: csvfile (file)  

*Input: csvfile, parameter passing     Output: csvfile*

**Task**: Opens existing LifePathReport.csv file and adds strings passed though from Main()  

**Names**:  Module is called "exportReport" because it exports to report. The Report is refering to name of the csv file LifePathReport.csv

  

## Modularity

  

### Modularity Principles Checklist

Modularity Principles covered by Modularity Checklist (they will be noted as MP# in table):  

- MP1. Loose Coupling - Coupling is is how much one module is dependant on another. Aiming for loose Coupling means changes in one module will be less likely to impact other modules  

- MP2. High Cohesion - Cohesion refers to the degree of relatedness modules are to eachother and how much each module does a single, well-defined task.  

- MP3. Avoids Code Redundancy  

  

Checklist below to be completed before each Feature Branch is merged into another branch:

 <span style="color:red;">Y</span> - bad, requires refactoring to improve Modularity  

 <span style="color:green;">N</span> - good, no changes required  

 <span style="color:yellow;">Y</span> - not good for modularity, however justified in comments below    

  

| Item | Question                                                           |   F1                                  | F1 V2                                |   F2F3                                |   F2F3 V2                            |   F4                                 |   F5                                | F6                                  |

| ---- | ------------------------------------------------------------------ | ------------------------------------- | ------------------------------------ | ------------------------------------- | ------------------------------------ | ------------------------------------ | ----------------------------------- | ----------------------------------- |

| 1    | Does the module have less than 3 parameters? (MP1)                 | <span style="color:green;">N</span>   | <span style="color:green;">N</span>  | <span style="color:green;">N</span>   | <span style="color:green;">N</span>  | <span style="color:green;">N</span>  | <span style="color:green;">N</span> | <span style="color:green;">N</span> |

| 2    | Are there any Global variables? (MP1)                              | <span style="color:green;">N</span>   | <span style="color:green;">N</span>  | <span style="color:green;">N</span>   | <span style="color:green;">N</span>  | <span style="color:green;">N</span>  | <span style="color:green;">N</span> | <span style="color:green;">N</span> |

| 3    | Are there any Control Flags used? (MP1) (MP2)                      | <span style="color:yellow;">Y</span>  | <span style="color:yellow;">Y</span> | <span style="color:green;">N</span>   | <span style="color:yellow;">Y</span> | <span style="color:yellow;">Y</span> | <span style="color:green;">N</span> | <span style="color:green;">N</span> |

| 4    | Does the module perform more than 2 tasks in sequence? (MP2)       | <span style="color:red;">Y</span>     | <span style="color:green;">N</span>  | <span style="color:green;">N</span>   | <span style="color:green;">N</span>  | <span style="color:yellow;">Y</span> | <span style="color:green;">N</span> | <span style="color:green;">N</span> |

| 5    | Are the tasks inside a module weakly related? (MP2)                | <span style="color:green;">N</span>   | <span style="color:green;">N</span>  | <span style="color:green;">N</span>   | <span style="color:green;">N</span>  | <span style="color:green;">N</span>  | <span style="color:green;">N</span> | <span style="color:green;">N</span> |

| 6    | Is there more than 1 edit if a constant needs to be changed? (MP3) | <span style="color:green;">N</span>   | <span style="color:green;">N</span>  | <span style="color:green;">N</span>   | <span style="color:green;">N</span>  | <span style="color:green;">N</span>  | <span style="color:green;">N</span> | <span style="color:green;">N</span> |

| 7    | Can a module be broken up into 2 or more functions? (MP2)          | <span style="color:red;">Y</span>     | <span style="color:green;">N</span>  | <span style="color:green;">N</span>   | <span style="color:green;">N</span>  | <span style="color:green;">N</span>  | <span style="color:green;">N</span> | <span style="color:green;">N</span> |

| 8    | Is the module performing the same task or subtasks? (MP3)          | <span style="color:green;">N</span>   | <span style="color:green;">N</span>  | <span style="color:green;">N</span>   | <span style="color:green;">N</span>  | <span style="color:green;">N</span>  | <span style="color:green;">N</span> | <span style="color:green;">N</span> |

| 9    | Is there any duplication across modules? (MP3)                     | <span style="color:green;">N</span>   | <span style="color:green;">N</span>  | <span style="color:red;">Y</span>     | <span style="color:green;">N</span>  | <span style="color:green;">N</span>  | <span style="color:green;">N</span> | <span style="color:green;">N</span> |

  

*Note: Module redesigns after Refactoring have been put in the Module Description section with "V2" or "V3" in their module number.

  

### Feature 1 Results & Refactoring

Item 3:

- <span style="color:yellow;">Y</span> Control Flag used in askUser() to ensure exception handling doesn't cancel program but gives user another chance to input a valid response. I think this doesn't affect Modularity too much and the benifits outweigh the negatives of using it.  

- <span style="color:yellow;">Y</span> Control Flag used in addDigits() to check for Master number. This increases Coupling between addDigits() and checkMaster(). This use of a Control Flag increases Cohesion (because if we didn't have it we would have to include a secondary task in addDigits() to stop at Master numbers). Having a checkMaster() seperate module will also increase reusability when coding Feature 3.  

Item 4:

- <span style="color:red;">Y</span> askUser() module performs three tasks in sequence. They are highly related tasks and if they were split up, a fourth module will have to be in place to link the tasks together. This is a better option.  

Item 7:

- <span style="color:red;">Y</span> askUser() can be split up into 4 different smaller tasks.

  

<u>Refactor:  </u>

See F1 V2 (Feature 1, Version 2) for checklist after refactoring module askUser() to be 4 different modules (This increases Cohesion).

  

askUser() is now:

- askUserDate()

- askUserMonth()

- askUserYear()

- dateString()  

See 1a.1-V2, 1a.2-V2, 1a.3-V2, 1a.4-V2 in Module Descriptions

  

<u>Feature 1 Code: (1a) askUser() before Refactoring</u>

  

![[askUserOLD.png]]

  

 <u>Feature 1 Code: (1a.1, 1a.2, 1a.3, 1a.4) askUser() after Refactoring</u>

  

![[1aV2-askUserREFACTORED.png]]

  

### Feature 2 & 3 Results & Refactoring

Item 9:

- <span style="color:red;">Y</span> printifPathMaster() is performing a similar task to checkMaster() except is printifPathMaster() prints to screen. The if statement is a duplication. The solution to this is add a control flag (increases Coupling) but this still reduces duplication.

Refactor:  

See F2F3 V2 (Feature 2 & Feature 3 Version 2) for checklist after refactoring module printifPathMaster() to now call checkMaster() inside if statement. This decreasing duplication and increases reuse.

<u>Feature 3 Code: (3a) printifPathMaster() before Refactoring</u>

  

![[isPathMasterOLD.png]]

  

 <u>Feature 3 Code: (3a) printifPathMaster() after Refactoring</u>

  

  *Note: Name Change from isPathMaster() to printifPathMaster() later in project*

  

![[isPathMasterREFACTORED.png]]

### Feature 4 Results & Refactoring

Item 3:

- <span style="color:yellow;">Y</span> Control Flag used in askUser2ndDate() to ensure exception handling doesn't cancel program but gives user another chance to input a valid response. I think this doesn't affect Modularity (Cohesion and Coupling) too much and the benifits outweigh the negatives of using it.  

Item 4:

- <span style="color:yellow;">Y</span> Module "printLPReport()" completes 3 tasks in sequence. This originally was part of the main() code, however to avoid duplication and the same module performing 2 similar subtasks (when asked if user wants to compare 2 birthdates), I made this sequence a function. This prints outputs of other functions in order for displaying to user. The benifits of using this increases coupling, reduces cohesion but not as much as it would affect duplication.

### Feature 5 Results & Refactoring

No issues with Feature 5. Passed all Modularity checks in checklist.

### Feature 6 Results & Refactoring

No issues with Feature 6. Passed all Modularity checks in checklist.

  

### Features Merged

Item 7:

- <span style="color:red;">Y</span> After merging Feature 5 into master branch - I reassessed all modules. Due to this I split dateString tasks into two different modules(). The new one called printDateGen. Marked (1a.5-V3) This increased Cohesion of Feature 1 (once it had decreased due to Feature 5 merging).

  

 <u>Feature 1 Code: (1a.4-V2) dateString() before Refactoring</u>

![[dateStringandprintDateGenOLD.png]]

  

 <u>Feature 1 Code: (1a.5-V3) dateString() and printDateGen() after Refactoring</u>

![[dateStringandprintDateGenREFACTORED.png]]

## Black Box Test Design

  

### Equivalence Partitioning

Test cases are designed by thinking of as many possible categories of scenarios that could be an input and then coming up with a Test Input for those scenarios.

  

#### Module 1a.1-V2: askUserDate()

  

| Categories     | Test Input | Expected Output |

| -------------- | ---------- | --------------- |

| below 1        | "0"        | "0"             |

| between 1 - 31 | "15"       | "15"            |

| above 31       | "32"       | "0"             |

  

#### Module 1a.2-V2 askUserMonth()

  

| Categories                          | Test Input | Expected Output |

| ----------------------------------- | ---------- | --------------- |

| below 1                             | "0"        | "00"            |

| between 1 - 12                      | "6"        | "6"             |

| above 12                            | "13"       | "00"            |

| JANUARY                             | january    | "01"            |

| FEBRUARY                            | february   | "02"            |

| MARCH                               | march      | "03"            |

| APRIL                               | april      | "04"            |

| MAY                                 | may        | "05"            |

| JUNE                                | june       | "06"            |

| JULY                                | july       | "07"            |

| AUGUST                              | august     | "08"            |

| SEPTEMBER                           | september  | "09"            |

| OCTOBER                             | october    | "10"            |

| NOVEMBER                            | november   | "11"            |

| DECEMBER                            | december   | "12"            |

| JAN                                 | jan        | "01"            |

| FEB                                 | feb        | "02"            |

| MAR                                 | mar        | "03"            |

| APR                                 | apr        | "04"            |

| JUN                                 | jun        | "06"            |

| JUL                                 | jul        | "07"            |

| AUG                                 | aug        | "08"            |

| SEP                                 | sep        | "09"            |

| OCT                                 | oct        | "10"            |

| NOV                                 | nov        | "11"            |

| DEC                                 | dec        | "12"            |

| Not month name or abbreviated month | " "        | "00"            |

#### Module 1a.3-V2 askUserYear()

  

| Categories          | Test Input | Expected Output |

| ------------------- | ---------- | --------------- |

| below 1901          | "1900"     | "0000"          |

| between 1901 - 2025 | "1960"     | "1960"          |

| above 2025          | "2026"     | "0000"          |

#### Module 1a.4-V2 dateString()

  

| Categories     | Test Input       | Expected Output |

| -------------- | ---------------- | --------------- |

| DD MM YYYY     | "07" "10" "1988" | "07 10 1988"    |

| Not DD MM YYYY | "100" " " "0"    | "00 00 0000"    |

#### Module 1a.5-V3 printDateGen()

| Categories     | Test Input       | Expected Output |

| -------------- | ---------------- | --------------- |

| DD MM YYYY     | "07" "10" "1988" | "07 10 1988"    |

| Not DD MM YYYY | "100" " " "0"    | "00 00 0000"    |

#### Module 1b  month2MM()

  

| Categories                       | Test Input | Expected Output |

| -------------------------------- | ---------- | --------------- |

| Month name or Month Abbreviation | "October"  | "10"            |

| Not a Month or Abbreviation      | "Blue"     | "0"             |

#### Module 1c dateLister()

  

| Categories   | Test Input   | Expected Output      |

| ------------ | ------------ | -------------------- |

| DD MM YYYY   | "07 10 1988" | ["07", "10", "1988"] |

| Empty string | ""           | [""]                 |

| One Space    | " "          | ["",""]              |

#### Module 1d calcList()

  

| Categories                                                        | Test Input           | Expected Output |

| ----------------------------------------------------------------- | -------------------- | --------------- |

| List of integers                                                  | ["07", "10", "1988"] | 16              |

| Empty string                                                      | [""]                 | 0               |

| One Space                                                         | ["",""]              | 0               |

| Master Number                                                     | ["11"]               | 11              |

| MN + MN = MN                                                      | ["11", "22"]         | 33              |

| int+int = MN (master number is made by D+D (2+9 =11, 11+1+6 = 18) | ["29", "01", "2004"] | 18              |

#### Module 1e lifePathNum()

| Categories                          | Test Input | Expected Output |

| ----------------------------------- | ---------- | --------------- |

| Single digit integer                | 5          | 5               |

| Multi digit integer                 | 44         | 8               |

| Empty String                        | ""         | 0               |

| Master Number                       | 11         | 11              |

| Integer that leads to Master Number | 29         | 11              |

***Note LifePathNum() failed on Integer that leads to Master NUmber - see comment and changes

  

#### Module 1f addDigits()

| Categories                                    | Test Input | Expected Output |

| --------------------------------------------- | ---------- | --------------- |

| string of Single digit integer                | "5"        | 5               |

| string of Multi digit integer                 | "44"       | 8               |

| String of Master Number                       | "11"       | 11              |

| String of Integer that leads to Master Number | "29"       | 11              |

***Note addDigits() failed on Integer that leads to Master NUmber - see comment and changes

  

#### Module 1g checkMaster()

| Categories          | Test Input | Expected Output |

| ------------------- | ---------- | --------------- |

| Master Number "11"  | "11"       | True            |

| Master Number "22"  | "22"       | True            |

| Master Number "33"  | "33"       | True            |

| Not a Master Number | "15"       | False           |

#### Module 2a path2Colour()

| Categories        | Test Input | Expected Output |

| ----------------- | ---------- | --------------- |

| Below 1           | 0          | None            |

| Between 1 and 9   | 5          | "Sky Blue"      |

| 10                | 10         | None            |

| 11                | 11         | "Silver"        |

| Between 12 and 21 | 15         | None            |

| 22                | 22         | "White"         |

| Between 23 and 32 | 25         | None            |

| 33                | 33         | "Crimson"       |

| Above 33          | 34         | None            |

#### Module 3a printifPathMaster()

| Categories          | Test Input | Expected Output                                |

| ------------------- | ---------- | ---------------------------------------------- |

| Master Number "11"  | "11"       | "Life Path Number 11 is a MASTER NUMBER!"      |

| Master Number "22"  | "22"       | "Life Path Number 22 is a MASTER NUMBER!"      |

| Master Number "33"  | "33"       | "Life Path Number 33 is a MASTER NUMBER!"      |

| Not a Master Number | "7361"     | "Life Path Number 7361 is not a Master Number" |

#### Module 4a askUser2ndDate()

| Categories               | Test Input | Expected Output |

| ------------------------ | ---------- | --------------- |

| "Y" or "y"               | "Y"        | "Y"             |

| "N" or "n"               | "n"        | "N"             |

| Not "Y", "y" or "N", "n" | "e"        | "0"             |

#### Module 4b printLPReport()

| Categories  | Test Input | Expected Output                                                                             |

| ----------- | ---------- | ------------------------------------------------------------------------------------------- |

| any integer | 11         | "Life Path Number:  11\nLife Path Number 11 is a MASTER NUMBER!\nLife Path Colour:  Silver" |

#### Module 4c printCompare()

| Categories                              | Test Input | Expected Output                                                                   |

| --------------------------------------- | ---------- | --------------------------------------------------------------------------------- |

| any integer = any integer               | 11, 11     | "It's a match! \nBoth birthdates have the same Life Path Number and Colour!"      |

| any integer not equal any other integer | 5, 11      | "It's not a match. \nEach birthdate has a different Life Path Number and Colour." |

#### Module 5a year2Gen()

| Categories            | Test Input | Expected Output     |

| --------------------- | ---------- | ------------------- |

| less than 1901        | 1900       | None                |

| between 1901 and 1945 | 1915       | "Silent Generation" |

| between 1946 and 1964 | 1950       | "Baby Boomers"      |

| between 1965 and 1979 | 1975       | "Generation X"      |

| between 1980 and 1994 | 1985       | "Millenials"        |

| between 1995 and 2009 | 2005       | "Generation Z"      |

| between 2010 and 2024 | 2015       | "Generation Alpha"  |

| 2025                  | 2025       | "Generation Beta"   |

| Above 2025            | 2026       | None                |

#### Module 5b printGen()

| Categories            | Test Input | Expected Output           |

| --------------------- | ---------- | ------------------------- |

| less than 1901        | 1900       | "Generation:  None"       |

| between 1901 and 2025 | 1988       | "Generation:  Millenials" |

| Above 2025            | 2050       | "Generation:  None"       |

#### Module 5c importGen()

| Categories                               | Test Input                           | Expected Output        |

| ---------------------------------------- | ------------------------------------ | ---------------------- |

| import file that doesn't exist           | testnonexist.csv                     | "File not found"       |

| import csv file with 3 columns           | generationmap.csv                    | {valid gen dictionary} |

| import empty file                        | testdatafiles/testemptyfile.csv      | {}                     |

| import csv file with less than 3 columns | testdatafiles/testunfinishedfile.csv | {}                     |

| import non-csv file                      | testdatafiles/testtextfile.csv       | "File not found"       |

| import csv file with more than 3 columns | testdatafiles/test5columnfile.csv    | {valid gen dictionary} |

#### Module 6a clearReport()

| Categories                          | Test Input            | Expected Output |

| ----------------------------------- | --------------------- | --------------- |

| write to report that doesn't exist* | testwritenonexist.csv | ""              |

| write to report that does exist     | testwritetoexist.csv  | ""              |

\* requires teardown() to remove created file

#### Module 6b exportReport()

| Categories                          | Test Input                 | Expected Output |

| ----------------------------------- | -------------------------- | --------------- |

| write empty string to report*       | testexportfile.csv, ""     | ""              |

| write string to report*             | testexportfile.csv, "x"    | ""              |

| write newline to report*            | testexportfile.csv, "x\ny" | "x,\ny,"        |

| write to report that doesn't exist* | testnoexportfile.csv, "x"  | ""              |

\* requires teardown() to either clear or remove created file

  

### Boundary Value Testing

Test cases are chosen for integer only modules (no floats in this code)

#### Module 1a.1-V2 askUserDate()

| Categories             | Test Input | Expected Output |

| ---------------------- | ---------- | --------------- |

| between invalid and 1  | "0"        | "0"             |

| between 1 - 31         | "1"        | "1"             |

|                        | "31"       | "31"            |

| between 31 and invalid | "32"       | "0"             |

#### Module 1a.2-V2 askUserMonth()

| Categories             | Test Input | Expected Output |

| ---------------------- | ---------- | --------------- |

| between invalid and 1  | "0"        | "0"             |

| between 1 - 12         | "1"        | "1"             |

|                        | "12"       | "12"            |

| between 12 and invalid | "13"       | "0"             |

#### Module 1a.3-V2 askUserYear()

| Categories               | Test Input | Expected Output |

| ------------------------ | ---------- | --------------- |

| between invalid and 1901 | "1900"     | "0000"          |

| between 1901 - 2025      | "1901"     | "1901"          |

|                          | "2025"     | "2025"          |

| between 2025 and invalid | "2026"     | "0000"          |

#### Module 2a path2Colour()

| Categories             | Test Input | Expected Output |

| ---------------------- | ---------- | --------------- |

| between invalid and 1  | 0          | None            |

| Between 1 and 9        | 1          | "Red"           |

|                        | 9          | "Gold"          |

| 10                     | 10         | None            |

| 11                     | 11         | "Silver"        |

| Between 12 and 21      | 12         | None            |

|                        | 21         | None            |

| 22                     | 22         | "White"         |

| Between 23 and 32      | 23         | None            |

|                        | 32         | None            |

| 33                     | 33         | "Crimson"       |

| between 33 and invalid | 34         | None            |

  

#### Module 5a year2Gen()

  

|                          | Categories | Test Input          | Expected Output |

| ------------------------ | ---------- | ------------------- | --------------- |

| between invalid and 1901 | 1900       | None                |                 |

| between 1901 and 1945    | 1901       | "Silent Generation" |                 |

|                          | 1945       | "Silent Generation" |                 |

| between 1946 and 1964    | 1946       | "Baby Boomers"      |                 |

|                          | 1964       | "Baby Boomers"      |                 |

| between 1965 and 1979    | 1965       | "Generation X"      |                 |

|                          | 1979       | "Generation X"      |                 |

| between 1980 and 1994    | 1980       | "Millenials"        |                 |

|                          | 1994       | "Millenials"        |                 |

| between 1995 and 2009    | 1995       | "Generation Z"      |                 |

|                          | 2009       | "Generation Z"      |                 |

| between 2010 and 2024    | 2010       | "Generation Alpha"  |                 |

|                          | 2024       | "Generation Alpha"  |                 |

| 2025                     | 2025       | "Generation Beta"   |                 |

| between 2025 and invalid | 2026       | None                |                 |

## White Box Test Design

  

Due to having to showcase my ability to test a wide variety of situations, I have chosen modules that test different data types (integer, boolean, string), various forms of inputs (parameter passing, keyboard input, import file) and outputs (return values, console output, exporting to file). I have also conducted white box testing on one module that has while loops, for loops and if statements to prove ability to test complexity.

  

**1f) addDigits()**

Input: Parameter Passing

Output: Return Value

Data Type/s: integer, string, boolean

  

| Path                                                                | Test Data | Expected Result |

| ------------------------------------------------------------------- | --------- | --------------- |

| 1. if CM is False, while len is not 1, if CM is False, if len is 1: | "12"      | 3               |

| 2. if CM is False, while len is not 1, if CM is not False (else):   | "1901"    | 11              |

| 3. if CM is False, while len is 1 (else):                           | "5"       | 5               |

| 4. if CM is True (else):                                            | "11"      | "11"            |

  

**(1g) CheckMaster()**  

Input: Parameter Passing

Output: Return Value

Data Type/s: String and Boolean

  

| Path                                          | Test Data  | Expected Result |

| --------------------------------------------- | ---------- | --------------- |

| 1. if number is ["11", "22", "33]:            | "11"       | True            |

| 2. if number is not ["11", "22", "33] (else): | "FLATTERS" | False           |

  

**(4a) askUser2ndDate()**  

Input: Keyboard Input

Output: Return Value

Data Type: String

  

| Path                             | Test Data | Expected Result |

| -------------------------------- | --------- | --------------- |

| 1. if input is not in "Y or N"   | "e"       | "0"             |

| 2. if input is "Y" or "N" (else) | "Y"       | "Y"             |

  

**(3a) printifPathMaster()**  

Input: Parameter passing

Output: console outputs

Data Type/s: Integer, String

  

| Path                          | Test Data | Expected Result                                |

| ----------------------------- | --------- | ---------------------------------------------- |

| 1. If checkmaster:            | 11        | "Life Path Number 11 is a MASTER NUMBER!"      |

| 2. if not checkmaster (else): | 7361      | "Life Path Number 7361 is not a Master Number" |

  

**(5c) importgen()**  

Input: File

Output: Parameter passing

Data Type/s: Integer, String, Dictionary

  

| Path                                              | Test Data                            | Expected Result        |

| ------------------------------------------------- | ------------------------------------ | ---------------------- |

| 1. if file found: if len(line) > 3:               | generationmap.csv                    | {valid gen dictionary} |

| 2. if file found: if len(line) is not > 3 (else): | testdatafiles/testunfinishedfile.csv | {}                     |

| 3. if file not found (else):                      | testnonexist.csv                     | "File not found"       |

**(6b) exportReport()**

Input: String, File

Output: File

Data Type/s: String

  

| Path                                 | Test Data | Expected Result |

| ------------------------------------ | --------- | --------------- |

| 1. if printedoutput is not '\n':     | "x"       | "x,"            |

| 2. if printedoutput is  '\n' (else): | "\n"      | "\n"            |

## Test Implementation and Test Execution

  

Testing Functions added to TestCode.py - Setting up and Tearing down

  

def setup():              <- items not requiring printout to be compared

    capOut = io.StringIO()

    sys.stdout = capOut

  

def teardownRemove(removefile):   <- testing of creating files (delete them after)

    os.remove(removefile)

  

def teardownClear(clearfile):     <- testing of writing to files (clear them after)

    with open(clearfile, 'w') as reportout:

        pass

### Test Execution of Equivelance Partitioning:

  

Issues:

- Test Code only works when "While True" is commented out in exception handling and return statements in ValidError commented in for askUserDate() askUserMonth() askUserYear() askUser2ndDate(). This exception handling helps with usability of the code so I have just noted it at the top of both code files that it requires manual commenting in and out.  

  

 <u>CTRL F: #TESTMARKER FOR ALL LINES AFFECTED</u>

  

 ![[TOTESTorTORUNcomment.png]]

  
  

- lifePathNum() and addDigits() failed on "String integer that leads to master number" showing there is an issue with the addDigits() code. This was rectified by adding another checkMaster() loop inside the calculation code to stop calculation if master number is created. This is an additional check to importing master numbers. See below for addDigits() that failed test and the edited version that passed. All tests were executed to ensure this didn't affect other results.

  

  <u>addDigits() that failed EP testing</u>

  

![[addDigitsFAULT.png]]

 <u>addDigits() that passed EP testing</u>

![[addDigitsFIX.png]]

*all code was retested after fixing addDigits()*

  *see comments above for indepth explanation of addDigits()*

  

### Test Execution of Boundary Value Analysis:

  

Issues:

-  testBVAaskUserYear "TEST between 1901 - 2025 - lower bound" found issue in code where it wouldn't take 1901. Fixed it by changing "1901 < year" to "1900 < year". Retested PASS.  

-

 <u>See Screenshots of before and after change:</u>

![[BVAFIXaskUserYear.png]]

  

![[BVAFIXaskUserYear.png]]

  

### Test Execution of White Box Testing:

No issues, all went as expected.  

  

## Summary of Work (Traceability Matrix)

  

![[TMscreen.png]]

  

## Run Program

  

To run code:

Before running program, please check that ProdCode.py is set up for running, not testing.

Due to a usability feature I coded into exception handling in the user input modules (askUser),

it affected my testing (UserInput will keep being asked until valid response)

- so I have built a running mode and test mode.

  

*Note: Program can still run in Test Mode, it will just pass 0s and Nones through

(rather than giving the User more chances to input valid entries)

  

To put in Run Mode & Use:

1. Crtl+F (control Find) all comments that say #TESTERMARK. There is 8 within the code (+1 in title comment).

2. Each line that has #TESTERMARK needs either a "while True" statement to be uncommented, or a "return" statement to be commented out.

3. Now run ProdCode.py

4. Follow prompts for user input sections.

5. Results are printed to screen and exported to LifePathReport.csv

  

<u>Sample Output</u>

  

![[SampleOutput.png]]

  

<u>Sample csv Output</u>

  

   ![[lifepathreportoutput.png]]

  

## Version Control

  

### Proposed Git Branch Plan

  

![Git Branch Plan](GitBranchPlan.drawio.png)

  

The plan for Version Control is to use the master branch for setting up and then testing (once all branches have merged). Branches are split where there is a different branch for each feature.

  

Due to the sequence of some features I have decided to:

1.  Branch 1 to be split off from Master Branch and used to create Feature 1 (code and module design).

2.  Branch 2 to be split off from Branch 1 to create Feature 2 and Feature 3 (small features that can be coded and module designed together).

3.  Branch 2 to be then merged into Branch 1.

4.  Branch 1 and 2 to be integrated and then merged into the Master Branch.

5.  Branch 3 and Branch 4 is then split off from Master Branch to design and code Feature 3 and Feature 4 respectively.

6.  Branch 3 to be merged into Master Branch.

7.  Branch 4 to be merged into Master Branch.

  

See above Git Branch Plan for a visual representation.

  

### Log of Version Control

  

![[githistoryshortened.png]]

  

### Git Branch Issues

  

Most of my proposed plan went smoothly. However:

  

- I was completing the last checks of this project and found to be able to satisfy the entire project scope, I will require adding in an import and export modules, their associated information and testing. This was a big upheaval of my assignment and needed to be added as a Feature. I decided to add another branch "F6" to contain all my changes while keeping a fresh untouched finished (but not satisfying all specifications) in the master branch. These changes were alteration to 5a year2Gen, addition of 5c importgen(), clearReport(), exportReport() and main(), their associated testCodes, testfiles and alterations to README, Traceability Matrix and this report. One added bonus I didn't realise until I was working in this seperate branch, before committing- I could see where my changes were compared to committed code in VS Code, this kept me from affecting more code than I had to. I merged them together successfully.

- Issue was found while testing Path2Colour for syntax errors (no else for while loop so single digit CalcList returned None eg. "20 10 1983" = calcList "6" and when lifePathNum() called addDigits(), Checkmaster was false but len(listitem) == 1 so it returned a None because I didnt have any code for this scenario.) - #fixed in F2 Branch instead of F1 Branch and kept note of it for the merge.

- Merging F4 and F5 created merge collisions that I had to rectify manually. I know I could of designed F4 and F5 to be completed in a sequence but I wanted to simulate what it would look like if a team was working on this project and experience the after effects such a merge collision. It was easy to work through (but a little stressful).

  

## Discussion

  

This allowed me to showcase my understanding and cement the fundamentals of Version Control, Black Box Testing, White Box Testing and Modularity.

  

Maintainability is a core value I have in my previous work history (Electrical Asset Maintenance) and now can translate this value to include Software as well. Modularity, splitting up projects by features (User Stories), Testing Frameworks and Version Control (Git) are new concepts to me and I will be using this learning as a basis for starting future projects as I continue on my Data Science degree.

  

The Black Box testing concepts I applied felt arduious, however I realised the importance of it when my testing framework found an issue with my addDigits() code that I didn't pick up myself - even with many birthday combinations (friends and family) I had used to trial when writing the code and comparing with manual calculations. No birthdate I had tested with had a master number that was calculated but not imported so I didn't find this fault until I broke down the many combinations possible for Black Box Testing. This highlighted the reason why such a rigorous testing strategy is required for engineering programs.  

  

I discovered to satisfy the entire project scope, I will require adding in an import and export file modules, their associated information and testing. This was a big upheaval of my assignment and would require adding to almost every section of my assignment and altering screenshots etc. I decided to add another branch "F6" (Feature 6) to contain all my changes while keeping a fresh untouched finished (but not satisfying all specifications) in the master branch. This mistake, highlighted to me the greatest use of the Git Version Control system and I can imagine that this would happen often in real life projects when a customer changes their mind last minute, or like this time, something is missing and not found until the end of the project.