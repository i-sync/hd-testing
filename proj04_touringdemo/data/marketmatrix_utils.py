"""
The market matrix excel utils
Get some footer links data from excel file. "MY19R_Social_footer_link.xlsx"
Get bike data from excel file. "MY19_FXDR_Market_Matrix.xlsx"
"""

__author__ = "Libby.Qin"

import openpyxl
from proj04_touringdemo.data.urls import current_url
__matrix_file_name__ = "proj04_touringdemo/data/MY19R_Social_footer_link.xlsx"
__matrix_bike_file_name__ = "proj04_touringdemo/data/MY19_FXDR_Market_Matrix.xlsx"

def get_social_footer_matrix():
    """
    Get all soical link matrix
    locale column B
    Facebook Url column C
    Instagram Url column D
    Twitter Url column E
    :return:
    """
    wb = openpyxl.load_workbook(__matrix_file_name__)
    sheet = wb["MY19R"]
    res = {}
    for index in range(2, 44):
        locale = sheet["B{}".format(index)].value
        facebook = sheet["C{}".format(index)].value
        instagram = sheet["D{}".format(index)].value
        twitter = sheet["E{}".format(index)].value
        res[locale] = [facebook, instagram, twitter]
    wb.close()
    return res
def get_bike_matrix():
    """
    Get All bike info matrix
    :return:
    """
    wb = openpyxl.load_workbook(__matrix_bike_file_name__)

    sheet = wb["MY19R"]
    bike_column =["H", "I", "J", "K", "L", "M", "N", "O"]
    bike_code = {}
    for col in bike_column:
        id = sheet["{}1".format(col)].value
        id=id.upper()
        bike_code[col]= id

    res = {}
    for index in range(2, 34):
        locale = sheet["B{}".format(index)].value
        res[locale] = []
        for col in bike_column:
            cc = sheet["{}{}".format(col, index)].value
            if cc and  not cc.startswith("NO"):
                res[locale].append(bike_code[col])

    wb.close()
    return res
def get_menu_links_matrix():
    """
       Get All menu links matrix
       :return:
    """
    wb = openpyxl.load_workbook(__matrix_bike_file_name__)
    sheet = wb["MY19R"]
    res = {}
    for index in range(2, 34):
        locale = sheet["B{}".format(index)].value
        home = sheet["E{}".format(index)].value
        booking = sheet["F{}".format(index)].value
        twitter = "https://twitter.com/intent/tweet?hashtags=&amp;text=+Open+road+freedom+starts+here.+Free%5ber%5d+to+discover%2c+the+power+to+go+further.++%23Harley+Touring+bike.+&amp;tw_p=tweetbutton&amp;url=" + current_url() + "/" + locale
        facebook = "http://www.facebook.com/sharer/sharer.php?u=" + current_url() + "/" + locale + "&appid=500689006785520"
        res[locale] = [home,booking,twitter,facebook]
    wb.close()
    return res