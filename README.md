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

**Class Diagram** 

Four models, which all relate to a single database table, are created in this commerce webapplication.
- The *user* class contains all info from the user logged in into the web application
- The *bids* class contains all info of one particular bid, it also contains the info of the *user* 
- The *comments* class gathers all info of the comments, it also contains the info of the *user* 
- The *listings* class represents all information about one individual listing, it also contains the info of the *user* who is the owner of the listed item. More over, it saves all bidding by objects of the *bids* class and it also saves all comments by objects of the *comments* class.

The complete overview is displayed in the image below.

![Overview](/images/ClassDiagram.png)


**Overview of database-info pro website page** 

The table below displays an overview of the database info which is used at each part of the website.

![Overview](/images/Database.png)