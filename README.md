<h1 align="center">🏣 pgMate - built with <b>Django</b> and ❤️.</h1>
<p align="center">
  production-ready Django application for managing PG accommodations! 
</p>

<p align="center">
  <a href="https://github.com/ursmaheshj/pgMate/issues/new/choose">🐞 Report Bug</a>
  ·
  <a href="https://github.com/ursmaheshj/pgMate/issues/new/choose">🚀 Request Feature</a>
  ·
  <a href="https://github.com/ursmaheshj/pgMate/issues/new/choose">💡 Propose Idea</a>
</p>

<hr>

## 🌟 Overview
Provides a two-sided marketplace, where PG (Paying Guest) Owners can list accommodations and Students/Seekers can browse and apply for them.

## 🛠️ Installation and Usage

Before you begin, ensure you have **Python** and **Django** installed on your system.

1. *Clone the Repository:* `git clone https://github.com/ursmaheshj/pgMate.git`
2. *Navigate to the Root Directory:* Ensure you are inside the `pgMate` folder before running the following commands.
3. *Set Up Virtual Environment (Optional but Recommended):* Create and activate a virtual environment using `venv` or `virtualenv`.
4. *Install Dependencies:* `pip install -r requirements.txt`
5. *Setup and Configuration:* Run following commands in order to prepare the application:
6. *Generate Migrations:* `python manage.py makemigrations`
7. *Apply Migrations:* `python manage.py migrate`
8. *Start the server:* `python manage.py runserver`
9. Now You are good to go register and login yourself as owner or seeker

## 🧐 Key Features
- **Multi-Role Dashboards:** Customized interfaces for PG owner and PG seeker.
- **Secure Auth:** Authentication with role-based access control.
- **Responsive Design:** Fully adaptive UI
- **Custom User Model:** Extend `AbstractUser` to include a `user_role` field.
    - `is_manager`: Can Add/Edit/Delete PG listings and view applications.
    - `is_seeker`: Can browse listings, search by city, and submit applications.

- **Search & Discovery**
    - Search by city
    - Filter by price range (min/max)
    - Filter by amenities (WiFi, AC, Food, Laundry)
- **Listing Management**
    - Create unlimited PG listings
    - Upload images
    - Edit/Delete listing details
    - Real-time updates
- **Application System**
    - Easy apply process
    - Optional message to owner
    - Status tracking (Pending/Approved/Rejected)
    - Seeker application history
- **Dashboard & Analytics**
    - Manager statistics
    - Application counts
    - Listing metrics

## 💻 Built with
- <a href="https://www.python.org/" target="blank">Python</a>
- <a href="https://www.djangoproject.com/" target="blank">Django</a>
- <a href="https://pillow.readthedocs.io/en/stable/" target="blank">Pillow</a>
- <a href="https://getbootstrap.com/" target="blank">Bootstrap 5</a>
- <a href="https://fontawesome.com/" target="blank">FontAwesome 6.4</a>

## 🍰 Contributing

Please contribute using [GitHub Flow](https://guides.github.com/introduction/flow); Create a branch, add commits, and [open a pull request](https://github.com/ursmaheshj/pgMate/compare).

## 🙏 Support
Dont hesitate to [fork](https://github.com/login?return_to=%2Fursmaheshj%2FpgMate) this repository and Give a ⭐[star](https://github.com/login?return_to=%2Fursmaheshj%2FpgMate) if you like it..
