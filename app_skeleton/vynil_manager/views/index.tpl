<html>
	<head>
		<title>book Manager</title>
	</head>
	<body>
		<h1>Welcome to the book Manager</h1>
		
		<h2>Our Music Library Includes:</h2> <br />
		
		<ul>
            %for a in books:
            <li>
                <a href="/books/{{a.id}}/">{{a.title}}, {{a.artist}}</a>
                <a href="/books/{{a.id}}/edit">[Edit]</a>
                <a href="/books/{{a.id}}/delete">[Delete]</a>
            </li>
            %end
        </ul>
		
		<a href="/books/new">[Create a book]</a> <br />
		<a href="/books/search">[Search for a book by title]</a> <br />
	</body>
</html>