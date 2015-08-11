from itertools import chain
from pytz import timezone
from fn.monad import Option
from operator import mul
from operator import setitem


def generate_timebands():
    """
    Generate Energy Time bands, in according to the provided table

    :return: the final dict containing all the needed data, divided per day and hours
    """
    def generate_workdays_bands():
        """
        Generate the Energy Time Bands for workdays
        """
        return dict(zip((i for i in range(0, 24)), chain(("f3",)*7, ("f2",), ("f1",)*11, ("f2",)*4, ("f3",))))

    def generate_saturdays_bands():
        """
        Generate the Energy Time Bands for saturday
        """
        return dict(zip((i for i in range(0, 24)), chain(("f3",)*7, ("f2",) * 16, ("f3",))))

    def generate_sunday_bands():
        """
        Generate the Energy Time Bands for sunday
        """
        return dict(zip((i for i in range(0, 24)), ("f3",)*24))

    # create the final dict containing all the needed data:
    _tb = Option\
        .from_call(generate_workdays_bands)\
        .map(lambda result: mul((result,), 5))\
        .map(lambda result: zip((i for i in range(0, 5)), result))\
        .map(lambda result: dict(result))\
        .get_or(dict())

    Option.\
        from_call(generate_saturdays_bands)\
        .map(lambda item: setitem(_tb, 5, item))\
        .get_or(dict())

    Option.\
        from_call(generate_sunday_bands)\
        .map(lambda item: setitem(_tb, 6, item))\
        .get_or(dict())

    return _tb


def get_holidays():
    """
    Fixed days to be considered as sunday
    """
    return (
        "01-01",
        "06-01",
        "25-04",
        "01-05",
        "02-06",
        "15-08",
        "01-11",
        "08-12",
        "25-12",
        "26-12"
    )

TIMEBANDS = generate_timebands()
HOLIDAYS = get_holidays()


def check_for_time_band(date):
    """
    Assign to a date the relative energy time band

    :param date: the date to be evaluated
    :return <str>: the computed energy time band
    """
    def in_holidays(date):
        """
        Check if provided date needs to be considered as holiday

        :param date: the date to be checked
        :return: None or 'f3'
        """
        return None if date.strftime("%d-%m") not in HOLIDAYS else "f3"

    def get_timezone():
        """
        Get the timezone
        """
        return timezone('Europe/Rome')

    return Option.\
        from_value(
            get_timezone().localize(date) + get_timezone().localize(date).utcoffset())\
        .map(lambda tz_date: in_holidays(tz_date))\
        .get_or(TIMEBANDS[date.weekday()][date.hour])
