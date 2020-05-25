import csv
import json
import sys
import xlwt


def conversiontocsv(fileOutput):
    print(fileOutput)
    with open(fileOutput[0], "r") as f, open(fileOutput[1], "w") as outputfile:
        output = csv.writer(outputfile)
        try:
            count = 0
            for line in f:
                # file_is_empty = os.stat("/home/rijoos/Desktop/pythontask/food2.csv").st_size == 0
                data = json.loads(line)
                # if file_is_empty:
                if count == 0:
                    output.writerow(data.keys())
                    count += 1
                output.writerow(data.values())
        except:
            print("Invalid Json format")


def conversiontojson(fileOutput):
    # jsonfile= open("/home/rijoos/Desktop/pythontask/food3.json", "a")
    print(fileOutput)
    with open(fileOutput[0], "r") as inputfile, open(fileOutput[1], "w") as outputfile:
        output = csv.DictReader(inputfile)
        for line in output:
            json.dump(line, outputfile)
            outputfile.write('\n')


def conversiontoxlsx(fileOutput):
    file_name = sys.argv[1]
    workbook = xlwt.Workbook(encoding="utf-8")
    worksheet = workbook.add_sheet('json exported', cell_overwrite_ok=False)
    outputfile = open(fileOutput[0], "r")
    count = 0
    j = 1
    try:
        for line in outputfile:
            data = json.loads(line)
            columns = data.keys()
            numlist = []
            i = 0
            for key, column in enumerate(columns):
                numlist.append(key)
                if count == 0:
                    worksheet.write(0, i, column)
                    i += 1
            count += 1
            values = data.values()

            column_count = 0
            for value in values:
                if isinstance(value, dict):
                    value = str(value)
                print(j,column_count)
                worksheet.write(j, column_count, value)
                column_count += 1
            j+=1
            try:
                workbook.save(file_name.split('.')[0] + '.xls')
            except:
                print("Can't write the xls file")
    except Exception as e:
        print(e)


if __name__ == '__main__':
    fileInputType = sys.argv[1:]
    length = len(fileInputType)
    print(fileInputType)
    if length != 3:
        print("check the command line arguments")
    elif fileInputType[2] == 'json':
        conversiontocsv(fileOutput=sys.argv[1:])
    elif fileInputType[2] == 'csv':
        conversiontojson(fileOutput=sys.argv[1:])
    elif fileInputType[2] == 'xlsx':
        conversiontoxlsx(fileOutput=sys.argv[1:])

        # ss
