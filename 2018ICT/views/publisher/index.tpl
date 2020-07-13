<html>
<body>
 <h1> Book List</h1>
 
	<ul>
 % for p in publishers:
 <li>
  <a href="/publisher/{{p.publisher_id}}/">{{p.name}}, {{p.country}}</a>
    <a href="/publisher/{{p.publisher_id}}/edit">[Edit]</a>
	<a href="/publisher/{{p.publisher_id}}/delete">[delete]</a>
	</li>
	%end
	</ul>
	<a href="/publisher/search"> search</a> </br>
	<a href="/publisher/new"> Add a book</a>
	<a href="/">index</a>
</body>
</html>
	