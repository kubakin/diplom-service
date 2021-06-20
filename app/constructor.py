class Constructor:
    groupByString = ''
    selectFrom = '`clickhousehistory`'
    lastYear = 'date_add(year,-1, now())'
    lastMonth = "date_add(month,-1, now())"
    asName = []
    possibleSteps = {'year':'toYear(date)','month':'toMonth(date)','day':'toDayOfMonth(date)','hour':'toHour(date)'}

    def fromRangeOrTable(self,user, rangeBy="'1970-01-01'", rangeTo='now()'):
        self.selectFrom='`clickhousehistory`'
        if not rangeBy:
            return self.selectFrom
        else:
            self.selectFrom = "(select * from clickhousehistory where date between {} and {})".format(rangeBy, rangeTo, user)
            return self.selectFrom

    def stps(self,step='month'):
        self.groupByString = ''
        fields = ['count']
        self.asName = []
        for i in self.possibleSteps:
            if i != step:
                self.groupByString+='{} as {}'.format(self.possibleSteps[i], i)
                self.groupByString+=', '
                self.asName.append(i)
                fields.append(i)
            else:
                self.groupByString += '{} as {}'.format(self.possibleSteps[i], i)
                self.asName.append(i)
                fields.append(i)
                break
        return ['concat', 'count']
    def get_qs_concat(self):
        qs = ''
        for i in self.asName:
            qs+='toString({})'.format(i)
            if self.asName[len(self.asName)-1] == i:
                break
            qs+=",'-',"
        return "SELECT concat({}) as concat, count from ({}) ".format(qs, self.get_query(self))
    def get_query(self):
        return 'SELECT {0}, count() as count FROM {1} GROUP BY {0} order by {0}'.format(self.groupByString, self.selectFrom)