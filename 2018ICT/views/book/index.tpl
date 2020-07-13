<html>
<body>
 <h1> Book List</h1>
 <ul>
 % for b in books:
 <li>
  <a href="/book/{{b.book_id}}/">{{b.title}}, {{b.author.lastname}}, {{b.publisher.name}}, {{b.genre.genreName}}, {{b.year}}</a>
    <a href="/book/{{b.book_id}}/edit">[Edit]</a>
	<a href="/book/{{b.book_id}}/delete">[delete]</a>
	</li>
	%end
	</ul>
	<a href="/book/search"> search an author(via surname)</a> </br>
	<a href="/book/new"> Add a book</a>
	<a href="/">index</a>
</body>
</html>
	