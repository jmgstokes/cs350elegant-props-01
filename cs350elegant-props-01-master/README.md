Lab 10 and Homework 9
====
TODO: properties App
----

### 1. Modify the project by implementing the detail template for a property object. The template file already exists but needs to be edited to show all of the information for the indicated property. Edit ==> `properties/templates/properties/detail.html`

`HINT:` The template variable name for an object in a DetailView defaults to `object`

### 2. The Property model does not have address information. Add an attribute to the model to store the zip code for any property. NOTE: set the field attribute `null=True` so that the new attribute does not interfere with existing objects. Run `makemigrations` and then `migrate` to make your changes to the db. Now go the admin site and either update an existing property with a new zip code or add a new property this time adding a zip code.

### 3. Return to the html page you edited above (task 1) and write code to show the zip code as well.

TODO: messenger App
----
__The messenger app is responsible for storing, displaying and managing communication between customers and real estate agents. Below are two example use cases for this app.__

_Use Case: Customer submits a message for a real estate agent regarding a specific property._

_Use Case: Real estate agent reads messages left by customers regarding a specific property._


### 4. Implement a model for the messenger app called __Message__ (messenger/models.py). This model has the following attributes: a subject line, the message text, date created, and email of the person submitting the message. 

a. Use the appropriate django model field types for each attribute: https://docs.djangoproject.com/en/2.0/ref/models/fields/#field-types

### 5. Add an admin panel for the new Message model.

a. messenger/admin.py ==> add `admin.site.register(Message)` to the file. Take a look at properties/admin.py to learn how to import the Message model from the models file in the messenger app.
b. Run `makemigrations` then `migrate` to create your new model in the db.
c. Run the server and go to the admin site. You should see a new panel for managing messages. Add a few then move on to the next task.

### 6. Add a way to display a list of all messages in the db in a html page.

a. Create a view in messenger/views.py that extends generic.ListView

b. Create an html template in the appropriate directory in the messenger app (review the properties app for guidance -- you're repeating the same process...). You decide on the layout and look and feel.

`HINT:` Review properties/templates/properties/list.html for an example of looping over variables produced by generic.ListView

c. Add a url messenger/urls.py to handle requests for the message list page. (again, review properties/urls.py as a guide for the messenger edits and yes, you will need to create the necessary files and folders in the messenger directory as needed.)

d. Run the server and test your new url to the message listing. It should show the messages you added above.






