"""
The market matrix excel utils
Get some matrix data from excel file. "BOTK2019-MarketMatrix-20181212.xlsx"
"""

__author__ = "Michael.Tian"

import openpyxl

__matrix_file_name__ = "proj01_botk/data/BOTK2019-MarketMatrix-20181212.xlsx"

def get_social_matrix():
    """
    Get all soical link matrix
    locale column D
    Facebook Url column V
    Instagram Url column W
    Twitter Url column X
    :return:
    """
    wb = openpyxl.load_workbook(__matrix_file_name__)
    sheet = wb["BOTK"]
    res = {}
    for index in range(3, 43):
        locale = sheet["D{}".format(index)].value
        facebook = sheet["V{}".format(index)].value
        instagram = sheet["W{}".format(index)].value
        twitter = sheet["X{}".format(index)].value
        res[locale] = [link for link in [facebook, instagram, twitter] if link]

    wb.close()
    return res