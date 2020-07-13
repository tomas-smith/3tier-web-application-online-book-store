<html>
%for a in author:
<li>
    <a href="/author/{{a.author_id}}/">{{a.lastname}}, {{a.firstname}}</a>
    <a href="/author/{{a.author_id}}/edit">[Edit]</a>
    <a href="/author/{{a.author_id}}/delete">[Delete]</a>
</li>
%end
<a href="/author">home</a>
</html>