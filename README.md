# redshift-json-query-generator
Generate RedShift query to parse and flatten JSON

# Problem statement

We need to parse JSON data stored in AWS Redshift into the table columns.

# Solution

Write query generator that can parse JSON structure as input and output Redshift SELECT query that extract each JSON value into the separate column.

# Notes

AWS Redshift has couple functions to work with JSON data:
1. https://docs.aws.amazon.com/redshift/latest/dg/JSON_EXTRACT_PATH_TEXT.html
1. https://docs.aws.amazon.com/redshift/latest/dg/JSON_EXTRACT_ARRAY_ELEMENT_TEXT.html

That should be sufficient to parce andy JSON, since by specs it consists of paris of key-values and ararays.
