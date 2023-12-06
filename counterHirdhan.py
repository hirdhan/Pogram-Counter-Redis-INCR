import redis

# Membuat koneksi ke Redis server yang berjalan dalam Docker
r = redis.Redis(host='localhost', port=6379, db=0)

# Key untuk data pelanggan
customers_key = 'customer_data'
# Key untuk counter
counter_key = 'program_counter'

# Fungsi untuk menampilkan menu
def display_menu():
    print("Choose a CRUD operation:")
    print("1. Create a new customer")
    print("2. Read customer info")
    print("3. Update customer data")
    print("4. Delete a customer")
    print("5. Show program counter")
    print("6. Exit")

# Fungsi untuk membuat data pelanggan baru
def create_customer():
    customer_id = input("Enter customer ID: ")
    customer_name = input("Enter customer name: ")
    customer_email = input("Enter customer email: ")
    customer_data = f'Name: {customer_name}, Email: {customer_email}'
    r.hset(customers_key, customer_id, customer_data)
    print(f"Customer (ID {customer_id}) created.")

# Fungsi untuk membaca data pelanggan
def read_customer(customer_id):
    customer_info = r.hget(customers_key, customer_id)
    if customer_info:
        print(f"Customer Info (ID {customer_id}): {customer_info.decode('utf-8')}")
    else:
        print(f"Customer (ID {customer_id}) not found.")

# Fungsi untuk mengupdate data pelanggan
def update_customer(customer_id, new_data):
    r.hset(customers_key, customer_id, new_data)
    print(f"Customer (ID {customer_id}) updated.")

# Fungsi untuk menghapus data pelanggan
def delete_customer(customer_id):
    r.hdel(customers_key, customer_id)
    print(f"Customer (ID {customer_id}) deleted.")

# Fungsi untuk menampilkan program counter
def show_program_counter():
    counter_value = r.get(counter_key)
    if counter_value:
        print(f"Program Counter: {counter_value.decode('utf-8')}")
    else:
        print("Program Counter not found.")

# Increment program counter
current_counter = r.incr(counter_key)

# Main program
while True:
    display_menu()
    choice = input("Enter your choice (1/2/3/4/5/6): ")

    if choice == '1':
        create_customer()
    elif choice == '2':
        customer_id = input("Enter customer ID to read: ")
        read_customer(customer_id)
    elif choice == '3':
        customer_id = input("Enter customer ID to update: ")
        new_data = input("Enter new customer data: ")
        update_customer(customer_id, new_data)
    elif choice == '4':
        customer_id = input("Enter customer ID to delete: ")
        delete_customer(customer_id)
    elif choice == '5':
        show_program_counter()
    elif choice == '6':
        break
    else:
        print("Invalid choice. Please choose a valid option.")

# Menutup koneksi Redis
r.close()
