<html>
<body>
 <h1> Genres List</h1>
 
	<ul>
 % for g in genres:
 <li>
  <a href="/genre/{{g.Genre_id}}/"> {{g.genreName}}</a>
    <a href="/genre/{{g.Genre_id}}/edit">[Edit]</a>
	<a href="/genre/{{g.Genre_id}}/delete">[delete]</a>
	</li>
	%end
	</ul>
	
	<a href="/genre/new"> Add a Genre</a>
	<a href="/genre/search"> search an author(via surname)</a> </br>
	<a href="/">index</a>
</body>
</html>
	