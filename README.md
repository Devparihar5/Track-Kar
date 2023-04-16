# House-of-Hackers

## PROBLEM STATEMENT:

**Website/App for Citizens and Police for management of crime records**
> Managing crime records is an essential function of law enforcement agencies, and it is crucial for citizens to have access to reliable information on crime incidents in their communities. A website or app that serves as a platform for citizens and police to manage crime records would be a useful resource for promoting transparency, accountability, and collaboration between law enforcement agencies and the public.

TEAM DETAILS:

Devendra Parihar (Data Scientist),

Gopika Varshini (Front-End Developer),

Sruthi Prabha (Front-End Developer)

## IDEA :
The main idea behind Trackkar is to provide a smart database management system for police use to track criminals in a more efficient and effective way. The system utilizes various data science and AI/ML techniques to help police track criminals using different identifiers such as mobile numbers, FIR numbers, facial recognition, fingerprint detection, and live facial detection from CCTV cameras. It also provides horizontal crowdsourcing using mobile numbers to get anyone's details, crime analysis and forecasting, and natural language processing to analyze people's feedback for police and suggest updates for better coordination.

## APPROACH:
The approach used to build Trackkar involved several steps:

1. Requirement Gathering: The first step was to gather all the requirements from the police department to understand their needs and challenges in tracking criminals.

2. Database Design: Based on the requirements, a database schema was designed to store all the necessary information and provide a unified search experience.

3. Development: The project was developed using various technologies such as Python, Flask, HTML/CSS, JavaScript, and MySQL database. The facial recognition and fingerprint detection features were developed using deep learning techniques and integrated with the system.

4. Integration: The developed features were integrated with the system and tested to ensure they work seamlessly.

## > Features 
* Login page according to their access on software
![image](https://user-images.githubusercontent.com/54232149/232333722-17fcb5d8-f478-4658-8149-93fa13b1c675.png)

* Designed and developed the unified database searching functionality for tracking criminals using their mobile number and FIR number.
![image](https://user-images.githubusercontent.com/54232149/232333664-f05984fd-919e-4ea7-a97d-78ffdcdb19ff.png)


* facial recognition feature using deep learning techniques to identify criminals.
* live facial detection feature from multiple CCTV cameras to detect criminals and trigger alarms.
![image](https://user-images.githubusercontent.com/54232149/232334179-a8b31067-8077-42e9-a238-235840314e19.png)


* Fingerprint detection feature without the need for any hardware to fetch criminal history.
![image](https://user-images.githubusercontent.com/54232149/232333917-c496c613-2b1d-4790-b194-1396dd1bbb0e.png)

* Horizontal crowdsourcing functionality using mobile numbers to get anyone's details for faster tracking.
![image](https://user-images.githubusercontent.com/54232149/232333948-62f1e2b4-9a08-4eda-a667-fc976923bf8f.png)

* Crime analysis and forecasting functionality based on current FIR registrations using various statistical and machine learning models.
![image](https://user-images.githubusercontent.com/54232149/232334228-fdcea9cd-2e7d-46ea-882f-d9dc46b8f3c6.png)

* crime prioritization based on the description of the crime from a specially created platform. Developed the platform where anyone can post about a crime anonymously, and the data is stored in the database. Utilized natural language processing and machine learning models to prioritize crimes based on their severity. Integrated the crime prioritization functionality into Track-Kar for efficient handling of cases by the police.
![image](https://user-images.githubusercontent.com/54232149/232334405-4076de32-6eef-451f-9ac5-fecd62046120.png)


--> Additional Features
* Natural language processing to analyze people's feedback for police and suggest updates for better coordination.



## TECH STACK USED:
* Python for backend development and data analysis
* Flask web framework for building the APIs
* HTML/CSS and JavaScript for front-end development
* MySQL database for data storage and retrieval
* OpenCV library for facial recognition and live facial detection
* Scikit-learn library for implementing various machine learning algorithms for crime analysis and forecasting
* NLTK library for natural language processing of user feedback
* Dlib library for fingerprint detection without the need for any hardware
