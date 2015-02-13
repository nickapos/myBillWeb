# myBillWeb
The goal of this project is to enable the user to run a self hosted multi user, myBill compatible cash flow web service.It will provide an import functionality for data exported as csv from existing desktop myBill installations, and expose those details over a REST API. 

The api can be consumed by any kind of clients, and the original intention is to create an Android client in order to increase the usage flexibility. 

Eventually the desktop myBill application will be fitted with a synchronization layer, so the user can update both the local desktop myBill database and the web service.

The service is quite lightweight and portable since it is using python and pip for its dependencies. I could easily be hosted on a raspberry pi

# Installation instructions
 MybillWeb is an application based on django. It is advised to use the pip python package manager and virtualenv to create a development environment. After the installation of those tools you can use the requirements file to install the necesarry dependencies by using the following pip command:

    pip install -r requirements.txt

 In order to start the project development server, use the usual django command

    python manage.py runserver

 In order to create a super user you can use the following command:

    python manage.py createsuperuser


# TODO
* Finish the database schema
* Add user login
* Provide the import functionality
* Finetune the rest api
* Implement a simple android client
