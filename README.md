# Flask Gallery API

This is a simple Flask-based API that retrieves images from a PostgreSQL database and serves them as base64-encoded strings in a JSON format. The API supports cross-origin requests (CORS) and returns categorized image data in a gallery format.

## Installation


1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/yourusername/your-repository.git
    cd your-repository
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # For Mac/Linux
    venv\Scripts\activate  # For Windows
    ```

3. Install the required Python dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root of the project to store your PostgreSQL database credentials. Here is the template for the `.env` file:

    ```
    DB_NAME=your_database_name
    DB_USER=your_database_user
    DB_PASSWORD=your_database_password
    DB_HOST=localhost
    DB_PORT=5432
    ```

    Replace `your_database_name`, `your_database_user`, and `your_database_password` with your actual PostgreSQL database details. The default PostgreSQL port is `5432`, but if you're using a different port, update it accordingly.

## Environment Variables

- **DB_NAME**: The name of your PostgreSQL database.
- **DB_USER**: The PostgreSQL username.
- **DB_PASSWORD**: The password for the PostgreSQL user.
- **DB_HOST**: The hostname where the PostgreSQL server is running (e.g., `localhost`).
- **DB_PORT**: The port PostgreSQL is listening on (default is `5432`).

## Running the Application

After setting up the `.env` file and installing dependencies, you can start the Flask application:

```bash
python app.py
```

## Endpoints

### `GET /api/gallery`
Returns the gallery with images and thumbnails in base64 encoding for different categories.
