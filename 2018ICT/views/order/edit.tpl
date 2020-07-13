<html>
	<body>

		<h1> Edit Order</h1>

		<form action="/order/{{order.order_id}}/update" method="post">
		<select name="customer">
			%for c in customer:
			<option value="{{c.customer_id}}">{{c.nameCustomer}}</option>
			%end
		</select>
		<select name="book">
			%for b in book:
			<option value="{{b.book_id}}">{{b.title}}</option>
			%end
		</select>
		
			date of purcase: <input type="text" name='dop' value="{{order.dop}}"><br/>
			<input type="submit" value = "Save"/>
		</form>

	</body>
</html>