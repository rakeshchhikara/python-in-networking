###################################################################
# This code will read csv file and print row by row.
###################################################################

# import csv
#
# with open('airtravel.csv') as f:
#     reader = csv.reader(f)
#
#     for row in reader:
#         print(row)




###################################################################
# This code will read csv and print output in a list. Each row will be printed as child list inside main list.
##################################################################

# import csv
#
# my_list = []
# with open('airtravel.csv') as f:
#     reader = csv.reader(f)
#
#     for content in reader:
#         my_list.append(content)
#
# print(my_list)


###################################################################
# This code will print Second Column from csv file
###################################################################


# import csv
#
# with open('airtravel.csv') as f:
#     reader = csv.reader(f)
#     #next(reader)                    # Use next function if you want to remove Header of row
#
#     for row in reader:
#         print(row[1])



###################################################################
#
###################################################################



###################################################################
# This code will read csv file and create dictionary. First column entries will be Keys and Second column will be
# respective value.
###################################################################


# import csv
#
# with open('airtravel.csv') as f:
#     reader = csv.reader(f)
#     next(reader)                    # Use next function if you want to remove Header of row
#     year_1958 = dict()
#
#     for row in reader:
#         year_1958[row[0]] = row[1]
#
#     print(year_1958)



###################################################################
#
###################################################################



# import csv
#
# with open('airtravel.csv') as f:
#     reader = csv.reader(f)
#     next(reader)                    # Use next function if you want to remove Header of row
#     year_1958 = dict()
#
#     for row in reader:
#         year_1958[row[0]] = row[1]
#
#     #print(year_1958)
#
#     max_1958 = max(year_1958.values())
#     print(max_1958)


###################################################################
#
###################################################################



# import csv
#
# with open('airtravel.csv') as f:
#     reader = csv.reader(f)
#     next(reader)                    # Use next function if you want to remove Header of row
#     year_1958 = dict()
#
#     for row in reader:
#        year_1958[row[0]] = row[1]
#
#     max_1958 = max(year_1958.values())
#     #print(year_1958.items())
#     #exit(1)
#
#     for k, v in year_1958.items():
#         if max_1958 == v:
#             print(f'Busiest Month in 1958:{k} with Flights:{v.strip()}')


###################################################################
#
###################################################################


# import csv
#
# with open('student_data.csv') as f:
#     reader = csv.reader(f)
#     next(reader)
#
#     student_list = list()
#     for student in reader:
#         student_list.append(student)
#     print(student_list)
