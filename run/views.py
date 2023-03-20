from django.shortcuts import render
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime 
def save(you,him,result):
    scope = ['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive.file','https://www.googleapis.com/auth/drive']
    cred = ServiceAccountCredentials.from_json_keyfile_name("run\cred.json",scope)
    client = gspread.authorize(cred)
    slot_sheet = client.open("imp").worksheet('que')
    date = str(datetime.now().date())
    time = str(datetime.now().strftime('%H:%M:%S'))
    row = [you,him,result,date,time]
    data = slot_sheet.insert_row(row,2)
def flames(name1, name2):
    # Remove spaces and convert to lowercase
    name1 = name1.replace(" ", "").lower()
    name2 = name2.replace(" ", "").lower()
    for char in name1:
        if char in name2:
            name1 = name1.replace(char, "", 1)
            name2 = name2.replace(char, "", 1)
    count = len(name1) + len(name2)
    flames = ["Friendship", "Love", "Affection", "Marriage", "Enemy", "Siblings"]
    while len(flames) > 1:
        index = (count % len(flames)) - 1
        if index >= 0:
            right = flames[index+1:]
            left = flames[:index]
            flames = right + left
        else:
            flames = flames[:-1]

    return flames[0]
def home(request):
    return render(request,"index.html")
def love_test(request):
    p1 = request.GET["you"]
    p2 = request.GET["him"]
    result = flames(p1,p2)
    save(p1,p2,result)
    return render(request,"result.html",{'result':result})