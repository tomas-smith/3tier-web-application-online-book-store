%for g in genre:
<li>
    <a href="/genre/{{g.Genre_id}}/">{{g.genreName}}</a>
    <a href="/genre/{{g.Genre_id}}/edit">[Edit]</a>
    <a href="/genre/{{g.Genre_id}}/delete">[Delete]</a>
</li>
%end
<a href="/author">home</a>