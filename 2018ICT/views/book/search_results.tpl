%for b in book:
<li>
    <a href="/book/{{b.book_id}}/">{{b.title}}, {{b.author.lastname}}, {{b.publisher}}, {{b.genre}}, {{b.year}}</a>
    <a href="/book/{{b.book_id}}/edit">[Edit]</a>
    <a href="/book/{{b.book_id}}/delete">[Delete]</a>
</li>
%end
<a href="/book">home</a>