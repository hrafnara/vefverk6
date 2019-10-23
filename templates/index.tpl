{% extends "base.html"%}
{% block title%}Eldsneytisverð - miðannarverkefni - json{% endblock %}
{% block content %}
<div class="wrapper">
    {% set oneco = [] %}
    {% for item in gogn['result'] %}
        {% if item.company not in oneco %}
            {% do oneco.append(item.company) %}
            <div class='box'>
                <a href="/company/{{item.company}}">
                    <img scr="static/{{ item.company }}.png" title="{{ item.company }}"
                <\a>
            <\div>
        {% endif %}
    {% endfor %}
<\div>

<div>
<h1>minDiesel()<\h1>
<h1>minPetrol()<\h1>
<\div>
{% endblock %}