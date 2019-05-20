"""
The market matrix excel utils
Get some matrix data from excel file. "SpringDemo-MarketMatrix-20190517.xlsx"
"""

__author__ = "Michael.Tian"

import openpyxl

__matrix_file_name__ = "proj02_springdemo/data/SpringDemo-MarketMatrix-20190517.xlsx"

def get_social_matrix():
    """
    Get all soical link matrix
    locale column E
    Facebook Url column AN
    Instagram Url column AO
    Twitter Url column AP
    :return:
    """
    wb = openpyxl.load_workbook(__matrix_file_name__)
    sheet = wb["Overview"]
    res = {}
    for index in range(5, 47):
        locale = sheet["E{}".format(index)].value
        facebook = sheet["AN{}".format(index)].value
        instagram = sheet["AO{}".format(index)].value
        twitter = sheet["AP{}".format(index)].value
        res[locale] = [facebook, instagram, twitter]

    wb.close()
    return res

def get_bike_matrix():
    """
    Get All bike info matrix
    :return:
    """
    wb = openpyxl.load_workbook(__matrix_file_name__)
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