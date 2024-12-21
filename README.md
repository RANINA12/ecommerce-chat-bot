<div align="center">
  <img src="client/public/logo.png">
</div>

<h1> society manage</h1>
The "ChatterBox" project is an interactive Django-based web application that serves as a chatbot, designed to answer user queries with a simple and user-friendly interface, leveraging HTML, CSS, and Django's robust framework for seamless functionality.
<br>

<h2>Features 🎯</h2>
<ul>
<li><strong>Interactive Query System:</strong> Users can input their queries in a chatbot-style interface and receive automated, logical responses.</li>
<li><strong>Dynamic Response Mechanism</strong> Incorporates rule-based responses, with the potential for AI-driven improvements like integrating OpenAI or similar APIs for smarter answers.</li>
<li><strong>User-Friendly Interface:</strong> Styled with HTML and CSS, the web application provides a visually appealing and intuitive experience for users.</li>
<li><strong>Django Admin Panel Ratings:</strong> Offers easy management of user data, logs, or query-response pairs directly through the admin interface</li>
<li><strong>Scalability and Customization:</strong> Built with Django, the application can be easily extended to include user authentication, persistent chat histories, or integration with external APIs. </li>

</ul>

<h2>Technologies Used</h2>
<ul>

  <li><strong>Django:</strong> The primary web framework used for building the backend, handling requests, and rendering responses.</li>
  <li><strong>JavaScript (JS):</strong> Adds interactivity to the user interface, making the chatbot more dynamic and responsive.</li>
  <li><strong>Python:</strong> Serves as the core programming language for developing the chatbot logic and server-side functionalities.</li>
  <li><strong>HTML:</strong> Provides the structure of the web application, ensuring a clean and semantic layout.</li>
  <li><strong>CSS:</strong> Enhances the visual appeal and styling of the application for a user-friendly experience.</li>

</ul>

<h2>Architecture</h2>
The ChatterBox project follows a modular MVC  architecture using Django. The frontend is built with HTML, CSS, and JavaScript, providing a dynamic and user-friendly interface. The backend, powered by Django and Python, handles routing, chatbot logic, and server-side processing. The database (MySQL) stores user queries and responses for persistence. Django's template system dynamically renders pages, while URL routing ensures smooth communication between the frontend and backend. Additionally, Django's admin panel is used for managing data and monitoring interactions. This architecture ensures scalability and maintainability for future enhancements.

<br>
<br>
<h1>🚀 Getting Started</h1>
To get started, download the zip file of the repository. Or use <br>
<code>git clone https://github.com/ranina12/</code><br>
<ul> <li> <strong>Prerequisites:</strong><br> Ensure the following are installed on your device:<br> <ul> <li><code>Python</code> (latest stable version)</li> <li><code>MySQL 8</code></li> <li><code>MySQL Client</code></li> <li><code>Django</code></li> <li><code>django-environ</code></li> </ul> </li><br> <li> <strong>Step 1: Create a MySQL Database</strong><br> Open your MySQL client and create a new database:<br> <code>CREATE DATABASE your_database_name;</code> </li><br> <li> <strong>Step 2: Configure Environment Variables</strong><br> Create a <code>.env</code> file in the root directory of the project and add the following details:<br> <code>DB_NAME=your_database_name</code><br> <code>DB_USER=your_username</code><br> <code>DB_PASSWORD=your_password</code><br> <code>DB_HOST=localhost</code><br> <code>DB_PORT=3306</code> (or your custom port)<br> </li><br> <li> <strong>Step 3: Import the Database Dump</strong><br> Move to the project’s root directory (e.g., <code>project/</code>) where the <code>database_dump.sql</code> file is located.<br> Run the following command:<br> <code>mysql -u your_username -p your_database_name < database_dump.sql</code> </li><br> <li> <strong>Step 4: Apply Migrations</strong><br> Run the Django migration command:<br> <code>python manage.py migrate</code> </li><br> <li> <strong>Step 5: Run the Project</strong><br> Start the Django development server:<br> <code>python manage.py runserver</code> </li><br> <li> <strong>Step 6: Access the Application</strong><br> Open your browser and go to <code>http://127.0.0.1:8000/</code>.<br> Register yourself on the platform to start using the chatbot. </li><br> </ul>

<h1>👉 How to use the site</h1>
After Register or login you will see a web-page , then click on a purplish color circle . This will give you a Chat- Box where you can interact.
<strong>You Can begin the Chat by sending Start </strong>
<ul>
  <li>After Sending Start , The bot will display 4 option and send '1' '2' '3' '4' , according which service you want</li>
  <li> After that Bot will Ask for model name , product id or any other . According to your Select Option</li>
  <li>Kindly read the bot message and give the answer according to the way ask for .</li>
  <li><strong>Here is Example></strong></li>
  <li>If you send 1 , then you have to add model: before writing your model name</li>
  <li>If you send 2 , then you have to add price: before writing your model name</li>
  <li>If you send 1 , then you have to add status: before writing your Product Id</li>
  <li>If you send 1 , then you have to add query: before writing your query</li>

  
</ul>
<h1>👥 Our Team</h1>
Our team consists of:

<ul>
  <li><strong>Nikunj Bisani:</strong>
  Connect with Nikunj on 
  <a href="https://www.linkedin.com/in/nikunjbisani/">
  LinkedIn
  </a> and 
  <a href="https://github.com/ranina12">
  GitHub
  </a>,
  </li>
</ul>
<br>

<h1>🙌 Contributions</h1>
We welcome contributions to our project. If you have any suggestions or improvements, feel free to submit a pull request or open an issue.
<br>
<br>


