<html>
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
	
	<a href="/order/new"> Add a Order</a>
	<a href="/">index</a>
</body>
</html>
	