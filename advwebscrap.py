import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_data(dept,deg):
    url = requests.get(f'https://www.{dept}.ruet.ac.bd/teacher_list').text
    soup = BeautifulSoup(url,'lxml')
    teachers = soup.find_all('tr')[1:]
    #print(teachers)
    name_en=[]
    designation=[]
    phone_no=[]
    email=[]
    depts=[]
    for teacher in teachers:
        name= teacher.find_all("td")[1].text.strip()
        desig= teacher.find_all("td")[3].text.strip()
        phone= teacher.find_all("td")[6].text.strip()
        em= teacher.find_all("td")[5].text.strip()
        department= teacher.find_all("td")[4].text.strip()
        for d in deg:
            if d==desig:
                name_en.append(name)
                designation.append(desig)
                phone_no.append(phone)
                email.append(em)
                depts.append(department)
                print("done")

        
    data=pd.DataFrame({'name':name_en,"Designation":designation,
                  "department":dept, "email":email,"phone":phone_no})
    return data
def main():
    st.title("RUIT Teacher' information")
    #department Selection
    deg=[]
    Depts=['EEE','CSE','CHEM','MATH','PHY']
    Dept_a=st.sidebar.selectbox('Select Department',Depts).lower()
    Desig1=st.sidebar.checkbox("Professor")
    Desig2=st.sidebar.checkbox("Associate Professor")
    Desig3=st.sidebar.checkbox("Assistant Professor")
    Desig4=st.sidebar.checkbox("Lecturer")
    if Desig1:
        deg.append("Professor")
    if Desig2:
        deg.append("Associate Professor")
    if Desig3:
        deg.append("Assistant Professor")
    if Desig4:
        deg.append("Lecturer")
    if Dept_a:
        st.write(deg)
        data=get_data(Dept_a,deg)
        st.dataframe(data)
    
if __name__=='__main__':
    main()