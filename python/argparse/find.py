





import argparse
import os


def do_find(location, name):
    # print name
    items = [location]
    result = []
    while items:
        d = items.pop()
        # print d
        dlist = os.listdir(d)
        # print dlist
        for dent in dlist:
            full_name = "{}/{}".format(d, dent)
            full_name = os.path.join(d, dent)
            # print full_name
            if os.path.isfile(full_name) and os.path.basename(full_name) == name:
                result.append(full_name)
            elif os.path.isdir(full_name):
                items.append(full_name)
    return result

        

def find():
    parser = argparse.ArgumentParser()
    parser.add_argument("directory", action="store")
    parser.add_argument("name", action="store")
    parser.add_argument("--type", action="store", dest="type")

    args = parser.parse_args()

    print "\n".join(do_find(args.directory, args.name))





if __name__ == '__main__':
    find()