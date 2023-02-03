import csv


quoting = csv.QUOTE_ALL


with open('data/data.csv', "w") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=['fname', 'lname', 'age'],
        quoting=quoting
    )
    writer.writeheader()
    writer.writerow(
        {
            "fname": "vadim",
            "lname": "liubin",
            "age": 37
        }
    )
    writer.writerow(
        {
            "fname": "elena",
            "lname": "liubina",
            "age": 38
        }
    )

with open('data.csv') as file:
    c = file.readline().strip().split(',')
    d = [line.strip().split(',') for line in file]


    def read_csv():
        f = {}
        p = []
        for i in range(len(d)):
            for j in range(len(d[i])):
                f.update({c[j]: d[i][j]})
            p.append(f)
            f = {}
        return p