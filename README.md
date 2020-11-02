# Gemography Backend Task Solution

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
      "total_items": int,
      "items":[
         {
            "language_name": str,
            "repos_count": int,
            "repos": List[str],
         }
  ]
  }
  ```
- Life Cycle:
  - URL:  
     `/repos/languages`
  - View Controller:  
     `list_trending_languages`
