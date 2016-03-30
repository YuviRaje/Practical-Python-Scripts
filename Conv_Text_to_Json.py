###	Quick Python Script to convert the Big List of Naughty Strings into a JSON file


import json

with open('../random.txt', 'r') as f:

    # put all lines in the file into a Python list
    filelist = f.readlines()
    
    # above line leaves trailing newline characters; strip them out
    filelist = [x.strip('\n') for x in filelist]
    
    # remove empty-lines and comments
    filelist = [x for x in filelist if x and not x.startswith('#')]
    
    # insert empty string since all are being removed
    filelist.insert(0, "")
    
    # special case: convert "\" to "\\" for valid JSON
    #filelist = map(lambda x: x.replace('\','\\'), filelist)
    
with open('../random.json', 'wb') as f:

	# write JSON to file; note the ensure_ascii parameter
	json.dump(filelist, f, indent=2, ensure_ascii=False)
    