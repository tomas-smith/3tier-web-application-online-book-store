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
%for a in customer:
<li>
    <a href="/customer/{{a.customer_id}}/">{{a.lastname}}, {{a.nameCustomer}}</a>
    <a href="/customer/{{a.customer_id}}/edit">[Edit]</a>
    <a href="/customer/{{a.customer_id}}/delete">[Delete]</a>
</li>
%end
<a href="/customer" class="button">home</a>
</html>