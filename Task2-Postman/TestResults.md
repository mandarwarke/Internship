# Test Results - API Testing with Postman

## 1. Overview
This document contains the results of API tests performed using Postman for authentication and data retrieval functionalities.

## 2. Tested API Endpoints
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/login` | POST | User authentication (Login) |
| `/api/users?page=2` | GET | Fetch user list |

## 3. Test Cases & Results
### **1. Login API Test**
**Request:**
```
POST https://reqres.in/api/login
Body:
{
  "email": "eve.holt@reqres.in",
  "password": "cityslicka"
}
```
**Expected Response:**
- Status Code: `200 OK`
- Response Body:
```
{
  "token": "QpwL5tke4Pnpja7X4"
}
```
**Actual Result:** ✅ Passed (Token received successfully)

### **2. Invalid Login Test**
**Request:**
```
POST https://reqres.in/api/login
Body:
{
  "email": "eve.holt@reqres.in",
  "password": "wrongpassword"
}
```
**Expected Response:**
- Status Code: `400 Bad Request`
- Response Body:
```
{
  "error": "user not found"
}
```
**Actual Result:** ❌ Failed (Token received instead of an error)

### **3. Fetch User List**
**Request:**
```
GET https://reqres.in/api/users?page=2
```
**Expected Response:**
- Status Code: `200 OK`
- Response contains a list of users.

**Actual Result:** ✅ Passed (User list retrieved successfully)

## 4. Observations & Issues
- **Login API should return an error for incorrect credentials, but it still returns a token.**
- **Fetching user list works correctly.**

## 5. Conclusion
Most tests passed successfully, but the Login API needs further investigation due to incorrect handling of invalid credentials.

---
_Test executed using Postman on [Date] by [Your Name]._

