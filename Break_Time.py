import webbrowser
import time

total_breaks = 3
break_count = 0

print("This program started on"+ time.ctime())
for break_count in range(total_breaks):
    time.sleep(10)
    webbrowser.open("http://www.youtube.com/watch?v=dQw4w9WgXcQ")
