
# 💼 Finance Automation Project Using Python-Streamlit-OpenCV-MediaPipe

A Streamlit-based Solo-Project built that simplifies bank statement analysis. The app uses Python libraries such as **pandas**, **NumPy**, **OpenCV**, and **MediaPipe**. It provides a smart login interface (via webcam hand gesture or direct button) and a project dashboard to display insights from uploaded bank statements.





## Demo 

👉 [Watch Demo of the project on Google Drive](https://drive.google.com/file/d/1fORkPLNfH14EJuQTYbJXca154I13BNTP/view?usp=sharing)

---





## Features

- ✋ **Smart Login Interface**
  - Login using hand gesture detection via webcam (OpenCV + MediaPipe) **webcam feature not allowed in Streamlit Cloud deployed App - Instead run locally on your Code Editor**
  - Option for direct login without camera

- 📊 **Dashboard Interface**
  - Upload your bank statement (CSV).
  - Automatically processes and analyzes your transactions.
  - Categorized expenses, total balance, monthly trends, etc.
  - Clear and simple visual summaries.




## 🔧 Tech Stack

- Python
- Streamlit
- OpenCV
- MediaPipe
- Pandas
- NumPy
- Plotly


## Installation and Local Project run
- 📁 Project Structure
 finance-automation-app
 - ├── Home.py                  # Main entry point
 - ├── pages/
     - ├── 1_Login.py           # Login interface
     - ├── 2_DashBoard.py           # Dashboard after login
 - ├── modules/
      -    └── full_hand_open.py   # Hand gesture detection logic
 - ├── requirements.txt        # All libraries used
 - ├── categories.json        # All category handling
 - ├── packages.txt        # streamlit cloud deploy handling
 - ├── sample_bank_statement.csv        
 - └── README.md               # Project overview
 - └── LICENSE               # MIT License


🔴
**Steps to Run the Project (With webcam feature) Locally:**
- Install Python 3.11
   - 
Scroll Down to Download and install Python 3.11 from:https://www.python.org/downloads/release/python-3110/

During installation, make sure to check “Add Python to PATH”

- Download Git/Git bash on yout local computer:
   - 
for reference: [Git downloads](https://git-scm.com/downloads)   
   
- Clone this Repo on VsCode Editor/Git Bash: 
   -
```bash
  cd .\Desktop\

```
```bash
  git clone https://github.com/makankosappoh/Finance-Automation-Project-.git

```
you will be able to see a folder on Desktop just open it through Your code editor (Vscode/pycharm etc).

- In vscode Terminal - Create a virtual Enivronment for project to Run
   - 
Windows:
```bash
  python -m venv venv 

```
```bash
  venv\Scripts\activate

```
MacOS/Linux:
```bash
  python -m venv venv 

```
```bash
  source venv/bin/activate

```
- In vscode Terminal - Install libraries for project functining:
   - 
```bash
  pip install -r requirements.txt
```
- Finally in Vscode Termnial - run the Streamlit app
```bash
  streamlit run Home.py

```
**Important:** Always activate the virtual environment before running the app.
Since the app uses the webcam, the user must have the necessary permissions to access it.

---
## Download sample csv file needed for Bank statement analysis

✅ As for currently , the project analyze only special types od csv files that have only specific columns for categorizing so **please ensure if you want the breakdown analysis kindly Download and do it on this sample_csv file.**

👉 [sample_csv_file](https://drive.google.com/file/d/10uVmHrXem8D8f-6zcXqAVg2ZOVUqAo8Y/view?usp=sharing)

---
## Direct Run app through Streamlit Cloud

Streamlit Cloud allows users to deploy and run fully fledged Projects very easily and smooth proper functioning.

**🔴 Although streamlit doesn't allow videocapture so you can just direct login to dashboard and see the project**

**🟢 still can run very smooth and clear interfaced streamlit app**
- Click Here/open in new Tab the badge to open the project Deployed as streamlit cloud app 👉
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://finanaceautomationapp.streamlit.app/)

---


## Pros / Cons of running MY PROJECT on streamlit cloud deployed project v/s on Local remote computer!

- ✔️ **Pros**
  - No need of manual Downloading dependencies/libraries or python version to run the app (Auto-done by Streamlit Cloud Interface)
  - Easy to Handle and fast loading/running speed.
  - Smooth transitions and effects maintained and stablized performance
- ❌ **Cons**
  - Doesn't allow live video capture features of mediapiepe/open-cv (only pictorial saved images or saved videos can be run on streamlit cloud)





## 🔗 references

Some cool references from which I studied, took reference, added my own ideas and created my project:

- simple dashboard tutorial: https://www.youtube.com/watch?v=wqBlmAWqa6A&t=3472s
- opencv mediapipe basics: https://www.youtube.com/watch?v=TACu8y2T2ps
## 😁 Credit

Solo Project by **Saharsh Sharma** 

Connect with me on:

- 🔗 [LinkedIn](https://www.linkedin.com/in/saharsh-sharma-a5712b287/)
- 🐙 [GitHub](https://github.com/makankosappoh)
- ✨ [Instagram](https://www.instagram.com/saharsh_ssj/)