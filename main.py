from datetime import datetime

moscow_date = "Wednesday, October 2, 2002"
moscow_datetime = datetime.strptime(moscow_date, "%A, %B %d, %Y")
print('The Moscow Times', moscow_datetime)

guardian_date = "Friday, 11.10.13"
guardian_datetime = datetime.strptime(guardian_date, "%A, %d.%m.%y")
print('The Guardian', guardian_datetime)

daily_date = "Thursday, 18 August 1977"
daily_datetime = datetime.strptime(daily_date, "%A, %d %B %Y")
print('Daily News', daily_datetime)

