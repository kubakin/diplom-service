import datetime
def fromRangeOrTable(rangeBy, rangeTo=datetime.datetime.now()):
    if not rangeBy:
        return '`clickhousehistory`'
