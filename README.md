# Django E-Commerce App

This is a fully functional e-commerce platform built with Django and styled using Tailwind CSS. The app includes modular components for managing products, categories, orders, carts, and an admin interface, providing a scalable solution for building an online store. It is designed to be extendable, with future plans for payment integration and shipment management.

The app is currently deployed on **Vercel** for seamless cloud hosting.

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
    - **Deployment**: Vercel

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

1. Clone the repository:
```bash
    git clone https://github.com/abdurezakfarah/django-e-commerce.git e-commerce
```
2. Navigate to the project folder:
```bash
    cd e-commerce
```
3. Set up a Python virtual environment (recommended):
    - Create a virtual environment:
    ```bash
        python -m venv venv
    ```
    - Activate the virtual environment:
        - On Windows:
        ```bash
            .venv/Scripts/activate
        ```
        - On MacOS:
        ```bash
            source venv/bin/activate
        ```
4. Install backend dependencies:
    ```bash
        pip install -r requirements.txt
    ```
5. Install Node.js dependencies for frontend:

    - Ensure Node.js is installed (If not, install it from [here](https://nodejs.org/en)).

    - Install Node.js dependencies:

    ```bash
        npm install
    ```
6. Build Tailwind CSS and start watching for changes:

    - The project uses Tailwind CSS for styling. To build and watch your Tailwind CSS file, run the following command:
    ```bash
        npm run tw:build
    ```
    - This command will:
        - Compile the static/css/tw.dev.css file.
        - Output the minified version into static/css/tw.css.
        - Watch for changes in your Tailwind CSS file and automatically rebuild it.

7. Apply migrations:
    ```bash
        python manage.py migrate
    ```
8. Create a superuser for the Django admin interface (optional):
    ```bash
        python manage.py createsuperuser
    ```

9. Run the development server:
    ```bash
        python manage.py runserver
    ```
10. Open your browser and go to http://127.0.0.1:8000 to see the app in action.

## Contributing

Contributions are welcome! Feel free to fork this repository and submit pull requests for new features, bug fixes, or improvements. Please follow the existing code style and include tests where applicable.

## License

This project is open-source and available under the MIT License.

## Author

This project was created and is maintained by **[Abdurezak Farah](https://www.twitter.com/abdurezakfarah)**. Feel free to reach out for any questions or collaboration!

---

> **Note**: This README is for the current version of the e-commerce app. Future updates will include details about payment integration, shipment management, and other new features as they are developed.

