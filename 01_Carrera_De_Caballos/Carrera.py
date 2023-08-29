import threading
import time

# Shared resource: Watering trough
watering_trough = 5  # Initial water level

# Function representing a horse's behavior
def horse_behavior(horse_id):
    global watering_trough

    # Horses access the watering trough
    for _ in range(3):
        time.sleep(0.5)  # Simulate some horse behavior
        print(f"Horse {horse_id} is approaching the watering trough.")

        # Simulating a race condition (data race)
        current_water_level = watering_trough
        time.sleep(0.2)  # Simulate another horse's behavior
        watering_trough = current_water_level - 1

        print(f"Horse {horse_id} drank from the watering trough. Water level: {watering_trough}")

# Create threads for each horse
threads = []
for i in range(4):
    horse_thread = threading.Thread(target=horse_behavior, args=(i,))
    threads.append(horse_thread)
    horse_thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

print("Race is over.")