# Easy curl request
curl http://localhost:5000

curl http://localhost:5000/companies

# GET request for employee data
curl http://localhost:5000/employees/2



curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"first_name":"Jim","last_name":"Miller","dob":"1/2/2077","company_id":2}' \
  http://localhost:5000/employees