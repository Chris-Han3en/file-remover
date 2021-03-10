import os, sys

for r, d, f in os.walk("D:\\"):  # what drive it searches
            for files in f:
                if files == "test.txt":  # file it is looking for, you also need the file extension e.g. exe or .txt
                    location = os.path.join(r, files)  # finds the location of the file
                    print(location)  # prints the location (mostly for dev purposes)
                    if os.path.exists(location):
                        os.remove(location)  # removes the file
