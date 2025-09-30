# NOT

The NOT logical statement does what we have already talked about... i.e.
negates from true to false or false to true.

## Common Errors

Negating Two things and combining with AND/OR and it doesn't mean what you expect.

```
customerId = input

if NOT (customerId = 1) OR NOT (customerId = 2) then
    output "Customer is not id 1 or 2"
endif
```

If we just input 2 as an example value, we can see this fail.
It DOES get inside the if statement.

This comes a faulty way to convert NOT statements between AND/OR

This is the rule we should be following:

# De Morgan Laws

## NOT (A AND B) = (NOT A) OR (NOT B)

## NOT (A OR B) = (NOT A) AND (NOT B)


