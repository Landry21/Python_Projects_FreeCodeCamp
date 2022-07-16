def past_days(days):
  if days ==1:
    return "(next day)"
  elif days>1:
    return f"({days} days later)"
  return ""


def add_time(start, duration, day = False):
  week_days =['monday', 'tuesday','wednesday', 'thursday','friday', 'saturday',
            'sunday']

  days_later = 0
  whole_day = 24
  half_day = 12
  #spliting everything individually. 
  hour= int(start.rpartition(':')[0])
  back=start.rpartition(":")[2]
  minutes=int(back.rpartition(' ')[0])
  dayPart=back.rpartition(" ")[2].strip().lower();
  hourofDuration=int(duration.rpartition(':')[0])
  minutesofDuration=int(duration.rpartition(":")[2])
  
  #adding the hours
  new_hour=int(hour)+int(hourofDuration)
  
  #addinf the minutes
  new_minute= int(minutes)+int(minutesofDuration)
  
  #handling over time
  if new_minute >= 60:
    new_hour += int(new_minute/60)
    new_minute = int(new_minute % 60) 
    
  if hourofDuration or minutesofDuration:
    if dayPart =="pm" and new_hour > half_day:
      if new_hour % whole_day>= 1.0:
        days_later+=1;
    if new_hour >=half_day:
      extraHours = new_hour/whole_day
      days_later += int(extraHours)

    #putting the clock back to 12 hours count
    while True:
      
      if new_hour < half_day:
        break
      else:
        if dayPart == "pm":
          dayPart = "am"
        elif dayPart == "am":
          dayPart = "pm"
          
        new_hour -= half_day
  remaining_hours = int(new_hour % half_day) or hour +1
  remaining_min = int(new_minute % 60)

  # shaping the results
  new_time = f'{remaining_hours}:{remaining_min:02} {dayPart.upper()}'
  #if days are included
  if day:
    day = day.lower()
    dayOfW = int((week_days.index(day) + days_later)%7)
    current = week_days[dayOfW]
    new_time +=f', {current.title()} {past_days(days_later)}'
  else:
    new_time = " ".join((new_time, past_days(days_later)))
  return new_time.strip()
