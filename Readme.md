# Django Blog Application

A full-featured blog application built with Django and Django REST Framework, featuring user authentication, post management, commenting system, and user profiles. This project demonstrates modern web development practices with a clean, responsive Bootstrap 5 interface.

## Features

### Authentication System
* **User Registration**: New users can create accounts with secure signup functionality
* **Session-Based Authentication**: Secure login/logout system using Django's built-in session management
* **Access Control**: Login required decorators protect sensitive routes and functionality
* **User Authorization**: Users can only edit and delete their own posts, ensuring content ownership

### Blog Management
* **Create Posts**: Authenticated users can create new blog posts with rich content
* **Edit Posts**: Users can modify their own posts with an intuitive editing interface
* **Delete Posts**: Post authors have the ability to remove their own content
* **Slug-Based URLs**: Clean, SEO-friendly URLs using slugs for individual post viewing
* **Dynamic Rendering**: Components are rendered dynamically based on user permissions and content

### User Profiles
* **Profile Management**: Each user has a dedicated profile page
* **User Information Display**: Comprehensive user details and statistics
* **Profile Customization**: Users can manage their account information

### Comments System
* **Nested Comments**: Hierarchical comment structure for organized discussions
* **Comment Management**: Users can engage with posts through a robust commenting system
* **Serialized Data**: Comments are efficiently handled through nested serializers

### Design & UI
* **Bootstrap 5**: Modern, responsive design using the latest Bootstrap framework
* **Template Inheritance**: DRY principle implementation with reusable base templates
* **Mobile Responsive**: Optimized for all device sizes and screen resolutions
* **Intuitive Interface**: Clean, user-friendly design with smooth navigation

## 🛠 Technologies Used

### Backend
* **Python**: Core programming language for server-side logic
* **Django**: High-level Python web framework for rapid development
* **Django REST Framework**: Powerful toolkit for building Web APIs

### Frontend
* **HTML5**: Semantic markup for structured content
* **Bootstrap 5**: CSS framework for responsive, mobile-first design
* **Template System**: Django's built-in templating engine with inheritance

### Database
* **PostgreSQL**: Production-ready relational database with advanced features and scalability

## Project Structure

The application is organized into four main Django apps:

### Authentication App
Dedicated to all authentication purposes including user login, registration, logout, password management, and session handling. This app ensures secure user access control throughout the application.

### Users App
Specifically focused on creating and managing user profiles. Handles user profile information, profile updates, user statistics, and profile-related functionality separate from authentication logic.

### Posts App
Handles all blog post related functionality including creation, editing, deletion, and display of blog posts with slug-based routing.

### Comments App
Manages the commenting system with nested serialization support, allowing for threaded discussions on blog posts.

## Installation & Setup

### Prerequisites
* Python 3.8 or higher
* pip (Python package manager)

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/django-blog.git
cd django-blog
```

### Step 2: Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate  # On Windows (default)
source venv/bin/activate  # On macOS/Linux
```

### Step 3: Install Dependencies
```bash
pip install django
pip install djangorestframework
pip install pillow
pip install psycopg2-binary
```

### Step 4: Database Configuration
Configure your PostgreSQL database in `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'myproject_db',  # The database name you created in pgAdmin
        'USER': 'postgres',      # Default PostgreSQL username
        'PASSWORD': 'your_password_here',  # Password you set during installation
        'HOST': 'localhost',     # Database server location
        'PORT': '5432',         # Default PostgreSQL port
    }
}
```

### Step 5: Database Setup
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 6: Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### Step 7: Run Development Server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/posts` to access the application.

## Key Concepts Demonstrated

### URL Routing with Slugs
Implementation of slug-based URLs for individual post viewing, creating SEO-friendly and human-readable web addresses that improve user experience and search engine optimization.

### Dynamic Component Rendering
Advanced templating techniques that render components based on user authentication status, permissions, and content ownership, providing a personalized experience for each user.

### Authentication & Authorization
Comprehensive security implementation using Django's built-in authentication system, including session management, login required decorators, and permission-based access control.

### Bootstrap 5 Integration
Modern frontend development using Bootstrap 5's utility classes, responsive grid system, and component library to create a professional, mobile-first user interface.

### Nested Serialization
Advanced Django REST Framework implementation featuring nested serializers that efficiently handle complex data relationships, particularly for displaying comments associated with blog posts.

### Template Inheritance
Implementation of DRY (Don't Repeat Yourself) principles through Django's template inheritance system, creating maintainable and reusable template structures.

## Security Features

* **CSRF Protection**: Built-in cross-site request forgery protection
* **Session Security**: Secure session-based authentication
* **Permission Validation**: Server-side permission checking for all sensitive operations
* **Input Sanitization**: Protection against common web vulnerabilities
* **User Authorization**: Strict content ownership validation

## Learning Outcomes

This project demonstrates proficiency in:

* **Full-Stack Development**: Integration of backend logic with frontend presentation
* **Django Framework**: Advanced usage of Django's features and conventions
* **REST API Development**: Building efficient APIs with Django REST Framework
* **Database Relationships**: Managing complex data relationships and migrations
* **User Experience Design**: Creating intuitive interfaces with Bootstrap 5
* **Security Best Practices**: Implementing authentication and authorization systems
* **Code Organization**: Structuring large applications with multiple apps and clear separation of concerns

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is open source and available for use.

## Contact

If you have any questions or suggestions, please feel free to reach out or open an issue in the repository.

---

**Built with ❤️ using Django and Django REST Framework**