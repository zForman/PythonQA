import csv
import json


def merge_json_and_csv(books, users):
    if books.endswith('.csv'):
        books = books
    else:
        raise Exception('choose a file in csv format')

    if users.endswith('.json'):
        users = users
    else:
        raise Exception('choose a file in json format')

    merged_data = []
    books_dict = []

    with open(books, 'r') as csv__book_file:
        book_list = csv.reader(csv__book_file)
        title = next(book_list)
        for book in book_list:
            books_dict.append(dict(zip(title, book)))

    with open(users, 'r') as file_users_json:
        users_list = json.loads(file_users_json.read())
        i = 0
        for user in users_list:
            if not user['isActive']:
                user['isActive'] = True
            i += 1
            user['books'] = books_dict[i]
            merged_data.append(user)
            with open('merged_file.json', 'w') as f:
                f.write(json.dumps(merged_data, indent=4))


merge_json_and_csv('books.csv', 'users.json')
