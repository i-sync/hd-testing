"""
The market matrix excel utils
Get some footer links data from excel file. "MY19R_Social_footer_link.xlsx"
Get bike data from excel file. "MY19_FXDR_Market_Matrix.xlsx"
"""

__author__ = "Libby.Qin"

import openpyxl

__matrix_file_name__ = "proj04_touringdemo/data/MY19R_Social_footer_link.xlsx"
__matrix_bike_file_name__ = "proj04_touringdemo/data/MY19_FXDR_Market_Matrix.xlsx"

def get_social_footer_matrix():
    """
    Get all soical footer link matrix
    locale column B
    Facebook Url column F
    Instagram Url column E
    Twitter Url column D
    please ignore Youtube
    :return:
    """
    wb = openpyxl.load_workbook(__matrix_file_name__)
    sheet = wb["Overview"]
    res = {}
    for index in range(2, 44):
        locale = sheet["B{}".format(index)].value
        facebook = sheet["F{}".format(index)].value
        instagram = sheet["E{}".format(index)].value
        twitter = sheet["D{}".format(index)].value
        res[locale] = [facebook, instagram, twitter]

    wb.close()
    return res

def get_bike_matrix():
    """
    Get All bike info matrix
    :return:
    """
    wb = openpyxl.load_workbook(__matrix_bike_file_name__)
    sheet = wb["Overview"]
    bike_column =["L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "AA" , "AB", "AC", "AD", "AE", "AF", "AG", "AH", "AI", "AJ", "AK", "AL"]
    bike_code = {}
    for col in bike_column:
        id = sheet["{}1".format(col)].value
        bike_code[col]= id

    res = {}
    for index in range(5, 47):
        locale = sheet["E{}".format(index)].value
        res[locale] = []
        for col in bike_column:
            cc = sheet["{}{}".format(col, index)].value
            if cc and  not cc.startswith("No"):
                res[locale].append(bike_code[col])

    wb.close()
    return res