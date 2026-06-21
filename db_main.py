from db_tables import create_all_tables
from db_crud_operations import insert_user, insert_post, get_all_users, get_user_by_id, get_post_by_user_id, update_user_name, delete_user_by_id

# create_all_tables()

# insert_user('Harold', 'Harold@gmail.com', 'Delhi')
# insert_user('Parmesh', 'Parmesh@gmail.com', 'Bangalore')
# insert_user('Jyotirmay', 'Jyotirmay@gmail.com', 'Hyderabad')

# insert_post(1, 'Agentic AI')
# insert_post(2, 'Data Science')
# insert_post(3, 'Machine Learning')
# insert_post(1, 'Java')
# insert_post(2, 'JavaScript')

# print(get_all_users())

# print(get_user_by_id(3))

# print(get_post_by_user_id(2))

# print(get_user_by_id(2))
# update_user_name(2, 'Parmesh Kumar')

# user = get_user_by_id(200)

# if not user:
#     print("User not found.")
# else:
#     print(user.name)

delete_user_by_id(1)