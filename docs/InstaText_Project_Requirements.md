# **1\. Team Info & Policies**

## **Team Members:**

* Nikita P. – Backend Lead – Project Owner (Integration) – Responsible for integrating the LLM and building the backend.  
* Sandro K. – LLM Developer – Project Owner (LLM) – Responsible for developing and fine-tuning the LLM.  
* Andzhur T. – Frontend Developer – Project Owner (Front End) – Focuses on building the UI and noise filtering solutions.  
* Matthew H. – Audio Engineer – Project Owner (Audio) – Handles audio input and live audio capture.  
* Tanneh J. – UI Designer – Project Owner (UI) – Ensures a seamless user experience from live audio capture to real-time transcription.

## **Project Artifacts:**

Git repository: [https://github.com/Neuublue/InstaText](https://github.com/Neuublue/InstaText)

## **Communication Channels and Policies:**

* Discord – Used for regular communication and updates between team members.  
* GitHub Issues – To track tasks and development progress.  
* Email – For formal communication and sharing of major updates.  
* Zoom \- Used for meetings.

# **2\. Product Description**

Product Overview:  
InstaText is an app that transcribes live speech into text. The target audience includes business professionals, international conference attendees, and casual users needing real-time transcription and translation.

## **Major Features (MVP):**

1. Live audio capture – The app will use an audio capture solution, such as PyAudio, to record speech in real time from the user, ensuring seamless integration with the transcription system.  
2. Real-Time Speech-to-Text Transcription – Near-instantaneous transcription of speech with support for multiple accents and languages.  
3. Achieve High Accuracy in Noisy Environments – Implement noise filtering techniques and optimize model performance for various soundscapes.

## **Stretch Goals:**

1. Text-to-Speech Conversion – Converts the translated text back into audio in the desired language.  
2. Integrated Translation – Seamless translation of the transcribed text into multiple languages.  
3. Custom Language Model (LLM) – A custom LLM optimized for real-time, multilingual transcription.

# **3\. Use Cases (Functional Requirements)**

**1\. Start Live Transcription in a Quiet Environment**

1. Actors: User (e.g., student, journalist).  
2. Trigger: The user wants to capture and transcribe a lecture or interview.  
3. Preconditions: The app is installed and ready, with the microphone setup.  
4. Postconditions (Success Scenario): The user sees an accurate real-time transcription of the audio on their screen.  
5. Steps:  
   1. The user opens the app and selects "Start Transcription."  
   2. The app begins capturing live audio from the environment.  
   3. The app processes the speech and displays the transcription in real time.  
6. Extensions: The user may pause or stop the transcription session at any time.  
7. Exceptions: Issues with microphone permissions or hardware could prevent the app from capturing audio.

**2\. Transcribe a Conversation in a Noisy Environment**

1. Actors: User (e.g., journalist, business professional).  
2. Trigger: The user is in a noisy environment (e.g., café, public event) and needs to transcribe a conversation.  
3. Preconditions: The app is set to capture audio with noise filtering enabled.  
4. Postconditions (Success Scenario): The app transcribes the conversation with minimized background noise interference.  
5. Steps:  
   1. The user opens the app and activates the "Noise Reduction" mode.  
   2. The user starts a transcription session.  
   3. The app captures audio, filters out background noise, and transcribes the conversation in real time.  
   4. The transcription appears on the screen for the user to follow.  
6. Extensions: The app can display feedback on audio quality and how noise reduction is performing.  
7. Exceptions: Very high noise levels may still impact transcription quality.

**3\. Save and Review Live Transcription**

1. Actors: User (e.g., student).  
2. Trigger: The user finishes a live transcription (e.g., class lecture) and wants to review it.  
3. Preconditions: The user has completed a transcription session.  
4. Postconditions (Success Scenario): The user can review the transcription immediately after the session.  
5. Steps:  
   1. After completing a transcription session, the user selects the "Save Transcription" option.  
   2. The app saves the transcription locally or in the user’s designated storage location.  
   3. The user can open the saved transcription to review the full text.  
6. Extensions: The app may allow for simple text edits or annotation during review.  
7. Exceptions: If the transcription is incomplete due to audio issues, the user may need to manually correct parts of the text.

**4\. Use Custom LLM for Transcribing Multiple Accents**

1. Actors: User (e.g., conference attendee).  
2. Trigger: The user needs to transcribe multiple speakers with different accents during a panel discussion.  
3. Preconditions: The app is set up to capture audio, and the custom LLM is optimized for recognizing various accents.  
4. Postconditions (Success Scenario): The app accurately transcribes the speech of multiple speakers with different accents in real-time.  
5. Steps:  
   1. The user starts a transcription session during a multi-speaker panel.  
   2. The app captures the audio and uses the custom LLM to transcribe the speech from various speakers with different accents.  
   3. The transcription appears in real time with high accuracy across speakers.  
6. Extensions: The user can tag or identify different speakers in the transcription.  
7. Exceptions: Some accents may pose challenges for the model, leading to occasional errors.

**5\. Transcribe Short Notes Using Voice**

1. Actors: User (e.g., individual needing to capture quick notes).  
2. Trigger: The user needs to transcribe short personal notes on-the-go using their voice.  
3. Preconditions: The app is set up, and the user is ready to speak into the microphone.  
4. Postconditions (Success Scenario): The app quickly transcribes the user’s short notes and displays them on-screen.  
5. Steps:  
   1. The user opens the app and selects "Start Transcription."  
   2. The user speaks short notes into the app, such as to-do items or ideas.  
   3. The app transcribes the spoken notes in real-time.  
   4. The transcribed notes are displayed and saved automatically  
6. Extensions: The app can automatically save notes in a designated folder for easy retrieval.  
7. Exceptions: If the user speaks too fast or the audio is unclear, the app might produce minor transcription errors.

# **4\. Non-Functional Requirements**

1. Reliability: The app must efficiently handle complex transcriptions consistently.  
2. Usability: The interface must be intuitive for users with minimal technical expertise. (Stretch: offering clear options for language selection and audio output)  
3. Security and Privacy: All transcriptions and translations should be securely handled locally, ensuring that sensitive conversations are not exposed.

# **5\. External Requirements**

1. Error Handling: The app must robustly handle invalid input or failures in audio capture, with fallback mechanisms to avoid disrupting the user experience.  
2. Installation and Accessibility: The product must be easy to download and install via public sources.  
3. Source Buildability: Instructions must be provided for building the app from source to allow new developers to set up the app.

# **6\. Team Process Description**

## **Software Toolset:**

1. PyTorch: For custom LLM development.  
2. PyAudio: For audio capture and processing.  
3. OpenAI GPT-3.5: For translation services.  
4. GitHub: For version control.  
5. Python: For ease of use and syntax familiarity.

## **Schedule:**

* Milestone 1: Audio capture setup (Week 2).  
* Milestone 2: Architecture for speech to text (Week 4).  
* Milestone 3: Initial transcription model (Week 6).  
* Milestone 4: Full MVP with testing and debugging (Week 8).  
* Milestone 5: Integration of translation and text-to-speech (Week 10).

## **Risks:**

1. LLM Development Complexity: The team may struggle with training the LLM efficiently.  
2. Noise Handling: Accurately transcribing speech in noisy environments could be difficult.  
3. System Integration: Integrating all system components may lead to unforeseen technical challenges.

## **External Feedback:**

Feedback from external users will be most useful after the MVP is developed (around Week 10). We plan to reach out to potential users for beta testing and usability feedback.

# **7\. Software Architecture**

## **Overview of System Components**

Our system consists of the following major components:

* Frontend: User-facing interface, responsible for providing transcription functionality and user interaction.  
* Backend: Core system logic, including LLM integration and speech-to-text processing.  
* Storage: Stores transcription data as plaintext that is time stamped using local time.  
* LLM Model: A language model that handles transcription processing, speech-to-text conversion, and noise filtering.

## **Interfaces Between Components**

* The frontend communicates with the backend via events attached to callback functions.  
* The backend interacts with the filesystem in order to store the recorder transcriptions.  
* The LLM model is hosted through the backend, and directly accessed there.

## **Data Storage**

The system stores transcription data in plaintext locally. The transcriptions are labeled according to a timestamp of when they ended.

## **Architectural Assumptions**

* High concurrency and low latency are required for processing real-time transcription requests.  
* Scalability is built into the architecture, allowing the system to handle increased loads by deploying different LLM instances.

## **Architectural Alternatives**

* **Event-Driven Architecture**  
  * Pros: Event-driven systems are ideal for handling tasks that don't require an immediate response, like logging, notifications, or data processing. Services can publish events, and other services can consume them when ready, making the system highly flexible and adaptable.  
  * Cons: Because events are processed asynchronously, there can be delays in processing if event queues become overloaded. This may introduce latency in the system, particularly for tasks that depend on the immediate processing of events.


* **Microservices Architecture**  
  * Pros: Individual services can be scaled independently based on their load and usage. This allows for more efficient use of resources, as only the components needing more resources can be scaled up.  
  * Cons: Communication between services happens over the network, which can introduce latency compared to in-process communication in monolithic systems.

# **8\. Software Design**

## **Component Definitions**

* Frontend: Built using a modern Python framework (Tkinter). Additionally built a website using a React framework for JavaScript and a Tailwindcss framework for CSS. Both contain UI components that handle user input, display results, and manage application state.   
* Backend: Designed as a modular Python service. Implements the logic for transcription processing and LLM integration.  
* LLM Model: Accessed via internal libraries. The model is responsible for speech-to-text conversion and noise filtering.

## **Responsibilities**

* Frontend: Responsible for rendering the user interface and handling real-time updates for transcriptions.  
* Backend: Manages requests from the frontend, processes transcription data using the LLM, and interacts with the database.  
* LLM Model: Responsible for high-quality transcription and noise filtering.

# **9\. Coding Guidelines**

## **Coding Guidelines**

* For Python, we will follow the [PEP 8](https://peps.python.org/pep-0008/) style guide to maintain code readability and consistency.   
* For React, we will follow the [Airbnb JavaScript Style Guide](https://airbnb.io/javascript/react/) with a focus on React-specific best practices to ensure code consistency and maintainability.

### **Rationale:**

We chose PEP 8 style guideline because it is widely accepted and promotes clean, maintainable, and readable code. We will enforce it using automated linters such as Flake8 for Python. As for Airbnb's JavaScript style guideline, it is one of the most popular and widely adopted guides in the JavaScript and React communities. It emphasizes readability, promotes the use of modern ES6+ syntax, and encourages good component structure, improving maintainability in React projects.

# **10\. Process Description**

## **Risk Assessment**

1. **LLM Model Accuracy**  
   *Likelihood*: Medium  
   *Impact*: High  
   *Evidence*: Early tests show good accuracy in controlled environments, but noisy environments may pose a challenge.  
   *Mitigation*: Continue testing under different conditions, apply noise filters.  
2. **Backend Scalability**  
   *Likelihood*: Medium  
   *Impact*: High  
   *Evidence*: Current infrastructure supports limited concurrency, where larger amounts of speech can bottleneck the LLM.  
   *Mitigation*: Implement threading for consecutive LLM processing.  
3. **Transcription Latency**  
   *Likelihood*: Low  
   *Impact*: Medium  
   *Evidence*: Latency is manageable but spikes under difficult transcriptions.  
   *Mitigation*: Implement audio filtering to avoid this scenario.  
4. **Team Availability**  
   *Likelihood*: Medium  
   *Impact*: Medium  
   *Evidence*: Team members may face unexpected personal or work conflicts, leading to delays.  
   *Mitigation*: Cross-train team members to handle critical tasks, and maintain clear documentation.  
5. **Platform Compatibility**  
   *Likelihood*: High  
   *Impact*: Low  
   *Evidence*: Early testing shows the packages not working on mac.  
   *Mitigation*: Implement platform specific implementations.

## **Project Schedule**

| Milestone | Task | Dependencies | Person Responsible | Due |
| ----- | ----- | ----- | ----- | ----- |
| GitHub Setup | Set up the GitHub repo for hosting the application source |  | Nikita | 9/18 |
| GitHub Branching | Established a branching strategy to ensure smooth collaboration. |  | Andzhur | 9/18 |
| Audio Capture | Implement live audio capture |  | Matthew | 9/25 |
| Hugging Face Setup | Set up the Hugging Face platform for LLM deployment |  | Nikita | 10/02 |
| Transcription | Set up Whisper small model for transcription | Hugging Face Setup | Sandro | 10/02 |
| UI Design | Design a prototype UI |  | Tanneh | 10/09 |
| UI Design (website) | Develop a frontend UI of the website |  | Andzhur | 10/09 |
| Live Transcription | Implement real-time transcription functionality | Audio Capture, Transcription | Sandro | 10/09 |
| Output Saving | Save transcriptions to plaintext files | Transcription | Matthew | 10/09 |
| UI Implementation | Integrate the UI created by Tanneh and Andzhur | UI Design, UI Design (website) | Nikita | 10/16 |
| Platform Support | Add support for mac & linux machines | Audio Capture | Matthew | 10/23 |
| UI Testing and Debugging | Test real-time transcription and UI interaction | UI Implementation | Andzhur | 10/23 |
| Speed Optimization | Optimize real-time transcription speed | Live Transcription | Nikita | 10/30 |
| Fine tuning the LLM | Fine tune the LLM for more accurate and fast transcription | еLive Transcription | Sandro | 10/30 |
| Documentation and Packaging | Write user guide for local app usage | Fine tuning the LLM | Andzhur | 11/06 |
| Door to Door Testing | See how other people utilize and set up our application | Documentation and Packaging | Tanneh | 11/06 |
| Revise Documentation | Work on making the documentation more refined | Door to Door Testing | Matthew | 11/13 |
| Final Integration | Perform end-to-end system tests | Fine tuning the LLM | Nikita | 11/20 |
| Distribution | Package the app for distribution | Final Integration, Documentation and Packaging | Matthew | 11/27 |

## **Team Structure**

* Nikita P. – Backend Lead – Project Owner (Integration) – Responsible for integrating the LLM and building the backend.  
* Sandro K. – LLM Developer – Project Owner (LLM) – Responsible for developing and fine-tuning the LLM.  
* Andzhur T. – Frontend Developer – Project Owner (Front End) – Focuses on building the UI and noise filtering solutions.  
* Matthew H. – Audio Engineer – Project Owner (Audio) – Handles audio input and live audio capture.  
* Tanneh J. – UI Designer – Project Owner (UI) – Ensures a seamless user experience from live audio capture to real-time transcription.

## **Documentation Plan**

1. **Installation Guide**  
   * **Purpose**: Provide clear, step-by-step instructions for users to install and set up the application on their local machines.  
   * **Contents**:  
     * **System Requirements**: Specify the necessary hardware and software prerequisites, including operating system compatibility and any dependencies (e.g., Python version, libraries).  
     * **Installation Steps**: Detail the process for downloading the application, setting up any required environments, and installing dependencies. This may include:  
       * Cloning the repository from version control (e.g., GitHub)  
       * Installing required packages (e.g., using pip for Python)  
       * Configuring the local environment (e.g., setting environment variables)  
     * **Troubleshooting**: Provide solutions for common installation issues that users may encounter, along with error messages and possible resolutions.  
2. **User Guide**  
   * **Purpose**: Offer comprehensive instructions on how to use the transcription features of the application, ensuring that users can effectively utilize its functionality.  
   * **Contents**:  
     * **Overview of Features**: Describe the main functionalities of the application, including audio capture, real-time transcription, and saving transcripts.  
     * **Step-by-Step Instructions**: Provide detailed usage instructions, including:  
       * How to start the application  
       * How to capture audio input and initiate transcription  
       * How to access and save transcription results  
     * **Best Practices**: Suggest tips for achieving optimal transcription accuracy (e.g., microphone placement, audio quality considerations).  
     * **FAQs**: Address common user questions and scenarios, helping users troubleshoot their issues without external assistance.  
3. **Developer Guide**  
   * **Purpose**: Serve as a reference for developers working on or extending the application, explaining the underlying architecture and design decisions.  
   * **Contents**:  
     * **Overview of the Architecture**: Describe the overall monolithic architecture, detailing how different components interact with each other (e.g., UI, transcription engine, file management).  
     * **Code Structure**: Outline the organization of the codebase, including key directories, modules, and their purposes.  
     * **Component Descriptions**: Provide in-depth explanations of critical components, such as:  
       * Audio capture module  
       * Transcription handling logic  
       * File I/O operations  
     * **Development Environment Setup**: Include instructions for developers to set up their development environment, ensuring consistency across the team (e.g., virtual environments, code style guidelines).  
     * **Contribution Guidelines**: Outline how other developers can contribute to the project, including code formatting standards, how to submit changes, and testing practices.

