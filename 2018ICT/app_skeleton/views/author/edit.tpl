<html>
<body>

<h1> Edit Contact</h1>

<form action="/author/{{author.author_id}}/update" method="post">


  First name:<input type="text" name="firstname" value="{{author.firstname}}"/><br/>
  Last name: <input type="text" name="lastname" value="{{author.lastname}}"/><br/>
  
  
  <input type="submit" value="Save">
</form>

</body>
</html>