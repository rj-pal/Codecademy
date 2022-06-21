# Codecadmy Project Files

This directory contains files pertaining to the Codecademy Data Scientist Machine Learning Specialist and will be kept in chronological order. 

1. **This is Jeopardy**- this directory contains an analysis of the jeopardy database. The notebook includes an analysis of word use in jeopardy questions. To try a short, 5-question quiz, run the python script *jeopardy.py* in the same directory as the *jeopardy.csv* file. Highlight functions include: 
    - A *set of three functions that interact to provide an interact quiz* which allows the user to answer questions and keeps track of the score. 
    - A *filtered data set* by key words in a list, both by string containment and by **exact matching of all words in the list**
    - A *filtered data set of summary stats* of **the number of shows grouped by another field**, like decade (default) or round, providing **the count and distribution** of the filtered data, and its **percentage to the whole** data set.   
    - A *modified data set inplace* with added new columns for **dollar** (float) value, or **datetime** and **decade**
     
2. **coded_correspondence**- this directory contains an analysis of ciphers. The notebook includes coding and decoding messages. Note that my coders and decoders take into account the case of the letter, and the function can set the direction of the offset. The main functions are:
    - A *Caesar Cipher* that codes messages based on a set offset.
    - A *Vigenere Cipher* that codes messages based on a keyword offset.

3. **Reggie's Linear Regression**- This directory contains functions for a linear regression by brute force. Note some differences in floating point errors depending on how one generates a list of numbers. The main functions are:
    - An *error calculation* function for obtaining the sum of errors for a set points on a given line. 
    - A *best fit* function for obtaining the best fit line for a list of possible slopes and intercepts.
    
    