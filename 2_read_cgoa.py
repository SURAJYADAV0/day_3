
from bs4 import BeautifulSoup

file_path="sample/21010305041_1800265903.html"


file_read=open(file_path,"r")

data_file=file_read.read()
print(data_file)

#/html/body/div[2]/table/tbody/tr[1]/td[2]/div[1]/table/tbody/tr[4]/td/table[4]/tbody/tr[1]/td[2]

soup=BeautifulSoup(data_file)

div_a=soup.find("div",{"class":"cont_outer"})

table_a=div_a.find("table",{"class":"cont_DIV_UN"})

div_b = table_a.find("div", {"id": "midd_part_UN"})

table_b=div_b.find("table")
td_a=table_b.find_all("td",{"class":"border1"})

cgpa=(td_a[-4:-3])
scgpa=(td_a[-5:-4])

scgpa=scgpa[0].text
print(scgpa)

cgpa=cgpa[0].text
cgpa=cgpa.replace("CGPA","")
print(cgpa)

