# Jinja2

Jinja2 is a template language for python.

It supports a ton of features, we will focus on the basics here.

```jinja
{# comment #}

{{ variable }}

{% if element %}
do some content
{% else %}
some content with {{ variable }}
{% endif %}

{% for element in list %}
……do somthing with {{ element }}
{% endfor%}

{# use filters on elements with | #}
{{ variable | upper }} {# make a string uppercase #}
{{ variable | regex_replace('foo', 'bar', ignorecase=True) }} {# search foo and replace it with bar #}
{# more filters see below #}
```


## Filter

See this [list](https://jinja.palletsprojects.com/en/2.11.x/templates/#builtin-filters) to checkout all built in filters

Additionally we support some custom filters:

- `regex_search` \_searches a string, returns a list of found elements

```jinja
{# search for foo in foobar and returns foo #}
{{ 'foobar' | regex_search('(foo)') }}

{# search for f[a-z] in foobar and returns fo #}
{{ 'foobar' | regex_search('(f\w)') }}

{# will return empty if it cannot find a match #}
{{ 'foo' | regex_search('(foobar)') }}

{# optional parameters are case insensitive search and multiline mode, will return bar#}
{{ 'foo\nBAR' | regex_search("^bar", multiline=True, ignorecase=True) }}
```

- `regex_replace` _search a string and replace it_

```jinja
{# search for foo and replace it with bar #}
{{ 'foobar' | regex_replace('foo', 'bar') }} {# output: barbar #}

{# ignorecase is supported as well #}
{{ 'FOObar' | regex_replace('foo', 'bar', ignorecase=True) }} {# output: barbar #}

{# grouping and referencig is supported as well #}
{{ 'FOObar' | regex_replace('^foo(\w+)^', '\\1\\1', ignorecase=True) }} {# output: barbar #}
```

- more to come

## Ressources

- [Jinja2 Documentation](https://jinja.palletsprojects.com/en/2.11.x/)
- and many more are found with your preferred web search engine ;)
