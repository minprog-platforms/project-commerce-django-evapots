# Design Document: *Commerce*

### **Aim**: *Design an eBay-like e-commerce auction site that will allow users to post auction listings, place bids on listings, comment on those listings, and add listings to a “watchlist.”*
<br>

**Application Workflow** <br>
The image below displays the general workflow of the commerce application. The default page is the *active listings* page. The outline of the website differs whether the user is logged in or not.

When the user **is not** logged in, the user has the option to register, to log in or to view the active listenings and thereby the individual listings pages. However, particular parts of the individual listing page, such as the bidding option and the option to add the listing to the watchlist, are not observable.

When the user **is** logged in, the header immediately changes. The user is now also able to:
- Get to a page which filter the active listenings by category
- Add listening to his/her watchlist and observe this watchlist
- Bid on active listenings
- Comment on active listenings
- Create a new listening 
- Log out and return to the default *active listings* page

When the logged in user is on an individual listenings page of his/her own, than there is also a button which enables the user to close the auction. The user that has won the auction is able to view that he/she won the bidding on the closed listening page. 


![Overview](/images/Commerce.png)

TODO 2: Anaylise which models you are going to need and create Class Diagram 
- each model maps to a single database table.
- each attribute of the model represents a database field.


TODO 3: Make an overview of which pages will be using what information from the database

## Getting Started

TODO: Describe steps to install requirements and get the application running.
