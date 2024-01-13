import time
import subprocess
import pyautogui

def open_notepad():
    subprocess.Popen(["notepad.exe"])

def hit_space_bar_every_10_seconds(total_duration_hours):
    total_duration_seconds = total_duration_hours * 3600  # Convert hours to secondsD
    start_time = time.time()

    while time.time() - start_time < total_duration_seconds:
        
        time.sleep(10)  # Wait for the specified delay in seconds
        pyautogui.press('D')  # Simulate pressing the space bar using pyautoguiD


    
if __name__ == "__main__":
    open_notepad()   
    duration_hours = 1  # Set the duration in hours
    print(f"Pressing space bar in Notepad every 10 seconds for {duration_hours} hour(s)...")
    hit_space_bar_every_10_seconds(duration_hours)
    print(f"Space bar pressed for {duration_hours} hour in Notepad!")
