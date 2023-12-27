import streamlit as st
import pandas as pd
import numpy as np
import pickle  
# import matplotlib.pyplot as plt
import streamlit.components.v1 as components
st.set_page_config(layout='wide')





@st.cache(suppress_st_warning=True)
def get_fvalue(val):    
    feature_dict = {"Can Convert":0,"Need more effort to Convert":1}    
    for key,value in feature_dict.items():        
        if val == key:            
            return value
        

def get_value(val,my_dict):    
    for key,value in my_dict.items():        
        if val == key:            
            return value
        
def main():
    app_mode = st.sidebar.selectbox('Select Page',['Visualization','Prediction']) #two pages
    if app_mode=='Visualization': 
        st.sidebar.subheader('Leads Conversion Statistics')
        st.sidebar.markdown("KPI's: ")
        st.sidebar.markdown("- **Conversion Statistics**")
        st.sidebar.markdown("- **Gender** wise conversions")
        st.sidebar.markdown("- **Stream** wise conversions")
        st.sidebar.markdown("- **State/City** wise conversions")
        st.sidebar.markdown("- **Course** wise conversions")
        st.sidebar.markdown("- **Detailed Report**")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.write(' ')
        with col2:
            st.image('logo.jpg')
        with col3:
            st.write(' ')
        
        st.markdown("<h1 style='text-align: center; color: black;'>Leads Data Viz.</h1>", unsafe_allow_html=True)
        # st.markdown('Dataset :')    
        # data=pd.read_csv('Leads_data_Uncleaned.csv')    
        df = pd.read_csv('Leads_data.csv')
        # st.write(data.head())
        # col1, col2 = st.columns(2)  
        # with col1:     
        #     st.markdown('Course vs Conversion Status ') 
        #     st.bar_chart(df[['Course','Conversion Status']].head(20))
        # with col2:
        #     tab = {'Index': [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18],
        #     'Course': ['Btech-IT', 'BCA', 'BSc-IT', 'Others', 'MCA', 'MSc-IT', 'Mtech-IT',
        #    'Diploma-IT', 'BVoc', 'Btech-Non IT', 'BSc-Non IT', 'BCom',
        #    'OTHERS', 'BA', 'Diploma-Non IT', 'MBA', 'Bvoc', 'MSc-Non IT',
        #    'MCom'] }
        #     # Create DataFrame
        #     course_tab = pd.DataFrame(tab)
        #     st.write(course_tab)
        html_temp = """<div class='tableauPlaceholder' 
                            id='viz1703679862775' 
                            style='position: relative'>
                            <noscript><a href='#'>
                            <img alt='Dashboard 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;
                            images&#47;Ta&#47;TableuRP2&#47;Dashboard1&#47;1_rss.png' style='border: none' /></a>
                            </noscript><object class='tableauViz'  style='display:none;'>
                        <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> 
                        <param name='embed_code_version' value='3' /> 
                        <param name='site_root' value='' />
                        <param name='name' value='TableuRP2&#47;Dashboard1' />
                        <param name='tabs' value='no' />
                        <param name='toolbar' value='yes' />
                        <param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ta&#47;TableuRP2&#47;Dashboard1&#47;1.png' /> 
                        <param name='animate_transition' value='yes' />
                        <param name='display_static_image' value='yes' />
                        <param name='display_spinner' value='yes' />
                        <param name='display_overlay' value='yes' />
                        <param name='display_count' value='yes' />
                        <param name='language' value='en-US' />
                        <param name='filter' value='publish=yes' /></object></div> 

                        <script type='text/javascript'>                    
                                    var divElement = document.getElementById('viz1703679862775');                    
                                    var vizElement = divElement.getElementsByTagName('object')[0];                    
                                    if ( divElement.offsetWidth > 800 ) { 
                                        vizElement.style.width='100%';
                                        vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} 
                                    else if ( divElement.offsetWidth > 500 ) { 
                                        vizElement.style.width='100%';
                                        vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} 
                                    else { 
                                        vizElement.style.width='100%';
                                        vizElement.style.height='1877px';}                     
                                    var scriptElement = document.createElement('script');                    
                                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
                                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                
                        </script>"""
        
        components.html(html_temp, width=1130, height=900)
            
    elif app_mode == 'Prediction':
        st.sidebar.subheader('Rounded Professional Program')
        st.sidebar.markdown("This is a demo web app for predicting the conversion status of a lead given the following details:")
        st.sidebar.markdown("- **Gender** [Male, Female]")
        st.sidebar.markdown("- **College** Type [Engineering, Arts & Science,Commerce]")
        st.sidebar.markdown("- **Course** [Various IT & Non-IT courses]")
        st.sidebar.markdown("- **State** [Kerala, Outside Kerala]")
        st.sidebar.markdown("- **City** [Cities in India]")
                        
                            
                        
        st.title('RP2 Leads Data Model')
        st.markdown('Classify whether a lead can be converted based on their Gender, City, College, and State')

        st.header("Lead Features")
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Gender & Education Details")
            gender = st.selectbox('Select Gender', ["Male", "Female"])
            college = st.selectbox('Select College type', ["Engineering", "Arts & Science, Commerce"])
            if college == "Engineering":
                course = st.selectbox('Select Course', ['Btech-IT',  'Mtech-IT','Btech-Non IT', 'Mtech-NonIT', 'Other'])
                if course=='Others':
                   course = st.text_input('Enter your Course') 
            else:
                course = st.selectbox('Select Course', [ 'BCA', 'BSc-IT', 'Others', 'MCA', 'MSc-IT', 
            'Diploma-IT', 'BVoc',  'BSc-Non IT', 'BCom',
             'BA', 'Diploma-Non IT', 'MBA', 'Bvoc', 'MSc-Non IT',
            'MCom'])
                if course=='Others':
                   course = st.text_input('Enter your Course')

            

        with col2:
            st.subheader("Demographic Details")
            state = st.selectbox('Select State', ['Kerala', 'Outside Kerala'])
            if state == 'Kerala':
                city = st.selectbox('Select City', ['Thrissur', 'Alappuzha', 'Idukki', 'Ernakulam',
                'Palakkad', 'Kottayam','Thiruvananthapuram',  'Kasargode','Malappuram', 'Kannur', 'Kozhikode', 'Wayanad',
            'Kollam', 'Pathanamthitta' ])
            else:
                city = st.selectbox('Select City', ['Telangana', 
            'Tamil Nadu', 'Nepal', 'Karnataka', 
            'New Delhi',  'Jharkhand', 
            'Uttar Pradesh',  'Maharashtra',
                'Andhra Pradesh',  'Jammu & Kashmir',
            'Madhya Pradesh',  'Bihar',
            'Haryana', 'Odisha', 'Rajasthan', 'West Bengal', 'Punjab',
            'Gujarat', 'Uttarakhand', 'Tripura', 'Chandigarh', 'Chattisgarh',
            'Dubai', 'Others'])
                if (city == 'Others'):
                    city = st.text_input('Enter your City')

        st.text('')
        from sklearn.ensemble import RandomForestClassifier
        #Loading up the Regression model we created
        model_rf = RandomForestClassifier()
        filename = 'final_estimator.pkl'
        model = pickle.load(open(filename, 'rb'))

        if gender=="Male":
            gender = 0
        else:
            gender = 1


        if city == "Thrissur":
            city = 0
        elif city == "Alappuzha":
            city = 1
        elif city == "Idukki":
            city = 2
        elif city == "Ernakulam":
            city = 3
        elif city == "Palakkad":
            city = 4
        elif city == "Kottayam":
            city = 5
        elif city == "Thiruvananthapuram":
            city = 6
        elif city == "Kasargode":
            city = 7
        elif city == "Malappuram":
            city = 8
        elif city == "Kannur":
            city = 9
        elif city == "Kozhikode":
            city = 10
        elif city == "Wayanad":
            city = 11
        elif city == "Kollam":
            city = 12
        elif city == "Pathanamthitta":
            city = 13
        elif city == "Telangana":
            city = 14
        elif city == "Tamil Nadu":
            city = 15
        elif city == "Nepal":
            city = 16
        elif city == "Karnataka":
            city = 17
        elif city == "New Delhi":
            city = 18
        elif city == "Jharkhand":
            city = 19
        elif city == "Uttar Pradesh":
            city = 20
        elif city == "Maharashtra":
            city = 21
        elif city == "Andhra Pradesh":
            city = 22
        elif city == "Jammu & Kashmir":
            city = 23
        elif city == "Madhya Pradesh":
            city = 24
        elif city == "Bihar":
            city = 25
        elif city == "Haryana":
            city = 26
        elif city == "Odisha":
            city = 27
        elif city == "Rajasthan":
            city = 28
        elif city == "West Bengal":
            city = 29
        elif city == "Punjab":
            city = 30
        elif city == "Gujarat":
            city = 31
        elif city == "Uttarakhand":
            city = 32
        elif city == "Tripura":
            city = 33
        elif city == "Chandigarh":
            city = 34
        elif city == "Chattisgarh":
            city = 35
        elif city == "Dubai":
            city = 36
        else :
            city = 37

        if college == 'Engineering':
            college = 0
        else:
            college = 1

        if course == 'Btech-IT':
            course = 0
        elif course == 'BCA':
            course = 1
        elif course == 'BSc-IT':
            course = 2
        elif course == 'MCA':
            course = 3
        elif course == 'MSc-IT':
            course = 4
        elif course == 'Mtech-IT':
            course = 5
        elif course == 'Diploma-IT':
            course = 6
        elif course == 'BVoc':
            course = 7
        elif course == 'Btech-Non IT':
            course = 8
        elif course == 'BSc-Non IT':
            course = 9
        elif course == 'BCom':
            course = 10
        elif course == 'BA':
            course = 11
        elif course == 'Diploma-Non IT':
            course = 12
        elif course == 'MBA':
            course = 13
        elif course == 'MSc-Non IT':
            course = 14
        elif course == 'MCom':
            course = 15
        else:
            course = 16


        if state == "Kerala":
            state=0
        else:
            state = 1







            

        data1={    'Gender':gender,
                    'City':city,
                'College':college,
                    'Course':course,
                    'State':state, }    

        features = pd.DataFrame(data1, index=[0])
        
        st.write(features) 
        # st.write(features.shape)
        single_sample = np.array(features).reshape(1,-1)
        # st.write(single_sample.shape)
        # st.write("single_sample",single_sample)
        if st.button("Predict Conversion Status"):
                result = model.predict(single_sample)
                st.text(result[0])
                if result[0] == 1 :            
                    st.error(    'According to our Calculations, this lead cannot be converted'    )            
                    # st.markdown(    f'<img src="data:image/gif;base64,{data_url_no}" alt="cat gif">',    unsafe_allow_html=True,)        
                elif result[0] == 0 :            
                    st.success(    'This lead can be converted. Work harder. All the best!'    )            
                    # st.markdown(    f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',    unsafe_allow_html=True,    )


        st.text('')
        st.text('')

if __name__=='__main__':
    main()

# if st.button("Predict"):        
#     file_ = open("6m-rain.gif", "rb")        
#     contents = file_.read()        
#     data_url = base64.b64
#     encode(contents).decode("utf-8")        
#     file_.close()        
#     file = open("green-cola-no.gif", "rb")        
#     contents = file.read()        
#     data_url_no = base64.b64
#     encode(contents).decode("utf-8")        
#     file.close()        
#     loaded_model = pickle.load(open('Random_Forest.sav', 'rb'))        
#     prediction = loaded_model.predict(single_sample)        
#     if prediction[0] == 0 :            
#         st.error(    'According to our Calculations, you will not get the loan from Bank'    )            
#         st.markdown(    f'<img src="data:image/gif;base64,{data_url_no}" alt="cat gif">',    unsafe_allow_html=True,)        
#     elif prediction[0] == 1 :            
#         st.success(    'Congratulations!! you will get the loan from Bank'    )            
#         st.markdown(    f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',    unsafe_allow_html=True,    )
