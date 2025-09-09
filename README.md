# Django Image Uploader

A simple yet elegant Django web application that allows users to upload and display images with a clean, responsive interface built using Bootstrap.

## Features

- **Image Upload**: Easy drag-and-drop or click-to-upload interface
- **Image Gallery**: Display uploaded images in a responsive grid layout
- **Timestamp Tracking**: Automatic timestamp recording for each uploaded image
- **Success Notifications**: User-friendly success messages after successful uploads
- **Responsive Design**: Mobile-friendly interface using Bootstrap 4
- **Media Management**: Organized storage of uploaded images with Django's media handling

## Technology Stack

- **Backend**: Django 4.2.3
- **Database**: SQLite (default, easily configurable for PostgreSQL/MySQL)
- **Frontend**: HTML5, CSS3, Bootstrap 4, JavaScript
- **Image Processing**: Pillow (PIL Fork)
- **Static Files**: WhiteNoise for production static file serving
- **Additional Tools**: 
  - django-debug-toolbar (development)
  - django-unused-media (media cleanup)
  - gunicorn (production WSGI server)
  - whitenoise (production static file serving)

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/ritiksharmaaa/django_image_uploader.git
cd django_image_uploader
```

### 2. Create and Activate Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
# Install all dependencies (includes whitenoise and other production dependencies)
pip install -r req.txt

# Alternative: Use requirement.txt (minimal dependencies, you may need to install whitenoise separately)
# pip install -r requirement.txt
# pip install whitenoise
```

### 4. Configure Settings (Optional)

The application comes with default settings suitable for development. For production deployment, you may want to:

- Generate a new `SECRET_KEY` in `image_uploader/settings.py`
- Set `DEBUG = False` for production
- Configure your preferred database in the `DATABASES` setting
- Update `ALLOWED_HOSTS` with your domain

### 5. Set Up Database

```bash
python manage.py migrate
```

### 6. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

## Usage

### Running the Development Server

```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

### Uploading Images

1. Navigate to the home page
2. Click on the file input or drag and drop an image
3. Click the "Upload" button
4. View your uploaded image in the gallery below

### Admin Interface

Access the Django admin interface at `http://127.0.0.1:8000/admin/` to manage uploaded images and user accounts.

## Project Structure

```
django_image_uploader/
├── app/                          # Main application directory
│   ├── migrations/              # Database migrations
│   ├── templates/               # HTML templates
│   │   └── myapp/
│   │       └── home.html       # Main upload/gallery page
│   ├── models.py               # Image model definition
│   ├── views.py                # View logic for image handling
│   ├── forms.py                # Upload form definition
│   └── admin.py                # Admin interface configuration
├── image_uploader/             # Project configuration
│   ├── settings.py            # Django settings
│   ├── urls.py                # URL routing
│   └── wsgi.py                # WSGI configuration
├── media/                      # Uploaded images storage
│   └── uploaded_image/        # Image upload directory
├── staticfiles/               # Collected static files
├── manage.py                  # Django management script
├── requirement.txt           # Core Python dependencies
├── req.txt                   # Full Python dependencies (recommended)
└── db.sqlite3               # SQLite database file
```

## Configuration

### Media Files

Uploaded images are stored in the `media/uploaded_image/` directory. The media URL is configured as `/media/` in the settings.

### Static Files

Static files are handled by WhiteNoise in production. For development, Django's built-in static file serving is used.

### Database

The application uses SQLite by default. To use a different database:

1. Install the appropriate database adapter (e.g., `psycopg2` for PostgreSQL)
2. Update the `DATABASES` setting in `image_uploader/settings.py`
3. Run migrations: `python manage.py migrate`

## Deployment

The application is configured for easy deployment with:

- WhiteNoise for static file serving
- Gunicorn WSGI server for production
- Production-ready settings structure
- WSGI configuration for deployment platforms

### Production Server

For production deployment, you can use Gunicorn:

```bash
# Collect static files
python manage.py collectstatic --noinput

# Run with Gunicorn
gunicorn image_uploader.wsgi:application --bind 0.0.0.0:8000
```

### Environment Variables (Recommended for Production)

Consider using environment variables for sensitive settings:

```python
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key')
DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost').split(',')
```

## Development

### Adding New Features

1. Create new views in `app/views.py`
2. Add URL patterns in `image_uploader/urls.py`
3. Create templates in `app/templates/myapp/`
4. Update models in `app/models.py` if needed
5. Run migrations: `python manage.py makemigrations && python manage.py migrate`

### Running Tests

```bash
python manage.py test
```

## Security Considerations

- **SECRET_KEY**: Generate a new secret key for production
- **DEBUG**: Set to `False` in production
- **ALLOWED_HOSTS**: Configure appropriate hosts for production
- **File Validation**: Consider adding file type and size validation
- **CSRF Protection**: Enabled by default in Django

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Troubleshooting

### Common Issues

**Import Error for Django**: Ensure Django is installed and virtual environment is activated
```bash
pip install Django==4.2.3
```

**Missing Static Files**: Collect static files for production
```bash
python manage.py collectstatic
```

**Permission Errors**: Ensure the media directory has write permissions
```bash
chmod 755 media/
```

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

For support, please open an issue on the GitHub repository or contact the maintainer.

---

**Note**: This application is designed for educational and development purposes. For production use, consider implementing additional security measures, file validation, and user authentication as needed.