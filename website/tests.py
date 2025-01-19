from django.test import TestCase
from django.urls import reverse
from .models import Customer, Product, Order, Employee, Supplier, Record

# Тесты для моделей
class CustomerModelTest(TestCase):

    def setUp(self):
        self.customer = Customer.objects.create(
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            phone="1234567890",
            address="123 Main St",
            created_at="2023-01-01T00:00:00Z"
        )

    def test_customer_creation(self):
        self.assertTrue(isinstance(self.customer, Customer))
        self.assertEqual(self.customer.__str__(), f"{self.customer.first_name} {self.customer.last_name}")

class ProductModelTest(TestCase):

    def setUp(self):
        self.product = Product.objects.create(
            name="Product 1",
            description="This is a test product.",
            price=9.99,
            created_at="2023-01-01T00:00:00Z"
        )

    def test_product_creation(self):
        self.assertTrue(isinstance(self.product, Product))
        self.assertEqual(self.product.__str__(), self.product.name)

class OrderModelTest(TestCase):

    def setUp(self):
        self.customer = Customer.objects.create(
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            phone="1234567890",
            address="123 Main St",
            created_at="2023-01-01T00:00:00Z"
        )
        self.product = Product.objects.create(
            name="Product 1",
            description="This is a test product.",
            price=9.99,
            created_at="2023-01-01T00:00:00Z"
        )
        self.order = Order.objects.create(
            customer=self.customer,
            quantity=2,
            order_date="2023-01-01",
            status="Pending"
        )
        self.order.product.add(self.product)

    def test_order_creation(self):
        self.assertTrue(isinstance(self.order, Order))
        self.assertEqual(self.order.__str__(), f"Order {self.order.id} by {self.order.customer}")

class EmployeeModelTest(TestCase):

    def setUp(self):
        self.employee = Employee.objects.create(
            first_name="Jane",
            last_name="Doe",
            email="jane.doe@example.com",
            phone="0987654321",
            position="Manager",
            hired_date="2023-01-01"
        )

    def test_employee_creation(self):
        self.assertTrue(isinstance(self.employee, Employee))
        self.assertEqual(self.employee.__str__(), f"{self.employee.first_name} {self.employee.last_name}")

class SupplierModelTest(TestCase):

    def setUp(self):
        self.supplier = Supplier.objects.create(
            name="Supplier 1",
            contact_name="Supplier Contact",
            phone="1231231234",
            address="456 Another St"
        )

    def test_supplier_creation(self):
        self.assertTrue(isinstance(self.supplier, Supplier))
        self.assertEqual(self.supplier.__str__(), self.supplier.name)

class RecordModelTest(TestCase):

    def setUp(self):
        self.record = Record.objects.create(
            first_name="Alice",
            last_name="Smith",
            email="alice.smith@example.com",
            phone="1233211234",
            address="789 Main St",
            created_at="2023-01-01T00:00:00Z"
        )

    def test_record_creation(self):
        self.assertTrue(isinstance(self.record, Record))
        self.assertEqual(self.record.__str__(), f"{self.record.first_name} {self.record.last_name}")

# Тесты для представлений
class CustomerViewTest(TestCase):

    def setUp(self):
        self.customer = Customer.objects.create(
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            phone="1234567890",
            address="123 Main St",
            created_at="2023-01-01T00:00:00Z"
        )

    def test_customer_list_view(self):
        response = self.client.get(reverse('customer_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "John Doe")
        self.assertTemplateUsed(response, 'customer_list.html')

    def test_customer_detail_view(self):
        response = self.client.get(reverse('customer_detail', args=[self.customer.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "John Doe")
        self.assertTemplateUsed(response, 'customer_detail.html')
