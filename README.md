# Django Inventory Management System / Ecommerce App

This is a fully functional e-commerce platform built with Django and styled using Tailwind CSS. The app includes modular components for managing products, categories, orders, carts, and an admin interface, providing a scalable solution for building an online store. It is designed to be extendable, with future plans for payment integration and shipment management.

The app is currently deployed on **pythonanywhere** for seamless cloud hosting.

## Features

- **Modular Apps**:

    - **Products**: Manage product details, images, prices, and more.
    - **Categories**: Categorize products for better navigation and organization.
    - **Orders**: Manage customer orders and track their status.
    - **Carts**: Handle shopping cart functionality for customers.
    - **Admin**: Full-featured admin interface for managing the store.

- **Tech Stack**:

    - **Backend**: Django (Python)
    - **Frontend**: Tailwind CSS
    - **Database**: SQLite (for development)
    - **Deployment**: Pythonanywhere

- **Future Enhancements**:
    - **Payment Integration**: Plans for integrating a payment gateway.
    - **Shipment Management**: Future addition of shipment tracking and options.

## Database Design

The database structure is designed based on the following ERD diagram, created using [Lucidchart](https://lucid.app/).

You can view the complete ERD diagram here:

[Database ERD Diagram](https://lucid.app/lucidchart/68b25839-5e43-4ad5-993b-d8ec15ee32d3/edit?viewport_loc=-2875%2C-1769%2C6400%2C2894%2C0_0&invitationId=inv_484d742a-fcf5-44ac-98d0-d4b22f67d848)

The database includes tables for products, categories, orders, carts, and other essential data related to an e-commerce system.

## Installation

Follow these steps to set up the project locally:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/a95z/django-e-commerce.git e-commerce
    ```

2. **Navigate to the project folder**:
    ```bash
    cd e-commerce
    ```

3. **Install Poetry**:
    - Follow the official Poetry installation guide: [https://python-poetry.org/docs/#installation](https://python-poetry.org/docs/#installation).

4. **Set up the project using Poetry**:
    - Install project dependencies and create a virtual environment (automatically managed by Poetry):
      ```bash
      poetry install
      ```

5. **Activate the Poetry virtual environment** (optional):
    - To activate the virtual environment, run:
      ```bash
      poetry shell
      ```
    - Alternatively, you can run commands directly in the virtual environment using `poetry run` (e.g., `poetry run python manage.py runserver`).

6. **Install Node.js dependencies for frontend**:
    - Ensure Node.js is installed (if not, install it from [here](https://nodejs.org/en)).
    - Install Node.js dependencies:
      ```bash
      npm install
      ```

7. **Build Tailwind CSS and start watching for changes**:
    - The project uses Tailwind CSS for styling. To build and watch your Tailwind CSS file, run the following command:
      ```bash
      npm run tw:build
      ```
    - This command will:
        - Compile the `static/css/tw.dev.css` file.
        - Output the minified version into `static/css/tw.css`.
        - Watch for changes in your Tailwind CSS file and automatically rebuild it.

8. **Apply migrations**:
    ```bash
    poetry run python manage.py migrate
    ```

9. **Create a superuser for the Django admin interface** (optional):
    ```bash
    poetry run python manage.py createsuperuser
    ```

10. **Run the development server**:
    ```bash
    poetry run python manage.py runserver
    ```

11. **Open your browser and go to http://127.0.0.1:8000** to see the app in action.

---

### Notes:
- Poetry automatically manages the virtual environment for you, so there’s no need to manually create or activate one using `venv`.
- All Python-related commands (e.g., `python manage.py ...`) should be prefixed with `poetry run` if you’re not inside the Poetry shell.
- If you ever need to add new dependencies, use `poetry add <package-name>` instead of manually editing `requirements.txt`.

## Contributing

Contributions are welcome! Feel free to fork this repository and submit pull requests for new features, bug fixes, or improvements. Please follow the existing code style and include tests where applicable.

## License

This project is open-source and available under the MIT License.

## Author

This project was created and is maintained by **[Abdurezak Farah](https://www.twitter.com/abdurezakfarah)**. Feel free to reach out for any questions or collaboration!

---

> **Note**: This README is for the current version of the Inventory management system / e-commerce app. Future updates will include details about payment integration, shipment management, and other new features as they are developed.

