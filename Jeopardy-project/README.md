# This is Jeopardy
This directory contains a jupyter notebook, a python script and a csv file. The jupyter notebook contains a full analysis of the jeopardy data base exploring how different words are used in the questions and change over time using the custom functions in the python script. The python script includes custom functions for:

- A *set of three functions that interact to provide an interact quiz* which allows the user to **answer questions** and keeps **track of the score** or winnings. 

  It uses the add float column function to modify the data first, and then selects a number of random questions. The default is number of questions is 5. The answers take into account edge cases where more than one possible response to the answer (i.e. a place that goes by two names) is possible, or where more than one response (i.e. name two of three) is required to answer the question. 
  
  It also allows for partial matching (i.e. just the last name or key word in the answer) to obtain the correct response, as this is consistent with the Jeopardy rules (i.e. last name only). However, this has a bug, for example, if the correct response uses the word 'the' and the user types only 'the', then the user will have the correct answer.
  
  **To try a short**, **5-question quiz**, **run the python script** *jeopardy.py* in the same directory as the *jeopardy.csv* file. 

- A *filtered data set* by key words in a list function, both by string containment and by **exact matching of all words in the list**.

  The first function will match any word with a subset of a filter word (i.e. matches *be* in *maybe*) because it searches the entire question as one string. The second function will match only a filter word itself because it searches by splitting the question into a list. Both return matches where all the words in the filter are matched.

- A *filtered data set of summary stats* of the **number of shows grouped by another field** function, like **decade** (the default field) or **round**, providing **the count and distribution** of the filtered data, and its **percentage to the whole** data set. 
  
  The function uses the **filtered data by keyword** function, aggregates, and provides statistical information on the filtered data. The default field to aggregate is **decade** and the add **date time and decade** function should be called first (see below for details). The function also allows for a word string with spaces, or list entry, for the key words filter.
  
- A *modified data set* function with added new columns for **dollar** (float) value, or **datetime** and **decade** in-place. 
  
  Both functions require that the order of the columns have not been changed nor a column deleted (changing the name of columns is fine). The first in-place function takes the dollar value column and adds a new column with the value as a float for summarizing purposes (default name is new value). The second in-place function converts the air date column to a datetime object and adds a new column which shows the decade of the air date for summarizing purposes.

- A *split data set* function of the jeopardy data into two: one containing Jeopardy and Double Jeopardy rounds, and another containing Final Jeopardy and Tiebreaker rounds.
- A *frequency* function that returns a series of value counts of any column. The default column is decade.
- A *filtered data set of summary stats* function for the decade column. This was a prototype for the more comprehensive stats summary function.
