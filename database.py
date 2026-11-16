"""MySQL connection and small query helpers for the job tracker."""

import os
from pathlib import Path

import mysql.connector
from dotenv import load_dotenv


# Load the project's local settings file. The real .env file is ignored by Git.
load_dotenv(Path(__file__).resolve().parent / ".env")


def get_db_connection():
    """Open and return a connection to the job_tracker MySQL database.

    Connection settings can be supplied through MYSQL_HOST, MYSQL_PORT,
    MYSQL_USER, MYSQL_PASSWORD, and MYSQL_DATABASE environment variables.
    """
    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "127.0.0.1"),
        port=int(os.getenv("MYSQL_PORT", "3306")),
        user=os.getenv("MYSQL_USER", "root"),
        password=os.getenv("MYSQL_PASSWORD", ""),
        database=os.getenv("MYSQL_DATABASE", "job_tracker"),
    )


def fetch_all(query, params=None):
    """Run a SELECT query and return all rows as dictionaries."""
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    try:
        cursor.execute(query, params if params is not None else ())
        return cursor.fetchall()
    finally:
        cursor.close()
        connection.close()


def fetch_one(query, params=None):
    """Run a SELECT query and return one row as a dictionary, or None."""
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    try:
        cursor.execute(query, params if params is not None else ())
        return cursor.fetchone()
    finally:
        cursor.close()
        connection.close()


def _run_write(query, params=None):
    """Run a data-changing query, commit it, and return its result details."""
    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(query, params if params is not None else ())
        result = (cursor.lastrowid, cursor.rowcount)
        connection.commit()
        return result
    except Exception:
        connection.rollback()
        raise
    finally:
        cursor.close()
        connection.close()


def insert_query(query, params=None):
    """Run an INSERT query and return the new row's auto-increment ID."""
    lastrowid, _ = _run_write(query, params)
    return lastrowid


def execute_query(query, params=None):
    """Run an UPDATE or DELETE query and return the number of affected rows."""
    _, rowcount = _run_write(query, params)
    return rowcount
