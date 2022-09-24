# Streamlit Timeline Component Example

import streamlit as st
from streamlit_timeline import timeline


# use full page width
st.set_page_config(page_title="Naithik BirthDay Wishes", layout="wide")

# Test/Title
#st.image('https://github.com/SurendraRedd/NaithikBirthday/blob/main/IMG-20210111-WA0003.jpg?raw=true',width=250)
st.markdown('# 🎂🎂 Happy 8th Birthday Naithik 🎂🎂🎂')

col1, col2, col3, col4, col5, col6, col7,col8 = st.columns(8)

col1.header('1')
col1.image('https://github.com/SurendraRedd/NaithikBirthday/blob/main/FB_IMG_1476548602809.jpg?raw=true',width=150)
col2.header('2')
col2.image('https://github.com/SurendraRedd/NaithikBirthday/blob/main/FB_IMG_1476548512154.jpg?raw=true',width=200)
col3.header('3')
col3.image('https://github.com/SurendraRedd/NaithikBirthday/blob/main/FB_IMG_1476549299555.jpg?raw=true',width=150)
col5.header('5')
col5.image('https://github.com/SurendraRedd/NaithikBirthday/blob/main/IMG20191003090734.jpg?raw=true',width=200)
col4.header('4')
col4.image('https://github.com/SurendraRedd/NaithikBirthday/blob/main/IMG_20170917_143555.jpg?raw=true',width=200)
col6.header('6')
col6.image('https://github.com/SurendraRedd/NaithikBirthday/blob/main/IMG20210830144700.jpg?raw=true',width=150)
col7.header('7')
col7.image('https://github.com/SurendraRedd/NaithikBirthday/blob/main/IMG-20210111-WA0003.jpg?raw=true',width=200)
col8.header('8')
col8.image('https://github.com/SurendraRedd/NaithikBirthday/blob/main/IMG20220813124814.jpg?raw=true',width=200)



# load data
with open('example.json', "r") as f:
    data = f.read()

# render timeline
timeline(data, height=800)
