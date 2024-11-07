# **Status Report 10/9**

## **Team Report**

### **Goals from Last Week**

* Make the program send chunks to whisper small when the user stops talking for more accurate transcription.  
* Measure the decibels of the input audio so we can stop the transcription when the user stops speaking.  
* Implement a UI instead of relying on a CLI.

### **Progress and Issues**

* Progress:  
  * Worked on the audio processing  
  * Figured out that there might be a better approach rather than silence detection, via overlapping chunks.  
  * Found a new library named SpeechRecognition which will make our work easier  
* What Worked:  
  * The speech recognition library that handles most of the speech recognition is great on its own.  
* Learnings:  
  * Speech recognition and chunking is hard.  
* Issues:  
  * Silence detection did not deal with edge cases very well (ex: whole audio file being silent).  
  * Large files being sent to the LLM took too long to process and slowed down audio capture.  
  * Current transcription code either repeats lines or replaces lines in its output.

### **Plans and Goals for Next Week**

* Implement a UI instead of relying on a CLI. (didn’t get to from last week)  
* Look into threading and making our own way to capture audio and recognize speech.  
* Figure out how to properly display “phrases” vs “sentences”.

## **Contributions of Individual Team Members**

### **Goals from Last Week**

* Nikita P.:   
  * Integrate Tanneh’s temporary UI with the current iteration of InstaText and continue working on making the transcription more accurate.  
* Sandro K.:  
  * Try to work with chunk sizes being dynamic, aka being dependent on the decibels instead of seconds so each chunk will be sent after each word or two said. Also need some db threshold to stop transcription when no one is speaking to avoid sus transcriptions.  
* Andzhur T.:  
  * Try to integrate transcriptions into the website. Work on creating better voice detection and help with possibly implementing captures of different languages.   
* Matthew H.:  
  * Integrate the silence detection program created last week with the current audio capture in order to reduce poor translations and more accurately chunk around words.  
* Tanneh J.:   
  * I plan to arrange my schedule and work with team members' schedules in order to schedule a meeting and do coding.

### **Progress and Issues**

* Nikita P.:  
  * Progress:  
    * Worked on the silence recognition until I realized that it was full of holes and made me die inside.  
  * What Worked:  
    * The speech recognition library that did what we wanted beautifully.  
  * Learnings:  
    * Speech recognition is its own world.  
  * Issues:  
    * Whisper hallucinates on quiet/empty chunks, resulting in weird transcriptions.  
* Sandro K.:  
  * Progress:  
    * Found a new library named SpeechRecognition which has easier audio processing than PyAudio  
  * What Worked:  
    * The new SpeechRecognition library  
  * Learnings:  
    * Learned that the chunked audio does not work even when you try to make it dynamic because of the delay and quiet frames  
  * Issues:  
    * The PyAudio audio processing and chunking with whispersmall was not working perfectly  
* Andzhur. T:  
  * Progress:  
    * Worked on UI and website (such as hero section, about section and navigation bar) as well as created a figma template of the website. Helped the team with some audio.  
  * What Worked:  
    * Something that worked was combining tailwindCSS and react together for a smoother and better experience. A template of live transcription also worked.  
  * Learnings:  
    * I learned more about the way tailwindCSS and react work and their syntax.  
  * Issues:   
    * Deploying the website had some difficulties as the repository is private, and creating a fork didn’t resolve the issue.  
* Matthew H.:  
  * Progress:  
    * Worked on integrating silence detection into current audio capture and transcription code.  
  * What Worked:  
    * The speech\_recognition module seems very useful for our purposes.  
  * Learnings:  
    * I learned how some of the basic features of the speech\_recognition module work.  
  * Issues:  
    * Silence detection is not a good way to approach the problems we were encountering with audio capture.  
* Tanneh J.:  
  * Progress:  
    *  Met with the team and discussed the direction of the project and the work that needs to be done  
  * What Worked  
    * The simple UI design even though it needs improvement.   
  * Learnings:  
    * Because I am responsible for the UI design of the project, my weekly learning involves the UI interfaces on the python.   
  * Issues:  
    * The issue is implementing a user friendly and aesthetically pleasing UI.

### **Plans and Goals for Next Week**

* Nikita P.:  
  * Catch up with the goals from last week and get the transcription running better.  
* Sandro K.:  
  * Work on implementing Whispersmall with SpeechRecognition  
* Andzhur T.:  
  * Help with implementing audio and speech recognition. The audio is a little bit inaccurate at times. I will also continue to work on the frontend, possibly adding more features.   
* Matthew H.:  
  * Look into the transcription repetition/replacing issue mentioned in the group issues section.  
* Tanneh J.:   
  * To really sit down and design a second design of the UI.   
    

