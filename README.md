#### Gemography Backend Task Solution

## Description
API endpoint to list the languages used by the 100 trending public repos on GitHub.

## Table of Contents
  - [APIs](#apis)
    - [list languages](#list-languages)

<div id='apis'/>
## APIs

<div id='list-languages'/>

### list languages
- Request:   
      http://localhost:8000/repos/languages
      
- Response:
    ```
      {
            "totalItems": int,
            "items":[
               {
                  "MemberFK": int,
                  "SessionsTotal": int,
                  "Date": str,
                  "Visits": int,
                  "MemberName": str,
                  "MemberEmail": str,
                  "ManagerName": str,
                  "ManagerPK": int,
                  "OrganizationalUnitName": str,
                  "Month": int,
                  "Year": int,
                  "CreatedAt": str
               }]
       }
    ```
- Life Cycle:
   - URL:   
   ` /repos/languages`
   - View Controller:   
   ` list_trending_languages`
