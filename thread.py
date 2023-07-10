import threading
import subprocess

def open_notepad():
    subprocess.call("notepad.exe")

def open_paint():
    subprocess.call("mspaint.exe")

if __name__ == "__main__":
    # Create two threads for opening Notepad and Paint
    thread1 = threading.Thread(target=open_notepad)
    thread2 = threading.Thread(target=open_paint)

    # Start the threads
    thread1.start()
    thread2.start()

    # Wait for both threads to finish
    thread1.join()
    thread2.join()

    print("Applications opened successfully!")
