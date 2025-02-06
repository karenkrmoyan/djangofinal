*** Django Final Project ***

This eCommerce website allows users to easily buy and sell clothes with a user-friendly interface and intuitive functionality. It offers seamless navigation, helping users quickly find products that best match their preferences. The platform is designed to enhance the shopping experience with its simple and efficient layout.

My project consists of 3 apps, each with unique functionalities.

* Store app
* Cart app
* Account app

Models:

 - I got 2 models for Store app.
    * Category
    * Product 

    - Category: 1. Category name
                2. Slugfield

    - Product: 1. category field which is a Foreignkey for Category table
               2. Title 
               3. Brand ("un-branded" by default)
               4. Descripiton (not required)
               5. Slugfield
               6. Price 
               7. Image (automaticaly uploading to static/media folder)  

    Each model has its absolute URL functionality          

