%for a in books:
<li>
    <a href="/books/{{a.id}}/">{{a.title}}, {{a.artist}}</a>
    <a href="/books/{{a.id}}/edit">[Edit]</a>
    <a href="/books/{{a.id}}/delete">[Delete]</a>
</li>
%end
