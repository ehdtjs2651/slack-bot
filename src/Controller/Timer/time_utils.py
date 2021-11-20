from datetime import timedelta, datetime, timezone


def daterange(start_date: datetime, end_date: datetime):
    """
    1일씩 반복    
    :param start_date: 
    :param end_date: 
    :return: 
    """
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


time_zone_KST = timezone(timedelta(hours=9))
