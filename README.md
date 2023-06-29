# Login-Authentication
A program that utilizes Python, SQLalchemy, and Flask to implement logic that allows users to register their information into a database and login if their data is already stored and their password is correct.After authenticated, the user is then directed to a secret page where they can download files only accessible to authenticated users.  The program encrypts user passwords through hashing using the Werkzeug module. In order to increase the level of security when hashing I added a salt length of 8 chars in order to make data more secure. When a user's email does not exist, the password is incorrect, or account already exists when registering The user is given a flash message letting them know what the error is.

<img width="1440" alt="Screenshot 2023-06-28 at 9 47 46 PM" src="https://github.com/Dillon1john/Login-Authentication/assets/50587936/30da5727-680a-43a8-9f7f-d4d000f1fbdd">
<img width="1440" alt="Screenshot 2023-06-28 at 9 47 58 PM" src="https://github.com/Dillon1john/Login-Authentication/assets/50587936/e74826bd-828d-4a58-9e64-7c520a325e60">
<img width="1440" alt="Screenshot 2023-06-28 at 9 50 48 PM" src="https://github.com/Dillon1john/Login-Authentication/assets/50587936/b43fbc92-9257-4532-b8b9-47bc5043e82b">
<img width="1440" alt="Screenshot 2023-06-28 at 9 51 10 PM" src="https://github.com/Dillon1john/Login-Authentication/assets/50587936/2b23a47a-d319-40b5-8eb2-695a2fcc25fa">
<img width="1440" alt="Screenshot 2023-06-28 at 9 51 26 PM" src="https://github.com/Dillon1john/Login-Authentication/assets/50587936/dd525bcc-aec3-4fdf-ac48-6a3b46454f30">
<img width="1440" alt="Screenshot 2023-06-28 at 9 51 41 PM" src="https://github.com/Dillon1john/Login-Authentication/assets/50587936/571aaaa6-d26c-43c6-9678-127ba0927126">
<img width="1440" alt="Screenshot 2023-06-28 at 9 53 36 PM" src="https://github.com/Dillon1john/Login-Authentication/assets/50587936/c6f8f121-8eec-4dbb-8c5b-90514fcd2640">
<img width="1440" alt="Screenshot 2023-06-28 at 9 55 11 PM" src="https://github.com/Dillon1john/Login-Authentication/assets/50587936/9adf0c96-77ec-459b-9bc7-e36f49c0a5a8">
<img width="1149" alt="Screenshot 2023-06-28 at 9 56 58 PM" src="https://github.com/Dillon1john/Login-Authentication/assets/50587936/4c7511ce-fbaf-4daa-9cad-2c069a9275a4">
