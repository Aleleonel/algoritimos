import json

filename = "data.txt"

dict1 = {}

fields = ['Prestador', 'Nome', 'Endereco', 'CEP', 'Cidade', 'Telefone1', 'Telefone2']


with open(filename) as fh:
    l = 1

    for line in fh:

        description = list(line.strip().split(",", 7))

        print(description)

        sno = 'Cod - '+str(l)

        i = 0

        dict2 = {}
        while i < len(fields):

            dict2[fields[i]] = description[i]
            i = i + 1
        dict1[sno]= dict2
        l = l + 1

out_file = open("test2.json", "w")
json.dump(dict1, out_file, indent=4)
out_file.close()