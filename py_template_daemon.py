#!/usr/bin/python3
# Copyright 2022 fnwinter@gmail.com
"""
python template daemon
"""

import argparse
import json
import os
import sys
import daemon
import psutil
import setproctitle

from daemon import pidfile
SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))

DAEMON_LOCK_PATH = os.path.join(SCRIPT_PATH, "lock.pid")

def start_daemon():
  if os.path.exists(DAEMON_LOCK_PATH):
    sys.exit()
  try:
    with daemon.DaemonContext(
        working_directory=SCRIPT_PATH,
        pidfile=pidfile.TimeoutPIDLockFile(DAEMON_LOCK_PATH)) as context:
        import time
        while True:
          time.sleep(1)
  except Exception as daemon_error:
    print("ERROR"+str(daemon_error))

def stop_daemon():
  if not os.path.exists(DAEMON_LOCK_PATH):
    print("no running daemon")
    sys.exit()
  else:
    kill_running_process()

def kill_running_process():
  pass

def restart_daemon():
  stop_daemon()
  start_daemon()

def read_config():
  config_file_path = os.path.join(SCRIPT_PATH, "daemon_config.json")
  with open(config_file_path) as f:
    config = json.load(f)
    title = config.get('title')
    print(title)
    setproctitle.setproctitle(title)    

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Daemon')
  parser.add_argument('--start', action='store_true', help='start Daemon')
  parser.add_argument('--stop', action='store_true', help='stop Daemon')
  parser.add_argument('--restart', action='store_true', help='restart Daemon')

  read_config()

  args = parser.parse_args()
  try:
    if args.start:
      start_daemon()
    elif args.stop:
      stop_daemon()
    elif args.restart:
      restart_daemon()
    else:
      parser.print_help()
  except Exception as e:
    pass
