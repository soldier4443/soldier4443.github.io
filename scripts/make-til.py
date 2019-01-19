import os
import sys
import random
from datetime import datetime

def some_nice_greeting_for(name):
  nice_greetings = [
    "Happy coding, {}",
    "Have a geek day, {} :)",
    "Good job {}! Let's dominate the world!",
  ]
  return random.choice(nice_greetings).format(name)

owner = "tura"

dt = datetime.now()

connected_format = "%Y%m%d"
hyphen_format = "%Y-%m-%d"
readable_date = "{}년 {}월 {}일.".format(dt.year, dt.month, dt.day)

filename = "{}-til-{}.md".format(dt.strftime(hyphen_format), dt.strftime(connected_format))
content = """
---
title: TIL - {}
layout: post
tags: [til]
excerpt: none
---

{}
""".strip().format(dt.strftime(connected_format), readable_date)

# Make dir if not exists.
target_dir = "_posts/" + str(dt.year)

if not os.path.isdir(target_dir):
  try:
    os.mkdir(target_dir)
    print("New directory created: [{}]".format(target_dir))
  except:
    print("Something goes wrong while creating a new directory: [{}]".format(target_dir))
    sys.exit(1)

# Check if the file already exists.
# If the file exists, ask if overriding existing file.
target_filename = target_dir + '/' + filename

if os.path.isfile(target_filename):
  print("Target file already exists: [{}]".format(target_filename))
  print("Override existing file? (y,n): ")
  override = input()
  if override == 'y' or override == 'Y' or override == 'yes' or override == "":
    print("Override existing file.")
  else:
    print("Preserve existing file. Exit the program.")
    sys.exit(1)

# Write a template for TIL.
try:
  with open(target_filename, 'w', encoding='utf-8') as f:
    f.write(content)
    print("Today's TIL file is created at [{}].".format(target_filename))
    print(some_nice_greeting_for(owner))
except Exception as e:
  print(e)
  