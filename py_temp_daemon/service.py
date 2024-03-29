#!/usr/bin/python3
# Copyright 2022 fnwinter@gmail.com
"""
python template daemon
"""

import argparse
import daemon
import json
import os
import psutil
import setproctitle
import sys

from daemon import pidfile

SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))
LOCK_PATH = os.path.join(SCRIPT_PATH, "lock.pid")
sys.path.append(SCRIPT_PATH)

from entry import entry_function

def start_daemon():
  if os.path.exists(LOCK_PATH):
    print("there is already running daemon")
    sys.exit()
  try:
    with daemon.DaemonContext(
        working_directory=SCRIPT_PATH,
        pidfile=pidfile.TimeoutPIDLockFile(LOCK_PATH)) as context:
      entry_function()
  except Exception as e:
    print(e)

def stop_daemon():
  if not os.path.exists(LOCK_PATH):
    print("no running daemon")
    sys.exit()
  else:
    kill_running_process()
    os.remove(LOCK_PATH)

def kill_running_process():
  try:
    with open(LOCK_PATH) as f:
      pid = f.readline().strip()
      print(f"process {pid} killed")
      process = psutil.Process(int(pid))
      process.kill()
  except Exception as e:
    print(e)

def restart_daemon():
  stop_daemon()
  start_daemon()

def read_config():
  config_file_path = os.path.join(SCRIPT_PATH, "config.json")
  with open(config_file_path) as f:
    config = json.load(f)

    # change process title
    title_ = config.get('title')
    setproctitle.setproctitle(title_)
    version_ = config.get('version')
    print(f"service title   : {title_}")
    print(f"service version : {version_}")

def main():
  parser = argparse.ArgumentParser(description='Python Template Daemon')
  parser.add_argument('--start', action='store_true', help='start daemon')
  parser.add_argument('--stop', action='store_true', help='stop daemon')
  parser.add_argument('--restart', action='store_true', help='restart daemon')

  args = parser.parse_args()
  try:
    if args.start:
      read_config()
      start_daemon()
    elif args.stop:
      stop_daemon()
    elif args.restart:
      restart_daemon()
    else:
      parser.print_help()
  except Exception as e:
    print(e)

if __name__ == '__main__':
  main()
