# Calendar
# Each member in a group stores a calendar of their availability
# The group merges these calendars to determine time intervals where all the 
# members are available.

from collections import defaultdict
from groupcalendar.src.model.DayEnum import Day

class Calendar:
  
  # Create a new calendar
  # days - Which specific days of the week the member is available
  # hours - Set of hours during the entire week that the member is available
  # For now, assume that the hours specified apply to all the days selected
  # Later on, the user can modify specific days of the week with specific time ranges
  def __init__(self, days: list[Day] = [], hours: list[int] = []) -> None:
    self.calendar: defaultdict[Day, list[int]] = defaultdict(list)

    for day in days:
      self.calendar[day] = hours

  # Indicate the time range a member is available on the specified day
  # day - Day the member is available
  # hours - Which hours of the day they're available
  def addDay(self, day: Day, hours: list[int] = []) -> None:
    self.calendar[day] = hours


  def getDays(self) -> list[Day]:
    return list(self.calendar.keys())


  # Update hours for each day the member is available
  # hours - Which hours they're available
  # Warning: overrides the entire week
  def addHours(self, hours: list[int]= [])-> None:
    self.hours = hours
    for day in self.calendar.keys():
      self.calendar[day] = hours
    
  # If a member is no longer available on a specific day, they can remove that
  # day from their calendar
  # day - day when the member is no longer available
  # KeyError - return if the member wasn't available that day in the first place
  def removeDay(self, day: Day) -> list[int]:
    return self.calendar.pop(day)
  
  # Check calendars for equality
  # value - other calendar to compare against
  # return True if the calendars are equal, False otherwise
  def __eq__(self, value):
    other_calendar_days = value.calendar.keys()
    if self.calendar.keys() != other_calendar_days:
      return False
    for day in self.calendar.keys():
      if self.calendar[day] != value.calendar[day]:
        return False
    return True
