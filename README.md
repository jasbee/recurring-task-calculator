# recurring-task-calculator
This function accepts 4 variables and calculates the dates when a task should recur.

The input variables:
firstDate - this is the first possible date when the task could recur.  For example "23/11/2016".  It uses the dd/mm/yyyy format.
k - an interval of weeks to repeat.  For example 2 would repeat every other week.
daysOfTheWeek - a list of weekdays to repeat on.  For example ["Monday", "Thursday"]. 
n - a number of times to repeat.  For example 4.

Then it returns the dates when the task should recur.  If we were to run the above example.

firstDate = "23/11/2016"
k = 2
daysOfTheWeek = ["Monday", "Thursday"]
n = 4

The output will be as follows.
----------------------------------
Based on the information received these are the dates of the recurring tasks: 
['24/11/2016', '28/11/2016', '08/12/2016', '12/12/2016']

firstDate = 23/11/2016 | k = 2 | daysOfTheWeek =['Monday', 'Thursday'] | n = 4
----------------------------------

'24/11/2016' is the first Thursday following the firstDate and is included
'28/11/2016' is the first Monday following the firstDate and is also included
'01/12/2016' is a Thursday and '05/12/2016' is a Monday, however because the interval k is 2 they are skipped
'08/12/2016' is the 3rd Thursday and is included
'12/12/2016' is the 3rd Monday and is included
