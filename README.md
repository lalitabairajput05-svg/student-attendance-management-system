# Student Attendance Management System

A Python-based Student Attendance Management System for adding students, marking attendance, viewing attendance records, and searching for individual student attendance.

## Project Overview

This project is a simple command-line based attendance management system. It stores student details and attendance records in a text file named `attendance.txt`.

The system provides a menu through which the user can:
- Add a new student
- Mark a student as Present or Absent
- View attendance records and percentages
- Search for a student using their roll number
- Exit the program

## Features

1. Add Student
   - Enter a student's roll number and name.
   - Prevents duplicate roll numbers.

2. Mark Attendance
   - Displays the list of students.
   - Allows the user to mark a student as Present or Absent.

3. View Attendance
   - Displays roll number, name, present count, absent count, and attendance percentage.

4. Search Student
   - Searches for a student using their roll number.
   - Displays the student's attendance details.

5. Data Storage
   - Student and attendance information is stored in `attendance.txt`.

## Technologies Used

- Python 3
- Text file handling
- Command-line interface

## Requirements

- Python 3.x
- No external Python libraries are required.

## Project Setup

### 1. Download or clone this repository

Open a terminal and navigate to the project folder.

### 2. Make sure Python 3 is installed

Check the Python installation using:

```bash
python --version
