from dates import check_for_time_band
import unittest
import datetime


class TimeBandsTest(unittest.TestCase):
    def test_time_holidays(self):
        self.assertEqual(
            check_for_time_band(
              datetime.
              datetime.utcnow().replace(day=25).replace(month=12).replace(hour=14).replace(minute=0)),
        "f3"
        )

        self.assertEqual(
            check_for_time_band(
              datetime.
              datetime.utcnow().replace(day=1).replace(month=1).replace(hour=18).replace(minute=0)),
        "f3"
        )


    def test_time_bands(self):
        self.assertEqual(
            check_for_time_band(
              datetime.
              datetime.utcnow().replace(day=16).replace(month=8).replace(hour=22).replace(minute=0)),
        "f3"
        )

        self.assertEqual(
            check_for_time_band(
              datetime.
              datetime.utcnow().replace(day=14).replace(month=8).replace(hour=9).replace(minute=0)),
        "f1"
        )

        self.assertEqual(
            check_for_time_band(
              datetime.
              datetime.utcnow().replace(day=15).replace(month=2).replace(hour=14).replace(minute=0)),
        "f3"
        )

if __name__ == '__main__':
    unittest.main()
