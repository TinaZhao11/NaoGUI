def get_line(filepath):
    fo = open(filepath, "r")
    time = []
    timeline = []
    count = 1
    for line in fo:
        time.append(line)
    for line in time:
        if(count > len(time) -1 ):
            break
        else:
            nextline = time[count]
            eachtime = float(nextline) - float(line)
            timeline.append(eachtime)
            count = count + 1


if __name__ == "__main__":
   get_line("out.csv")

