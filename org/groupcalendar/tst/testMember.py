import unittest
from groupcalendar.src.model.DayEnum import Day
from groupcalendar.src.model.Member import Member
from groupcalendar.src.model.Calendar import Calendar

class TestMember(unittest.TestCase):
  def test_createMember(self):
    newMember = Member(id="test@gmail.com", name="test")
    self.assertEqual(newMember.name, "test")
    self.assertIsNone(newMember.calendar)

  def test_createMemberWithCalendar(self):
    newCalendar = Calendar(days=[Day.MON, Day.TUES], hours=[9,10,11,12])
    newMember = Member(name="test2", calendar=newCalendar)
    self.assertEqual(newMember.name, "test2")
    self.assertEqual(newMember.calendar, newCalendar)

  