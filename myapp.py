"""
# My first app
Here's our first attempt at using data to create a table:
"""

import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import sqlite3

st.title("Machine Learning for more efficient SCM processing")
st.sidebar.subheader("Upload File")
uploaded_file= st.sidebar.file_uploader(label="Upload your CSV or Excel file.",type=['csv','xlsx'])
conn = sqlite3.connect("data.db", check_same_thread = False)
cursor = conn.cursor()
#sql='''CREATE TABLE XRDDATA(
#Chemical_Phase CHAR(35), Weight_Percent FLOAT, Crystal_Structure CHAR(35))'''
#cursor.execute(sql)
#print("Table created succesfully...")

#cursor.execute('''INSERT INTO XRDDATA(Chemical_Phase, Weight_Percent, Crystal_Structure) VALUES("Quartz",22.5,"Hexagonal")''')
#cursor.execute('''INSERT INTO XRDDATA(Chemical_Phase, Weight_Percent, Crystal_Structure) VALUES("Calcite",0.9,"Rhombo")''')
#st.title("Display Graph")
conn.commit()
conn.close()

if uploaded_file is not None:
     # Can be used wherever a "file-like" object is accepted:
     try:
         dataframe = pd.read_csv(uploaded_file)
     except Exception as e:
         print(e)
         dataframe = pd.read_excel(uploaded_file)
     st.write(dataframe)

st.write("G Schist")
st.write("XRD Data")

st.write(pd.DataFrame({
    'Chemical Phases': ["Quartz","Calcite","Illite","Muscovite","Clinochlore","Dicite","Anorthite","Titanium Oxide","Albite"],
    'weight %': [22.5, 0.9, 24.5,23.1,6.5, 4.8,12.1, 1.8, 3.8], 'Crystal Structure':["Hexagonal", "Rhombo", "Monoclinic", "Monoclinic", "Monoclinic", "Monoclinic", "Triclinic", "Monoclinic", "Triclinic"]
}))

st.write("EDX Data")

gschist = pd.DataFrame({
    'Element': ["Sodium","Magnesium","Aluminum","Silicon","Potassium","Calcium","Iron","Titanium"],
    'atom no': [11, 12, 13,14,19, 20,26, 22], 'mass (%)':[0.78, 1.81, 24.69, 57.12, 6.26, 1.13, 5.71, 2.49], 'atom (%)':[1, 2.19,26.91, 59.82,4.71, 0.83,3.01, 1.53]
})
st.write(gschist)


first_atom = st.selectbox('Select first atom type:',("Sodium","Magnesium","Aluminum","Silicon","Potassium","Calcium","Iron","Titanium"))
st.write('You selected:',first_atom)
second_atom = st.selectbox('Select second atom type:',("Sodium","Magnesium","Aluminum","Silicon","Potassium","Calcium","Iron","Titanium"))
st.write('You selected:', second_atom)
idfirst = gschist.index[gschist["Element"] == first_atom].tolist()[0]

idsecond = gschist.index[gschist["Element"] == second_atom].tolist()[0]

#caoversi = (gschist.iloc[idca]['mass (%)']) / (gschist.iloc[idsi]['mass (%)'] )


firstoversecond = (gschist.iloc[idfirst]['mass (%)']) / (gschist.iloc[idsecond]['mass (%)'] )
st.write("{} to {} ratio is: {:.2f}".format(first_atom, second_atom, firstoversecond))

#idal = gschist.index[gschist["Element"] == "Aluminum"].tolist()[0]
#aloversi = (gschist.iloc[idal]['mass (%)']) / (gschist.iloc[idsi]['mass (%)'] )
#st.write("Al to Si ratio is: {:.2f}".format(aloversi))
#st.write(caoversi)

st.image('./EDX_G_schist.png')

import streamlit as st

st.write("C Schist")
st.write("XRD Data")
st.write(pd.DataFrame({
    'Chemical Phases': ["Quartz","Calcite","Muscovite I","Muscovite II","Albite","Clinochlore","Kaolinite","Anorthite","Titanium Oxide"],
    'weight %': [35, 3.8, 28.2,16.1,4, 3.3,3.7, 5, 0.9], 'Crystal Structure':["Hexagonal", "Rhombo", "Monoclinic", "Hexagonal", "Triclinic", "Monoclinic", "Triclinic", "Triclinic", "Orthorhombic"]
}))
st.write("EDX Data")

cschist =pd.DataFrame({
    'Element': ["Sodium","Magnesium","Aluminum","Silicon","Potassium","Calcium","Iron","Titanium"],
    'atom no': [11, 12, 13,14,19, 20,26, 22], 'mass (%)':[0.74, 1.7, 25.38, 57.17, 6.08, 2.29, 5.97, 0.67], 'atom (%)':[0.94, 2.05,27.57, 59.66,4.56, 1.68,3.13, 0.41]
})
st.write(cschist)

idca = cschist.index[cschist["Element"] == "Calcium"].tolist()[0]

idsi = cschist.index[cschist["Element"] == "Silicon"].tolist()[0]

caoversi = (cschist.iloc[idca]['mass (%)']) / (cschist.iloc[idsi]['mass (%)'] )

st.write("Ca to Si ratio is: {:.2f}".format(caoversi))
idal = cschist.index[gschist["Element"] == "Aluminum"].tolist()[0]
aloversi = (cschist.iloc[idal]['mass (%)']) / (cschist.iloc[idsi]['mass (%)'] )
st.write("Al to Si ratio is: {:.2f}".format(aloversi))

import streamlit as st

st.write("P Schist")
st.write("XRD Data")
st.write(pd.DataFrame({
    'Chemical Phases': ["Quartz","Calcite","Illite","Muscovite","Clinochlore","Dicite","Anorthite","Titanium Oxide","Albite"],
    'weight %': [22.5, 0.9, 24.5,23.1,6.5, 4.8,12.1, 1.8, 3.8], 'Crystal Structure':["Hexagonal", "Rhombo", "Monoclinic", "Monoclinic", "Monoclinic", "Monoclinic", "Triclinic", "Monoclinic", "Triclinic"]
}))
st.write("EDX Data")

pschist = pd.DataFrame({
    'Element': ["Sodium","Magnesium","Aluminum","Silicon","Potassium","Calcium","Iron","Titanium"],
    'atom no': [11, 12, 13,14,19, 20,26, 22], 'mass (%)':[0.78, 1.01, 29.08, 53.47, 3.04, 6.9, 5, 0.72], 'atom (%)':[1,1.22,31.59, 55.8,2.28, 5.04,2.63, 0.44]
})
st.write(pschist)

idca = pschist.index[pschist["Element"] == "Calcium"].tolist()[0]

idsi = pschist.index[pschist["Element"] == "Silicon"].tolist()[0]

caoversi = (pschist.iloc[idca]['mass (%)']) / (pschist.iloc[idsi]['mass (%)'] )

st.write("Ca to Si ratio is: {:.2f}".format(caoversi))
idal = pschist.index[pschist["Element"] == "Aluminum"].tolist()[0]
aloversi = (pschist.iloc[idal]['mass (%)']) / (pschist.iloc[idsi]['mass (%)'] )
st.write("Al to Si ratio is: {:.2f}".format(aloversi))

import streamlit as st

st.write("B Schist")
st.write("XRD Data")
st.write(pd.DataFrame({
    'Chemical Phases': ["Quartz","Calcite","Ankerite","Muscovite I","Clinochlore","Graphite","Mg-Annite","Rutile","Albite","Pyrite"],
    'weight %': [38, 4.7, 14.3,19.7,3.7, 5,8.77, 1.32, 3.7,0.9], 'Crystal Structure':["Hexagonal", "Rhombo", "Rhombo", "Hexagonal", "Monoclinic", "Hexagonal","Monoclinic", "Tetragonal", "Triclinic", "Cubic"]
}))

st.write("EDX Data")

bschist = pd.DataFrame({
    'Element': ["Sodium","Magnesium","Aluminum","Silicon","Potassium","Calcium","Iron","Sulfur","Titanium"],
    'atom no': [11, 12, 13,14,19, 20,26, 16,22], 'mass (%)':[0.88, 4.59, 15.99, 46.77, 3.3, 20.78, 6.45, 0.39,0.87], 'atom (%)':[1.18, 5.84,18.33, 51.51,2.61, 16.04,3.57, 0.37,0.56]
})
st.write(bschist)

idca = bschist.index[bschist["Element"] == "Calcium"].tolist()[0]

idsi = bschist.index[bschist["Element"] == "Silicon"].tolist()[0]

caoversi = (bschist.iloc[idca]['mass (%)']) / (bschist.iloc[idsi]['mass (%)'] )

st.write("Ca to Si ratio is: {:.2f}".format(caoversi))
idal = bschist.index[bschist["Element"] == "Aluminum"].tolist()[0]
aloversi = (bschist.iloc[idal]['mass (%)']) / (bschist.iloc[idsi]['mass (%)'] )
st.write("Al to Si ratio is: {:.2f}".format(aloversi))

import streamlit as st

st.write("L Schist")
st.write("XRD Data")
st.write(pd.DataFrame({
    'Chemical Phases': ["Quartz","Calcite","Montmorillonite","Montmorillonite-22A","Clinchlore","Albite","Titanium Oxide"],
    'weight %': [37.1, 8.7, 8.9,9.4,8.5, 25.4,2], 'Crystal Structure':["Hexagonal", "Rhombo", "Monoclinic", "Monoclinic", "Monoclinic", "Triclinic","Orthorhombic"]
}))
st.write("EDX Data")

lschist = pd.DataFrame({
    'Element': ["Sodium","Magnesium","Aluminum","Silicon","Calcium","Iron","Titanium"],
    'atom no': [11, 12, 13,14, 20,26, 22], 'mass (%)':[0.68, 2.61,19.88,59.41,9.58,6.61,1.22], 'atom (%)':[0.88,3.19,21.85,62.73,7.09,3.51,0.76]
})

st.write(lschist)

idca = lschist.index[lschist["Element"] == "Calcium"].tolist()[0]

idsi = lschist.index[lschist["Element"] == "Silicon"].tolist()[0]

caoversi = (lschist.iloc[idca]['mass (%)']) / (lschist.iloc[idsi]['mass (%)'] )

st.write("Ca to Si ratio is: {:.2f}".format(caoversi))
idal = lschist.index[lschist["Element"] == "Aluminum"].tolist()[0]
aloversi = (lschist.iloc[idal]['mass (%)']) / (lschist.iloc[idsi]['mass (%)'] )
st.write("Al to Si ratio is: {:.2f}".format(aloversi))




def make_clickable(link):
    # target _blank to open new window
    # extract clickable text to display for your link
    text = link.split('=')[1]
    return f'<a target="_blank" href="{link}">{text}</a>'

# link is the column with hyperlinks




st.table(pd.DataFrame({
    'Chemical Phases': ["Quartz","Calcite","Montmorillonite","Montmorillonite-22A","Clinchlore","Albite","Titanium Oxide","Ankerite","Muscovite I","Graphite","Mg-Annite","Rutile","Pyrite"],
    'Chemical Formula': ["SiO2","CaCO3","(Na, Ca)0.3(Al, Mg)2Si4O10(OH)2.xH2O","Na0.3(Al, Mg)2Si4O10(OH)2.8H2O","(Mg2.96Fe1.55 Fe0.136Al1.275)( Si2.622Al1.376O10)(OH)8","(Na, Ca) (Si, Al)4 O8","Ti3O5","Ca(Mg0.67 Fe+20.33)(CO3)2","(K, Na)(Al, Mg, Fe)2(Si3.1Al0.9)O10(OH)2","C","K(Mg, Al)2.04(Si3.34Al0.66)O10(OH)2","TiO2","FeS2"],
'Materials Project Link':["https://next-gen.materialsproject.org/materials/mp-559091","CaCO3","(Na, Ca)0.3(Al, Mg)2Si4O10(OH)2.xH2O","Na0.3(Al, Mg)2Si4O10(OH)2.8H2O","(Mg2.96Fe1.55 Fe0.136Al1.275)( Si2.622Al1.376O10)(OH)8","(Na, Ca) (Si, Al)4 O8","Ti3O5","Ca(Mg0.67 Fe+20.33)(CO3)2","(K, Na)(Al, Mg, Fe)2(Si3.1Al0.9)O10(OH)2","C","K(Mg, Al)2.04(Si3.34Al0.66)O10(OH)2","https://next-gen.materialsproject.org/materials/mp-1147#summary","FeS2"] }))

#mydata =pd.DataFrame
#    'Chemical Phases': ["Quartz","Calcite","Montmorillonite","Montmorillonite-22A","Clinchlore","Albite","Titanium Oxide","Ankerite","Muscovite I","Graphite","Mg-Annite","Rutile","Pyrite"],
#    'Chemical Formula': ["SiO2","CaCO3","(Na, Ca)0.3(Al, Mg)2Si4O10(OH)2.xH2O","Na0.3(Al, Mg)2Si4O10(OH)2.8H2O","(Mg2.96Fe1.55 Fe0.136Al1.275)( Si2.622Al1.376O10)(OH)8","(Na, Ca) (Si, Al)4 O8","Ti3O5","Ca(Mg0.67 Fe+20.33)(CO3)2","(K, Na)(Al, Mg, Fe)2(Si3.1Al0.9)O10(OH)2","C","K(Mg, Al)2.04(Si3.34Al0.66)O10(OH)2","TiO2","FeS2"],
#'Materials Project Link':["SiO2","CaCO3","(Na, Ca)0.3(Al, Mg)2Si4O10(OH)2.xH2O","Na0.3(Al, Mg)2Si4O10(OH)2.8H2O","(Mg2.96Fe1.55 Fe0.136Al1.275)( Si2.622Al1.376O10)(OH)8","(Na, Ca) (Si, Al)4 O8","Ti3O5","Ca(Mg0.67 Fe+20.33)(CO3)2","(K, Na)(Al, Mg, Fe)2(Si3.1Al0.9)O10(OH)2","C","K(Mg, Al)2.04(Si3.34Al0.66)O10(OH)2","https://next-gen.materialsproject.org/materials/mp-1147#summary","FeS2"] })
#mydata['Materials Project Link'] = mydata['Materials Project Link'].apply(make_clickable)
#mydata = mydata.to_html(escape=False)
#st.write(mydata, unsafe_allow_html=True)


#mydata.style.set_properties(subset=mydata.columns, **{'width': '300px'})
#st.write(mydata.style.set_properties(subset=mydata.columns, **{'width': '500px'}))
