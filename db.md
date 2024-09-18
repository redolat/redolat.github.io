# Naming tables and classes


Between `wtp_result` and `wtp_results`, the better choice for a database table name is typically **`wtp_results`**. Here's why:

### 1. **Plural for Tables Representing Collections:**
   - **`wtp_results` (plural)** is more commonly used because a table generally represents a collection of records, each corresponding to one result. It’s a widely accepted convention in database design to name tables in the plural form, as the table will hold multiple instances of "results."

   Example: Each row in `wtp_results` would represent a single result.

### 2. **Consistency with ORM and Framework Conventions:**
   Many Object-Relational Mappers (ORMs) like SQLAlchemy (used with Flask) assume that table names are plural by default. It also helps maintain consistency across the project if all tables representing collections follow the plural form, which is helpful for readability and maintainability.

### 3. **Singular for Specific Instances:**
   On the other hand, **`wtp_result` (singular)** might be appropriate if you're dealing with a special or unique record that represents a single instance or if your project’s naming convention requires singular table names. However, in most cases, this is less common for tables holding multiple rows.

### Recommendation:
- Use **`wtp_results`** for a table that holds multiple result records.
When naming a class that corresponds to a database table, the convention typically differs from table naming. While database table names are usually plural to reflect that they store collections of records, class names are generally singular, as each instance of the class represents a single record or entity.

### Recommended Class Name:
The class name should be **`WTPResult`** (singular). 

Here’s why:
1. **Singular Entity Representation:**
   A class represents a single instance of an entity, so it is a good practice to use the singular form. Each instance of `WTPResult` would correspond to one row in the `wtp_results` table.

2. **ORM Convention:**
   ORMs like SQLAlchemy and Django often map classes (singular) to tables (plural). It’s common practice for class names to be singular, reflecting the fact that a class instance represents a single object or record in the table.

### Example:

- **Class Name:** `WTPResult` (singular)
- **Table Name:** `wtp_results` (plural)

Here’s what it might look like in code:

```python
from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class WTPResult(db.Model):
    __tablename__ = 'wtp_results'
    
    id = Column(Integer, primary_key=True)
    result_name = Column(String(50))
    # Other fields...
```

### Summary:
- Use **`wtp_results`** (plural) for the table name.
- Use **`WTPResult`** (singular) for the class name, following common conventions for ORM mappings.

* Migration 
- Flask-Migrate should be installed.
- Should be imported and used inside the flask app.
- `flask --app ../run.py db init`
- `flask --app ../run.py db migrate -m 'message'`
- Check the versions and modify the added migration file.
- `flask --app ../run.py db upgrade`

* Seeders
- Flask-Seeder should be installed.
- Check and add seeds using:
- `flask --app ../run.py seed run`
