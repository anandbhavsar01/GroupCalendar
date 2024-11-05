import unittest
from groupcalendar.src.model.Calendar import Calendar
from groupcalendar.src.model.DayEnum import Day

class TestCalendar(unittest.TestCase):
  def setUp(self):
    self.newCalendar = Calendar()
    self.oneDayCalendar = Calendar()
    self.oneDayCalendar.addDay(Day.WED, [0,1,2,3,4])

  def test_createCalendar(self):
    self.assertEqual(self.newCalendar.days, [])
    self.assertEqual(self.newCalendar.hours, [])
    self.assertEqual(self.newCalendar.calendar, {})

  def test_Calendar_addDay(self):
    self.assertEqual(self.oneDayCalendar.calendar[Day.WED], [0,1,2,3,4])

  def test_Calendar_addHoursNoDays(self):
    self.newCalendar.addHours([0,1,2,3,4,5])
    self.assertEqual(self.newCalendar, Calendar())

  def test_Calendar_addHoursWithDays(self):
    self.oneDayCalendar.addHours([0,1,2,3,4,5])
    self.assertEqual(self.oneDayCalendar.calendar[Day.WED], [0,1,2,3,4,5])

  def test_Calendar_removeDay(self):
    self.assertEqual(self.oneDayCalendar.calendar[Day.WED], [0,1,2,3,4])
    self.oneDayCalendar.removeDay(Day.WED)
    self.assertEqual(self.oneDayCalendar, self.newCalendar)


