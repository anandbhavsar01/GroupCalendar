# Group
# Stores a group of members who need to find a common time when they can meet.
from groupcalendar.src.model.Member import Member
from groupcalendar.src.model.Calendar import Calendar
from collections import defaultdict

class Group:
  # Create a new group
  # members - list of members in the group
  # autoincrement an id to avoid mixing up members with the same name
  def __init__(self, name: str="", members: list[Member] = []):
    self.name = name
    self.members = defaultdict()
    for member in members:
      self.members[member.name] = member

  # Add a new member
  # member - new member
  def addMember(self, member: Member) -> None:
    self.members[member.name] = member
  
  # Get a member from the group
  # name - member's name
  def getMemberByName(self, name: str) -> Member:
    return self.members[name]
  
  def getMembers(self) -> list[Member]:
    member_list = []
    for member in self.members.keys():
      member_list.append(self.members[member])
    return member_list
  
  # Remove a member from the group
  # name - member's name
  def removeMember(self, member: Member) -> None:
    self.members.pop(member.name)
