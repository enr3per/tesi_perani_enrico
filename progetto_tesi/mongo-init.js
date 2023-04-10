db.users.insert([
    {
      name: "Alice",
      age: 25,
      email: "alice@example.com"
    },
    {
      name: "Bob",
      age: 30,
      email: "bob@example.com"
    }
  ]);
  
  db.customers.insert([
    {
      name: "Acme Inc.",
      address: "123 Main St.",
      city: "Anytown",
      state: "CA",
      country: "USA"
    },
    {
      name: "XYZ Corporation",
      address: "456 Oak St.",
      city: "Anytown",
      state: "CA",
      country: "USA"
    }
  ]);
  
  db.products.insert([
    {
      name: "Product 1",
      description: "A great product",
      price: 9.99
    },
    {
      name: "Product 2",
      description: "Another great product",
      price: 19.99
    }
  ]);