import requests
import xlrd
import fille
import os
def get_timetable():
    import fille
    dirfile = 'https://s11028.edu35.ru/attachments/article/224/'
    file_name_list = fille.get_name_file()
    count_var=len(file_name_list)
    t1=False
    g=0
    while g<count_var:
        fille = file_name_list[g]
        r = requests.get(dirfile+fille)
        if r.ok==True:
            files = [f for f in os.listdir('.') if f.endswith('.xls')]
            print(files)
            os.remove(files[0])
            with open(fille, "wb") as code:
                code.write(r.content)
                t1=True
                break
        g=g+1
    if t1==False:
        return(t1,fille)
    if t1==True:
        return(t1,fille)
def get_book(fille):
    rb =xlrd.open_workbook(fille)
    sheet = rb.sheet_by_index(0)
    #val = sheet.row_values(6)[85]
    print(sheet.ncols)
    print(sheet.nrows)

    i=0
    while i<sheet.ncols:
        if sheet.row_values(2)[i] == '11а':
            rownum = i

            break
        i=i+1
    print(rownum)
    f=3
    result=[]
    while f<sheet.nrows:
        if sheet.row_values(f)[rownum]!='':
            result.append(sheet.row_values(f)[rownum])
        else:
            break;
        f=f+2
    print(result)
    lessons=len(result)
    print(lessons)
    result_string=''
    s=0
    while s<lessons:
        result_string=result_string+result[s]+'\n'
        s=s+1
    return(result_string)
#print(get_timetable()[0])
#print(os.listdir(path="."))
def get_lastfille():
    files = [f for f in os.listdir('.') if f.endswith('.xls')]
    fille=files[0]
    return(fille)

"""
print(os.path.getmtime(files[0]))
i=0
while i<len(files):    
    os.path.getmtime(files[i])
    i=i+1"""

