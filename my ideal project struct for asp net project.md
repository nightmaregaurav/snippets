### 1. **Core Layer:** (`AppName.Domain` Class Library)
The innermost layer containing the most fundamental business logic and domain entities.
- **Purpose:** Represents the core business model and rules.
- **Contains:**
    - `Entities`: POCO classes representing data structures (e.g., `Product`, `Order`).
    - `Enums`: Enumerations used within entities.
    - `RepositoryInterfaces`: Contracts for repositories (`IRepository<T>`, `IProductRepository`).

---

### 2. **Application Layer:** (`AppName.Application` Class Library)
Defines the application's behavior and use cases. It interacts with the domain layer via interfaces and implements business rules.
- **Purpose:** Implements business logic and use cases.
- **Contains:**
    - `Services`: Classes implementing business use cases (e.g., `OrderService`, `ProductService`).
    - `Models`: Data Transfer Objects to handle data flow between layers.
    - `ServiceInterfaces`: Service contracts (`IOrderService`, `IProductService`).

---

### 3. **Infrastructure Layer:** (`AppName.Infrastructure` Class Library)
Provides the implementations for external concerns like data access, file storage, third-party services, etc.
- **Purpose:** Handles all external integrations and implementations of core interfaces.
- **Contains:**
    - `Repositories`: Implementations of repository interfaces (`ProductRepository : IProductRepository`).
    - `DataContext`: Entity Framework **DbContext** for database interactions.
    - `Configurations`: Entity configurations for EF Core (`ProductConfiguration`).
    - `ExternalServices`: API clients, email services, etc.

---

### 4. **Presentation Layer:** (`AppName.Web` or `AppName.WebAPI` or `AppName.UI` or `AppName.Client` or `AppName.Presentation` Class Library)
The outermost layer responsible for presenting data to the user, typically through an API or UI.
- **Purpose:** Acts as the entry point for user interaction.
- **Contains:**
    - `Controllers`: Define API endpoints (`ProductsController`, `OrdersController`).
    - `ViewModels`: Request and response models.
    - `Middleware`: Exception handling, logging, authentication.
    - `Startup.cs` or `Program.cs`: Application configuration, DI setup, and middleware pipeline.

---

## **Dependency Flow:**
```
WebAPI --> Application --> Domain
WebAPI --> Infrastructure --> Domain
```

## **Folder Structure:**

```
MyApplication
│
├── MyApplication.Domain
│    ├── Entities
│    ├── RepositoryInterfaces
│    └── Enums
│
├── MyApplication.Application
│    ├── Services
│    ├── Models
│    └── ServiceInterfaces
│
├── MyApplication.Infrastructure
│    ├── Data
│    │     ├── Configurations
│    │     ├── Repositories
│    │     └── DataContext.cs
│    └── ExternalServices
│
└── MyApplication.WebAPI
     ├── Controllers
     ├── ViewModels
     ├── Middlewares
     ├── Startup.cs / Program.cs
     └── appsettings.json
```
