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

 After that, you can visit the Django admin interface in:

    http://localhost:8000/admin

 and the existing REST API at:

    http://localhost:8000/api/v1/?format=json

# Usage of the api

 If you want to use the api all you need to do is to use the usual GET,POST,PUT,DELETE HTTP commands. In order to find out the internal structure of each end point, you cah visit its schema e.g:

http://localhost:8000/api/v1/category/schema/?format=json will return:

```json
{"allowed_detail_http_methods": ["get"], "allowed_list_http_methods": ["get"], "default_format": "application/json", "default_limit": 20, "fields": {"add_date": {"blank": true, "default": "2015-10-25T07:40:04.647741", "help_text": "A date & time as a string. Ex: \"2010-11-10T03:07:43\"", "nullable": false, "readonly": false, "type": "datetime", "unique": false}, "categoryName": {"blank": false, "default": "No default provided.", "help_text": "Unicode string data. Ex: \"Hello World\"", "nullable": false, "readonly": false, "type": "string", "unique": false}, "checksum": {"blank": false, "default": "No default provided.", "help_text": "Unicode string data. Ex: \"Hello World\"", "nullable": false, "readonly": false, "type": "string", "unique": false}, "comment": {"blank": false, "default": "No default provided.", "help_text": "Unicode string data. Ex: \"Hello World\"", "nullable": false, "readonly": false, "type": "string", "unique": false}, "id": {"blank": true, "default": "", "help_text": "Integer data. Ex: 2673", "nullable": false, "readonly": false, "type": "integer", "unique": true}, "resource_uri": {"blank": false, "default": "No default provided.", "help_text": "Unicode string data. Ex: \"Hello World\"", "nullable": false, "readonly": true, "type": "string", "unique": false}}, "filtering": {"id": 1, "user": 2}}
```

This provides us with all the details we need. What fields are there, if they are mandatory or not, what values they can accept, any constraints etc.
In order to create a new record all we need to do is to POST to the http://localhost:8000/api/v1/category/ endpoint a properly formatted json file.
You can retrieve the available records by visiting 

http://localhost:8000/api/v1/category/?format=json

```json
{"meta": {"limit": 20, "next": null, "offset": 0, "previous": null, "total_count": 1}, "objects": [{"add_date": "2015-02-11", "categoryName": "groceries", "checksum": "ed0f23d23cc3d78ad4e5dbc4ce91597b", "comment": "a test category", "id": 1, "resource_uri": "/api/v1/category/1/"}]}
```

After that we can use the id of the record of our choice in order to manipulate its data using PUT or DELETE.

# TODO
* Finish the database schema - done
* Add user login
* Provide the import functionality
* Finetune the rest api
* Implement a simple android client
