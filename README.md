# Spring Boot Intern 2025 July

A Spring Boot application developed during the 2025 July internship program.

## 🚀 Project Overview

This repository contains a Spring Boot application built with modern Java development practices and best practices.

## 📋 Prerequisites

- Java 17 or higher
- Maven 3.6+ or Gradle 7+
- Git

## 🛠️ Technology Stack

- **Framework**: Spring Boot
- **Language**: Java
- **Build Tool**: Maven/Gradle
- **Version Control**: Git

## 📁 Project Structure

```
src/
├── main/
│   ├── java/
│   │   └── com/
│   │       └── example/
│   │           └── helloworld/
│   │               ├── HelloWorldApplication.java
│   │               ├── controllers/
│   │               ├── services/
│   │               ├── models/
│   │               └── repositories/
│   └── resources/
│       ├── application.properties
│       ├── static/
│       └── templates/
└── test/
    └── java/
        └── com/
            └── example/
                └── helloworld/
```

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/Nithyaganesh43/Spring_Boot_Intern_2025_july.git
cd Spring_Boot_Intern_2025_july
```

### 2. Build the Project
```bash
# Using Maven
./mvnw clean install

# Using Gradle
./gradlew build
```

### 3. Run the Application
```bash
# Using Maven
./mvnw spring-boot:run

# Using Gradle
./gradlew bootRun
```

The application will be available at `http://localhost:8080`

## 📝 API Endpoints

- `GET /` - Welcome page
- `GET /api/hello` - Hello World endpoint
- `GET /health` - Health check endpoint

## 🧪 Testing

```bash
# Run tests with Maven
./mvnw test

# Run tests with Gradle
./gradlew test
```

## 📦 Building for Production

```bash
# Create JAR file with Maven
./mvnw clean package

# Create JAR file with Gradle
./gradlew build
```

## 🔧 Configuration

The application can be configured using `application.properties` or `application.yml`:

```properties
# Server configuration
server.port=8080
server.servlet.context-path=/

# Database configuration (if applicable)
spring.datasource.url=jdbc:h2:mem:testdb
spring.datasource.driverClassName=org.h2.Driver
spring.datasource.username=sa
spring.datasource.password=

# JPA configuration
spring.jpa.database-platform=org.hibernate.dialect.H2Dialect
spring.jpa.hibernate.ddl-auto=create-drop
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Nithyaganesh43**
- GitHub: [@Nithyaganesh43](https://github.com/Nithyaganesh43)

## 🙏 Acknowledgments

- Spring Boot team for the amazing framework
- Internship program organizers
- All contributors and mentors

---

**Note**: This is a learning project developed during the 2025 July internship program.

## 🎯 Latest Update
- Added comprehensive project documentation
- Included setup instructions and API endpoints
- Added contributing guidelines and project structure
