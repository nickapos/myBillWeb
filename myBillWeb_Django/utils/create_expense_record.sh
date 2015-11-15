curl -v --user "nickapos:nickapos" -H "Content-Type: application/json" -X POST --data '{"pay_date":"2013-06-15","issue_date":"2013-06-15","company":"/api/v1/company/1/","mybillId":"-1","amount":"20","type_of_record":"EX","comment":"a comment","checksum":"a checksum","user":"/api/v1/user/1/"}' http://localhost:8000/api/v1/record/?format=json

