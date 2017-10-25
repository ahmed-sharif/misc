



filename = "/etc/passwd"
filename = "/Users/asharif/new_empty"

with open(filename) as fd:
    has_content = len(list(fd))
    if has_content:
        print filename, " is not empty"
    else:
        print filename, " is empty"
        

