**Setup Instructions**

Clone the Repository:

git clone https://github.com/Divyanaik14/L7_aplication.git

cd chocolate-house

Install Dependencies:

pip install -r requirements.txt

Set Up the Database:

python setup_database.py

Run the Application:

python app.py


**Build and Run the Docker Container**

Build the Docker Image:

docker build -t chocolate-house-app .


Run the Docker Container:

docker run -p 8000:5000 chocolate-house-app
