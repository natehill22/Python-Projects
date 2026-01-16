from datetime import datetime, time
from zoneinfo import ZoneInfo

#Setting the timezone info/variables for the three zones being used
tz_la = ZoneInfo("America/Los_Angeles")
tz_ny = ZoneInfo("America/New_York")
tz_london = ZoneInfo("Europe/London")

#Setting a list of locations of new branches
locations = ["Portland HQ:", "New York Location:", "London (UK) Location:"]

#Running through the list of locations
for loc in locations:
    location = loc #Setting the location variable to use the list value through each iteration 
    if loc == "Portland HQ:": #Setting timezone configuration to match each location
        current_datetime = datetime.now(tz=tz_la)
    elif loc == "New York Location:":
        current_datetime = datetime.now(tz=tz_ny)
    else:
        current_datetime = datetime.now(tz=tz_london)
    #Setting a variable to show a formatted version of the date and time for each location
    formattedDate = current_datetime.strftime("%A, %d %B %Y %I:%M:%S%p")

    def operatingHours():
        current_time = current_datetime.time() #Finds a time-only value of the previously-set datetime
        start_time = time(9, 0)
        end_time = time(17, 0)
        if start_time <= current_time and current_time <= end_time: 
            print("Open") #If the local time is between 9AM and 5PM, print "Open"
        else:
            print("Closed") #Otherwise print "Closed"


    print("{} {}".format(location, formattedDate)) #Calls the location and formatted date (on one string) for each location
    operatingHours() #Shows the result of the function (Open or Closed status)
