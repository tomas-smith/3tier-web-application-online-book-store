<html>
	<body>
		<h1>New book</h1>
		<form action="/book/create" method="POST">
		Title: <input type="text" name='title' value=""><br/>
		Author:
		<select name="author">
			%for a in author:
			<option value="{{a.author_id}}">{{a.lastname}}</option>
			%end
		</select>
		
		Publisher:
		<select name="publisher">
			%for p in publisher:
			<option value="{{p.publisher_id}}">{{p.name}}</option>
			%end
		</select>		
		Genre: 
		<select name="genre">
			%for g in genre:
			<option value="{{g.Genre_id}}">{{g.genreName}}</option>
			%end
		</select>
		Year: <input type="text" name='year' value=""><br/>
		<input type="submit" value = "Save"/>
		</form>
		
 
 
	</body>
</html>
	