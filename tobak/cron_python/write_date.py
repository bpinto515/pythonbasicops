import datetime
with open('date_info.txt', 'a') as a out_file:
    out_file.write('\n' + str(datetime.datetime.now()))
