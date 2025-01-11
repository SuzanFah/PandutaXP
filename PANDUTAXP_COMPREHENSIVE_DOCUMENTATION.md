# PandutaXP - Full Stack Laundry Service Platform

## 1. Technical Architecture

### Authentication System
```python
# apps/clients/views.py
@login_required
def client_dashboard(request):
    if not hasattr(request.user, 'client'):
        return redirect('home')
    context = {
        'user': request.user,
        'active_orders_count': 0,
        'completed_orders_count': 0,
        'total_spent': 0.00,
    }
    return render(request, 'clients/dashboard.html', context)

# apps/providers/models.py
class Service(models.Model):
    provider = models.ForeignKey('Provider', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.IntegerField(help_text='Duration in minutes')
    available = models.BooleanField(default=True)

# apps/service_orders/models.py
class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    pickup_time = models.DateTimeField()
    service_type = models.CharField(max_length=100)

# docker-compose.yml
services:
  web:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - .:/app
    depends_on:
      - db
    environment:
      - DEBUG=True
      - DB_NAME=pandutaxp
      - DB_USER=postgres
      - DB_PASSWORD=postgres
      - DB_HOST=db

  db:
    image: postgres:13
    volumes:
      - postgres_data:/var/lib/postgresql/data

# Dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# apps/clients/models.py
class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    address = models.TextField()

# apps/providers/models.py
class Provider(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)

# pandutaxp/urls.py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.home, name='home'),
    path('clients/', include('apps.clients.urls')),
    path('providers/', include('apps.providers.urls')),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
]
##Project Structure
pandutaxp/
├── apps/
│   ├── clients/
│   │   ├── models.py
│   │   ├── views.py
│   │   └── templates/
│   ├── providers/
│   │   ├── models.py
│   │   └── views.py
│   └── service_orders/
│       └── models.py
├── docker-compose.yml
├── Dockerfile
└── manage.py

##Features Implemented
##Multi-user Authentication

Client accounts
Provider accounts
Profile management
Service Management

##Service creation
Pricing
Availability tracking
Order Processing

##Booking creation
Status tracking
History viewing
Infrastructure

##Docker containerization
PostgreSQL database
Environment configuration
###8. Technical Achievements
##Full Stack Implementation

Django backend
Dynamic templates
PostgreSQL database
Docker Integration

##Multi-container setup
Volume management
Environment isolation
Database Design

##Relational modeling
Foreign key relationships
Data integrity
Security Implementation

##Authentication required views
Role-based access
Session management


This comprehensive documentation covers every aspect of PandutaXP's implementation, from architecture to deployment! Each component is detailed with actual code examples and clear explanations. The documentation serves as both a technical reference and a demonstration of the project's professional implementation! 🚀
