**1.**      **Verifying Non-Functional Requirements (NFRs)**

**Determine which of the following are valid NFRs. For each valid NFR, briefly describe how you would test it. For each invalid NFR, explain why it is invalid**
**(a)**    **The system must support the PNG, JPG and GIF file formats when saving and loading images.**
Valid - interoperatability


**(b) The system must support acquiring images from screenshots and connected camera devices.**
not valid - functional
not valid - ambigious

**c) The system must save images within 1ms.**
<span style="color:#ff0000">not valid - performance but does not specify fixed hardware</span>

**(d) The system must support images of up to 100 megapixels.**
<span style="color:#ff0000">not valid - ambigiou</span>s

**(e) The “colour enhance” function should take at most 250 ms to enhance a 10 megapixel image on an average PC.**
not valid - can't say "average PC" - model should be specified

**(f) When performing the full range of image manipulation functions on images of up to 100 megapixels, the system should crash no more than once every 1000 hours it spends running.**
valid - reliability - ROFOD

**(g) Once restarted after a crash, the system should be able to recover unsaved images open at the time of the crash.**
not valid - functional

**(h) Photo-manipulated images must be suitable for inclusion in a photo album.**
not valid - not in scope, ambigious

**(j) An average user must take over 1 minute to open an image, on top of the time taken by the system to read and display the file.**
not valid - not in scope (no one wants this)


**2.**      **Performance Requirements**
**Propose a useful and valid performance requirement for each of the following:**

**(a)**    **A software system that enables a car to drive itself.**
The braking system must respond within 1 second of seeing a pedestrian inside it's driving lane (tested on a 2024 base model)

**(a)**    **A text-to-speech system that can read documents out loud.**
The text-to-speech system must translate atleast 70 words per minute (tested on its early release model)

**(a)**    **An equation-proof system that tries to automatically prove that two sides of a mathematical equation are equal.**
The equation-proof system must not use more than 500MB of RAM for proving a mathematical equation with less than 3 operators (evaluated on the free-release version)

**3.**      **Reliability Requirements Propose a useful and valid reliability requirement for each of the following:**

**(a)**    **A software system that enables a car to drive itself.**
The autonomous car software system must have an MTTF (mean time to failure) of 2 years

**(b) A face recognition system for spotting wanted suspects in a crowded public place.**
The facial recognition system must have a POFOD (probability of failure on demand) of 0.01% of ATTEMPTS

**(c) A software system for monitoring weather data to forecast cyclones and other storms.**
The weather forecast system must a MTTF of 12 months


**4.**      **Usability Requirements**

**Propose a useful and valid usability requirement for each of the following:**
**(a)**    **A software system that enables a car to drive itself.**
The navigation system must enable the user to select a destination on a single screen

**(b) On online banking system.**
The online banking system must allow users to complete an internal transfer within 5 clicks

**(c) A voice-activated “smart-home” system (for remotely/automatically controlling various devices around your house).**
The smart home must enable users to select the correct device to control at least 98% of the time


**5.**      **Additional task: NFRs other than performance, reliability, and usability**

**Select any of the systems given in question 2, 3 or 4 and propose a useful and valid,**

**(a) Security requirement,**
The online banking system must not store unencrypted passwords 

**(b) Interoperability requirement,**
The smart home system must be able to communicate to zigabee protocol controlled devices (in addition to it's home brand)

**(c) Localization requirement,**
The autonomous car navigation system must be able to be displayed in Chinese and English

**(d) Accessibility requirement,**
The text to speech system must be able to take voice commands to alter settings

