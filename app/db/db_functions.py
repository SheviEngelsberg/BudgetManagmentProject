from app.db.db_connector import my_db
from app.utils import to_json


async def get_all(collection_name):
    try:
        cursor = my_db[collection_name].find({})
        results = await cursor.to_list(length=None)
        return to_json(results)
    except Exception as e:
        raise RuntimeError(f"Error retrieving documents from collection {collection_name}: {e}")


async def get_by_id(object_id, collection_name):
    try:
        user = await my_db[collection_name].find_one({"id": object_id})
        return to_json(user)
    except Exception as e:
        raise RuntimeError(f"Error cannot get this {object_id} object: {e}")


async def add(document, collection_name):
    try:
        result = await my_db[collection_name].insert_one(document)
        return {"inserted_id": str(result.inserted_id)}
    except Exception as e:
        raise RuntimeError(f"Error adding document to collection {collection_name}: {e}")


async def update(document, collection_name):
    try:
        existing_document = await get_by_id(document['id'], collection_name)
        if existing_document:
            await my_db[collection_name].replace_one({"id": document['id']}, document)
            return f"Document with ID {document['id']} updated successfully."
        else:
            return f"No document found with ID {document['id']}."
    except Exception as e:
        raise RuntimeError(f"Error updating document: {e}")
