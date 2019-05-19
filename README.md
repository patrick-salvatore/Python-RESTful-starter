# API docs 

## The use case: Eleven Speed is an ecommerce site that uses React.js and Python's flask to help understand better development practices and the respective technologies

All responses will be in the format: 

```json 
{
    "message": "describing what happened", 
    "data": "mixed content holding the response"
}
```

## GET ITEMS

**DEFINITON**
method = GET 
'/bikes'

**RESPONSE**
'200 OK' on success 

```json 
[
    {   
        "id": 1, 
        "identifier": "road", 
        "brand": "specialized", 
        "name": "allez", 
        "price": "$1200",
        "image": "some url"
    }, 
    {
        "id": 2,
        "identifier": "road", 
        "brand": "fuji", 
        "name": "sportif 1.01",
        "price": "$1100",
        "image": "some url"
    }
]
```

## POST ITEM

**DEFINITON**
method = POST
'/bikes'

**ARGUMENTS**
`'identifier: string' a general indentifier for the product`
`'brand: string' the brand name of product`
`'name: string' the model name of the product`
`'price: string' the price for the product`

**RESPONSE**
'201 CREATED' on success 

## GET ITEM w/ id 

**DEFINITON**
method = GET 
'/bikes/<str:brand>/'

**RESPONSE**
`404 not found` if item is not found 
`200 OK` on success

```json
{
    "id": 1,
    "identifier": "road", 
    "brand": "specialized", 
    "name": "allez", 
    "image": "some url",
    "price": "$1200"
}
```

## DELETE item 

**DEFINITON**
method = DELETE 
'/bikes/<num:id>'

**RESPONSE**
`404 not found` if item is not found 
`204 No Content` on success

```json
{
    "id": 1,
    "identifier": "road", 
    "brand": "specialized", 
    "name": "allez", 
    "price": "$1200", 
    "image": "some url"
}
```
