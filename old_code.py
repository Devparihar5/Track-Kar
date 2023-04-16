#website for Police to easy there work
from flask import Flask, render_template, request, redirect, session, Response
import cv2
import sqlite3
import os
import numpy as np
import json
import phonenumbers
import warnings
import urllib.request
import glob
import pandas as pd
from werkzeug.utils import secure_filename
import face_recognition
from truecallerpy import search_phonenumber
warnings.filterwarnings('ignore')
os.chdir("E:/House-of-Hackers/")


global capture
capture = 0
# Convert binary data to proper format and write it on Hard Disk
def write_file(data, filename):
    with open(filename, 'wb') as file:
        file.write(data)
#initialise the app
app = Flask(__name__)
app.secret_key = 'ItShouldBeAnythingButSecret'
camera = cv2.VideoCapture(0)

conn = sqlite3.connect('E:/House-of-Hackers/Criminal_Database.db')
df_db = pd.read_sql_query("SELECT * from suspect", conn)

# generate frame by frame from camera
def gen_frames():
    global capture
    while True:
        ret, frame = camera.read()
        if ret:
            # capture image
            if (capture):
                capture = 0
                path = "static/captures/suspect.png"
                cv2.imwrite(path, frame)
                camera.release()
                cv2.destroyAllWindows()
                face_info()
            try:
                ret, buffer = cv2.imencode('.jpg', cv2.flip(frame, 1))
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            except Exception as e:
                pass

def face_info():
    try:
        criminal_id = 1
        #initialize some variables
        # face_locations = []
        # face_encodings = []
        face_names = []
        process_this_frame = True
    
        # run a loop and extract the images from the database
        for i in range(0, len(df_db)):
            img = df_db['picture'][i]
            img = np.fromstring(img, np.uint8)
            img = cv2.imdecode(img, cv2.IMREAD_COLOR)
            cv2.imwrite('static/captures/suspect.png', img)
            known_image = face_recognition.load_image_file(
                "static/imgs/user_img.png")
            unknown_image = face_recognition.load_image_file(
                "static/captures/suspect.png")

            name_1 = df_db['name'][i]
            biden_encoding = face_recognition.face_encodings(known_image)[
                0]
            unknown_encoding = face_recognition.face_encodings(unknown_image)[
                0]
            
            known_face_encodings = [
                biden_encoding
                ]
            known_face_names = [
                name_1
            ]
            matches = face_recognition.compare_faces(known_face_encodings,unknown_encoding)
            name = "Unknown Person"
            face_distance = face_recognition.face_distance(known_face_encodings, unknown_encoding)
            best_match_index = np.argmin(face_distance)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            face_names.append(name)

            # if matches == [True]:
            #     query = f"SELECT * FROM suspect WHERE criminal_id LIKE %{criminal_id}%"
            #     print("Sucesss")
            #     output(query)
            #     break
            # else:
            #     criminal_id = criminal_id + 1
        # output(query)
    except:
        global numb
        numb = "suspect not available in database"
        return numb

# open pass.json file for get username and password and api's
with open('static/pass.json', 'r') as c:
    user = json.load(c)["pass"]
# A decorator used to tell the application
# which URL is associated function
api = user['api']



# function for getting all data form truecaller
def true(num):
    id = 'a1i0R--cvttz2FZ-ky8i5vx2XFHWFlKr-cHOnPQyF153JBj7l9iRL2_Ej6dt93dP'
    print("Errorrrrrrrrrrrrrrrrrrrrrrrrrrr")
    df = search_phonenumber(num, "IN", id)
    try:
        name = df['data'][0]['name']
    except:
        name = ' '
    print(name)
    try:
        mail = df['data'][0]['internetAddresses'][0]['id']
    except:
        mail = ' '
    # print(mail)
    try:
        address = df['data'][0]['addresses'][0]['city'] + ", " + df['data'][0][
            'addresses'][0]['address']
    except:
        address = ' '
    # print(add)
    try:
        link = df['data'][0]['image']
    except:
        link = 'https://icon-library.com/images/unknown-person-icon/unknown-person-icon-10.jpg'
    try:
        age = df['data'][0]['birthday']
    except:
        age = ' '
    f = open('static/imgs/user_img.png', 'wb')
    f.write(urllib.request.urlopen(link).read())
    f.close()
    number = num
    fir_no = int('0000')
    # show(fir_no,name,number,mail,age,address)     
    show(fir_no,name,number,mail,age,address)

# function for get output
def show(fir_no,name,number,mail,age,address):  
    fir_no = str(fir_no)  
    dict1 = {
        'data': {
            'Name': name,
            'Number': number,
            'MailId': mail,
            'DOB': age,
            'pre_address': address,
            'fir_no': fir_no
        }
    }
    out_file = open("static/userData.json", "w")
    json.dump(dict1, out_file)
    out_file.close()
    print("json file write successfully")


def output(num):
        print("info function inline")
        #check that dataframe is empty or not
        def check_empty(result):
            if result.empty:
                return redirect('/error1')
            else:
                return False
        print(len(num))
        if len(num) == 10:
            print("Number input")
            result = df_db[df_db['number'] == num]
            check_empty(result)
        elif len(num) == 4 or len(num) == 5:
            print("Fir no input")
            result = df_db[df_db['fir_no'] == int(num)]
            check_empty(result)
        print("task complated.....")
        fir_no = result['fir_no'].values[0]
        name = result['name'].values[0]
        number = result['number'].values[0]
        mail = result['mail'].values[0]
        age = result['dob'].values[0]
        address = result['address'].values[0]
        pic = result['picture'].values[0]
        write_file(pic, 'static/imgs/user_img.png')
        print(fir_no,name,number,mail,age,address)
        # dict1 = {
        #     'data': {
        #         'Name': name,
        #         'Number': number,
        #         'MailId': mail,
        #         'DOB': age,
        #         'pre_address': address,
        #         'fir_no': fir_no
        #     }
        # }
        # out_file = open("static/userData.json", "w")
        # json.dump(dict1, out_file)
        # out_file.close()
        print("user data generated")
        show(fir_no,name,number,mail,age,address)


# for facial recognition
@app.route('/face')
def cam():
    return render_template('cam.html')

from tracker2 import *

# for facial recognition
@app.route('/speed')
def speed():
    # import cv2
    # import numpy as np
    end = 0

    #Creater Tracker Object
    tracker = EuclideanDistTracker()

    #cap = cv2.VideoCapture("Resources/traffic3.mp4")
    cap = cv2.VideoCapture("E:/Kainskep/carsss/SpeedRadar-OpenCV-/traffic4.mp4")
    f = 25
    w = int(1000/(f-1))


    #Object Detection
    object_detector = cv2.createBackgroundSubtractorMOG2(history=None,varThreshold=None)
    #100,5

    #KERNALS
    kernalOp = np.ones((3,3),np.uint8)
    kernalOp2 = np.ones((5,5),np.uint8)
    kernalCl = np.ones((11,11),np.uint8)
    fgbg=cv2.createBackgroundSubtractorMOG2(detectShadows=True)
    kernal_e = np.ones((5,5),np.uint8)

    while True:
        ret,frame = cap.read()
        if not ret:
            break
        frame = cv2.resize(frame, None, fx=0.5, fy=0.5)
        height,width,_ = frame.shape
        #print(height,width)
        #540,960

        #Extract ROI
        roi = frame[50:540,200:960]

        #MASKING METHOD 1
        mask = object_detector.apply(roi)
        _, mask = cv2.threshold(mask, 250, 255, cv2.THRESH_BINARY)

        #DIFFERENT MASKING METHOD 2 -> This is used
        fgmask = fgbg.apply(roi)
        ret, imBin = cv2.threshold(fgmask, 200, 255, cv2.THRESH_BINARY)
        mask1 = cv2.morphologyEx(imBin, cv2.MORPH_OPEN, kernalOp)
        mask2 = cv2.morphologyEx(mask1, cv2.MORPH_CLOSE, kernalCl)
        e_img = cv2.erode(mask2, kernal_e)


        contours,_ = cv2.findContours(e_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        detections = []

        for cnt in contours:
            area = cv2.contourArea(cnt)
            #THRESHOLD
            if area > 1000:
                x,y,w,h = cv2.boundingRect(cnt)
                cv2.rectangle(roi,(x,y),(x+w,y+h),(0,255,0),3)
                detections.append([x,y,w,h])

        #Object Tracking
        boxes_ids = tracker.update(detections)
        for box_id in boxes_ids:
            x,y,w,h,id = box_id


            if(tracker.getsp(id)<tracker.limit()):
                cv2.putText(roi,str(id)+" "+str(tracker.getsp(id)),(x,y-15), cv2.FONT_HERSHEY_PLAIN,1,(255,255,0),2)
                cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 255, 0), 3)
            else:
                cv2.putText(roi,str(id)+ " "+str(tracker.getsp(id)),(x, y-15),cv2.FONT_HERSHEY_PLAIN, 1,(0, 0, 255),2)
                cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 165, 255), 3)

            s = tracker.getsp(id)
            if (tracker.f[id] == 1 and s != 0):
                tracker.capture(roi, x, y, h, w, s, id)

        # DRAW LINES
    
        cv2.line(roi, (0, 410), (960, 410), (0, 0, 255), 2)
        cv2.line(roi, (0, 430), (960, 430), (0, 0, 255), 2)

        cv2.line(roi, (0, 235), (960, 235), (0, 0, 255), 2)
        cv2.line(roi, (0, 255), (960, 255), (0, 0, 255), 2)


        #DISPLAY
        #cv2.imshow("Mask",mask2)
        #cv2.imshow("Erode", e_img)
        cv2.imshow("ROI", roi)

        key = cv2.waitKey(w)
        if key==27:
            tracker.end()
            end=1
            break

    if(end!=1):
        tracker.end()

    cap.release()
    cv2.destroyAllWindows()



# for getting video frame
@app.route('/video')
def video():
    return Response(gen_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
# to capture images
@app.route('/requests', methods=['POST', 'GET'])
def tasks():
    global camera
    if request.method == 'POST':
        if request.form.get('click') == 'Capture':
            global capture
            capture = 1
    with open('static/userData.json', 'r') as c:
        data = json.load(c)["data"]
    return render_template("output.html", data=data)


@app.route('/home', methods=["GET", "POST"])
def IN():
    if ('user' in session and session['user'] == user['username']):
        try:  
            if request.method == "POST":
                # global num
                # get the post parameters
                # getting input with name = fname in HTML form
                num = request.form.get("mnumber")
                #remove any whitespace from the num
                num = num.replace(" ", "")

                print(len(num))
                if len(num) > 4 and len(num) < 10:
                    return redirect('/invalid')
                num = str(num)
                print(num)
                output(num)
                return redirect('/result')
        except:
            print(" I dont know what happened")
            return redirect('/error1')
    return render_template('index.html')


@app.route('/crime_analysis')
def crime_analysis():
    import subprocess
    subprocess.Popen(["streamlit", "run", "crime_analysis.py"])
    return render_template('index.html')

@app.route('/NLP_model')
def NLP_model():
    import subprocess
    subprocess.Popen(["streamlit", "run", "NLP_model.py", "--server.port", "8963"])
    return render_template('index.html')

@app.route('/Police_caller')
def Police_caller():
    import subprocess
    subprocess.Popen(["streamlit", "run", "Police_caller.py", "--server.port", "9024"])
    return render_template('index.html')

@app.route('/truecaller', methods=["GET", "POST"])
def true_id():
    if request.method == "POST":
        num = request.form.get("mnumber")
        #remove any whitespace from the num
        num = num.replace(" ", "")
        print(num)
        num = str(num)
        print(num)
        output(num)
        # return redirect('/result')
    return render_template('truecaller.html')

@app.route('/', methods=['POST', 'GET'])
@app.route('/login', methods=['POST', 'GET'])
def login():
    if (request.method == 'POST'):
        username = request.form.get('username')
        password = request.form.get('password')
        if username == user['username'] and password == user['password']:
            session['user'] = username
            return redirect('/home')
        return redirect('/error')
    return render_template("login.html")


@app.route('/not_valid')
def nvalid():
    return render_template('not_valid.html')

#output page 
@app.route('/result')
def out():
    with open('static/userData.json', 'r') as c:
        data = json.load(c)["data"]
    return render_template("output.html", data=data)

# error page
@app.route('/error1')
def error1():
    return render_template('error_1.html')
    # with open('static/userData.json', 'r') as c:
    #     data = json.load(c)["data"]
    # return render_template("output.html", data=data)

@app.route('/invalid')
def invalid():
    return render_template('invalid.html')

@app.route('/error')
def error():
    return render_template('error.html')


@app.route('/upload')
def finger():
    return render_template('upload.html')

@app.route('/face_upload')
def face_upload():
    return render_template('face_upload.html')


@app.route('/face_uploader', methods=['GET', 'POST'])
def upload_face():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename('face.png'))

        try:
            # Define the cameras
            camera1_url = 0
            camera2_url = 1

            # Load the known faces
            criminal_image = face_recognition.load_image_file("./face.png")
            criminal_face_encoding = face_recognition.face_encodings(criminal_image)[0]

            # roice_image = face_recognition.load_image_file("roice.jpg")
            # roice_face_encoding = face_recognition.face_encodings(roice_image)[0]

            known_face_encodings = [
                criminal_face_encoding
            ]
            known_face_names = [
                "Criminal Detected"
            ]

            # Open the cameras and start processing frames
            video_capture1 = cv2.VideoCapture(camera1_url)
            video_capture2 = cv2.VideoCapture(camera2_url)

            while True:
                # Capture a frame from camera1
                ret1, frame1 = video_capture1.read()
                rgb_frame1 = frame1[:, :, ::-1]

                # Capture a frame from camera2
                ret2, frame2 = video_capture2.read()
                rgb_frame2 = frame2[:, :, ::-1]
                font = cv2.FONT_HERSHEY_DUPLEX
                # Process camera1 frame
                face_locations1 = face_recognition.face_locations(rgb_frame1)
                face_encodings1 = face_recognition.face_encodings(rgb_frame1, face_locations1)
                for (top, right, bottom, left), face_encoding in zip(face_locations1, face_encodings1):
                    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                    name = "Unknown"
                    face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)
                    if True in matches:
                        name = known_face_names[np.argsort(face_distance)[0]]
                    cv2.rectangle(frame1, (left, top), (right, bottom), (0, 0, 255), 2)
                    cv2.rectangle(frame1, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                    
                    cv2.putText(frame1, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

                # Process camera2 frame
                face_locations2 = face_recognition.face_locations(rgb_frame2)
                face_encodings2 = face_recognition.face_encodings(rgb_frame2, face_locations2)
                for (top, right, bottom, left), face_encoding in zip(face_locations2, face_encodings2):
                    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                    name = "Unknown"
                    face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)
                    if True in matches:
                        
                        name = known_face_names[np.argsort(face_distance)[0]]

                        #generate a alarm for that
                    cv2.rectangle(frame2, (left, top), (right, bottom), (0, 0, 255), 2)
                    cv2.rectangle(frame2, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                    cv2.putText(frame2, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
                # Display the resulting image
                cv2.imshow('Camera1', frame1)
                cv2.imshow('Camera2', frame2)

                # Hit 'q' on the keyboard to quit!
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            # Release handle to the webcam
            video_capture1.release()
            video_capture2.release()
            cv2.destroyAllWindows()
            
        except:
            return redirect('/error1')
        return redirect('/home')



@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename('finger.BMP'))
        try:
            # read path from html page
            path = 'finger.BMP'
            MIN_MATCH_COUNT = 15
            input_img = cv2.imread(path)
            input_img = input_img.astype('uint8')
            gray = cv2.cvtColor(input_img, cv2.COLOR_BGR2GRAY)
            sift = cv2.SIFT_create()
            kp = sift.detect(input_img, None)
            img1 = cv2.drawKeypoints(input_img, kp, input_img)

            flag = 0

            os.chdir("E:/House-of-Hackers/Dataset/Altered/Altered-Easy/")
            for file in glob.glob("*.BMP"):

                frame = cv2.imread(file)
                frame = frame.astype('uint8')
                gray1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                sift = cv2.SIFT_create()
                kp = sift.detect(frame, None)
                img2 = cv2.drawKeypoints(frame, kp, frame)
                kp1, des1 = sift.detectAndCompute(img1, None)
                kp2, des2 = sift.detectAndCompute(img2, None)
                FLANN_INDEX_KDTREE = 0
                index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
                search_params = dict(checks=50)
                flann = cv2.FlannBasedMatcher(index_params, search_params)
                matches = flann.knnMatch(np.asarray(
                    des1, np.float32), np.asarray(des2, np.float32), k=2)
                good = []
                for m, n in matches:
                    if m.distance < 0.7*n.distance:
                        good.append(m)
                # print(len(good))
                if len(good) > 25:
                    src_pts = np.float32(
                        [kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
                    dst_pts = np.float32(
                        [kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)
                    M, mask = cv2.findHomography(
                        src_pts, dst_pts, cv2.RANSAC, 5.0)
                    matchesMask = mask.ravel().tolist()
                    score = len(good)/len(matches)*200
                    # print(score)
                    Matched = str(file)
                    # print(Matched)
                    # save the score in score.json file
                    dict_finger = {
                        "data" : {
                            "Finger_Name" : Matched,
                            "Score" : score
                        }
                    }
                    os.chdir("E:/House-of-Hackers/static/")
                    out_file = open("score.json", "w")
                    os.chdir("E:/House-of-Hackers/Dataset/Altered/Altered-Easy/")
                    json.dump(dict_finger, out_file)
                    out_file.close()
                    flag = 1
                else:
                    matchesMask = None

                draw_params = dict(matchColor=(0, 255, 0),  # draw matches in green color
                                   singlePointColor=None,
                                   matchesMask=matchesMask,  # draw only inliers
                                   flags=2)

                img3 = cv2.drawMatches(
                    img1, kp1, img2, kp2, good, None, **draw_params)
                # cv2.imshow("Match",img3)

                # save the matched image
                if flag == 1:
                    # print('Success')
                    os.chdir("E:/House-of-Hackers/static/")
                    cv2.imwrite("FingerPrintData.png", img3)
                    os.chdir("E:/House-of-Hackers/Dataset/Altered/Altered-Easy/")
                    flag = 5

                # automatically closes the window after 1 seconds
                # cv2.waitKey(50)
                # cv2.destroyAllWindows()

            if flag == 0:
                # print("No Matches among the given set!!")
                # read image
                img3 = cv2.imread('E:/House-of-Hackers/not found.png')
                os.chdir("E:/House-of-Hackers/static/")
                dict_finger = {
                        "data" : {
                            "Finger_Name" : "No any Match Found",
                            "Score" : '0.00'
                        }
                    }
                out_file = open("score.json", "w")
                json.dump(dict_finger, out_file)
                out_file.close()
                cv2.imwrite("FingerPrintData.png", img3)

            # read the matched image
            # img = cv2.imread('Matched_image.png')
            # cv2.imshow('Matched Image',img)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()
        except:
            print("Error Occured!!")
        return redirect('/Fingerprint')


@app.route('/Fingerprint')
def finger_print():
    os.chdir("E:/House-of-Hackers/")
    with open('static/score.json', 'r') as c:
        data = json.load(c)["data"]
    return render_template('up_out.html',data=data)



if __name__ == '__main__':
    app.run(debug=True, port="8963")