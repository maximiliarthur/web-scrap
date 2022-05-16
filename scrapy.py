from bs4 import BeautifulSoup
import requests
import numpy as np
from csv import writer

def insert_data(a,b):
    for i in a:
        b.append(i.text)

def insert_id(a,b):
    for i in a:
        b.append(i.text[5:])

n = []
i = []
y = []
j = 1

while (j <= 18): # untuk mengulang sebanyak 18 page

    url= "https://sinta3.kemdikbud.go.id/affiliations/authors/2042?page={}".format(j)

    page=requests.get(url) # akses ke url

    soup = BeautifulSoup(page.content, 'html.parser') # ngambil isi html

    nama =  soup.find_all('div', class_="profile-name") # ngambil data nama
    id = soup.find_all('div', class_="profile-id") # ngambil data id
    year3 = soup.find_all('div', class_="stat-num text-center") # ngambil data score


    insert_data(nama,n) # masukkan data ke variable n
    insert_id(id,i) # masukkan data ke i
    insert_data(year3,y) # masukkan data ke y
    j += 1



y = np.array(y) # [264,666,0,0,249,544,0,0]
y = y.reshape(-1,4) # [264,666,0,0,249,544,0,0] -> [[264,666,0,0],[249,544,0,0]]


with open('test.csv','w',encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['ID', 'NAMA', '3 YEAR SCORE', 'ALL YEAR SCORE']
    thewriter.writerow(header)

    for idx, id in enumerate(i):
        info = [id,n[idx],y[idx][0],y[idx][1]] # idx, nama, year 3, all year
        thewriter.writerow(info) # buat nulis isi dari info ke csv