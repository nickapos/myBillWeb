curl -v --user "nickapos:nickapos" -H "Content-Type: application/json" -X POST --data '{"user":"/api/v1/user/1/","add_date":"2013-06-15","categoryName":"hehe","comment":"a comment","checksum":"a checksum"}' http://localhost:8000/api/v1/category/?format=json

