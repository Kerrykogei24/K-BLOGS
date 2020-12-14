# K-BLOGS
## By Kerry Kogei 

## Description
Are you looking for a Picth of the week to brighten up your day and your week? Here you can find a list of positive quotes to help you get through a tough week!    


## User Story

1. As a user, I would like to see the blogs other people have posted.
2. As a user, I would like to vote on the blog they liked and give it a downvote or upvote.
3. As a user, I would like to be signed in for me to leave a comment
4. As a user, I would like to receive a welcoming email once I sign up.
5. As a user, I would like to view the blogs I have created in my profile page.
6. As a user, I would like to comment on the different pitches and leave feedback.
7. As a user, I would like to submit a blog in any category.
8. As a user, I would like to view the different categories.            

## Setup Installation
* Clone the repository
 ```https://github.com/Kerrykogei24/K-BLOGS```

* cd k-pitches

* To test the application
 ```python3.6 manage.py test```

* To run the application, in your terminal:

        $ chmod +x start.sh
        $ ./start.sh

## Behaviour Driven Development
| Behavior            | Input                         | Output                        | 
| ------------------- | ----------------------------- | ----------------------------- |
| View Product Pitches | Click on any category | Taken to the clicked category | Click on `Click    submit To Post A Pitch` | Redirected to the login page | Signs In/ Signs Up |
| Click on `Click create a new To Post A Blog` | If logged in, display form to add a pitch | Redirected to the home page |
| Click upvote/ downvote button | Redirects to home page | Upvote/ downvote count changes | Click add comment button | Redirects to the comment page | Displays a comment form | Click on Sign Out | Redirects to the home page | Signs user out |
| Click on profile | Redirects to the profile page | User adds bio and profile picture |

## Technology used

* Python3.6
* Flask
* Heroku

## Contact Information 

If you have any question or contributions, please email me at [kerrykomar@gmail.com]

### License
  [MIT] Copyright (c) 2020 Kerry Kogei

