from  docx2csv import extract

#Путь подается в ковычках  'path'
#создает файлы xls, csv  по одному на таблицу

def ft_docx_to_csv_xls_converteer(path_to_docx):
        extract(filename=path_to_docx, format="csv",singlefile=False)
        extract(filename=path_to_docx, format="xls",singlefile=False)



