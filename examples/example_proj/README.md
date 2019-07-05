### Example project 1

#### Model:
`TestModelA`

##### Migrations:
`0001`: Initial model with single field `name`  
`0002`: Add fields `first_name` and `last_name`, split content of `name` into new fields  
`0003`: remove field `name`


##### Test:
`TestAppMigration0001To0003TestCase`: Tests correct split of `name` into `first_name` and `last_name`
