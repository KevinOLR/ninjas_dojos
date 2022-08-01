from mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.age = data['age']
        self.created_id = data['created_id']
        self.updated_id = data['updated_id']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL('ninjas_dojos').query_db(query)
        ninjas = []
        for ninja in results:
            ninjas.append( cls(ninja) )
        return ninjas

    @classmethod
    def save(cls, data):
        query = "INSERT INTO ninjas (first_name,last_name,email,age) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(age)s);"

        # comes back as the new row id
        result = connectToMySQL('ninjas_dojos').query_db(query,data)
        return result

    @classmethod
    def get_one(cls,data):
        query  = "SELECT * FROM ninjas WHERE id = %(id)s";
        result = connectToMySQL('ninjas_dojos').query_db(query,data)
        return cls(result[0])
