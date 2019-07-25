"""
The market matrix excel utils
Get some matrix data from excel file. "MY20-RYI-Matrix-V3.1.xlsx"
"""

__author__ = "Michael.Tian"

import openpyxl

__matrix_file_name__ = "proj12_ryi/data/MY20-RYI-Matrix-V3.1.xlsx"

def get_social_matrix():
    """
    Get all soical link matrix
    locale column B
    Facebook Url column U
    Instagram Url column V
    Twitter Url column W
    :return:
    """
    wb = openpyxl.load_workbook(__matrix_file_name__)
    sheet = wb["Overview"]
    res = {}
    for index in range(2, 35):
        locale = sheet["B{}".format(index)].value.split()[0]
        facebook = sheet["U{}".format(index)].value
        instagram = sheet["V{}".format(index)].value
        twitter = sheet["W{}".format(index)].value
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
    bike_column =["J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T"]
    bike_code = {}
    for col in bike_column:
        id = sheet["{}1".format(col)].value
        bike_code[col]= id

    res = {}
    for index in range(2, 35):
        locale = sheet["B{}".format(index)].value.split()[0]
        res[locale] = []
        for col in bike_column:
            cc = sheet["{}{}".format(col, index)].value
            if cc and  not cc.startswith("N"):
                res[locale].append(bike_code[col])

    wb.close()
    return res