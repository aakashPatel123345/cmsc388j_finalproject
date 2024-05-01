
## CMSC 388J Final Project Proposal

**Group Members (1-4 members):**


```
Select your group members in gradescope!!!
```

**Directions:**

Read the project specifications and fill out all the questions **in gradescope!**

> [!IMPORTANT]
> All the answers to the questions should be submitted to the gradescope submission with all
> of your group members selected


## Logistics

There are 4 things you will submit for the final project (only 1 group member has to submit, but select all members names in gradescope):

1. Proposal
2. Project code
3. Writeup (submit when you submit your project’s code)
4. Pretty Project (Extra credit due at the end of the semester)


Both the Proposal and Writeup use this document as a template (your writeup will likely be the same or similar to your proposal depending on how much has changed since your proposal document).

**Due dates (unless specified elsewhere):**

Proposal: April 12, 2024

* We **highly recommend** you complete this as early as possible so you have more time to work on the project. We will review your proposal within 1-2 days of submission.

## Overview

The final project for this class is to create a Flask app in a group of 1-4. You have a lot of freedom for this project as long as you meet the requirements. 

**You’re welcome to use Project 4 (or any other project from this course) as a base (though you’re not required to–in fact, we encourage you to try creating something from scratch)**. *If you choose to use a course project, you need to make a “substantial” change. Examples of “substantial” changes include:*

* Using a different API (instead of the OMDB API) + minor feature to demonstrate knowledge of Flask
* It’s no longer a “review site” but something else
* It’s still a “review site” but you add a major feature
* Examples: ability to reply to reviews

Use your best judgment here but reach out to course instructors if you’re unsure. 

```
Description of your final project idea:

This is a music searcher, reviewer, and playlist creation app. Using the Spotify Web API, users can search for any song or artist. They are then presented with the top 16 results. Users can click each track to get more information on the song. Users can leave reviews, add a song to their favorites playlist, and view reviews left by other users. 

```



## Requirements

Note that some of these requirements overlap with each other so some features may satisfy multiple requirements.  

**Registration and Login:**



* There needs to be some sort of user control: logging in, registering, logging out.
* Certain features should only be available to logged-in users.

```
Describe what functionality will only be available to logged-in users:

Logged-in users get the following functionalities that non-users do not get
  --> Leaving reviews for songs
  --> Adding songs / tracks to a favorites playlist that is specific to their account
  --> View an account information where they can see their user information including their favorites


```



**Forms:**



* At least 4 forms (can include registration and login forms)
* Must be CSRF protected

```
List and describe at least 4 forms:

Form 1:

  --> Login Form
      This form asks users for a username and password, and if correct are successfully logged in to the website

  --> Registration Form
      This registration form asks users for a username, email, password, and a passform confirmation field. Usernames or emails that are already taken 

  --> Review Form
      This form allows users to provide a review (in the form of a TextField)


  --> Search Form
      This form allows users to search for whatever artist or track they want. 
```



**Blueprints:**



* Must have at least 2 blueprints 
* Each blueprint should have at least 2 visible and accessible routes

```
List and describe your routes/blueprints (don't need to list all routes/blueprints you may have–just enough for the requirement):

--> Song Blueprint
      This blueprint is for songs
      Here are all the routes for this blueprint

            “/” ⇒ the home page
            “/search_results/<query> ⇒ the route that leads users to their search results (based on what they searched)
            “/song/<song_id>” ⇒ the route that leads user to a specific song after they click on a result.
            “/user/<username>” ⇒ the route that leads users to a specific user’s profile. 


--> User Blueprint
      This blueprint is for users
      Here are all the routes for this blueprint
            “/register” ⇒ the route that lets users complete the registration form
            “/login” ⇒ the route that lets users complete the login form. Users are redirected to this route after registration
            “/logout” ⇒ log the current user out
            “/account_details” ⇒ displays the account details for the user

```



**Database:**



* Must use MongoDB

```
In MongoDB I will store the following

--> User Information
      User information necessary for logging in. I will store each user’s username, email, and hashed password. In addition I will also store an array representing the user’s favorites playlist
--> Reviews
      Each review will be stored with the following information: review content, date, username (which user submitted the review)
```



**Another Python Package or API:**



* Find and use another Python package or API.
* Must be a package/API we haven’t used in any of the projects (though anything mentioned in lecture material that wasn’t used in a project is fair game).
* You can use a package/API we’ve already used if you’re using it in a way that’s _very_ different from how we used it in the projects.
* Must affect the user experience in some way.

Examples (feel free to use these or come up with your own):



* Flask-Mail to send emails to users
* CalorieNinjas API with Requests package to access the API
* Spotify API
* Requests package to display data retrieved from an HTTP request
* BeautifulSoup4 to display data parsed from a website
* SciPy, NumPy, SymPy, etc
* Plotly  
* Discord OAuth
* CAS 

```
Describe what Python package or API you will use and how it will affect the user experience:

I have used the Spotify Web API
Every time the website is loaded, I request an access token to be used in the search process. The request token is then loaded (hourly limit which can be reset by refreshing the page) and is then used in the track / track information retrieval process. 

```

**Presentation:**

* Doesn’t have to be pretty but it needs to be usable.
  
> [!NOTE]
> Theres going to be a EC part of the project due on the last day of the semester where you can use tailwind/react/svelte/css to make your website more pretty, up to 25%!!!

## Grading

<table>
  <tr>
   <td>Requirement
   </td>
   <td>Points
   </td>
  </tr>
  <tr>
   <td>Proposal submitted
   </td>
   <td>100
   </td>
  </tr>
  <tr>
   <td>Writeup submitted (same format as the proposal) 
   </td>
   <td>100
   </td>
  </tr>
  <tr>
   <td>Registration and Login
   </td>
   <td>75
   </td>
  </tr>
  <tr>
   <td>Forms
   </td>
   <td>50
   </td>
  </tr>
  <tr>
   <td>Blueprints
   </td>
   <td>50
   </td>
  </tr>
  <tr>
   <td>Database
   </td>
   <td>50
   </td>
  </tr>
  <tr>
   <td>Another Python package or API
   </td>
   <td>75
   </td>
  </tr>
</table>


Total: 500 points
