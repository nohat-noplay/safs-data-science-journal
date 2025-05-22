Reliability is to the extent the system works. Depending on how the system works - we measure reliability in different ways: MTTF/MTBF, AVAIL, POFOD, ROCOF

	Q: Is the system continuous?  (when it's turned on)
                              
                              YES
                                             Can the system be restarted immediately?  
                                                                           YES = AVAIL
                                                                           NO = MTTF

                              NO
                                             Is the system waiting to be used?

                                                                           YES = POFOD
                                                                           NO = ROCOF


*Is the system doing something continuously over weeks/months years?*
MTTF/MTBF: Mean Time To/Between Failure – how long do you expect the system to run
MTTF – average of uptimes, MTBF = average of times between failures
	- <font style="color:green">"The temperature recording system component must have a MTTF of atleast 3 months"</font>

*Is the system running continuously BUT you care more about uptime and downtime + the system can be restarted immediately?*
AVAIL: Availability – what percentage of time the system is working
AVAIL = total uptime / total overall time
	- <font style="color:green">"The system's user registration component must be available 99.9% of the time"</font>

*Is the system waiting to be used? We don’t care about reliability when we use them?*
POFOD: Probability of Failure on Demand – percentage of attempts to use system fail.
POFOD = number of failures / number of attempts
	- <font style="color:green">"The system's print feature must fail on no more than 0.1% of attempts"</font>

*Are we concerned with the cost of each failure?*
ROCOF: Rate of occurrence of Failure – How many failures expected in a given period
ROCOF = number of failures / total overall time
		- <font style="color:green">"The system must not make more than 1 incorrect payment in every 1000 hours"</font>


How to Test: 
We take multiple measurements by running multiple copies of the software simultaneously.  We assume Reliability is “stochastic” which means unpredictable variation or “noise”.