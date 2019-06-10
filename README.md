Takeaway
==

Django Milestone project.<br>
Project is for an online takeaway service.<br>
Website is designed for hungry users to easily view a wide selection of food to select and to make payment as intuitive and quick and easy as possible.<br>

UX
--

The main idea is to allow a user to make a food selection quickly and make a checkout for payment.<br>

Feature – Accounts app

As a customer user, I want to be able to register an account so that I can make orders
As a customer user, I want to be able to login to an account so that I can make orders
As a customer user, I want to be able to logout to an account so that I end my order session

Feature – Takeaway app


As a customer user, I want to be able to view all food items even if I am not login so that I know the food items available
As a customer user, I want to be able to search food items by name so that I can search for a particular food item
As a customer user, I want to be able search food by food categories so that I can search for a particular food item from a category
As a customer user, I want to view more of a food item so that I can decide to purchase the food item

Feature – Cart app


As a customer user, I want to be able to add a food item to cart so that I can order the food.
As a customer user, I want to select the quantity of food I want to order so that I do not need to click multiple times if I want to buy more than 1 quantity of the food item
As a customer user, I want to view the number of items in my cart from the dashboard so that I can keep track on my orders
As a customer user, I want to view all my orders and the total amount it cost so that I can review before payment

Feature – checkout app


As a customer user, I want to be able to input payment details at checkout so that I can make payment<br>

Features
==

In this section, you should go over the different parts of your project, and describe each in a sentence or so.

Existing Features<br>

Feature – Accounts app<br>

Feature is a user management tool that allow users to register and setup an account by filling out a form
A user upon registered, will be able to login to add orders and checkout<br>

Feature – Takeaway app<br>

Feature allow users to view all food items by loading all food items regardless if user is login<br>
Users are able to search through a search field and any characters input will search the database for the food item that matches the input<br>
Food categories are also display prominently at the top for user to click and upon click, will display the food items that belong to the category<br>
A view more button is available so that on click a user can click to view more of the food item<br>

Feature – Cart app

User can track their cart order(s) by viewing the cart at the menu bar which will display the number of orders if there is at least 1 order
On click of cart, user can see all the orders in the cart and able to make further changes to the order before checkout
The cart will also calculate the total amount of the orders.<br>

 Feature – checkout app

On click of checkout, user will allow to make payment to complete his/her order by filling out a payment form.

Features Left to Implement
--

Feature to track order history made by a user

Technologies Used
==
Django1.11<br>
python3<br>
PostgreSQL<br>
sqlite3<br>
Stripe<br>
HTML5<br>
CSS3<br>
Javascript<br>
bootstrap 4<br>

Testing
==

I tested the HTML and CSS By Chrome Developer Tools to ensure that it displays correctly at all screen sizes.<br>
I tested all forms and models for each app by writing testing code in test.py in the respective app.<br>

 I also tested search bar by: <br>
 
1.	Type in the input
2.	If words match then it will return no food.
3.	If search match with any food name in the database then all result display right.

I also tested cart app by: <br>

Logout user functions:<br>
1.	Try to add to cart button in home page and will redirect me to login page to login
2.	Do not display “Cart’ at the navbar but “Register”

Login user functions:<br>

1.	Display “Cart” at the navbar instead of “Register”
2.	Try add to cart button in home page, 
3.	Try to add to cart without selecting a quantity – default quantity is ‘1’  and then clicking cart to check the order
4.	Try to add to cart by selecting a quantity and then clicking cart to check the order
5.	Try to add to cart of the same order to see if the cart will add to the quantity instead of creating duplicate food item
6.	Try to see if I can amend the order quantity at “Cart” page and see if the total amount is updated after I click the “Amend” button
7.	Try to see if I amend the order quantity to “0” the food item will be deleted

Deployment
==

I have deployed this project to the hosting platform Heroku with a separate GitHub branch.<br>
heroku: https://takeaway-app.herokuapp.com/ <br>
github: https://github.com/WenlingDing/takeaway <br>

Deployment instructions
==

Please note that running this page locally without connecting to a database will result in errors.<br>
To connect to your own database, you need to update the database settings in the settings.py file.<br>
After you have reconfigured your own database, type the following in the command line:<br>
$python3 manage.py makemigrations<br>
$python3 manage.py migrate<br>
$python3 manage.py createsuperuser<br>
$python3 manage.py runserver<br>
Then open the app in your local host to view locally<br>
Do not forget to install the requirements.txt<br>

Credits
==

Media<br>
The photos were copied from the https://thewoksoflife.com<br>

Acknowledgements
==
This is not business use.<br>

