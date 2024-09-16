# Given a list of 24-hour clock time points in "HH:MM" format, 
# return the minimum minutes difference between any two 
# time-points in the list.
 

# Example 1:
# Input: timePoints = ["23:59","00:00"]
# Output: 1


# Example 2:
# Input: timePoints = ["00:00","23:59","00:00"]
# Output: 0
 

# Constraints:
# 2 <= timePoints.length <= 2 * 104
# timePoints[i] is in the format "HH:MM".

def find_min_difference(time_points):
    
    # helper function to convert "HH:MM" to total minutes
    def time_to_minutes(time):
        hours, minutes = map(int, time.split(":"))
        return hours * 60 + minutes
    
    minutes = [time_to_minutes(time) for time in time_points]

    # sort the list of time in points in minutes
    minutes.sort()

    # initialize the minimum difference as large as possilbe
    min_diff = float("inf")

    # compare consecutive time points
    for i in range(1, len(minutes)):
        min_diff = min(min_diff, minutes[i] - minutes[i -1])

    # also compare the first and last time points considering the wrap-around 
    min_diff = min(min_diff, (1440 + minutes[0] - minutes[-1]))

    return min_diff


time_points = ["23:59", "00:00"]
print(find_min_difference(time_points))