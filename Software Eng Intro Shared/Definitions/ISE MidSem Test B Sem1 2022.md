Question 1: PROJECT PLANNING
a) Iterative Waterfall: <span style="color:#00b0f0">RDIVM </span>
- Requirements, 
- Design, 
- Implementation (Coding), 
- Verifications (Testing), 
- Operations/Maintenance
Progress with the ability to backtrack

Spiral Model:<span style="color:#00b0f0"> IEDP</span>
 - Identify and Set Objectives
 - Evaluate Options and Risks
 - Develop and Verify
 - Plan next iteration
		
b) Draw AON graph for a project
MUST BE ABLE TO DRAW AOA AND AON
MUST DRAW START AND END TASKS

b) Find Duration of project
<span style="color:#00b050">Earliest Start = Biggest Earliest Finish from Dependencies</span>
<span style="color:#00b050">Latest Finish = Earliest Finish of concurrent Critical Path task</span>
<span style="color:#00b050">Earliest Finish (EF) = Earliest Start (ES) + Duration</span>
<span style="color:#00b050">Latest Start (LS) = Latest Finish (LF) – Task Duration</span>

c) Find Slack Time for Slack Activities
<span style="color:#00b0f0"><span style="color:#00b0f0"><span style="color:#00b0f0"><span style="color:#00b0f0"><span style="color:#00b0f0"><span style="color:#00b050"></span></span>Earliest Finish - Latest Finish</span></span></span></span>

d) Find critical path
<span style="color:#ffea00">Those that don't have slack time</span>

e) Explain how knowing Slack Time and Critical Path can be useful to managing a project
Slack Time:  means a semiflexible task start date, this allows for project managers to schedule teams across multiple tasks reducing the downtime of those teams. 
Critical Path: Project Managers will know which tasks can not be delayed by looking Critical Tasks and pool resources into those tasks to ensure they are finished on time
                          


Question 2: FUNCTIONAL REQUIREMENTS

1. a) Briefly explain 3 parts of a User Story
<span style="color:#00b050">User - The person that would want this function</span>
<span style="color:#ff0000">Ability - What does the user want to do?</span>
<span style="color:#00b0f0">Benefit - Why does the user want to do this?</span>


b) Consider an online system to book railway tickets for long distance journeys. 
	Write down TWO user stories relate to the functionality of the above system

-------As a Commuter, I want to search Destinations by Suburb to ensure I select a station closest to my final destination

-------As a Customer Service Rep, I want to search online purchased tickets by receipt code to check a commuters ticket


2. Consider the following description about a software for plotting an analyzing scientific data from experiments using different chart types such as scatter, line etc. 
a) Specify the following: 
	
	Goal: 
	To plot data with a selected dataset
	
	Primary Actor: 
	USer

	Secondary Actor: 
	Research Database
	
	Pre-condition:
	User must be logged in
	
	Trigger: 
	User selects "Plot data" option
	
b) Write down the flow of events for the use case
	1. System selects datasets in Research database that User is cleared to use
	2. System displays these datasets as a list
	3. User selects one dataset from list
	4. System displays column titles of selected dataset with descriptions and a form with plotting options
	5. User selects columns to be plotted, fills form (which rows to be plotted, type of chart, colour, title ) and clicks "OK"
	6. System recieves form and generates chart from dataset in research database with parameters specified in form
	7. System exports chart to downloads folder as a png file
	8. System displays chart on screen
 

c) Write down ONE extension for the use case
	6A: Selected columns contain non-numeric data
		1. System shows pop-up box warning User that chart can only be generated with numeric data and other data will be excluded a
		2. User checks "I understand" box and clicks "proceed"
		3. System changes form to exclude rows that contain non-numeric data
		4. Continue with Event 6...

d) Identify TWO task level goals of the system other than plotting data and identify the primary actors for them
	
	Authoriser - Approves or denies access right elevation requests
	Prospective User - Requests system access

	
Q3: Functional and Non-Functional Requirements

1) 2 differences between FR and NFR:
	FR describes what the system must do while NFR describes the characteristics the system must have. 
	
	FR identify separate features of the system
	NFR is mostly about the whole system
	
	A NFR can not be in the form of a Use Case.
	
2) Invalid NFRs:
a) <span style="color:#ff0000">"System must allow students to see available courses and the timetable of them" </span>
- this is a Functional Requirement

b) <span style="color:#ff0000">"Ticketing system should show the users all available ticket types in a user friendly manner"</span>
- This is Ambiguous

3) Rewrite b
<span style="color:#00b050">"The ticketing system must show all available ticket types on a single screen"</span>

4) System that displays oxygen level and blood pressure...
a) Valid Performance NFR
<span style="color:#00b050">"The system must take oxygen level measurements every 3 seconds (evaluated on the base model of the system)"</span>

b) Reliability NFR

SYSTEM IS CONTINUOUS
because when it's turned on its always running. 
AVAIL - can be restarted immediately
<span style="color:#00b050">The blood pressure recording system must be available 99% of the time
</span>

d) another NFR parameter:
<span style="color:#ffea00">Localisation</span> to allow for it to be used in different hospitals around the world with the most common languages for doctors and nurses to read it
<span style="color:#00b050">"The User Interface on the Oxygen and Blood Pressure System must be displayable in English, Spanish and Chinese"
</span>

Q4: AGILE PROJECT MANAGEMENT

a) <span style="color:#ffea00">planned progress per day = sum of task durations / planned project duration</span>
200/100 = 2

b)<span style="color:#ffea00"> planned progress at day 30 </span>= 
<span style="color:#ffea00">30 x 2 (planned progress per day) </span>= 60

c) <span style="color:#ffea00">actual progress at day 30 = </span>
<span style="color:#ffea00">a</span><span style="color:#ffea00">dd all the Estimated Duration days up where the Actual Finish Times are less than 30</span>
30+10+8+12 = 60

d) Planned Progress and Actual Progress are the same at Day 30 and therefore we are on schedule
         

2) WIP limit is useful because it can avoid bottlenecks and keeps the tasks progressing towards the Done column before the team takes on too many other tasks
-Create a new task card and put it in the ToDo column. 

3) 
Product Backlogs:
are all tasks that need to be competed for the entire project. They can be in the form of user stories

Sprints Backlog:
The todo list for a sprint. They can be in the form of broken down user stories to make tasks

Sprints: 
Each sprint is a mini project that takes 1-4 weeks. This mini project must have something deliverable (made from the sprint backlog) to the customer at the end. 

4) Ceremonies
Sprint Planning meeting is a day long meeting where developers talk to the customer and figure out what to complete in a sprint

Sprint Review meeting is a half day meeting at the end of the sprint where the developers present a finished project to the customer                         


NEW QUESTION: IMAGINING HARM
Must answer:
<span style="color:#00b050">- who has been harmed</span>
-<span style="color:#ff0000"> How have they been harmed</span>
<span style="color:#00b0f0">- How has the software contributed to this harm </span>
-<span style="color:#ffea00"> What mistakes could lead to the software harming a person</span>

A software package for helping design houses

<span style="color:#00b050">Who has been harmed: Builders and Contractors</span>
<span style="color:#ff0000">How have they been harmed: Financially and Reputation</span>
<span style="color:#00b0f0">How has the software contributed to this harm: Not used Updated Construction regulations causing rework later in the project</span>
<span style="color:#ffea00">Software mistake: Software has no ability to update it's functions when new regulations come out allowing for users to create designs that are illegal to build </span>

ASC Code of Ethics:
1. The Primacy of Public Interest - place interests of public above all else
2. The Enhancement of Quality of Life 
3. Honesty - representation of skills, knowledge, services, products
4. Competence - Work diligently for your stakeholders
5. Professional Development - for you and your staff
6. Professionalism - integrity and respect