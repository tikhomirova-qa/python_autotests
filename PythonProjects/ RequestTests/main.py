from urllib import response
import requests

response = requests.post("https://petstore.swagger.io/v2/pet", json={
  "id": 421,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "Pluto",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
})
print(response.text)


response = requests.put("https://petstore.swagger.io/v2/pet", json=
{
  "id": 1,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "Simba",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
})
print(response.text)


response = requests.get("https://petstore.swagger.io/v2/pet/1", json=
{
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
)
print(response.text)