# SyntaxError
The purpose of the project is to create a minimal-setup, android controlled, multiplayer game. The game allows two users to connect to their laptop using their phone and play the classic "Space Invaders" with the fun twist of Multiplayer. 

The game allows for a smooth, engaging experience with friends.

# Setup
Main1.py is the standalone python file for the entire project. No extra installations, just one file to get started. On the android end, any simple third part android sensor can be used to connect to the game. A socket connection is established between android app and python app that continuously recieves data. When a user connects, he/she is assigned one of the two characters. The game begins when both users have connected.

# Challenges 
The primary challenges and hurdles were - 
Handling data from two users at once
,Creating android app to provide sensor data
,Running multiple linked threads
,Optimizing raw sensor data to provide smooth motion
,Optimizing game logic for multiplayer

Most of the bugs were hard to debug due to the multiple running threads. We were only successful in creating a native react app that reads sensor data. Unfortunately we had to use a third party sensor app because our android app was not able to send data through sockets.










































