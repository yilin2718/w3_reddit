# w3_reddit

User sentiment 


Install git and clone this repo

sudo apt install git
git clone https://github.com/yilin2718/w3_reddit.git

Run it!

cd ..
cd w3_reddit
docker build -t user-sentiment .
docker run -d -p 8080:8080 user-sentiment

