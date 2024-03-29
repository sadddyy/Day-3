#!/usr/bin/env python
# coding: utf-8

# In[7]:


### Google text to speech for various inputs.

from gtts import gTTS
import os

def text_to_speech():
    
    while True:
        text=input()
        tts=gTTS(text=text, lang='en', slow=True)
        tts.save("output2.mp3")
        os.system("start output2.mp3")
        
        yesno=input()
        if yesno=="no":
            break


# In[ ]:


text_to_speech()


# In[ ]:




