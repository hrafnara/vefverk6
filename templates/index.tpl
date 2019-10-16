{% extends "base.html"%}
{% block title%}Eldsneytisverð - miðannarverkefni - json{% endblock%}
{% block content %}
<div class="wrapper">
    {% set oneco = [] %}
    {% for item in gogn['result']%}
        {% if item.company not in oneco}
            {% oneco.append(item.company)%}
            <div class='box'>
                <a href="/company/{{item.company}}">
                    <img scr="static/{{ item.company }}.png" title="{{ item.company }}"
  
