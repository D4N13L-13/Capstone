# Django Capstone

[![Django Version](https://img.shields.io/badge/Django-4.x-blue)](https://www.djangoproject.com/)
[![Python Version](https://img.shields.io/badge/Python-3.x-yellow)](https://www.python.org/)

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Contributing](#contributing)
7. [License](#license)

---

## Project Overview

This project is a simple Django application that allows you to to vote
on a polls app and also shows you my CV for self-promotion(obviously).
It's built using the Django web framework and follows best
practices for scalability, security, and performance.

## Features

- Allows you to select which poll you would like to vote on.
- Allows you to vote(once again, obviously).
- Allows you to view the votes of previous voters.
- Allows you to view my CV.
- User authentication (registration, login, logout)
- Admin panel with extended capabilities: YUH HUH

## Requirements

- Python 3.x
- Django 4.x
- Other dependencies (listed in `requirements.txt`)

## Installation

To set up the project locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/D4N13L-13/Capstone
   ```

2. Change into the project directory:

   ```bash
   cd your-project
   ```

3. Create and activate a virtual environment:

   ```bash
   python3 -m venv env
   source env/bin/activate  # For Windows use `env\Scripts\activate`
   ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Set up the database:

   ```bash
   python manage.py migrate
   ```

6. Create a superuser for the Django admin:

   ```bash
   python manage.py createsuperuser
   ```

7. Run the development server:

   ```bash
   python manage.py runserver
   ```

## Usage

Once the server is running, you can access the application at `http://127.0.0.1:8000/`. Log in to the admin panel at `http://127.0.0.1:8000/admin/` with the superuser credentials created earlier.

## Contributing

Contributions are not welcome!

## License

This project is licensed under the Pee Pee Poo Poo - see the [LICENSE](LICENSE) file for details.
