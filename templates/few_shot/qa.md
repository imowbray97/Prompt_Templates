# Few-Shot Question Answering

Context:
{{ context }}

Examples:
{% for ex in examples %}
Q: {{ ex.question }}
A: {{ ex.answer }}
{% endfor %}

Q: {{ question }}
A: 