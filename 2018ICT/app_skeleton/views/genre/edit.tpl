<html>
<body>

<h1> Edit Genre</h1>

<form action="/genre/{{genre.genre_id}}/update" method="post">


  First name:<input type="text" name="firstname" value="{{genre.firstname}}"/><br/>
  Last name: <input type="text" name="lastname" value="{{genre.lastname}}"/><br/>
  
  
  <input type="submit" value="Save">
</form>

</body>
</html>