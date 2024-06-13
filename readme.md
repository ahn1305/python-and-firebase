# Firebase in python

### **What is firebase ?**

Firebase is a Backend-as-a-Service (Baas). It provides developers with a variety of tools and services to help them develop quality apps, grow their user base, and earn profit. It is built on Google's infrastructure. Firebase is categorised as a No SQL database program, which stores data in JSON-like documents.

**PS:** Don't worry much about the explanation about Firebase, it's just a definition from google. Firebase is  just some cloud thing that provides various features like **storage, authentication, and  real-time database support**, which we can use to integrate in our code.

 Here we will be mainly focusing on how to integrate Firebase and python.

### **How do we integrate Firebase (not only firebase any application) to our program ?** (Traditional Way)

A traditional way of doing this is using an **API** (Application Programming Interface) directly,  In laymen terms it is nothing but some URL's using which we can access a specific website for fetching data and using their services.

**EG:** Lets take the weather forecast applications in our mobile as an example, the **application provider does not go and setup some weather detectors** and give us that data, **rather what they do is they use API's provided by some third party** which has got these data already, the application provider just fetches the data and displays it.

If you want a better understanding of what an API is you can watch this video: https://www.youtube.com/watch?v=s7wmiS2mSXY

### **Problem with the traditional way** 

Doing the API call directly in our code is way too complicated than what we think. As a beginner we'll like **WTF are these things bro**. Don't worry Firebase ka docs has suggested an easy way to use their API, it's nothing but an **API Wrapper**.  

### **What are API wrappers?**

**API wrappers** are **language-specific kits or packages that wrap sets of XML API calls into easy-to-use functions**.

Again don't worry about what this is, the line says that **rather writing multiple lines of code to do an API call** you can use **wrappers** that are nothing but some **functions** (functions are just block of codes that does a specific jobs that are repetitive). In even more simple terms rather writing multiple lines of code We will be using something called functions and pass some values to it, which does the same job.

### **Pyrebase**

So in order to use Firebase API we will be using a API wrapper called **Pyrebase** (version 4) using which we can connect to our **Firebase Application.** If you don't know what is Firebase Application just forget these things, I'll cover this up later. 

Ultimately what I'm trying to convey is we will be using this API wrapper called **Pyrebase4** that is a python package using which we can connect to an Firebase application from our local machine, basically it's an intermediate.

https://github.com/ahn1305/python-and-firebase/tree/main/application - Try this sample application that I have made

<b>Other Resources:</b> <br>
https://github.com/nhorvath/Pyrebase4 - Pyrebase Package <br>
https://sharma-vikashkr.medium.com/firebase-how-to-setup-an-app-in-firebase-9ddbacfe8ad1 - Tutorial to setup a firebase project<br>
https://firebase.google.com/docs - Firebase Official Docs







