# AFL-2-Database

This project involves creating a MySQL database to manage student (`mahasiswa`) information including their grades based on their scores.

## Prerequisites

Ensure you have the following installed:
- Python 3.12.3
- MySQL Server (Im using Laragon to connect the database)
- `mysql-connector-python` package

## Installation

1. Install `mysql-connector-python` if you haven't already:

    ```sh
    pip install mysql-connector-python
    ```

2. Ensure MySQL server is running.

## Database and Table Creation

The script performs the following steps:
1. Connects to MySQL server using the root user without a password.
2. Creates a database named `mahasiswa_db` if it doesn't already exist.
3. Creates a table named `mahasiswa` with the following columns:
    - `NIM` (Primary Key)
    - `Nama`
    - `Nilai`
    - `Grade`

## Grade Determination

The `determine_grade` function is used to assign grades based on the `Nilai` (score) of each student:
- `A` for scores >= 90
- `A-` for scores >= 85
- `B+` for scores >= 80
- `B` for scores >= 75
- `B-` for scores >= 70
- `C+` for scores >= 60
- `C` for scores >= 55
- `D` for scores >= 45
- `E` for scores < 45

## Before Insert Trigger Simulation

The `before_insert_trigger` function simulates a database trigger by determining the grade before inserting the student record into the database. This function prints the student's details and the assigned grade.

## Data Insertion

A list of students (`mahasiswa`) is provided with their NIM, Nama, and Nilai. The script iterates over this list, determines the grade for each student, and inserts the data into the `mahasiswa` table.

## Running the Script

To run the script, simply execute it using Python:

```sh
python script_name.py
