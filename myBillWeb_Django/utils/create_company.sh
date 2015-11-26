curl -v --user "nickapos:nickapos" -H "Content-Type: application/json" -X POST --data '{"add_date":"2013-06-15","category":"/api/v1/category/1/","companyName":"company name2","comment":"a comment","checksum":"a checksum","user":"/api/v1/user/1/"}' http://localhost:8000/api/v1/company/?format=json

