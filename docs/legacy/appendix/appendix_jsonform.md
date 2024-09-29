# JSON Form

JSON Schema is used for rendering forms from providers and tasks in the frontend.

Example of JSON Form:

```JSON
{
  "$id": "https://neops.io/schema/example.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Demo Form JSON Schma",
  "type": "object",
  "required": [
    "foo",
    "bar"
  ],
  "properties": {
    "foo": {
      "title": "Foo",
      "type": "string",
      "description": "Foo rendered as normal input field"
    },
    "bar": {
      "title": "Bar",
      "type": "string",
      "description": "Bar rendered as editor with syntax highliting for jinja2",
      "x-display": "editor-jinja2"
    },
    "bool": {
      "title": "bool",
      "type": "boolean",
      "description": "boolean is rendered as checkbox"
    }
  }
}
```

Will render this form:

![Form from Example JSON schema](./_media/jsonform.png)

Fields:

- `$id`: _global identifier, used if multiple forms are renderd on one page_
- `$schema`: \_reference to the json schema for validation (use `http://json-schema.org/draft-07/schema#`)
- `title`: _form title or on sub-element field title_
- `type`: _globally it's always an object (which holds sub-elements in properties), on fields it defines all common data types (string, boolean, number and more)_
- `required`: _used for validation, which fields are required_
- `properties`: _sub-elements_
- `x-display`: _used to affect form rendering_

Form more information checkout the ressources below.

## Ressources

- [JSON Form Documentation](https://json-schema.org/learn/getting-started-step-by-step.html)
- [Datastructure to JSON Form](https://www.jsonschema.net/home)
- [Demo of Vutify JSON Form](https://koumoul-dev.github.io/vuetify-jsonschema-form/latest/?example=basic)
