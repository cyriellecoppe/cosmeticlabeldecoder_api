# cosmeticlabeldecoder_api
Cosmetic Label Decoder API - demo website

### Concept

**Cosmetic Label Decoder** helps you understand your **cosmetics** at a glance, providing an overview of their **composition**. Based on the *International Nomenclature of Cosmetics Ingredients*, CLD assesses each ingredient composing a product and rates its value and environmental impact.

### Contributing

This API backend is built using Django, Django RESTFramework and PostgreSQL.

#### Install the required components
`pip install -r requirements.txt`

`createdb cld`

`python3 manage.py migrate`

#### Run development server
`python3 manage.py runserver`

You can use the admin site to populate database: http://localhost:8000/admin.

#### Run tests
`python3 manage.py test`

### Access website UI: 
This repository is only used for backend. To access website UI, checkout the [UI repository](https://github.com/cyriellecoppe/cosmeticlabeldecoder_ui).
