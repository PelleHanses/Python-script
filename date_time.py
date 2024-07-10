#!/usr/bin/python3
"""
date_time.py
Date and time functions.
"""

import calendar
import time
from datetime import datetime, timedelta

def convert_timestamp(timestamp):
    """
    Function to convert timestamp to readable datetime
    """
    return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

def get_last_mont():
    """
    Get the month before this mont, ex 2024-05 for year 2024 nad month may if it is year 2024 and july now
    """
    # Get the current date
    current_date = datetime.now()

    # Calculate the first day of the current month
    first_day_of_current_month = current_date.replace(day=1)

    # Subtract one day from the first day of the current month to get the last day of the previous month
    last_day_of_last_month = first_day_of_current_month - timedelta(days=1)

    # Extract the year and month of the last day of the previous month
    year = last_day_of_last_month.year
    month = last_day_of_last_month.month

    # Format the result as "YYYY-MM"
    last_month = f"{year}-{month:02d}"

    return last_month

def get_first_last_timestamps(year_month):
    """
    Get Unix timestamps for the first and last day of a given year-month.
    year_month should be like 2024-05 for year 2024 and may.
    """
    year, month = map(int, year_month.split('-'))

    first_day = datetime(year, month, 1)
    first_day_timestamp = int(first_day.timestamp())

    last_day = datetime(year, month, calendar.monthrange(year, month)[1], 23, 59, 59)
    last_day_timestamp = int(last_day.timestamp())

    return first_day_timestamp, last_day_timestamp


## Start
current_timestamp = time.time()  # Get the current Unix timestamp
print("")
readable_date = convert_timestamp(current_timestamp)
print(f"Todays date and time: {readable_date}")

last_month = get_last_mont()
print(f"Last month: {last_month}")

first_day_timestamp, last_day_timestamp = get_first_last_timestamps(last_month)
print(f"First day timestamp = {first_day_timestamp}. Last day timestamp = {last_day_timestamp}")
print("")
