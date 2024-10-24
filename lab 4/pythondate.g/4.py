from datetime import datetime

date1 = datetime(2024, 10, 24, 12, 0, 0)  
date2 = datetime(2024, 10, 23, 9, 30, 0) 

difference = date1 - date2

seconds_difference = difference.total_seconds()

print("Difference in seconds:", seconds_difference)
