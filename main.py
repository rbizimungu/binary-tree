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

class Filesystem:
    
    def time(timestamp):
        curr_dt = datetime.now()
        timestamp = int(round(curr_dt.timestamp()))
        return timestamp

    



# key: timestamp
# value: VersionNode -> diff (first diff is orginal, second is the modified) 
# *you can js take empty string and repeat its diff's inside the ordered map
# while true: input("select?") *create input names
#save_version()  input()   save_version()   input()    show_log()