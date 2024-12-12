from pymongo import MongoClient

# Replace with your MongoDB URI
MONGO_URI = "mongodb+srv://ayonjd178:ayonjd178@cluster0.wqxk9a6.mongodb.net/todo_db?retryWrites=true&w=majority&appName=Cluster0"


client = MongoClient(MONGO_URI)
db = client.todo_db
tasks_collection = db.tasks
