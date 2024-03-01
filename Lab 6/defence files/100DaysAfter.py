from datetime import datetime, timedelta
today = datetime.now()

finishing_date = today + timedelta(days=100)

print("100 Days after today is: " + finishing_date.strftime("%a"))