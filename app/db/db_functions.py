from app.db.db_connector import my_db
from app.utils import to_json


async def get_all(collection_name):
    """
    Retrieves all documents from a specified collection in the database.

    Args:
        collection_name (str): The name of the collection in the database.

    Returns:
        list: A list containing dictionaries of retrieved documents.
    """
    try:
        cursor = my_db[collection_name].find({})
        results = await cursor.to_list(length=None)
        if not results:
            raise ValueError("List not found")
        return to_json(results)
    except ValueError as ve:
        raise ve
    except Exception as e:
        raise RuntimeError(f"Error retrieving documents from collection {collection_name}: {e}")


async def get_by_id(object_id, collection_name):
    """
    Retrieves a document by its ID from a specified collection in the database.

    Args:
        object_id (any): The ID of the document to retrieve.
        collection_name (str): The name of the collection in the database.

    Returns:
        dict: A dictionary containing the retrieved document.
    """
    try:
        user = await my_db[collection_name].find_one({"id": object_id})
        if user is None:
            raise ValueError("User not found")
        return to_json(user)
    except ValueError as ve:
        raise ve
    except Exception as e:
        raise RuntimeError(f"Error cannot get this {object_id} object: {e}")


async def add(document, collection_name):
    """
    Adds a document to a specified collection in the database.

    Args:
        document (dict): The document to be added.
        collection_name (str): The name of the collection in the database.

    Returns:
        dict: A dictionary containing the inserted ID.
    """
    try:
        result = await my_db[collection_name].insert_one(document)
        return {"inserted_id": str(result.inserted_id)}
    except Exception as e:
        raise RuntimeError(f"Error adding document to collection {collection_name}: {e}")


async def update(document, collection_name):
    """
    Updates a document in the specified collection.

    Args:
        document (dict): The updated document.
        collection_name (str): The name of the collection in the database.

    Returns:
        str: A message indicating the success of the update.
    """
    try:
        existing_document = await get_by_id(document['id'], collection_name)
        if existing_document:
            new_document = {key: value for key, value in document.items() if key != '_id'}
            await my_db[collection_name].update_one({"id": document['id']}, {"$set": new_document})
            return f"Document with ID {document['id']} updated successfully."
        else:
            return f"No document found with ID {document['id']}."
    except Exception as e:
        raise RuntimeError(f"Error updating document: {e}")


async def login(collection_name, object_name, object_password):
    """
    Logs in a user.

    Args:
        collection_name (str): The name of the collection in the database.
        object_name (str): The username of the user.
        object_password (str): The password of the user.

    Returns:
        list: A list of dictionaries containing user information.
    """
    try:
        all_users = await get_all(collection_name)
        filtered_users = [user for user in all_users if user['user_name'] == object_name and user['password'] == object_password]
        if not filtered_users:
            raise ValueError("User not found")
        return filtered_users
    except ValueError as ve:
        raise ve
    except Exception as e:
        raise RuntimeError(f"Error during login: {e}")

