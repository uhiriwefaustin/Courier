import os
import django
from decimal import Decimal

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'courier_system.settings')
django.setup()

from companies.models import Company
from logistics.models import BusRoute, Station, Driver
from clients.models import Client, Receiver
from packages.models import Package, PackageType

from accounts.models import User

def seed_data():
    print("Seeding database...")

    # Users
    users_to_create = [
        ('manager', 'manager@example.com', 'password123', 'Manager'),
        ('clerk', 'clerk@example.com', 'password123', 'Clerk'),
        ('driver_user', 'driver@example.com', 'password123', 'Driver'),
        ('auditor', 'auditor@example.com', 'password123', 'Auditor'),
    ]

    for username, email, password, role in users_to_create:
        if not User.objects.filter(username=username).exists():
            User.objects.create_user(username=username, email=email, password=password, role=role)
            print(f"User '{username}' with role '{role}' created.")
        else:
            u = User.objects.get(username=username)
            u.set_password(password)
            u.role = role
            u.save()

    # Companies
    c1, _ = Company.objects.get_or_create(name="Rwanda Express", contact="+250 123 456", headquarters="Kigali")
    c2, _ = Company.objects.get_or_create(name="Swift Logistics", contact="+250 987 654", headquarters="Musanze")

    # Package Types
    pt1, _ = PackageType.objects.get_or_create(type_name="Standard", description="Standard delivery package")
    pt2, _ = PackageType.objects.get_or_create(type_name="Fragile", description="Handle with care")

    # Clients
    cl1, _ = Client.objects.get_or_create(name="Jean Bosco", phone="+250 788 111", address="Kigali, Nyarugenge", email="bosco@example.com")
    cl2, _ = Client.objects.get_or_create(name="Maria Umutoni", phone="+250 788 222", address="Gisenyi, Rubavu", email="maria@example.com")

    # Receivers
    rc1, _ = Receiver.objects.get_or_create(name="John Doe", phone="+250 788 333", address="Butare, Huye")
    rc2, _ = Receiver.objects.get_or_create(name="Alice Gates", phone="+250 788 444", address="Kibuye, Karongi")

    # Routes
    r1, _ = BusRoute.objects.get_or_create(company=c1, departure_city="Kigali", arrival_city="Musanze", duration="2 hours", frequency="Daily")
    r2, _ = BusRoute.objects.get_or_create(company=c2, departure_city="Kigali", arrival_city="Gisenyi", duration="3.5 hours", frequency="Twice Daily")

    # Stations
    Station.objects.get_or_create(route=r1, station_name="Kigali Main", city="Kigali")
    Station.objects.get_or_create(route=r1, station_name="Nyabugogo", city="Kigali")
    Station.objects.get_or_create(route=r2, station_name="Rubavu Station", city="Gisenyi")

    # Drivers - Username matches driver name for simple testing
    d1, _ = Driver.objects.get_or_create(name="driver_user", phone="+250 788 555", vehicle_type="Toyota Hiace", company=c1)
    d2, _ = Driver.objects.get_or_create(name="Saidi Hakizimana", phone="+250 788 666", vehicle_type="Isuzu Elf", company=c2)

    # Packages
    p1, _ = Package.objects.get_or_create(
        sender=cl1, receiver=rc1, package_type=pt1, 
        weight=2.5, status="In Transit",
        driver=d1, company=c1, route=r1, delivery_fee=Decimal('5000.00')
    )
    p2, _ = Package.objects.get_or_create(
        sender=cl2, receiver=rc2, package_type=pt2, 
        weight=1.0, status="Exception",
        driver=d2, company=c2, route=r2, delivery_fee=Decimal('3500.00')
    )

    # Exceptions
    from tracking.models import PackageException
    PackageException.objects.get_or_create(
        package=p2,
        exception_type="Damaged",
        description="Box arrived crushed at Kigali Main station."
    )

    print("Database seeding completed successfully.")

if __name__ == "__main__":
    seed_data()
