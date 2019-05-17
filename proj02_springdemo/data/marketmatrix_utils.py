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
