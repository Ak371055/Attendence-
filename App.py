import pandas as pd
from datetime import datetime

# Function to record attendance
def record_attendance(name, status):
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    attendance_data = {'Name': name, 'Status': status, 'Time': current_time}

    # Load existing attendance or create a new one
    try:
        attendance_df = pd.read_csv('attendance.csv')
    except FileNotFoundError:
        attendance_df = pd.DataFrame(columns=['Name', 'Status', 'Time'])

    # Append new attendance data
    attendance_df = attendance_df.append(attendance_data, ignore_index=True)
    attendance_df.to_csv('attendance.csv', index=False)

    print(f"Attendance recorded for {name}: {status} at {current_time}")

# Example usage
name = input("Enter your name: ")
status = input("Enter status (Present/Absent): ")
record_attendance(name, status)
