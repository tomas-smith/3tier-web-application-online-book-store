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
	
	<a href="/genre/new"  class="button"> Add a Genre</a>
	<a href="/genre/search"  class="button"> search an author(via surname)</a> </br>
	<a href="/" class="button">index</a>
</body>
</html>
	