# Student-Performance-Analytics

A Python File Handling Based Project containing a csv(Comma Separated Values) file with students name and their marks.
The main objective is to understand how raw data can be converted into meaningful information using Python.

# Project Overview

We divided the project into five main functions.

## Function 1 - read_data() function

This function reads the data from the csv file and return the data in the form of a list containing students name and their marks as 1 element of a list.

## Function 2 - clean_data() function

This function reads the data from the csv file and return 2 elements 
**1. A list of valid students name and their marks in the file named valid_students**
**2. An integer of invalid students in the file names invalid_count**

## Function 3 - analyse_data() function

This function takes **valid_students** and **invalid_count** as parameters, reads the data from the csv file and calculate **Total students as total_students**, **Invalid students as invalid_students**, **Average marks as average_marks**, **Highest marks and student who scored highest marks as max_marks and max_marks_name**, **Lowest marks and student who scored lowest marks as min_marks and min_marks_name**, **Number of students passed as passed_students**, and **Passing percentage of total students as pass_percentage** and stores all of these in a dictionary named **report** and returns this report.

## Function 4 - generate_report() function

This function takes **report** as parameter and print a full report.

## Function 5 - main() function

Connects all functions and controls the execution of the complete program.

# Technology Used

**Python** as **Main programming language**
**CSV module** for **Reading and writing CSV files**
**VS Code**	for **Writing and running code**
**Python Terminal** for **Executing the program**
**CSV file** for **Storing student records**

# Concepts Learned

**Functions for Dividing a program into smaller reusable blocks**
**File handling	for Opening and reading/writing files**
**CSV handling for Working with tabular data**
**DictReader() for Reading CSV rows as dictionaries**
**writerow() for Writing records into CSV files**
**Lists	for Storing multiple student records**
**Tuples for Storing student name and marks together**
**Dictionaries for Organising the final report**
**Loops	for Iterating through student records**
**Conditional statements for Checking valid and invalid records**
**continue for Skipping invalid records**
**try-except for Handling conversion errors**
**sum(), max(), min() for Performing calculations**
**len()	for Counting records**
**main() for Controlling program execution**

# Project Output

{'Name': 'Asha', 'Marks': '78'}
{'Name': 'Ravi', 'Marks': '35'}
{'Name': 'Meera', 'Marks': '92'}
{'Name': 'Kabir', 'Marks': '60'}
{'Name': '', 'Marks': '50'}
{'Name': 'Isha', 'Marks': ''}
{'Name': 'Dev', 'Marks': '105'}

====== STUDENT PERFORMANCE REPORT ======

Total Valid Students: 4
Invalid Records Removed: 3

Average Marks: 66.25

Highest Marks: Meera ( 92 )
Lowest Marks: Ravi ( 35 )

Students Passed: 3
Pass Percentage: 0.75

========================================

# Learning Outcome

Learned the fundamentals of data collection, data cleaning and data analysis, which are essential foundations for Data Science and Machine Learning.
