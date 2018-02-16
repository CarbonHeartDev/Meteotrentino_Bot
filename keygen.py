from modules.file_url_helper import relative_to_absolute
from modules.users import UsersDatabase

database = UsersDatabase(relative_to_absolute('\\Data\\Users_Database\\users.json'),relative_to_absolute('\\Data\\Users_Database\\tokens.json'))
print(database.generaChiave)
