# AMQ_Song_Lookup
This is basically a local version of https://anisongdb.com/ that runs in command line. 
made because i am a lazy fuck who cant be bothered to click a few extra times
you can run the python file directly, but to make it easier on people i have included amq.bat which you can put into PATH to run like other programs like ffmpeg or smth. 

this is a relatively small project so list of availabe songs is not universal. instead get a json of the songs that you want (can be found through anisongdb or the custom song list (CSL) userscript https://github.com/kempanator/amq-scripts) and name it songs.json or whatever else you want to call it, though you will have to change line 65 (one of the first few lines of main if number doesnt seem right) in lookup.py to what you want it to be. Can add functionality such as joining all available jsons within a folder or smth if people want it or smth but idk. 

if anyone knows how to always have the up to date version of the json do let me know so that i can implement it.

## getting started
1. download amq_lookup.zip
2. move it to desired location and then add amq_lookup to PATH
3. open command line and type 'amq'
4. Yuri!!!!

## user manual
Basically type in name of anime/artist/song and it will find all matches. search enging works similar to that of amq in which spaces do funny stuff.

notes:
- add a ' ' directly after search in order to further search for op/ed/ins and their respective number (ex: gintama ins3)
- afterwards, input the number in front of the song you want. it will automatically pop up in your browser!
