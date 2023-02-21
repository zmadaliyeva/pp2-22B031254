from datetime import timedelta, datetime

now = datetime.now()
print(now)
five_days = timedelta(5)
past_five_days = now - five_days
print(past_five_days)
