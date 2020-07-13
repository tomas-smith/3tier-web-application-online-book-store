<html>
    <body>
        <h1>New book</h1>
        <form action="/books/create" method="post">
            Title: <input type="text" name='title' value="" /><br />
            Artist: <input type="text" name='artist' value="" /><br />
            Year: <input type="text" name='year' value="" /><br />
			Genre:
			<select name='genre'>
				%for g in genre:
				<option value="{{g.id}}">{{g.name}}</option>
				%end
			</select>
            <br />
            <input type="submit" value="Save" />
        </form>
    </body>
</html>