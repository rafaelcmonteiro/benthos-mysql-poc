Simple sequence diagram about this poc:

> **Warning**  
> **IF THE DIAGRAM DIDIN'T LOAD**: upgrade your browser or change it to another(Tested in Chrome and Firefox)

```mermaid
sequenceDiagram;
    dummy_data->>+mysql: generate real time data;
    mysql->>+Benthos: get insert/changes in real time;
    Benthos-->>-postgres: sql insert to psql;
```