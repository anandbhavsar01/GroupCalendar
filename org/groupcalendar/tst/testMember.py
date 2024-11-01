import unittest
from groupcalendar.src.DayEnum import Day
from groupcalendar.src.Member import Member
from groupcalendar.src.Calendar import Calendar

class TestMember(unittest.TestCase):
  def test_createMember(self):
    newMember = Member("test")
    self.assertEqual(newMember.name, "test")
    self.assertIsNone(newMember.calendar)

  def test_createMemberWithCalendar(self):
    newCalendar = Calendar(days=[Day.MON, Day.TUES], hours=[9,10,11,12])
    newMember = Member("test2", newCalendar)
    self.assertEqual(newMember.name, "test2")
    self.assertEqual(newMember.calendar, newCalendar)

  