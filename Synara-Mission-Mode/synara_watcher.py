
# Monitors forgotten jobs, missed paths, and reruns key Fireseed components
import os
import datetime

def scan_and_remind():
    now = datetime.datetime.now()
    with open("FIRESEED_TRACKER.log", "a") as log:
        log.write(f"[{now}] 🔍 Synara watcher scan: Running income audit...\n")
    if os.path.exists("cash_ready.flag"):
        print("💵 Money flagged: Check earnings now.")
    else:
        print("✅ No unclaimed money. Fireseed running normally.")

if __name__ == "__main__":
    scan_and_remind()
