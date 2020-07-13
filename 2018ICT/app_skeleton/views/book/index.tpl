<html>
<style>
.button {
    background-color: #4CAF50;
    border: none;
    color: white;
    padding: 15px 32px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
	font-family: arial, sans-serif;
}
</style>
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
	<a href="/book/search" class="button"> search a book</a> </br>
	<a href="/book/new" class="button"> Add a book</a>
	<a href="/" class="button">index</a>
</body>
</html>
	