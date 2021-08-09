import json
import os
import pathlib
from datetime import datetime
from constants import WEEKDAYS

parent_folder = pathlib.Path(__file__).parent.absolute()
config_filepath = os.path.join(parent_folder, 'config.json')

with open(config_filepath) as f:
  data = json.load(f)

now = datetime.now()
weekday = WEEKDAYS[now.weekday()]

times_from_today = data[weekday]
current_time = now.time()

folder_found = False

for time in times_from_today:
  current_time_string = f'{current_time.hour}:{current_time.minute}'
  current_hours_and_minutes = datetime.strptime(current_time_string, '%H:%M')

  start_string = time['start']
  start_time = datetime.strptime(start_string, '%H:%M')

  end_string = time['end']
  end_time = datetime.strptime(end_string, '%H:%M')

  time_started = current_hours_and_minutes >= start_time
  time_in_progress = current_hours_and_minutes <= end_time

  if time_started and time_in_progress:
    folder_found = True

    filename = now.strftime('%H:%M:%S %d-%m-%Y') + '.png'
    
    output_dir = pathlib.Path(time['folder'])

    if not os.path.exists(output_dir):
      os.makedirs(output_dir)
    
    output_filepath = os.path.join(output_dir, filename)

    os.system(f"gnome-screenshot -w -f '{output_filepath}'")

if not folder_found:
  filename = 'S ' + now.strftime('%H:%M:%S %d-%m-%Y') + '.png'
    
  output_dir = pathlib.Path(data['default_folder'])

  if not os.path.exists(output_dir):
    os.makedirs(output_dir)
  
  output_filepath = os.path.join(output_dir, filename)

  os.system(f"gnome-screenshot -w -f '{output_filepath}'")
