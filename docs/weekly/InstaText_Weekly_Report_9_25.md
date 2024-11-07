# **Status Report 9/25**

## **Team Report**

### **Goals from Last Week**

* Start development with off-the-shelf libraries / implementations.  
* Familiarize ourselves with live audio capture.

### **Progress and Issues**

* Progress:  
  * Initiated the integration of audio capture with the whisper small LLM.  
  * Began research into user interface development options.  
* What Worked:  
  * Successfully utilized the Huggingface platform for LLM development and deployment.  
* Learnings:  
  * Discovered that audio streams are processed in chunks.  
  * Identified multiple suitable UI libraries available for Python development.  
* Issues:  
  * Encountered difficulties in integrating the audio processing system with LLM-based transcription.  
  * Faced issues related to Python’s handling of external libraries.

### **Plans and Goals for Next Week**

* Continue working on live audio capture integration with the whisper small LLM.  
* Think about how to arrange the user interface.  
* Research methods of dividing audio to send to LLM  
* Start thinking about custom LLM training

## 

## 

## **Contributions of Individual Team Members**

### **Goals from Last Week**

* Nikita P.:  
  * Start coding.  
* Sandro K.:  
  * Start working on the LLM  
* Andzhur T.:  
  * Start discussing the website structure/continue working on the website.  
* Matthew H.:  
  * Look into Pyaudio for live capture of audio.  
* Tanneh J.:  
  * Researching the UI library to use.

### **Progress and Issues**

* Nikita P.:  
  * Progress:  
    * Began coding and contributed to the integration of live audio capture with the whisper small LLM for real-time transcription.  
  * What Worked:  
    * The Huggingface platform, for effective development and deployment of whisper small.  
  * Learnings:  
    * Gained an understanding of how audio streams are read in discrete chunks.  
  * Issues:  
    * Faced difficulties in aligning the audio capture with LLM-based transcription.  
    * Encountered issues with Python not recognizing a particular library.  
* Sandro K.:  
  * Progress:  
    * Found an existing LLM for speech recognition on Hugginface named Whisper small  
  * What Worked:  
    * The Hugging Face platform, for effective development and deployment of whisper small.  
  * Learnings:  
    * Learned what existing LLM models are available on Huggingface and found the one we can use in our project.  
  * Issues:  
    * Not sure how to start fine-tuning the Whisper small.  
* Andzhur. T:  
  * Progress:  
    * Began working on the creation of the website, trying to set up Figma to create a template of how our website is going to look and started to read some documentation on filtering noise from audio.   
  * What Worked:  
    * Setting up the website and Figma account with different templates.   
  * Learnings:  
    * Learned more about how filtering works in audio and how Figma works.  
  * Issues:  
    * Some issues that appeared were not understanding how to combine filtering noise from audio with LLM for real-time transcription and not being sure about the website’s design.  
* Matthew H.:  
  * Progress:  
    * I created a test program for creating and playing wav file with PyAudio.  
  * What Worked:  
    * PyAudio was able to automatically detect the mic on my computer, which means that the final product will likely be able to as well.  
    * PyAudio was able to play sounds from a wav file that was created while the program was running, which will make any speech-to-text-to-speech relatively trivial.  
  * Learnings:  
    * I learned the basics of handling PyAudio.  
  * Issues:  
    * The current plan for the live transcription is to break off the wav file at convenient points during speech, send it to the LLM, and then continue recording. I am unsure how exactly I will get the program to recognize a good breakpoint.  
* Tanneh J.:  
  * Progress:   
    * I started researching libraries for creating a button that will do the  transcription, specifically libraries within python.   
  * What Worked:  
    *  Google was helpful in providing options of libraries that are already being used to create buttons that will transcribe audio into text.   
  * Learnings:  
    * I learned that codes do not always need to be built from scratch because there are already pre-existing codes that I can add upon in order to build what I am trying to build, a button.   
  * Issues:  
    * Figuring out how the py libraries work and can be downloaded on a mac. The instructions on the internet about installing py-audio libraries on a mac are not clear enough. This poses a struggle because the button will not transcribe audio without the py-audio library. 

### **Plans and Goals for Next Week**

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

