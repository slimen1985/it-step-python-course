import csv


csv.register_dialect('my_dialect', delimiter='~', lineterminator="\r")
with open("data/classmates.csv", mode="w") as file:
    file_writer = csv.writer(file, 'my_dialect')
    file_writer.writerow(["Name", "Class", "Age"])
    file_writer.writerow(["Nick", "3", 10])
    file_writer.writerow(["Mick", "5", 12])
    file_writer.writerow(["Helen", "11", 18])
