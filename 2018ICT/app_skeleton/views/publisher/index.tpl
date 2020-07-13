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
 <h1> Publisher List</h1>
 
	<ul>
 % for p in publishers:
 <li>
  <a href="/publisher/{{p.publisher_id}}/">{{p.name}}, {{p.country}}</a>
    <a href="/publisher/{{p.publisher_id}}/edit">[Edit]</a>
	<a href="/publisher/{{p.publisher_id}}/delete">[delete]</a>
	</li>
	%end
	</ul>
	<a href="/publisher/search" class="button"> search</a> </br>
	<a href="/publisher/new" class="button"> Add Publisher</a>
	<a href="/" class="button">index</a>
</body>
</html>
	