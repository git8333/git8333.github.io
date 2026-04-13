# CS Final

## Self Assessment

Throughout the Computer Science program, I was able to build a strong foundation across multiple areas of the field, such as software engineering, database management, algorithms, and security. This ePortfolio represents the work I have done throughout the program, and showcases the skills I have developed through a single enhanced artifact, which is an animal shelter dashboard built using Python, Dash, and MongoDB.


### Collaborating in a Team Environment

Throughout the program, working with others was a big part of the experience. Creating a code review and receiving feedback from the instructor constantly taught me how important it is to write code that is clean and easy to follow, not just code that works. The code review I did for this capstone was a good example of that, as I had to go through existing code, identify what was wrong with it, and explain my findings and plans in a way that someone else could understand and follow.

### Communicating with Stakeholders

Communicating clearly is something I have improved on throughout the program. Writing narratives and doing presentations helped me get better at explaining technical things to people who may not have the same background. The narratives I wrote for each enhancement show that I am able to break down what I did and why I did it in a way that makes sense to whoever is reading it.


### Data Structures and Algorithms

For the algorithms and data structures enhancement, I had to analyze where the performance issues were and figure out how to fix them. The original filtering logic was scanning the entire dataset every single time the user selected a filter, which was slow and inefficient. I implemented a dictionary-based caching system to store the results so they would not have to be recalculated every time. I also fixed the charts to show data for the full filtered dataset instead of just the current page, which required understanding how data moves through the application.


### Software Engineering and Database

For the software engineering enhancement, I took the original single file application and broke it into four separate modules, each handling a specific part of the application. This made the code much easier to maintain and understand. I also replaced the hardcoded credentials with environment variables and replaced the broken map component with an Outcome Type bar chart that actually works with the available data. For the database enhancement, I added error handling to all four CRUD operations, fixed logic errors in the update and delete methods, and added indexes on commonly queried fields to speed up queries on the large dataset.


### Security

Security was something I had to actively think about during this project. The original code had the database credentials hardcoded directly into the source file, which is a serious vulnerability if the code is ever shared or uploaded publicly. I fixed this by moving the credentials to environment variables, which keeps them out of the codebase entirely and aligns with how it should be done professionally.


### Summary

The artifact in this ePortfolio, the animal shelter dashboard, brings together all three areas of enhancement into one project. The software engineering enhancements improved the structure and security of the application. The algorithms and data structures enhancements improved its performance. The database enhancements made it more reliable and scalable. Together these improvements show my growth across the different areas of computer science covered throughout the program and my readiness to work as a software developer.

## Code Review

[Click here to watch the Code Review](https://www.youtube.com/watch?v=oxhRv6z0qtc)

## Artifact: Animal Shelter Dashboard

This project is an animal shelter dashboard built using Python, Dash, and MongoDB.

## Enhancement One: Software Design and Engineering

**Original Code:** - [Download Original Code (zip)](Original%20No%20Enhancement%20Code%20(2).zip)
- [ProjectTwoDashboard (1).ipynb](ProjectTwoDashboard%20(1).ipynb)
- [python_module_one.py](python_module_one.py)

**Enhanced Code:** - [Download Enhanced Code (zip)](Final%20CS%20Code%20Enhanced.zip)
- [dashboard.ipynb](dashboard.ipynb)
- [database.py](database.py)
- [layout.py](layout.py)
- [callback.py](callback.py)
- [python_data.py](python_data.py)

**Narrative:**

The artifact selected for this enhancement is the animal shelter dashboard created during an earlier class. It was originally built to identify dogs suitable for search and rescue training through filtering based on breed, age, and sex. The project is a Python-based web dashboard built using the Dash framework, with a MongoDB database to store animal records, and a CRUD module to handle database operations.

This artifact was selected because it showcases a wide range of skills and abilities in software development, such as web development, database management, data handling, and software design. The modularization of the code demonstrates an understanding of software design principles, and the redesign of the map component into an Outcome Type bar chart demonstrates the ability to identify shortcomings and adjust accordingly. The use of the Dash framework alongside MongoDB also demonstrates the ability to work with a full-stack application. The artifact was significantly improved by separating the single-file application into four distinct modules: database.py, layout.py, callback.py, and dashboard.ipynb. Each file handling a different part of the application. Hardcoded credentials were moved to environment variables to address a security vulnerability, and the broken map component was replaced with an Outcome Type bar chart that better reflects the available data.

The process of enhancing and modifying the artifact presented a few challenges. The first was that the environment originally used in the previous class had its own dedicated database for the animal shelter, which was no longer accessible. This required rebuilding the database connection, re-importing the dataset, and rewriting parts of the code to work in a local environment. This experience reinforced how important it is to write environment-independent code, as not every developer will be running a project in the same setup. Replacing the map component also provided a valuable learning experience, as it required learning how to implement a new chart type, which took a while. All course outcomes planned for this enhancement were met. The planned functionalities were implemented, several bugs found throughout the code were corrected, and the modularity issue, which was the most significant concern given that all logic was in a single file has been fully addressed.

Feedback received from the instructor during the review reinforced that the enhancement plan was on the right track and that the course outcomes were being addressed.


## Enhancement Two: Algorithms and Data Structures

**Code:** Same artifact as above
**Original Code:** - [Download Original Code (zip)](Original%20No%20Enhancement%20Code%20(2).zip)
**Enhanced Code:** - [Download Enhanced Code (zip)](Final%20CS%20Code%20Enhanced.zip)

**Narrative:**

The artifact selected for this enhancement is the animal shelter dashboard created during an earlier class. It was originally built to identify dogs suitable for search and rescue training through filtering based on breed, age, and sex. The project is a Python-based web dashboard built using the Dash framework, with a MongoDB database to store animal records, and a CRUD module to handle database operations.

This artifact was selected because it showcases a wide range of skills and abilities in software development, such as web development, database management, data handling, and software design. The filter callback demonstrates my ability to work with data structures to manipulate and organize huge datasets. The implementation of a dictionary caching system shows my fundamental understanding of how data structures can be utilized to improve performance. Through storing previous filter results in a dictionary and checking for cached results before reprocessing, the application avoids redundant computation on each filter select.

The process of enhancing the algorithms and data structures category of the project taught me a lot about data and how it flows through an application. It took a while to fix all the filters to work as expected, and once they were working, the dataset was very large and filtering was slow. Adding caching significantly improved the performance, which taught me how important it is to consider performance early on in a project rather than as an afterthought. Fixing the charts to reflect the full dataset instead of just the current page was also challenging at first, since filtering to a specific animal type had to be reflected accurately across all the charts at the same time. Overall, the process was a very valuable learning experience. All course outcomes planned for this enhancement were met. The planned functionalities were implemented. All the previous bugs in the filtering logic were corrected, a caching system was implemented to improve performance, and the charts were fixed to show data for the full dataset instead of just the current page. Those were the enhancements completed for this category. 

Feedback received from the instructor during the review reinforced that the enhancement plan was on the right track and that the course outcomes were being addressed.


## Enhancement Three: Databases

**Code:** Same artifact as above
**Original Code:** - [Download Original Code (zip)](Original%20No%20Enhancement%20Code%20(2).zip)
**Enhanced Code:** - [Download Enhanced Code (zip)](Final%20CS%20Code%20Enhanced.zip)

**Narrative:**

The artifact selected for this enhancement is the animal shelter dashboard created during an earlier class. It was originally built to identify dogs suitable for search and rescue training through filtering based on breed, age, and sex. The project is a Python-based web dashboard built using the Dash framework, with a MongoDB database to store animal records, and a CRUD module to handle database operations.

This artifact was selected because it showcases a wide range of skills and abilities in software development, such as web development, database management, data handling, and software design.  This artifact is also a project centered around a database. It directly involves database management, and the main idea of the project is to manipulate the data retrieved from the database. Proper error handling was implemented across all four CRUD operations, and indexes were added on commonly queried fields such as Animal Type and Breed, which improved the performance of the app. This demonstrates my ability to optimize database performance as well as my ability to write reliable code with error handling.

The process of enhancing and modifying the database category taught me a lot about the importance of proper error handling. There was not much error handling prior to this enhancement, which luckily did not cause issues since the application worked as expected. However, in a full scale application where input is constantly being added, proper error handling is essential, as it helps developers identify and fix problems and prevents the application from crashing randomly. Adding error handling taught me how to write safer code. Adding indexes also reinforced the importance of considering performance early on in a project, as the indexes had a noticeable impact on the speed of database queries when working with a large dataset. All course outcomes planned for this enhancement were met. The planned functionalities were implemented. Error handling was implemented across all CRUD operations, which ensures that any errors that arise are caught and handled properly rather than crashing the application. Indexes were also added on commonly queried columns, which was necessary given the size of the dataset as querying was taking a noticeable amount of time without them. All planned course outcomes have been covered and the project is finalized.

Feedback received from the instructor during the review reinforced that the enhancement plan was on the right track and that the course outcomes were being addressed.
