<html>
<body>

<h1> Edit Customer</h1>

<form action="/customer/{{customer.customer_id}}/update" method="post">


  First name:<input type="text" name="firstname" value="{{customer.firstname}}"/><br/>
  Last name: <input type="text" name="lastname" value="{{customer.lastname}}"/><br/>
  
  
  <input type="submit" value="Save">
</form>

</body>
</html>