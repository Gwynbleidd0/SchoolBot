import requests
import xlrd
import fille
import os.path
def get_timetable():
    import fille
    dirfile = 'https://s11028.edu35.ru/attachments/article/224/'
    file_name_list = fille.get_name_file()
    print(file_name_list)
    count_var=len(file_name_list)
    t1=False
    g=0
    while g<count_var:
        fille = file_name_list[g]
        r = requests.get(dirfile+fille)
        if r.ok==True:
            with open(fille, "wb") as code:
                code.write(r.content)
                t1=True
                break
        g=g+1
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



