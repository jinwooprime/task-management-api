# Task Management API (CRUD)

A REST API built upon FastAPI that performs CRUD operations utilizing MongoDB.

---

## 📋 Prerequisites

Before getting started, make sure you have the following:

- A **MongoDB database/account** (e.g., [MongoDB Atlas](https://www.mongodb.com/atlas))
- An API testing tool such as **Postman** or **Insomnia**
- **Python 3.8+** installed on your system

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/jinwooprime/task-management-api.git
cd task-management-api
```

### 2. Create virtual environment
```bash
python3 -m venv venv

# Activate it
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip3 install -r requirements.txt
```

### 4. Configure Environment Variables & URI
1. Create a ```.env``` file in the root directory and add your MongoDB database user's credentials:
```bash
DB_USERNAME=<database-user-username>
DB_PASSWORD=<database-user-password>
```
2. In ```mongo_config.py```, add your database's connection string to the ```uri``` variable:
```bash
uri = f"<db-connection-string>"
```
> **Example:** mongodb+srv://{db_username}:{db_password}@backenddb.2ansun2.mongodb.net
3. In ```mongo_config.py```, the value of ```db``` should be the name of your database:
```bash
db = client.<database-name>
```
4. In ```mongo_config.py```, the value of ```collection``` should be the name of your database's collection:
```bash
collection = db["<database-collection-name>"]
```

---

## 🚀 Running/Stopping the API
### Start the app using Uvicorn
```bash
uvicorn main:app --reload
```
Once running, you can access the API at:
```bash
http://127.0.0.1:8000
```
### Stop the app
To stop the app, you can use ```ctrl + C``` to terminate the process, and run ```deactivate``` in the terminal to exit the python virtual environment.

---

## 🧪 Testing the API
Use **Postman** or **Insomnia** to test the CRUD endpoints.

> **Note:** All routes are prefixed with ```/tasks```

| Method | Endpoint               | Description                                       |
| ------ | ---------------------- | ------------------------------------------------- |
| POST   | /create                | Create task.                                      |
| GET    | /all                   | Get all tasks.                                    |
| GET    | /{task_id}             | Get specific task.                                |
| PUT    | /update/{task_id}      | Update a specified task. Partial updates allowed. |
| PATCH  | /recover/{task_id}     | Recover a **soft-deleted** task.                  |
| DELETE | /soft_delete/{task_id} | **Soft-delete** a task (can be recovered).        |
| DELETE | /perm_delete/{task_id} | **Permanently** delete a task.                    |

---

## 🛠️ Custom OpenAPI Spec
By default, FastAPI automatically generates the OpenAPI spec. If you'd' like to customize it, you will need to first generate the default spec by running ```generate_openapi.py```. This will create a folder in the root directory (```/docs```) containing the generated spec.
> **Note:** Any modifications to the spec should also be reflected in the API code. For example, adding new fields to a request in the spec won't automatically make the API handle them.
