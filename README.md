[![Coverage Status](https://coveralls.io/repos/github/ro6ley/flask-diary/badge.svg?branch=main)](https://coveralls.io/github/ro6ley/flask-diary?branch=main)

# Flask-Diary

Diary is an online journal where users can pen down their thoughts and feelings. You can also use it to track your online reading list by adding links to read later and mark them as `read` once read for convenience.

The building blocks are:

* Python 3.8
* Flask 2.2
* PostgreSQL

## Still pending

* [ ] User account management
* [ ] Front-end app to consume the API
* [ ] Deploy to AWS using Terraform


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

## Prerequisites

You need the following to be able to run the project:
* Python 3 installed
* Virtualenv
* Postgres
* Docker (Optional)

## Setting Up for Development

These are instructions for setting up Diary API in development environment.

* clone the project:
  ```
  $ git clone https://github.com/ro6ley/flask-diary.git
  $ cd flask-diary
  ```

* prepare virtual environment and install the project requirements:
  ```
  $ virtualenv --python=python3 venv
  $ source venv/bin/activate
  $ pip install -r requirements.txt
  ```

* make sure PostgreSQL server is installed and running, create
  database "flask_diary":
  ```
  $ psql --user postgres
  postgres=# create database flask_diary;
  ```

* create database tables:
  ```
  $  python -m flask db migrate
  ```

* run development server:
  ```
    $ python -m flask run
  ```

The API is now available at `http://localhost:5000/`.

## Documentation

The API endpoints in summary:

| Endpoint                                                    | Functionality                      |
|:----------------------------------------------------------- |:---------------------------------- |
| **Entries**                                                 |                                    |   
| GET /api/entries/                                           | Fetch all entries                  |
| GET /api/entries/\<entryId>/                                 | Fetch a single entry               |
| POST /api/entries/                                          | Create an entry                    |
| PATCH /api/entries/\<entryId>/                                 | Modify an entry                    |
| DELETE /api/entries/\<entryId>/                              | Delete an entry                    |
| **Categories**                                              |                                    |
| GET /api/categories/                                        | Fetch all categories               |
| GET /api/categories/\<categoryId>/                          | Fetch a single category            |
| POST /api/categories/                                       | Create a category                  |
| PATCH /api/categories/\<categoryId>/                          | Modify a category                  |
| DELETE /api/categories/\<categoryId>/                       | Delete a category                  |
| **Articles**                                                |                                    |
| GET /api/categories/\<categoryId>/articles/                 | Fetch all articles in a category   |
| GET /api/categories/\<categoryId>/articles/\<articleID>/    | Fetch a single article             |
| POST /api/categories/                                       | Create an article                  |
| PATCH /api/categories/\<categoryId>/articles/\<articleID>/    | Modify an article                  |
| DELETE /api/categories/\<categoryId>/articles/\<articleID>/ | Delete an article                  |


## Running the tests

To run the tests:

```
  $ pytest
```
