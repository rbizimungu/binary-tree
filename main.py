from friendsbalt.acs import OrderedMap, StringDiff, AVLTree
from datetime import datetime
# make a version control system
# - store the version history
#     a. save function  
# - do previous for multiple files
# - restore any previous versions
#     a. restore func
# - show a time log og any file
# - built in function on time class, how many secons time stamp


x = OrderedMap()
orderedMap = ""
a = "Hello\nWorld"
b = "Hello\nWorld!"
c = "Hello\nWorld!!"
d = "Hello\nWorld!!!"
diff1 = StringDiff(a, b)
diff2 = StringDiff(b, c)
diff3 = StringDiff(c, d)
print(StringDiff.raw_diff(a,b))

class Filesystem:
    
    def time(timestamp):
        curr_dt = datetime.now()
        timestamp = int(round(curr_dt.timestamp()))
        versions = {diff1: "version1", diff2: "version2", diff3: "version3"}
        return timestamp

    def save(timestamp, versions, diff1, diff2, diff3):
        om = OrderedMap
        om.append(versions)
        while True:
            input("diff1")
            if input == "save":
                om.append(diff1)
            elif input == "restore":
                om.append(diff2)
            elif input == "show_log":
                print(om)
            else:
                print("invalid input")

        


# key: timestamp
# value: VersionNode -> diff (first diff is orginal, second is the modified) 
# *you can js take empty string and repeat its diff's inside the ordered map
# while true: input("select?") *create input names
#save_version()  input()   save_version()   input()    show_log()