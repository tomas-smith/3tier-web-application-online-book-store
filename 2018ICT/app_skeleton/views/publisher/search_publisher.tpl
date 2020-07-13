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
		<h1>Search for a publisher</h1>
		<form action="/publisher/searchTitle" method="post">
			Enter the Title:
			<input type="text" name='name' value="" />
			<input type="submit" value="Search" /> <br />
		</form>
		
		<a href="/publisher" class="button">Home</a>
	</body>
</html>


