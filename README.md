#TechAfrica

Introduction 
I had this idea during one of my early morning thoughts – Morning Pages.
The idea came up from a problem I identified, I remember I usually surf the internet for a related problem to my gadget or a client’s gadget before attempting a fix. All my searches were about 80% foreign-based experiences and how they got them resolved based on their environments. As a computer engineer, I am able to relate since I have been educated and trained, my pressing thoughts, ‘but what of the average African computer literate?’ What of the individual whose daily activities does not align with continuous usage of the pc but randomly encounters these technical issues using them? 
Such people and tech geniuses can have this common tech grounds where they can share their experiences with gadgets or tech tools based on our African settings, which can be of invaluable assistance to someone somewhere in Africa. I got this quote thinking about this problem, “your conquered mountain is another person’s obstacle, share how you successfully conquered it and you’d make a leader out of yourself” 
What is TechAfrica?
TechAfrica is an online platform where people (Africans as targeted audience) can visit, register as Technical experts who can share a tech problem and solution and also to offer expert’s simple-approach or give advice to technical issues before initiating an on-premises assistance if needed or usual users who registers to share a technical problem needing technical advice. Let us talk about Tech problems and solutions in ways we can resonate with as Africans, that we can understand Africans. 


TechAfrica

1. Project Goal
Build a RESTful backend API where:
•	Normal users post tech issues and share thoughts
•	Experts respond with solutions and tips
•	Experts have a visible badge
•	Images can be uploaded for issues, solutions, and tips
•	Secure, scalable, and production-ready architecture
________________________________________
2. Tech Stack
•	Python 3
•	Django
•	Django REST Framework
•	JWT Authentication
•	PostgreSQL (prod) / SQLite (dev)
•	Pillow (image uploads)
________________________________________
3. Project Structure
TechAfrica/
├── TechAfrica/        # Project config
│   ├── settings.py
│   ├── urls.py
│
├── accounts/          # Users & experts
├── issues/            # Tech issues
├── solutions/         # Expert solutions
├── tips/              # Tech tips
├── comments/          # User thoughts/comments
├── manage.py
________________________________________



Sample users and issues
{
    "username":
        "Frank"
    ,
    "password":
        "frank123"
}


{
    "title": "iPhone 8 charging issue",
    "description": "I struggle to make my Iphone 8 charge",
    "user": 1
}

{
    "username":
        "Mike"
    ,
    "password":
        "mike123"
}


{
    "title": "Dell laptop suddenly overheating ",
    "description": "My dell laptop I bought last year is suddenly overheating,
    "user": 1
}

