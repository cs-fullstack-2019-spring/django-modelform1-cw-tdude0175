## POINTS: 2
## KEY: Well done! You are the only one to submit working code and not forget the 'published_date' field 
# Django Model Forms 1 CW

### Exercise 1: Create a basic blog entry page
* Create a BlogPost model with the following fields:
```
title
text
created_date (should be populated with current dat/time when record created)
published_date (should be populated when record created and if updated)
```
* Create a model form bound to the BlogPost model that asks ONLY for the following fields:
```
title
text
```
* Use the Django admin console to confirm that your form adds Users to the database

### Challenge:
Try to implement a new view that will allow you to edit an existing entry
