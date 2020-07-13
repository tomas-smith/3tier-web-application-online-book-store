<html>
<body>
 <h1> Author List</h1>
 
	<ul>
 % for a in authors:
 <li>
  <a href="/author/{{a.author_id}}/">{{a.lastname}}, {{a.firstname}}</a>
    <a href="/author/{{a.author_id}}/edit">[Edit]</a>
	<a href="/author/{{a.author_id}}/delete">[delete]</a>
	</li>
	%end
	</ul>
	<a href="/author/search"> search an author(via surname)</a> </br>
	<a href="/author/new"> Add a author</a>
	<a href="/">index</a>
</body>
</html>
	