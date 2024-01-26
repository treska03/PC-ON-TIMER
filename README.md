# PC-ON-TIMER

A program that tracks time device has spent turned ON each day.\
If a certain threshold has been exceeded, a window pops up.

Fork repository to use it.

User can specify in config.json:\
-remind: if true, the window will pop up, otherwise false\
-sound: if true, the sound will be played when window pops up\
-threshold: number of seconds at which the window appears.

For timer to turn ON automatically:

-Windows OS: 
1) Open command prompt
2) Type shell:startup and enter
3) Add a shortcut to main.pyw
