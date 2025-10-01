# NOT

The NOT logical statement does what we have already talked about... i.e.
negates from true to false or false to true.

## Unary Operator

So most operators take two values to work. These are considered binary operators. Like
1 == 12

The NOT operator only needs to take 1 operator, this makes it a **UNARY OPERATOR**




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


