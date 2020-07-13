%for p in publisher:
<li>
    <a href="/publisher/{{p.publisher_id}}/">{{p.name}}, {{p.country}}</a>
    <a href="/publisher/{{p.publisher_id}}/edit">[Edit]</a>
    <a href="/publisher/{{p.publisher_id}}/delete">[Delete]</a>
</li>
%end
<a href="/publisher">home</a>