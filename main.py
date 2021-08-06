import json
from pprint import pprint
import os
import pathlib
from datetime import datetime
from constants import WEEKDAYS

# monday 0 sunday 6

parent_folder = pathlib.Path(__file__).parent.absolute()
config_filepath = os.path.join(parent_folder, 'config.json')

with open(config_filepath) as f:
  data = json.load(f)

now = datetime.now()
today = now.weekday()
weekday = WEEKDAYS[today]

pprint(weekday)

times_from_today = data[weekday]
current_time = now.time()

pprint(current_time.hour)
print('>>>>>')


pprint(times_from_today)
for time in times_from_today:
  current_time_string = f'{current_time.hour}:{current_time.minute}'
  current_hours_and_minutes = datetime.strptime(current_time_string, '%H:%M')

  start_string = time['start']
  start_time = datetime.strptime(start_string, '%H:%M')

  end_string = time['end']
  end = datetime.strptime(end_string, '%H:%M')

  time_started = current_hours_and_minutes >= start_time
  time_in_progress = current_hours_and_minutes <= end

  if time_started and time_in_progress:
    print('helllllo')



  [start_hour, start_minute] = map(int, time['start'].split(':'))
  [end_hour, end_minute] = map(int, time['end'].split(':'))






# for time in times_from_today:
if (data['relative']):
  output_filepath = os.path.join(parent_folder, data['output_filepath'])
else:
  output_filepath = data['output_filepath']


os.system(f"gnome-screenshot -w -f {output_filepath}")