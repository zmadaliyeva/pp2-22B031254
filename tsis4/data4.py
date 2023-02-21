from datetime import datetime, time

def date_diff_in_Seconds(dt2, dt1):
  timedelta = dt2 - dt1

date1 = datetime.strptime('2023-02-16 01:00:00', '%Y-%m-%d %H:%M:%S')

date2 = datetime.now()
print("\n%d seconds" %(date_diff_in_Seconds(date2, date1)))
print()

"""
import datetime

d=int(input('Enter how many days difference: '))

dt1=datetime.datetime.today().replace(microsecond=0)
dt2=dt1-datetime.timedelta(d)

sum=dt1-dt2

a=sum.total_seconds()

print(f'Difference in seconds: {a}')
print(f'Current date is {dt1}'), 

"""