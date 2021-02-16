

import os
for i in range(7,101):
    os.mkdir(f"Day {i}")
    
for i in range(7,101):
    os.chdir(rf"C:\Users\bhautik\Desktop\100daysofpython\Day {i}")
    # os.remove(f"Day{i}")
    f = open(f"Day{i}.py","w+")
    f.write(f"#This is Day {i} File")
    f.close()
