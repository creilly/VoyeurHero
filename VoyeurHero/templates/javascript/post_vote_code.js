{% extends "javascript/jquery_base.html" %}

{% block jq_setup  %}
{% include "javascript/post_vote_setup.js" %}
{% endblock jq_setup %}

{% block jq_init %}
{% include "javascript/post_vote_init.js" %}
{% endblock jq_init %}

