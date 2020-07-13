<html>
    <body>
        <h1>Edit book</h1>
        
        <form action="/books/{{book.id}}/update" method="post">
            Title: <input type="text" name='title' value="{{book.title}}" /><br/>
            Artist: <input type="text" name='artist' value="{{book.artist}}" /><br/>
            Year: <input type="text" name='year' value="{{book.year}}" /><br/>
			Genre: {{book.genre}}
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