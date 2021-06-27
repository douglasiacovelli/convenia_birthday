# Convenia Birthday

## Description
This script is made in Python and fetches the birthdays from the Convenia website.

## How to use it

### Set the variables
Make sure you change the following variables:

`company_id` and `user_token`

Both can be found after you log into the Convenia website and then inspect the network requests filtering by "month". There you'll be able to find these values.

### Optional
If you want to filter by name, then you can change the value of the `members` variable. This will look for a substring, so mind possible mismatches, such as "Gabriel" matching "Gabriela"

### Run the script on the terminal
`python birthday.py`.



