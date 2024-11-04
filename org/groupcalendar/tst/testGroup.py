import unittest

from groupcalendar.src.Group import Group
from groupcalendar.src.Member import Member

class TestGroup(unittest.TestCase):
  def setUp(self):
    self.member1 = Member("test1")
    self.member2 = Member("test2")
    self.newGroup = Group()

  def test_createGroup(self):
    self.assertEqual(self.newGroup.members, {})

  def test_createGroup_withMembers(self):
    self.newGroup = Group(members=[self.member1, self.member2])
    self.assertEqual(self.newGroup.members["test1"][0].name, self.member1.name)
    self.assertEqual(self.newGroup.members["test2"][0].name, self.member2.name)

  def test_getMember(self):
    self.newGroup = Group(members=[self.member1, self.member2])
    self.assertEqual(self.newGroup.getMemberByName("test1")[0].name, self.member1.name)
    self.assertEqual(self.newGroup.getMemberByName("test2")[0].name, self.member2.name)

  def test_addMember(self):
    self.assertEqual(self.newGroup.members, {})
    self.newGroup.addMember(self.member1)
    self.assertEqual(self.newGroup.getMemberByName("test1")[0].name, self.member1.name)

  def test_removeMember(self):
    self.newGroup.addMember(self.member1)
    self.assertEqual(self.newGroup.getMemberByName("test1")[0].name, self.member1.name)

    removeMember = self.newGroup.getMemberByName(self.member1.name)[0]
    self.newGroup.removeMember(removeMember)
    self.assertEqual(self.newGroup.members, {})


    