# API Testing with Postman

This repository contains API testing scripts and test results for authentication and data retrieval using Postman. The tests were conducted as part of **Task 2: API Testing** in the **CodTech Internship**.

## Overview

We used [ReqRes](https://reqres.in/) as a public API for testing authentication and data retrieval functionalities. The test includes verifying login functionality and validating API responses.

## Setup Instructions

1. Install [Postman](https://www.postman.com/downloads/) if not already installed.
2. Import the provided **CodTech-APITests.postman\_collection.json** file into Postman.
3. Run the requests in the collection.

## API Test Cases

### 1. Authentication (Login) Test

- **Endpoint:** `POST https://reqres.in/api/login`
- **Request Body (JSON):**
  ```json
  {
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
  }
  ```
- **Expected Response:**
  ```json
  {
    "token": "QpwL5tke4Pnpja7X4"
  }
  ```
- **Test Cases:**
  - Validate status code `200 OK` for correct credentials.
  - Verify if the response contains a `token`.
  - Validate error response for incorrect credentials.

## Running Tests in Postman

1. Open Postman and navigate to the imported collection.
2. Open the **Login Test** request.
3. Click on the **Tests** tab and ensure the following test script is present:
   ```javascript
   pm.test("Status code is 200", function () {
       pm.response.to.have.status(200);
   });
   pm.test("Response has a token", function () {
       pm.expect(pm.response.json().token).to.be.a('string');
   });
   ```
4. Click **Send** to execute the test.
5. Check the **Test Results** tab for validation results.

## Deliverables

- **Postman Collection**: `CodTech-APITests.postman_collection.json`
- **Test Results**: Available in `TestResults.md`
- **Documentation**: This `README.md` file
