from friendsbalt.acs import OrderedMap, StringDiff
from datetime import datetime


class VersionedFile:   
    
    def __init__(self, file_path):
        self.file_path = file_path
        self.versions = OrderedMap()
        file_string = self.read_from_file()
        initial_diff = StringDiff("", file_string)
        timestamp = int(round(curr_dt.timestamp()))
        curr_dt = datetime.now()
        self.versions[timestamp] = initial_diff
        return timestamp
    
    def read_from_file(self):
        with open(self.file_path, "r") as file:
                content = file.read()
                return (content)


    def save(self):
       
        #read the file from disk
        # compute lastest version of file from version_map
        # compute the diff between 1 & 2
        # lastly add that diff into 
        previous_version = self.build_lastest()
        current_version = self.read_from_file()    
    
    def build_lastest(self):
        #starting from th empty string, successirley apply diffs in version map
        #return the result
        current = ""
        for _, diff in self.versions:
            StringDiff.apply_diff(current, diff)
        
        return current   
    
x = VersionedFile("example.txt")
print(x.read_from_file())