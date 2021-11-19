import streamlit as st
import pandas as pd
import cv2
import numpy  

# st.header("Welcome to Hakul's world")

# st.image('media/dog-beach-lifesaver.png')

menu = ['Home', 'About me', 'Read data', ' Camera']

choice = st.sidebar.selectbox('Menu', menu)

if choice == 'Home':
    st.header("Welcome to Hakul's world")
    # st.image('media/dog-beach-lifesaver.png')
    st.video('media/dogs.mp4')

    col1, col2 = st.columns(2)
    with col1:
        dog_name = st.text_input("What's dog name?")
        st.write('Your dog name: ', dog_name)    
    with col2:
        age = st.slider('Dog age', min_value = 1, max_value = 20)
        st.write('Your dog age: ', age)

    # dog_name = st.text_input("What's dog name?")
    # st.write('Your dog name: ', dog_name)           # input từ người dùng 
    
    # age = st.slider('Dog age', min_value = 1, max_value = 20)  # tạo slider kéo 
elif choice == 'Read data':
    df = pd.read_csv('media/AB_NYC_2019.csv')
    st.dataframe(df)

elif choice == 'About me':
    # st.audio('media/Impact_Moderato.mp3')
    fileUp = st.file_uploader('Your upload', type = ['jpg', 'jpeg', 'png'])   # max size = 200MB
    st.image(fileUp)
    # model.predict(fileUp)  # hint for weekly project, should resize / preprocessing before predict

elif choice == 'Camera':
    st.title('Open your webcam')
    st.warning('Webcam show on local computer ONLY')
    show = st.checkbox('Show!')
    FRAME_WINDOW = st.image([])
    camera = cv2.VideoCapture(0) # device 1/2

    while show:
        _, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        FRAME_WINDOW.image(frame)
    else:
        camera.release()

    cam = cv2.VideoCapture(0) # device 0. If not work, try with 1 or 2

    if not cam.isOpened():
        raise IOError("Cannot open webcam")

    while True:
        ret, frame = cam.read()
        frame = cv2.flip(frame, 1)
        
        cv2.imshow('My App!', frame)

        key = cv2.waitKey(1) & 0xFF
        if key==ord("q"):
            break

    cam.release()
    cv2.destroyAllWindows()