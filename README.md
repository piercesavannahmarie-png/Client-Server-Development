# Client-Server-Development
# CS 340: Client/Server Development Portfolio Reflection

## Artifact Included

* Project Two Dashboard Application
* Project Two README Documentation

---

## How do you write programs that are maintainable, readable, and adaptable?

I write programs that are maintainable, readable, and adaptable by organizing code into separate modules, using meaningful variable and function names, and including comments where necessary to explain important sections of code. During this course, I created a CRUD Python module in Project One that handled all database interactions. Separating the database operations from the dashboard application made the code easier to maintain because changes to the database connection or queries could be made in one location without affecting the rest of the application.

Using the CRUD module also improved code reuse. Instead of writing database connection code throughout the dashboard, the dashboard simply called methods from the CRUD module whenever data was needed. This approach reduced duplication and made debugging easier. In the future, I could reuse this CRUD module as the foundation for other applications that need to connect to the same database, such as web applications, reporting tools, or mobile applications.

## How do you approach a problem as a computer scientist?

When approaching a problem as a computer scientist, I first analyze the requirements and break the project into smaller, manageable tasks. For the Grazioso Salvare dashboard project, I started by understanding how the database stored animal rescue information and then determined how users would interact with that data through the dashboard interface. After understanding the requirements, I developed the database functionality, tested the CRUD operations, and then integrated those functions into the dashboard components.

This project differed from many previous assignments because it required connecting multiple technologies together rather than focusing on a single programming concept. I had to combine database management, Python programming, and data visualization into a complete solution. In future projects, I would continue using a structured approach that includes requirements analysis, modular design, testing throughout development, and continuous evaluation of how the system meets client needs.

## What do computer scientists do, and why does it matter?

Computer scientists design, develop, and maintain systems that solve real-world problems through technology. Their work matters because organizations rely on accurate, efficient, and secure systems to make informed decisions and improve productivity.

The dashboard developed for Grazioso Salvare demonstrates how computer science can help organizations work more effectively. By providing interactive filtering, visualizations, and location mapping, the dashboard allows users to quickly identify animals that meet specific rescue training criteria. This reduces the time required to analyze large amounts of data and helps the organization make better decisions. Projects like this show how software solutions can transform raw data into meaningful information that supports an organization's goals and improves overall efficiency.
