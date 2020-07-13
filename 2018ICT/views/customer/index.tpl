<html>
<body>
 <h1> Customers List</h1>
 
	<ul>
 % for c in customers:
 <li>
  <a href="/customer/{{c.customer_id}}/">{{c.nameCustomer}}, {{c.lastname}}</a>
    <a href="/customer/{{c.customer_id}}/edit">[Edit]</a>
	<a href="/customer/{{c.customer_id}}/delete">[delete]</a>
	</li>
	%end
	</ul>
	
	<a href="/customer/new"> Add a Customer</a>
</body>
</html>
	