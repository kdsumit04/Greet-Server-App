#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask
app = Flask(__name__)
@app.route("/greeting/<name>")
def greeting(name):
        return "Hello " + name 

if __name__ == "__main__":
    app.run(host ='0.0.0.0',port=80)


# In[ ]:




