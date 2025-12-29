from datetime import datetime


class DeliveryLog:
    def __init__(self, trip_id):
        self.trip_id = trip_id
        self.entries = []   # list of dict log records

    def add_entry(self, action, user="System"):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        record = {
            "time": timestamp,
            "user": user,
            "action": action
        }
        self.entries.append(record)
        print(f"[LOG] {action} ({timestamp})")

    def display_log(self):
        print("\n===== DELIVERY LOG =====")
        if not self.entries:
            print("No log records yet.")
            return

        for entry in self.entries:
            print(f"{entry['time']} | {entry['user']} | {entry['action']}")

    def summarize_actions(self):
        print("\n===== LOG SUMMARY =====")
        print(f"Total Recorded Actions: {len(self.entries)}")

    def get_latest_action(self):
        return self.entries[-1]["action"] if self.entries else None
