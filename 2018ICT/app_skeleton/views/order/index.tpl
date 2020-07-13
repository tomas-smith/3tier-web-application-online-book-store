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
 <h1> Orders List</h1>
 
	<ul>
 % for o in orders:
 <li>
  <a href="/order/{{o.order_id}}/">{{o.order_id}}</a>
    <a href="/order/{{o.order_id}}/edit">[Edit]</a>
	<a href="/order/{{o.order_id}}/delete">[delete]</a>
	</li>
	%end
	</ul>
	
	<a href="/order/new" class="button"> Add a Order</a>
	<a href="/" class="button">index</a>
</body>
</html>
	