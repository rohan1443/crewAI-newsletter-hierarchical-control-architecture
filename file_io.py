from datetime import datetime

def save_markdown(task_output):
  # get todays date in the format YYYY-MM-DD
  todays_date = datetime.now().strftime('%Y-%m-%d')
  # set the filename with todays date
  filename = f"{todays_date}.md"
  # Write the task output to the markdown file
  with open(filename, 'w') as file:
    file.write(task_output.result)

  print(f"Newsletter saved as {filename}")
