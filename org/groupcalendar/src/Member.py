# Member
# An individual belonging to a group. Members can join and leave groups.
# They each store their own calendar specifying their availability.
from calendar import Calendar

class Member:
  # Create a new member
  # name - member's name
  # calendar - member's weekly availability
  def __init__(self, name: str = "", calendar: Calendar = None) -> None:
    self.name = name
    self.calendar = calendar