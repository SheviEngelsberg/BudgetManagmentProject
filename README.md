```markdown
# Budget Management System Overview
This project is a budget management system implemented in Python, designed to manage the incomes and expenses of users. It provides functionalities for retrieving, adding, updating, and deleting users, expenses, and revenues. Additionally, it offers visualization features to display graphs of the financial data.

## Project Structure
The project is organized into several directories and files:

- **controllers**: Contains three controllers: users, expenses, and revenues.
- **services**: Contains three services: users, expenses, and revenues.
- **models**: Contains three models: User, Expense, and Revenue.
- **DB**: Contains files for database connection and data access functions.
- **tests**: Contains test files for each service (users, expenses, and revenues).
- **visualization**: Contains router and functions responsible for visualization.

## Dependencies
To run the project, the following dependencies need to be installed:

- **fastapi**: A web framework for building APIs with Python.
- **uvicorn**: ASGI server implementation.
- **motor**: Asynchronous driver for MongoDB.
- **pytest**: Testing framework for Python code.
- **pydantic**: Data validation and settings management using Python type annotations.
- **matplotlib**: Plotting library for creating visualizations in Python.
- **pandas**: Data manipulation and analysis library.

## Usage
1. Install the dependencies:
    ```bash
    pip install fastapi uvicorn motor pytest pydantic matplotlib pandas
    ```
2. Start the server:
    ```bash
    uvicorn main:app --reload
    ```
3. Access the API documentation at [http://localhost:8000/docs](http://localhost:8000/docs).

Use the provided endpoints to manage users, expenses, and revenues.

## Supported Operations
### Users
- Fetch user by ID
- Fetch all users
- Add user
- User login
- Update user profile
- Delete user

### Expenses and Revenues
- Fetch expense/revenue by ID
- Fetch all expenses/revenues for a specific user
- Add expense/revenue
- Update expense/revenue
- Delete expense/revenue

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvement, please feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
