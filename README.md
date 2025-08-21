# Morse Code Translator

A Django-based web application that allows you to translate text to and from Morse code. It provides a simple and intuitive interface for both encoding and decoding messages. Additionally, it offers a REST API for managing the Morse code mappings.

## Features

*   **Morse Code to Text Decoding:** Translate Morse code into plain English text.
*   **Text to Morse Code Encoding:** Convert plain English text into Morse code.
*   **User-Friendly Interface:** A clean and simple web interface for easy translation.
*   **REST API:** A comprehensive API for managing Morse code mappings, including endpoints for listing, creating, retrieving, updating, and deleting mappings.
*   **API Documentation:** The API is documented using Swagger UI and Redoc, making it easy to explore and test the available endpoints.

## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

*   Python 3.12
*   Django
*   Django REST Framework


## Usage

### Web Interface

*   **Decoder:** Navigate to `/decoder/` to translate Morse code to text.
*   **Encoder:** Navigate to `/encoder/` to translate text to Morse code.

### API

The API allows you to manage the Morse code mappings programmatically. The base URL for the API is `/api/`.

#### API Endpoints

*   `GET /api/morse_mappings/`: Retrieve a list of all Morse code mappings.
*   `POST /api/morse_mappings/`: Create a new Morse code mapping.
*   `GET /api/morse_mappings/<id>/`: Retrieve a specific Morse code mapping by its ID.
*   `PUT /api/morse_mappings/<id>/`: Update a specific Morse code mapping.
*   `DELETE /api/morse_mappings/<id>/`: Delete a specific Morse code mapping.

#### API Documentation

You can access the API documentation at the following endpoints:

*   **Swagger UI:** `/api/schema/swagger-ui/`
*   **Redoc:** `/api/schema/redoc/`