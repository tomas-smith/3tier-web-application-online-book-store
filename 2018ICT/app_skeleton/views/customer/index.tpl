<html>
<style>
.button {
    background-color: #4CAF50;
    border: none;
    color: white;
    padding: 15px 32px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
	font-family: arial, sans-serif;
}
</style>
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
	<a href="/customer/search" class="button"> search an customer)</a> </br>
	<a href="/customer/new"  class="button"> Add a Customer</a>
	<a href="/" class="button">index</a>
</body>
</html>
	