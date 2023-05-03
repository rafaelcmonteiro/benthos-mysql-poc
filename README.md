Simple sequence diagram about this poc:

```mermaid
sequenceDiagram;
    dummy_data->>+mysql: generate real time data;
    mysql->>+Benthos: get insert/changes in real time;
    Benthos-->>-postgres: sql insert to psql;
```