from zeep import Client

# Using a public SOAP calculator web service
WSDL_URL = "http://www.dneonline.com/calculator.asmx?WSDL"

print("=" * 60)
print("🧮 SOAP API - CALCULATOR (Addition of Two Numbers)")
print("=" * 60)

try:
    # Create SOAP client
    print("\n🔗 Connecting to SOAP service...")
    client = Client(wsdl=WSDL_URL)
    
    print("✓ Connected successfully!\n")
    
    # Get two numbers from user
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    
    print(f"\n📤 Sending SOAP request to add {num1} + {num2}...")
    
    # Call the Add operation
    result = client.service.Add(num1, num2)
    
    print(f"\n✅ SOAP Response Received!")
    print(f"📊 Result: {num1} + {num2} = {result}")
    
    # Display available operations
    print("\n" + "=" * 60)
    print("📋 Other Available Operations in this SOAP service:")
    print("=" * 60)
    
    # Show all available operations
    for service in client.wsdl.services.values():
        print(f"\nService: {service.name}")
        for port in service.ports.values():
            operations = sorted(port.binding._operations.keys())
            for operation in operations:
                print(f"  - {operation}")
    
    # Demonstrate other operations
    print("\n" + "=" * 60)
    print("🔢 Demonstrating All Calculator Operations:")
    print("=" * 60)
    
    print(f"\n➕ Addition: {num1} + {num2} = {client.service.Add(num1, num2)}")
    print(f"➖ Subtraction: {num1} - {num2} = {client.service.Subtract(num1, num2)}")
    print(f"✖️  Multiplication: {num1} × {num2} = {client.service.Multiply(num1, num2)}")
    
    if num2 != 0:
        print(f"➗ Division: {num1} ÷ {num2} = {client.service.Divide(num1, num2)}")
    else:
        print(f"➗ Division: Cannot divide by zero")

except ValueError:
    print("❌ Error: Please enter valid numbers!")
except Exception as e:
    print(f"❌ Error: {e}")

print("\n" + "=" * 60)
