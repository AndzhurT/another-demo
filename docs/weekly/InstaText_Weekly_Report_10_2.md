# **Status Report 10/2**

## **Team Report**

### **Goals from Last Week**

* Continue working on live audio capture integration with the whisper small LLM.  
* Think about how to arrange the user interface.  
* Research methods of dividing audio to send to LLM  
* Start thinking about custom LLM training

### **Progress and Issues**

* Progress:  
  * Implemented PyAudio with Whisper small, some progress on live audio transcription.  
* What Worked:  
  * ChatGPT and Huggingface examples & documentation.  
* Learnings:  
  * That live audio transcription is quite a bit more involved than static audio file transcription.  
* Issues:  
  * Problems with live audio transcription because the chunk size is set seconds instead of being dynamic.

### **Plans and Goals for Next Week**

* Make the program send chunks to whisper small when the user stops talking for more accurate transcription.  
* Measure the decibels of the input audio so we can stop the description when the user stops speaking.  
* Implement a UI instead of relying on a CLI.


## **Contributions of Individual Team Members**

### **Goals from Last Week**

* Nikita P.:  
  * Continue general integration of parts from Sandro, Tanneh, Matthew and Andzhur. Think about what needs to be done / make a backlog of todo issues.  
* Sandro K.:  
  * Continue working on Whisper small and trying to figure out how to fine-tune it.   
* Andzhur T.:  
  * Continue to research more about filtering audio and work on designing the Figma template for a website.  
* Matthew H.:  
  * Research different methods of dividing the audio files  
* Tanneh J.:  
  * My intention is to have a button fully coded and sent over to the rest of the team. 


### **Progress and Issues**

* Nikita P.:  
  * Progress:  
    * Got live transcription up and running using whisper small, somewhat janky but it works for now.  
  * What Worked:  
    * ChatGPT and huggingface examples & documentation.  
  * Learnings:  
    * You can save audio in a numpy array for processing it for transcription, instead of a traditional audio format like wave.  
  * Issues:  
    * Currently the model fails if you chunk the audio in the middle of a word.

    

* Sandro K.:  
  * Progress:  
    * Came up with an idea to split the audio into multiple inputs to make the transcription live.  
  * What Worked:  
    * Managed to get some live transcription with 2 second intervals.  
  * Learnings:  
    * Learned on how Whispersmall transcribes audio using chunks  
  * Issues:  
    * Problems with live audio transcription because the chunk size is set seconds instead of being dynamic. 

    

* Andzhur. T:  
  * Progress:   
    * Worked on creating the website and helped with the code for transcription   
  * What Worked:  
    * The website is up and running, as well as janky transcription works  
  * Learnings:  
    * Learned more about whisper small and how you can translate voice to NumPy array of numbers  
  * Issues:  
    * I had some issues with the website, git merges, and transcriptions weren’t working initially. 


* Matthew H.:  
  * Progress:  
    * I looked into different methods of dividing the audio.  
    * I created a program that records sound to a wav file until it detects extended silence.  
  * What Worked:  
    * Numpy allowed for simple interpretation of the audio frames recorded. This made it easy to determine the “silentness” of each frame.  
  * Learnings:  
    * I learned about how PyAudio measures volume.  
  * Issues:  
    * I had to miss a team meeting due to work in another class, which prevented communication about the chunking problem.

    

* Tanneh J.:  
  * Progress:   
    *  As of today, I have not made any progress. The reason for that is simply management of time and work-load.   
  * What Worked:   
    * This week, I have not been able to meet with the team due to scheduling conflicts, so we have not been able to do any workable things.   
  * Learnings:  
    * This week I have learned that communicating and collaborating are other important skills for a computer developer that will work with a team.    
  * Issues:  
    * Oue issue so far has been getting every team member together at the same time. 

### **Plans and Goals for Next Week**

* Nikita P.: 

  Integrate Tanneh’s temporary UI with the current iteration of InstaText and continue working on making the transcription more accurate.

* Sandro K.:

  Try to work with chunk sizes being dynamic, aka being dependent on the decibels instead of seconds so each chunk will be sent after each word or two said. Also need some db threshold to stop transcription when no one is speaking to avoid sus transcriptions.

* Andzhur T.:

  Try to integrate transcriptions into the website. Work on creating better voice detection and help with possibly implementing captures of different languages. 

* Matthew H.:  
  	Integrate the silence detection program created last week with the current audio capture in order to reduce poor translations and more accurately chunk around words.

    
* Tanneh J.: I plan to arrange my schedule and work with team members' schedules in order to schedule a meeting and do coding.

