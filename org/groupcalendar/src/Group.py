# Group
# Stores a group of members who need to find a common time when they can meet.
from Member import Member
from collections import defaultdict

class Group:
  # Create a new group
  # members - list of members in the group
  # autoincrement an id to avoid mixing up members with the same name
  def __init__(self, members:list[Member] = []):
    self.id = 0
    self.members = defaultdict(list)
    for member in members:
      self.members[member.getName()].append(member)

  # Add a new member
  # member - new member
  # return - integer providing the member with an id.
  def addMember(self, member: Member) -> int:
    self.members.append(member)
  
  # Get a member from the group
  # name - member's name
  def getMember(self, name:str) -> Member:
    return self.members[name]
  
  # Remove a member from the group
  # name - member's name
  def removeMember(self, name:str) -> Member:
    return self.members.pop(name)