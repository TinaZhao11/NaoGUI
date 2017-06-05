---------------
Introduction
---------------
This code package contains the system function module and GUI design, also provide a database to store user animation design.
--------------------
Software Environment
--------------------
Python 2.7 and Pycharm Version 2017.1.2  are used to implement system function and desktop application. 
The library need for this project include Naoqi, Librosa, pyQt, rosampy. 
--------------------
Source Structures
--------------------
The source code can get from the github: 
https://github.com/TinaZhao11/NaoGUI


Source code structures are shown below:
├── NaoGUI                    
    │   ├── Database
    │   │   ├── animation.db
    │   │   ├── getData.py
    │   │   ├── InitDatabase.py
    │   │   ├── setfootstep.py
    │   ├── GUI
    │   │   ├── MainWindow.py         <- Main Enter for Desktop Application
    │   │   ├── connectRobot.py
    │   │   ├── mainMenu.py
    │   │   ├── animation_view.py
    │   │   ├── audio_view.py    
    │   │   ├── suprise_view.py
    │   │   ├── Controller.py                 <- Event Controller
    │   │   ├── manageData.py        <- Data Manager
    │   ├── robot
    │   │   ├── ALMemoryKey.py         
    │   │   ├── FilesRW.py
    │   │   ├── footstep.py                <- Separate evaluate footstep and music match
    │   │   ├── Upperbody.py                <- Contains function module
    │   │   ├── Util.py   
    │   ├── music_tracker
    │   │   ├── beat_tracker.py        <- Track the beat for music
    │   ├── DemoFile
    │   ├── image