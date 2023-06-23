def add_time(start, duration, initial_day=False):
  initial_time = start.split(" ")
  time_duration = duration.split(":")

  initial_hours = initial_time[0].split(":")[0]
  duration_hours = time_duration[0]
  new_hours = int(initial_hours) + int(duration_hours)

  initial_minutes = initial_time[0].split(":")[1]
  duration_minutes = time_duration[1]
  new_minutes = int(initial_minutes) + int(duration_minutes)

  initial_turn = initial_time[1].upper()
  turn = " "
  time = " "

  if initial_day == str(initial_day):
    initial_day = initial_day.lower()
    initial_day = initial_day.capitalize()

  weekdays = [
    "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",
    "Sunday"
  ]
  next_days = ["next day", "days later"]
  next_day = 0
  days = 0

  for day in weekdays:
    if initial_day == False: break
    elif day == initial_day: break
    else: days += 1

  if new_minutes > 59:
    new_minutes -= 60
    new_hours += 1

  if new_minutes < 10: new_minutes = f"0{str(new_minutes)}"

  if initial_turn == "PM": new_hours += 12

  while new_hours > 23:
    new_hours -= 24
    days += 1
    if days > 6: days = 0
    next_day += 1

  if new_hours < 1:
    new_hours += 12
    turn = "AM"
  elif new_hours == 12:
    turn = "PM"
  elif new_hours > 12 and new_hours < 24:
    new_hours -= 12
    turn = "PM"
  elif new_hours > 0 and new_hours < 12:
    turn = "AM"

  if next_day > 1: after_days = f"({str(next_day)} {next_days[1]})"
  elif next_day == 1: after_days = f"({next_days[0]})"

  time = f"{str(new_hours)}:{new_minutes} {turn}"

  if initial_day == False and next_day == 0: 
    new_time = time
  elif initial_day == False and next_day != 0:
    new_time = f"{time} {after_days}"
  elif initial_day != False and next_day == 0:
    new_time = f"{time}, {weekdays[days]}"
  else:
    new_time = f"{time}, {weekdays[days]} {after_days}"

  return new_time
