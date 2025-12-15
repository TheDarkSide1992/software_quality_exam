from datetime import datetime, timedelta

START_DATE_NOT_IN_FUTURE = [
        (datetime.now() + timedelta(days=-1), datetime.now() + timedelta(days=1)),
        (datetime.now() + timedelta(days=-2), datetime.now() + timedelta(days=5)),
        (datetime.now() + timedelta(days=-20), datetime.now() + timedelta(days=-18)),
        (datetime.now() + timedelta(days=-32), datetime.now() + timedelta(days=-35)),
    ]

START_DATE_IN_FUTURE = [(datetime.now() + timedelta(days=1), datetime.now() + timedelta(days=9)),
        (datetime.now() + timedelta(days=2), datetime.now() + timedelta(days=5)),
        (datetime.now() + timedelta(days=21), datetime.now() + timedelta(days=22)),
        (datetime.now() + timedelta(days=32), datetime.now() + timedelta(days=35)),]

FUTURE_DATES_RESERVED = [
        (datetime.now() + timedelta(days=10), datetime.now() + timedelta(days=11)),
        (datetime.now() + timedelta(days=19), datetime.now() + timedelta(days=21)),
        (datetime.now() + timedelta(days=15), datetime.now() + timedelta(days=18)),
        (datetime.now() + timedelta(days=10), datetime.now() + timedelta(days=22)),
    ]

START_DATE_HIGHER_THAN_END_DATE = [
        (datetime.now() + timedelta(days=9), datetime.now() + timedelta(days=5)),
        (datetime.now() + timedelta(days=29), datetime.now() + timedelta(days=22)),
        (datetime.now() + timedelta(days=5), datetime.now() + timedelta(days=0)),
        (datetime.now() + timedelta(days=32), datetime.now() + timedelta(days=28)),
    ]