<html>
<body>

<h1> New Contact</h1>

<form action="/book/{{book.book_id}}/update" method="POST">

	Title: <input type="text" name="title" value="{{book.title}}">br/>
  
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
	yEAR: <input type="text" name="year" value="{{book.year}}">br/>
  
  <input type="submit" value="Save">
</form>

</body>
</html>