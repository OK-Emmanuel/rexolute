# Rexolute

Rexolute is a backend API for a mental health application designed to assist users with therapists' appointments, bookings, session management, video and audio calls, accountability, emergencies, and more.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Therapists Appointment**: Schedule and manage appointments with therapists.
- **Bookings**: Book sessions with available therapists.
- **Session Management**: Manage therapy sessions, including notes and progress tracking.
- **Video and Audio Calls**: Facilitate remote therapy sessions through video and audio calls.
- **Accountability**: Track and manage accountability tasks and goals.
- **Emergencies**: Provide emergency contact and support options.

## Installation

To install and run the Rexolute backend API, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/OK-Emmanuel/rexolute.git
    cd rexolute
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the development server:

    ```bash
    python manage.py runserver
    ```

## Usage

To use the Rexolute API, you will need to set up your environment variables and configure the application settings. You can use the provided example configuration file as a starting point.

## API Endpoints

Below are some of the key API endpoints available in Rexolute:

- **/api/appointments**: Manage therapist appointments.
- **/api/bookings**: Handle session bookings.
- **/api/sessions**: Oversee therapy sessions.
- **/api/calls**: Manage video and audio calls.
- **/api/accountability**: Track accountability tasks and goals.
- **/api/emergencies**: Access emergency support options.

For a complete list of endpoints and their usage, please refer to the API documentation.

## Contributing

We welcome contributions to Rexolute! If you would like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
