def excel_column_name_to_number(column_title):
    sum = 0
    x = len(column_title)-1
    for i in column_title:
        sum += (ord(i)-64)*(26**x)
        x += -1
    return sum