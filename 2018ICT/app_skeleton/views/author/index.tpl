<html>
<head>
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
</head>
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
	<a href="/author/search" class="button"> search an author(via surname)</a> </br>
	<a href="/author/new" class="button"> Add a author</a>
	<a href="/" class="button">index</a>
</body>
</html>
	