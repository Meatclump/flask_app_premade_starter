import modules.db_interface as db_interface

def validate_new_user(username: str, password: str) -> list:
    error_list = []
    if db_interface.user_exists(username):
        error_list.append(f"The username '{username}' already exists. Please choose a different one.")

    if len(username) < 3:
        error_list.append(f"Your username may not be shorter than 3 characters.")
    
    if username.isalpha() is False:
        error_list.append(f"Your username may only use english alphabetic characters")
    
    if len(password) < 6:
        error_list.append(f"Your password must be at least 6 characters. Please choose a different one.")
    
    return error_list