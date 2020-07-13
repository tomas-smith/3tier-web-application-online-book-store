<<html>
<body>

<h1> Edit Publisher</h1>

<form action="/publisher/{{publisher.publisher_id}}/update" method="post">


  First name:<input type="text" name="name" value="{{publisher.name}}"/><br/>
  Last name: <input type="text" name="country" value="{{publisher.country}}"/><br/>
  
  
  <input type="submit" value="Save">
</form>

</body>
</html>