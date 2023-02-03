with open('data/data.csv') as file:
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

print(read_csv())