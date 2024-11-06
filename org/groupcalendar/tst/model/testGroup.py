import unittest

from groupcalendar.src.model.Group import Group
from groupcalendar.src.model.Member import Member

class TestGroup(unittest.TestCase):
  def setUp(self):
    self.member1 = Member(name="test1")
    self.member2 = Member(name="test2")
    self.newGroup = Group()

  def test_createGroup(self):
    self.assertEqual(self.newGroup.members, {})

  def test_createGroup_withMembers(self):
    self.newGroup = Group(members=[self.member1, self.member2])
    self.assertEqual(self.newGroup.members["test1"].name, self.member1.name)
    self.assertEqual(self.newGroup.members["test2"].name, self.member2.name)

  def test_getMember(self):
    self.newGroup = Group(members=[self.member1, self.member2])
    self.assertEqual(self.newGroup.getMemberByName("test1").name, self.member1.name)
    self.assertEqual(self.newGroup.getMemberByName("test2").name, self.member2.name)

  def test_addMember(self):
    self.assertEqual(self.newGroup.members, {})
    self.newGroup.addMember(self.member1)
    self.assertEqual(self.newGroup.getMemberByName("test1").name, self.member1.name)

  def test_removeMember(self):
    self.newGroup.addMember(self.member1)
    self.assertEqual(self.newGroup.getMemberByName("test1").name, self.member1.name)

    removeMember = self.newGroup.getMemberByName(self.member1.name)
    self.newGroup.removeMember(removeMember)
    self.assertEqual(self.newGroup.members, {})


    