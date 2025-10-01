import csv
#opening and reading printing files
# file = open('joke.txt','r')
# content = file.read()
# print(content)
# file.close()

# Dealing with Each line of text in a file
#With - key workd that opens and closes a file automatically
# with open('joke.txt','r') as file:
#     lines = file.readlines()
#     for line in lines:
#         print(line.strip())

#Writing to a file
# overwrites what already there in fule
# with open('joke.txt','w') as file:
#     file.write('What did the .... ummm ...ummmmmm ....ummmm,\n')

#appending aline to file
# addtional_lines = ['What did the ????\n', 'knock knock.......\n']
#
# with open('joke.txt','a') as file:
#     file.write('What did the .... ummm ...ummmmmm ....ummmm,\n')
#     file.writelines(addtional_lines)

#reading date to csv files
# with open('joke.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     for row in csv_reader:
#         print(f' joke:  {row[0]} comment: {row[1]}')


# #writing date to csv files
# addtional_rows = [[ 'joke1','you\'re getting lazy'],
#                   [ 'joke2','you\'re getting really lazy'],
#                   [ 'joke3','you\'re getting really really lazy']]
#
# with open('joke.csv', 'a', newline='') as csv_file:
#      csv_writer = csv.writer(csv_file)
#      csv_writer.writerow(['joke','comments'])
#      csv_writer.writerows(addtional_rows)

modified_dad_jokes = []
def grade(score):
    rating= int(score)
    if rating > 8:
        catagory = "pretty good"
    elif rating <= 8:
        catagory = "horrible"
    else:
        catagory = "stop talking"
    return catagory
        

with open('joke.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)

    header = next(csv_reader)
    header.append('grade')
    modified_dad_jokes.append(header)

    for row in csv_reader:
      row.append(grade(row[2]))
      modified_dad_jokes.append(row)

with open('joke_modified.csv','w',newline='') as new_csv:
    csv_writer = csv.writer(new_csv)
    csv_writer.writerows(modified_dad_jokes)






