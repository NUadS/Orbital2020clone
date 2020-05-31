Team Name: NU(advert)S

Proposed Level of Achievement: Gemini (Intermediate)

Problem Motivation: Currently, there is a lack of a common platform for survey conductors to publicise their surveys to the NUS community. As such, many students often take to various social media platforms such as Telegram, Instagram etc. to call for respondents. However, requests for survey respondents through such means are usually ignored as respondents do not see any form of benefits. Furthermore, the constant influx of messages and posts on social media platforms means that such surveys are usually neglected.

Aim: The aim of this project is to create a one-stop, comprehensive platform (website) where survey conductors can conveniently source for survey respondents and also to create incentives for the NUS community to participate in surveys. By resolving the lack of response motivation and lack of survey outreach, survey conductors can obtain a higher diversity/quantity/quality of responses and survey respondents can unlock attractive benefits while offering help through sharing their opinions.

Proposed Core Features:
1. Index, Login, Logout
- (optional) Authentication (Link account to email, forget password)

2. Administration page
- For handling database

3. Registration page
- List of compulsory/optional fields to be filled in

4. User Profile Page 
- Allow user to edit personal information

5. Surveys - Uploading and Details
 - Post a survey link which redirects users to the respective survey form (on external sites eg Google forms)
- Selection of target users attributes --> survey will only be pushed to users with such attributes
- Upon posting of survey link on database, eligible users will receive a notification and the survey link will be reflected on the ‘survey page’ of such users

6. Survey Completion
- Users must be able to click on the survey link and they should be redirected to the respective Google Forms
- The survey status on the app should show completed only when the google forms has been submitted.
- Each user is limited to one completion attempt. The system automatically records any completed attempts by any individual for any survey and denies subsequent attempts.

7. Reward System
- Points should be awarded to users after completion of each survey. 
- Points can be exchanged for vouchers (Points should be deducted after they receive the voucher)
- Users should be able to view how many points and vouchers they have. 

8. Report function
- To prevent misuse of application
- For respondents: to report inappropriate surveys eg contains discriminatory questions
- Reports will be redirected to admin, who will then carry out the necessary actions against rule-breakers.

9. Dashboard
- View of current points
- Create Survey button 
- View of pushed surveys
 
User Stories:
1. As a surveyor who wants to obtain authentic opinions from the NUS student community, I will be able to have a platform to share my survey to a diversity of students at a more efficient, effective and wide-ranging level.

2. As a surveyor with a target audience in mind, I will be able to filter out a target group of students to take my survey, based on certain attributes (eg Faculty/Gender). The survey will then be promoted accordingly to these groups of students.

3. As a surveyor who wants my surveys to have a wider reach, I will be able to promote my survey listings by participating in other surveys to gain points.

4. As a student respondent who wants to help out fellow students, I will be able to provide immense assistance to the NUS community by providing my opinions.

5. As a surveyor who would like to ensure that student respondents do not participate in the same survey more than once, I will be able to limit completed survey attempts to once per individual. The system automatically records any completed attempts by any individual for any survey.

6. As a student respondent who would like to be incentivised after completing a survey, I will be able to earn points after every survey completion, which can then be used to exchange for different rewards/vouchers that are typically related to amenities and dining offers in NUS. 

7. As users of the system, I will be able to flag out inappropriate survey content and responses. The administrators of the system will then send out warnings and subsequently ban users who continue doing so.

Tech Stack:
- Framework: Django 
- Database: SQL (django)
- Front-end Web Languages: HTML, CSS, Bootstrap 
- Back-end: Python, Javascript
 
Development Plan (Views):
- Index 
--> Allows users to choose between login and register
--> If users are already logged in, users should be redirected to the dashboard.

- Login 
--> Existing users: enables log in
--> Non-existing users: link to Registration page

- Logout 
--> When users logout from the dashboard, they will be redirected to the index page.

- Registration 
--> Users are to fill up mandatory fields to create their profile
--> Authentication link will be sent after registration. Upon verification of authentication, they will be linked to the Login page.
--> If account already exists, there should be a button which redirects them to login page.

- Dashboard
--> Should show: 
    1. No. of Points
    2. “Create Survey Link” Button (redirects to new post page)
    3. Recently pushed survey links (which they may complete)

- Navigation bar: 
--> Profile (Edit personal information)
--> Survey (Redirects to surveys page below)
--> Rewards (Redirects to rewards page below)
--> Logout (Redirects to logout page above)

- Profile 
--> Users should be able to edit their personal information/profile
--> Changes made using user’s account should be reflected accordingly on the Django administration page. 
--> (Depending on progress) Users should be able to delete their account. This should be reflected accordingly on the Django administration page.  

- Surveys
--> 3 different sections: 
    1. Completed Surveys: List of completed surveys and Points awarded for its completion
    2. Available Surveys: List of available surveys, which links the user to the respective Survey Details page. 
    3. Created Surveys: List of created surveys, which links the user to the respective Survey Details page. 

- Survey Details 
--> Users should be able to see the survey details (date of post, category etc.)

- Create Survey Link Post
--> Users should be able to post their survey links and details.
--> Survey links should be able to be viewed by other users as well. 
--> Users should be able to select the survey’s target group (optional). These surveys will then be pushed to the relevant users of that target group in the form of notifications. These surveys will also appear on the target users’ dashboards. 
--> Users should be able to delete their posted surveys
--> Users should be able edit the details of their posted surveys. 

- Survey Completion Page
--> After users successfully submit the surveys on Google Forms, they will be redirected to a survey completion page which indicates that:
    1. They have submitted the survey successfully
    2. Points earned from this survey 
    3. Total number of points they currently have
    4. View Rewards Button which will redirect them to the rewards page 

- Rewards Page
--> Display of current available points
--> Display of redeemable items 
--> (Depending on progress) Display of top items redeemed by NUadvertS users
