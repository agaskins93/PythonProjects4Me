import PyPDF2
import sys
import os

with open('dummy.pdf', 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    writer = PyPDF2.PdfFileWriter()
    print(reader.numPages)
    page = reader.getPage(0)

    with open('twopage.pdf', 'rb') as file2:
        reader2 = PyPDF2.PdfFileReader(file2)


        for re in reader2.pages:
            print(re)
            page.mergePage(re)

    page.rotateCounterClockwise(90)
    writer.addPage(page)
    with open('tilt.pdf', 'wb') as new_file:
        writer.write(new_file)

#take in file path of current directory
def combinepdfs(filelist):
    merge = PyPDF2.PdfFileMerger()
    for fi in filelist:
        merge.append(fi)
    merge.write("merge.pdf")












# take all the files and put them in list

#combine them and print to current directory


combinepdfs(['dummy.pdf','twopage.pdf', 'wtr.pdf'])
